__author__ = 'EM'

import csv
from collections import Counter

f = open('MakeDonaldDrumpfAgain-20160303-image-urls.txt', 'r')
all_urls = f.read().split('\n')
f.close()


def get_unique_urls(url_list):
    """
    Returns text file with list of unique URLS
    """
    unique_urls = list(set(url_list))
    with open('unique_img_urls.txt', mode='wt') as myfile:
        myfile.write('\n'.join(str(line) for line in unique_urls))


def get_top_twenty_count(urls):
    """
    Returns text file with list top 20 URLs in set and list of count
    """
    lines = (Counter(urls).most_common(20))
    with open('top_twenty_images.txt', mode='wt') as myfile:
        myfile.write('\n'.join(str(line) for line in lines))


def get_all_by_count(urls):
    """
    Returns csv file with all URLs in set and list of count
    """
    url_by_count = Counter(urls)
    with open('unique_by_count.csv', mode='wt') as myfile:
        w = csv.writer(myfile)
        w.writerows(url_by_count.items())


get_unique_urls(all_urls)
get_top_twenty_count(all_urls)
get_all_by_count(all_urls)

