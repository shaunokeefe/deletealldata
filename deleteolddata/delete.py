import datetime


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
    return depth_to_field[recursion_depth]


def process_dir(datasets, min_date, root, directory):
    pass


def delete(older_than_days, dataset_name, dry_run):
    pass
