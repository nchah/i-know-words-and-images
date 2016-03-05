# i-know-words-and-images

On February 28, 2016, the comedian John Oliver called upon viewers of Last Week Tonight to undermine Republican presidential primary candidate Donald Trump’s veneer of success, honesty, and affluence through the powers and peculiarities of social media: let the world know that Trump is not Trump but _Drumpf_, a man of failures, dishonesty, and violent chauvinism. A flood of social media activity followed: meme, word, image, hashtag, comment, retweet. 

A Web Archives Hackathon at the University of Toronto happened to coincide with this Drumpfing of Trump. Drumpf famously declared "I love words. I have the best words." We set off a set of (#nottiny)-hands-on inquiries into what investigating Twitter through not just words but words _and_ images might look like: what people say, how they make/re-make images words, how computers classify images. 

## Workflows

Researching Meme Events

The toolkit in #iknowwordsandimages emerged out of response to this still unfolding meme event, drawing on a data set of tweets and associated images connected by the hashtag Oliver had put forward, #makedonalddrumpfagain. The team assumed researchers in a variety of fields would find much to study in this meme event and others like it. Here are some of the questions we thought researchers might ask:

- How did John Oliver’s original broadcast influence the kinds of themes that meme participants pursued in their contributions?

- Do people alter the way they introduce or label the images that they share through their tweet text? If so, in what ways and for what reasons?

- How does the use of the tweet appear to affect the success or failure of an image’s propagation through Twitter?

Workflows

Researches could try to get at these questions through browsing Twitter, or through scanning their database manually—but they would quickly run into issues of speed, reliability, and coverage. The code shared here offers some tools for different kinds of workflows that a researcher might follow. Here is an example workflow.

1. Common Theme

(a) Researcher examines database of images, either manually through OS or with the aid of script for returning images by frequency.

(b) A specific theme emerges across different images: for example, the various ways of comparing Donald Trump to Hitler.

(c) The researcher gathers unique Image IDs.

(d) Researcher can do a couple things at this stage: using ImageHash and PhotoHash, find similar images in the database. This process also returns the hamming distance. 

(e) Do analysis on images and add to list those of similarity at a researcher-determined level of confidence.

(f) Get the all Tweet IDs associated with images. 

(g) Hydrate for full JSON Twitter metadata (see below).

(h) Extract selected parameters into CSV, e.g., "text", "date", "retweet number", "ID", "source", and "description."

(i) Now you have options! Do ImagePlot mapped by time and similarity. Use Google Cloud Vision API to add further metadata to CSV. Run other analytics on the set. Or bravely go forth and scan the data on your own!


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

### Samples

The "Getting Started" tutorial provides a dog.jpg image to run in the first API call. 

![dog.jpg](/images/dog.jpg?raw=true)

It works as intended and correctly identifies the image as a dog. Extending the maxResults returns even more results as follows.
```
{
  "responses": [
    {
      "labelAnnotations": [
        {
          "mid": "/m/0bt9lr",
          "description": "dog",
          "score": 0.89208293
        },
        {
           "score": 0.85700572, 
           "mid": "/m/09686", 
           "description": "vertebrate"
        }, 
        {
           "score": 0.84881896, 
           "mid": "/m/01pm38", 
           "description": "clumber spaniel"
        }, 
        {
           "score": 0.84757507, 
           "mid": "/m/04rky", 
           "description": "mammal"
        }
      ]
    }
  ]
}
```
