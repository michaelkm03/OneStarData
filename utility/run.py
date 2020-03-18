import sys
from utility import firebase_config
from utility.functions import build_master_json_v0, Google_Reviews_generate_modified_json

if __name__ == '__main__':
    try:
        '''
            Create connection object to Firebase DB; API capable with GET, PUT, DELETE methods
        '''
        firebase_DB = firebase_config.Configuration()
        if sys.argv[1] == "updateJson":
            firebase_DB.put_request("/v0", build_master_json_v0())
        elif sys.argv[1] == "deleteJson":
            firebase_DB.put_request("/v0", {})
        elif sys.argv[1] == "getJson":
            Google_Reviews_generate_modified_json()
            #v0 = firebase_DB.get_request("/v0")
        else:
            print("arg_variable %s not found" % sys.argv[1])
    except IndexError:
        print("Argument is empty, pass one of the following parameters to run.py")
        print('===============================================================================================')
        print("updateJson:  Generate new template_master_json_v0 file and replace FirebaseDB")
        print("deleteJson:  Delete existing template_master_json_v0 file in FirebaseDB")
        print("getJson:     Get existing template_master_json_v0 file in FirebaseDB")
        print('===============================================================================================')