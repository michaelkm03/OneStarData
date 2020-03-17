import sys
from utility import firebase_config
from utility.functions import Google_Reviews_generate_modified_json, build_master_json_v0

firebase_DB = firebase_config.Configuration()

if __name__ == '__main__':

    try:
        if sys.argv[1] == "updateJson":
            firebase_DB.put_request("/_modified_reviews_json", Google_Reviews_generate_modified_json())
            firebase_DB.put_request("/v0", build_master_json_v0())
        elif sys.argv[1] == "deleteJson":
            firebase_DB.put_request("/_modified_reviews_json", {})
            firebase_DB.put_request("/v0", {})
        elif sys.argv[1] == "getJson":
            modified_reviews_json = firebase_DB.get_request("/_modified_reviews_json")
            v0 = firebase_DB.get_request("/v0")
        else:
            print("arg_variable %s not found" % sys.argv[1])
    except IndexError:
        print("Argument is empty, pass one of the following parameters to run.py")
        print('===============================================================================================')
        print("updateJson:  Generate new master_json_v0 and modified_reviews_json file and replace FirebaseDB")
        print("deleteJson:  Delete existing master_json_v0 and modified_reviews_json file in FirebaseDB")
        print("getJson:     Get existing master_json_v0 and modified_reviews_json file in FirebaseDB")
        print('===============================================================================================')