import click
import datetime
import os

from delete import delete


@click.command()
@click.option('--older-than-days',
              default=10, type=click.IntRange(0, None),
              help="Drop data older than this number of days")
@click.option('--dataset-name', default=None,
              help="Only delete data for this dataset name."
              "If this is not given, all datasets will be pruned of old data")
@click.option('--dry-run', default=False, type=bool, is_flag=True,
              help="Don't actually do anything, just output the"
              "directories that would have data deleted")
@click.argument('path', type=click.Path(exists=True))
def delete_old_data(older_than_days, dataset_name, dry_run, path):

    if not os.path.isdir(os.path.join(path, dataset_name)):
        print "{0} is not a valid dataset".format(dataset_name)
        return 1

    ds_string = " for dataset {0}".format(dataset_name) if dataset_name else ""
    message = "deleting records older than {0} days{1}".format(
        older_than_days, ds_string)
    print message

    if dry_run:
        print "Dry run - will not delete any files"

    today = datetime.datetime.today()

    # Remove trailing slashes
    path = path.rstrip('/')

    delete(path, today, older_than_days, dataset_name, dry_run)

if __name__ == '__main__':
    delete_old_data()
