import os
import datetime
import shutil


def remove_directory(directory, dry_run):
   # convenience which switches to simply printing
   # directory names if dry run is specified
    print "deleting directory: {0}".format(directory)
    if dry_run:
        return
    shutil.rmtree(directory)


def date_from_days(today, days):
    # Convenience function for calculating the
    # earliest possible date we want to keep
    delta_days = datetime.timedelta(days)
    min_date = today - delta_days
    return [min_date.year, min_date.month, min_date.day]


def calculate_recursion_depth(base_root, current_root):
    # Check what types of folders (e.g. datasets, years, months)
    # the current dirictory contains
    base_root_length = len(base_root.split('/'))
    root_length = len(current_root.split('/'))
    recursion_depth = root_length - base_root_length
    depth_to_field = {
        0: 'dataset',
        1: 'year',
        2: 'month',
        3: 'day',
    }
    return depth_to_field.get(recursion_depth, 'skip')


def process_directories(root, directories, filters, current_level, dry_run):
    # There are no directories to process here so we're done
    if not len(directories):
        return

    # We're past the longest relevant recursion depth (day) so just remove
    # all entries from the `directories` list so that os.walk will skip them
    if current_level == 'skip':
        for i in range(len(directories)):
            directories.pop(0)
        return

    # If we're at the data set level of recursion but no dataset
    # has been specified, we can return as there's no need to filter
    # out directoreis based on dataset
    if current_level == 'dataset'and not filters['dataset']:
        return

    if current_level == 'dataset':
        # Remove entires from `directories` that dont match the user specified
        # dataset. This will cause os.walk to skip processing them
        #
        # Note: Need to use mutable sequence here to make in place
        # change to list
        # TODO (sokeefe): probably a nicer way to do this...
        for i in range(len(directories)):
            directories.pop(0)
        directories.append(filters['dataset'])
        return

    # Get the minimum allowable value for this particular level.
    # Directories with values lower can be deleted. Directories with
    # higher values can be kept and hence removed from the processing queue.
    # Directories with the same value will need to be recursed into.
    min_value = filters[current_level]

    for dir in [dir for dir in directories if int(dir) < min_value]:
        remove_directory(os.path.join(root, dir), dry_run)

    values_to_skip = [val for val in directories if int(val) != min_value]
    for val in values_to_skip:
        directories.remove(val)


# For a specified directory remove all folders that are older than specified
# number of days
def delete(top_directory, today, older_than_days, dataset_name, dry_run):

    min_date = date_from_days(today, older_than_days)
    filters = {
        'dataset': dataset_name,
        'year': min_date[0],
        'month': min_date[1],
        'day':   min_date[2]
    }

    # Iterate through each directory inside of root.
    for root, directories, files in os.walk(top_directory):
        current_level = calculate_recursion_depth(top_directory, root)
        process_directories(root, directories, filters, current_level, dry_run)
