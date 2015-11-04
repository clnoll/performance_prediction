import csv
import sys
import operator


def sort_csv(unsorted_filepath, sorted_filepath):
    with open(unsorted_filepath, "rt", encoding='utf-8') as sankey:
        raw_reader = csv.reader(sankey, delimiter=",")
        header = next(raw_reader, None)
        sorted_data = sorted(raw_reader, key=operator.itemgetter(0))

    with open(sorted_filepath, 'w', newline='') as myfiletest:
        wr = csv.writer(myfiletest)
        if header:
            wr.writerow(header)
        wr.writerows(sorted_data)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ImportError("Source and destination filepaths are missing")
    if len(sys.argv) < 3:
        raise ImportError("Destination path is missing")
    sort_csv(sys.argv[1], sys.argv[2])
