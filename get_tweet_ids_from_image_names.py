__author__ = 'EM'


"""
Assumes format of text file for input of image urls and tweet ids is each line as:
704918662784880645 http://pbs.twimg.com/media/CchfyO4XIAA-fEZ.jpg
"""

f = open('MakeDonaldDrumpfAgain-image-urls-with-ids.txt', 'r')
all_items = f.read().split('\n')
f.close()


def dict_imgname_to_tweet_id(plaintext):
    dict_imgs_tweetids = {}

    for item in plaintext:
        tweet_id = item[0:18]
        url = item[-19:]
        if url in dict_imgs_tweetids:
            dict_imgs_tweetids[url].append(tweet_id)
        else:
            dict_imgs_tweetids[url] = [tweet_id]

    return dict_imgs_tweetids


def output_tweet_list(image_name_list, dict_mapping):
    """
    input:: list of image names
    output:: all tweet ids that reference that image based on URL / name
    """

    tweet_id_list = []

    for item in image_name_list:
        for i in dict_mapping[item]:
            tweet_id_list.append(i)

    with open('output_tweet_ids.txt', mode='wt') as myfile:
        myfile.write('\n'.join(str(line) for line in tweet_id_list))


images_to_check = ["CcWvpe0UMAA4HRN.jpg"]
images_and_tweet_ids = dict_imgname_to_tweet_id(all_items)

output_tweet_list(images_to_check, images_and_tweet_ids)
