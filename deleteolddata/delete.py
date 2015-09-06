import os
import datetime


def remove_directory(directory, dry_run):
    pass


def date_from_days(today, days):
    delta_days = datetime.timedelta(days)
    min_date = today - delta_days
    return [min_date.year, min_date.month, min_date.day]


def calculate_recursion_depth(base_root, current_root):
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
    if not len(directories):
        return

    if current_level == 'skip':
        for i in range(len(directories)):
            directories.pop(0)
        return

    if current_level == 'dataset'and not filters['dataset']:
        return

    if current_level == 'dataset':
        # Need to use mutable sequence here to make in place change to list
        # TODO (sokeefe): probably a nicer way to do this...
        for i in range(len(directories)):
            directories.pop(0)
        directories.append(filters['dataset'])
        return

    min_value = filters[current_level]

    for dir in [dir for dir in directories if int(dir) < min_value]:
        remove_directory(os.path.join(root, dir), dry_run)

    values_to_skip = [val for val in directories if int(val) != min_value]
    for val in values_to_skip:
        directories.remove(val)


def delete(top_directory, today, older_than_days, dataset_name, dry_run):

    min_date = date_from_days(today, older_than_days)
    filters = {
        'dataset': dataset_name,
        'year': min_date[0],
        'month': min_date[1],
        'day':   min_date[2]
    }

    for root, directories, files in os.walk(top_directory):
        current_level = calculate_recursion_depth(top_directory, root)
        process_directories(root, directories, filters, current_level, dry_run)
