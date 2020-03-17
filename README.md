## :star2: OneStarReview :star2:
General Setup and Description TBD

### :hammer_and_wrench: Utility

#### Functions
Static methods to transform data, build/sort lists and generate JSON files for upload to Firebase DB

#### Firebase_config 
Class to authenticate with Firebase and send API requests (GET, PUT, DELETE)

#### Run
Script to take in argument variables and run project

### :computer: Command Line

````
// Arguments

updateJson:  Generate new master_json_v0 and modified_reviews_json file and replace FirebaseDB
deleteJson:  Delete existing master_json_v0 and modified_reviews_json file in FirebaseDB
getJson:     Get existing master_json_v0 and modified_reviews_json file in FirebaseDB

// CLI Example

python run.py updateJson
````
