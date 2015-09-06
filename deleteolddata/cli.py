import click
from delete import *


#$ ./delete-old-data --help
#
#Usage: delete-old-data [options] <path>
#
#Deletes all data in an hourly partitioned hierarchy older than
#some number of days.  <path> is the base location of the hourly
#partitioned data.
#
#Options:
#  -h --help                      Show this help message and exit.
#  -d --older-than-days=<days>    Drop data older than this number of days.
#                                 [default: 10]
#  -D --dataset-name=<name>       Only delete data for this dataset name.
#                                 If this is not given, all datasets will be
#                                 pruned of old data.
#  -n --dry-run                   Don't actually do anything, just output the
#                                 directories that would have data deleted.
@click.command()
@click.option('--older-than-days', default=10, help="Drop data older than this number of days")
@click.option('--dataset-name', default=None, help="Only delete data for this dataset name. If this is not given, all datasets will be pruned of old data")
@click.option('--dry-run', default=False, help="Don't actually do anything, just output the  directories that would have data deleted")
def delete_all_data(older_than_days, dataset_name, dry_run):

    dataset_string = " for dataset {0}".format(dataset_name) if dataset_name else ""
    print "deleting records older than {0} days{1}".format(older_than_days, dataset_string)
    if dry_run:
        print "Dry run - will not delete any files"

    delete(older_than_days, dataset_name, dry_run)

if __name__ == '__main__':
    delete_all_data()
