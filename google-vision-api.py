#!/usr/bin/env python
"""
Uses the Google Cloud Vision API, currently in beta as of March 2016.
"""

import argparse
import base64
import httplib2
import datetime
import json
import os
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

__author__ = "NC"

# Globals
timestamp = str(datetime.datetime.now())
storage_file_name = timestamp + "-vision-api-output.json"


def process_images(dir_name):
    image_exts = ['.jpg', 'jpeg', '.png']
    ignore_files = ['.DS_Store']
    for fn in os.listdir(dir_name + '/'):
        ext = os.path.splitext(fn)
        if fn not in ignore_files and ext[1] in image_exts and not os.path.isdir(fn):
            print(fn)
            main(dir_name + '/' + fn)


def store_json(json_input):
    with open(storage_file_name, "a") as f:
        f.write(json_input)
        f.write('\n')


def main(photo_file):
    """Run a label request on a single image"""

    API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
    http = httplib2.Http()

    credentials = GoogleCredentials.get_application_default().create_scoped(
            ['https://www.googleapis.com/auth/cloud-platform'])
    credentials.authorize(http)

    service = build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(
              body={
                'requests': [{
                  'image': {
                    'content': image_content
                   },
                  'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10,
                   },
                   {
                    'type': 'TEXT_DETECTION',
                    'maxResults': 10,
                   }]
                 }]
              })
    response = service_request.execute()

    try:
        labels = response['responses'][0]['labelAnnotations']
        for label in labels:
            # label = response['responses'][0]['labelAnnotations'][0]['description']
            label = label['description']
            print('Found label: %s' % label)
    except KeyError:
        print("N/A labels found")

    print('\n')

    try:
        texts = response['responses'][0]['textAnnotations']
        for text in texts:
            # text = response['responses'][0]['textAnnotations'][0]['description']
            text = text['description']
            print('Found text: %s' % text)
    except KeyError:
        print("N/A text found")

    print('\n= = = = = Image Processed = = = = =\n')

    response["query"] = photo_file
    response = json.dumps(response, indent=3)
    store_json(response)

    return 0

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('image_file', help='The image you\'d like to label.')
#     args = parser.parse_args()
#     main(args.image_file)

if __name__ == '__main__':
    """ for batch processing of images in folder, otherwise use main()"""
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_name', help='The folder containing images you\'d like to query')
    args = parser.parse_args()
    process_images(args.dir_name)

