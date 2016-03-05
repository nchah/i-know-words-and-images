# i-know-words-and-images

## Workflow





## Google Cloud Vision API

```
$ python google-vision-api.py [images]
```

The [Google Cloud Vision API](https://cloud.google.com/vision/docs/) beta was released on March 01, 2016. The API currently allows for label detection, text detection, and face detection among many others. 

### Setting Up

1. You'll need a Google Developers account to create the API keys and to take care of other authentication details. Google's documentation for setting up this API is [here](https://cloud.google.com/vision/docs/getting-started). This is enough to get set up on your local machine.

2. For the Python script, the [Label Detection Tutorial](https://cloud.google.com/vision/docs/label-tutorial) is a good start. You'll need to run a few "pip install" commands for "google-api-python-client", "oauth2client".

	```
	$ pip install apiclient
	$ pip install oauth2client
	$ pip install httplib2
	```

3. Run the script. You can have a folder of images you'd like to call the API on or use individual images.

	```
	$ python google-vision-api.py images/
	$ python google-vision-api.py dog.jpg
	```

4. Specifiy features you'd like to query. The body portion of the service_request variable can be adjusted to include other data you'd like to get. Currently only label detection and text detection are included in this script but the [documentation](https://cloud.google.com/vision/docs/concepts) includes more.

	```
	LABEL_DETECTION	Execute Image Content Analysis on the entire image and return
	TEXT_DETECTION	Perform Optical Character Recognition (OCR) on text within the image
	FACE_DETECTION	Detect faces within the image
	LANDMARK_DETECTION	Detect geographic landmarks within the image
	LOGO_DETECTION	Detect company logos within the image
	SAFE_SEARCH_DETECTION	Determine image safe search properties on the image
	IMAGE_PROPERTIES	Compute a set of properties about the image (such as the image's dominant colors)
	```
