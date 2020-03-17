import ast
from _operator import itemgetter
from random import randrange

import nltk
from flask import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from utility import firebase_config

# Constants
raw_reviews_json_path = "/Users/victorious/misc/misc/files/google_reviews_raw.json"
modified_reviews_json_path = "//Users/victorious/OneStarReview/files/google_reviews_modified.json"
master_json_path_v0 = "/Users/victorious/OneStarReview/files/master_json_v0"
firebase = firebase_config.Configuration()

def get_amazon_item_endpoint(asin):
    url = 'https://www.amazon.com/dp/' + str(asin)
    return url


def Amazon_Reviews_generate_json_files(file_name):
    path = "/Users/victorious/misc/datasets/amazon/" + file_name
    review_map = {}
    internal_id = 0

    with open(path) as file:
        for i in file:
            internal_id += 1
            if internal_id % 10 == 0:
                break
            else:
                review_map[internal_id] = i
                review_map["score"] = 0


    with open('/Users/victorious/misc/misc/files/amazon_reviews_modified.json', 'w') as file:
        json.dump(review_map, file, indent=4)

    return review_map


def Google_Places_generate_modified_json():
    file_name = "test_places.clean.json"
    path = "/Users/victorious/misc/datasets/google/" + file_name
    review_map = {}
    internal_id = 0

    with open(path) as file:
        for i in file:
            internal_id += 1
            if internal_id % 100 == 0:
                break
            else:
                i = ast.literal_eval(i)
                review_map[str(internal_id)] = i
                review_map[str(internal_id)]["score"] = 0
                sentiment = determine_sentiment(review_map[str(internal_id)]["reviewText"])
                review_map[str(internal_id)]["sentiment"] = sentiment

    with open('/Users/victorious/misc/misc/files/google_places_modified.json', 'w') as file:
        json.dump(review_map, file, indent=4)

    return review_map


def Google_Reviews_generate_modified_json():
    file_name = "test_reviews.clean.json"
    path = "/Users/victorious/OneStarReview/datasets/google/" + file_name
    review_map = {}
    internal_id = 0

    with open(path) as file:
        for i in file:
            internal_id += 1
            if internal_id % 100 == 0:
                break
            else:
                i = ast.literal_eval(i)
                review_map[str(internal_id)] = i
                review_map[str(internal_id)]["score"] = 0
                sentiment = determine_sentiment(review_map[str(internal_id)]["reviewText"])
                review_map[str(internal_id)]["sentiment"] = sentiment

    with open('/Users/victorious/OneStarReview/files/google_reviews_modified.json', 'w') as file:
        json.dump(review_map, file, indent=4)

    return review_map


def Google_Users_generate_modified_json():
    file_name = "test_users.clean.json"
    path = "/Users/victorious/misc/datasets/google/" + file_name
    review_map = {}
    internal_id = 0

    with open(path) as file:
        for i in file:
            internal_id += 1
            if internal_id % 100 == 0:
                break
            else:
                i = ast.literal_eval(i)
                review_map[str(internal_id)] = i
                review_map[str(internal_id)]["score"] = 0
                sentiment = determine_sentiment(review_map[str(internal_id)]["reviewText"])
                review_map[str(internal_id)]["sentiment"] = sentiment

    with open('/Users/victorious/misc/misc/files/google_users_modified.json', 'w') as file:
        json.dump(review_map, file, indent=4)

    return review_map


def update_user_vote_count(list_of_adds):
    firebase = firebase_config.Configuration()
    firebase.key = "2"
    firebase.get_request()

    list_of_updates = []

    with open(modified_reviews_json_path) as file:
        modified_json = json.loads(file.read())
        for item in list_of_adds:
            review_item = modified_json[item["internal_id"]]
            review_item["score"] += 1
            modified_json[item["internal_id"]] = review_item
            list_of_updates.append(review_item)
            print(item)

    with open('/Users/victorious/misc/misc/files/google_reviews_modified.json', 'w') as file:
        json.dump(modified_json, file, indent=4)

    return modified_json


def build_page_lists():

    all_reviews = []
    one_star_review_list = []

    with open(modified_reviews_json_path) as file:
        review_data = json.loads(file.read())

        for item in review_data:
            if review_data[item]["unixReviewTime"] is None:
                time = 9999999999
            else:
                time = review_data[item]["unixReviewTime"]
            view_item = {
                "by": review_data[item]["reviewerName"],
                "descendants": 0,
                "id": item,
                "score": review_data[item]["score"],
                "time": time,
                "title": review_data[item]["reviewText"],
                "type": review_data[item]["rating"],
                "url": "http://www.google.com"
            }
            if review_data[item]["rating"] == 1.0:
                one_star_review_list.append(view_item)
            all_reviews.append(view_item)

    list_of_review_item_ids = []
    for review_item in sorted(one_star_review_list, key=itemgetter("score"), reverse=True):
        list_of_review_item_ids.append(review_item["id"])
    return list_of_review_item_ids, all_reviews


def build_master_json_v0():

    with open(master_json_path_v0) as template:
        master_json_v0 = json.loads(template.read())

    topstories, item = build_page_lists()

    master_json_v0["topstories"] = topstories
    master_json_v0["item"] = item

    return master_json_v0


def retrieve_random_new_reviews(number_of_random_reviews):
    modified_json = firebase.get_request("")
    size = len(modified_json)
    random_review_objects = []
    index = 0

    while number_of_random_reviews > index:
        random_id = randrange(size)
        random_review_objects.append(modified_json[random_id])
        index += 1

    # print("Returning random objects list of size " + str(len(random_review_objects)))

    return random_review_objects


def determine_sentiment(text):

    nltk.download('vader_lexicon')

    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(str(text))

    return sentiment
