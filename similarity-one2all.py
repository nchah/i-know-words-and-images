#!/usr/bin/env python
from PIL import Image
import imagehash
import photohash


def compareone2all(userpath, hashfunc = imagehash.phash):
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
            compareme = '/Users/kpham/Desktop/drumpfingarchives/image-download3/Ccg5K73XEAErgpK.jpg'
            distance = photohash.hash_distance(photohash.average_hash(compareme), photohash.average_hash(image_filenames[i]))
            if distance < 12:
                print (distance, image_filenames[i])

userpath='/Users/kpham/Desktop/drumpfingarchives/image-download3'
compareone2all(userpath=userpath, hashfunc=imagehash.phash)