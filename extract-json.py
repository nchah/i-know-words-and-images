#!/usr/bin/env python
"""
Extracts JSON fields and outputs a csv
"""

import argparse
import json
import csv
import datetime

__author__ = "NC"

timestamp = str(datetime.datetime.now())


def main(input_file):
    with open(input_file, "r") as f:
        json_data = f.readlines()

    for j in json_data:
        # Extract ID, text, date, retweet_count, source

        j = json.loads(j)

        id = str(j['id'])
        text = j['text']
        date = j['created_at']
        retweet_count = str(j['retweet_count'])
        source = j['source']

        with open(timestamp + "_" + input_file.split(".")[0] + '_extracted.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                spamwriter.writerow([id, text, date, retweet_count, source])
            except UnicodeEncodeError:  # TODO: handle unicode OR just run with Python 3 :)
                spamwriter.writerow(["ERROR"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The json file you\'d like to extract.')
    args = parser.parse_args()
    main(args.input_file)


