import datetime


def date_from_days(today, days):
    delta_days = datetime.timedelta(days)
    min_date = today - delta_days
    return [min_date.year, min_date.month, min_date.day]


def delete(older_than_days, dataset_name, dry_run):
    pass
