#!/usr/bin/env python
from PIL import Image
import imagehash
import photohash


def similarity(userpath, hashfunc = imagehash.phash):
    import os
    def is_image(filename):
    	f = filename.lower()
    	return f.endswith(".jpg") or f.endswith(".jpeg") 
    
    image_filenames = [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]
    images = {}
    for img in sorted(image_filenames):
    	hash = hashfunc(Image.open(img))
    	images[hash] = images.get(hash, []) + [img]
    

    for i in range (len(image_filenames)):
        for j in range (i+1, len(image_filenames)):
            distance = photohash.hash_distance(photohash.average_hash(image_filenames[i]), photohash.average_hash(image_filenames[j]))
            print (image_filenames[i], image_filenames[j], distance)

    for k, img_list in images.iteritems():
    	if len(img_list) > 1:
    		print(" ".join(img_list))

userpath='whateverman'
similarity(userpath=userpath, hashfunc=imagehash.phash)
# use phash, ahash, average_hash