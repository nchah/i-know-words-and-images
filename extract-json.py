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

    # Writer headers
    with open(timestamp + "_" + input_file.split(".")[0] + '_extracted.csv', 'a') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['user_id', 'user_name', 'user_startdate', 'user_description', 'user_location',
                                     'tweet_id', 'tweet_text', 'tweet_date', 'retweet_count', 'source'])

    for j in json_data:
        # Extract ID, text, date, retweet_count, source

        j = json.loads(j)

        id = str(j['id'])
        text = j['text']
        date = j['created_at']
        retweet_count = str(j['retweet_count'])
        source = j['source']
        user_name = j['user']['name']
        user_start = j['user']['created_at']
        user_desc = j['user']['description']
        user_loc = j['user']['location']
        user_id = j['user']['screen_name']

        with open(timestamp + "_" + input_file.split(".")[0] + '_extracted.csv', 'a') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                csv_writer.writerow([user_id, user_name, user_start, user_desc, user_loc,
                                     id, text, date, retweet_count, source])
            except UnicodeEncodeError:  # TODO: handle unicode OR just run with Python 3 :)
                csv_writer.writerow(["ERROR"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The json file you\'d like to extract.')
    args = parser.parse_args()
    main(args.input_file)


