Usage: python cli.py --older-than-days 4  ../data [options] <path>

Deletes all data in an hourly partitioned hierarchy older than
some number of days.  <path> is the base location of the hourly
partitioned data.

Options:
  -h --help                      Show this help message and exit.
  -d --older-than-days=<days>    Drop data older than this number of days.
                                 [default: 10]
  -D --dataset-name=<name>       Only delete data for this dataset name.
                                 If this is not given, all datasets will be
                                 pruned of old data.
  -n --dry-run                   Don't actually do anything, just output the
                                 directories that would have data deleted.
