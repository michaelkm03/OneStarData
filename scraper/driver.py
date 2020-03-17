import time
import json
import re
import gzip

from selenium import webdriver

# Pass argument variables via command-line
#url = sys.argv[1]
from selenium.webdriver.common.by import By

place_url = "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0146574,17z/data=!3m1!4b1!4m7!3m6!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687!9m1!1b1"
person_url = "https://www.google.com/maps/contrib/100145551853115296988/reviews"
list_of_user_ids = []
count = 0



def get_lowest_reviews_for_place(driver):
    url = "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0146574,17z/data=!3m1!4b1!4m7!3m6!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687!9m1!1b1"

    driver.get(url)
    driver.set_window_size(1440, 900)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[8]/div/div').click()
    time.sleep(3)
    driver.find_element_by_xpath("//body/div[2]/div[4]/div").click()
    time.sleep(3)
    list_of_reviews_lowest_asc = driver.find_elements_by_class_name("section-review-review-content")
    list_of_reviewers = driver.find_elements_by_class_name("section-review-title")
    print(len(list_of_reviewers))
    for element in range(len(list_of_reviewers)):
        list_of_reviewers[element].click()
        driver.switch_to.window(driver.window_handles[1])
        user_id = re.search(r'/contrib/([^?]+)', driver.current_url).group(1)
        print(user_id)
        list_of_user_ids.append(user_id)
        driver.sw


    driver.close()


def get_reviews_for_user(user_id, driver):
    s = driver.get("https://www.google.com/maps/contrib/" + str(user_id) + "?hl=en-US"

'''

    # Creating an empty dictionary
    review_map = {}

    # Adding list as value
    user_id = "100145551853115296988"
    # Configure scraper
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    scraper = webdriver.Chrome(options=options, executable_path="/Users/victorious/OneStarReview_data/utility/chromedriver")

    get_lowest_reviews_for_place(scraper)


    # get the number of stars
    stars = scraper.find_elements_by_class_name("section-review-stars")
    review_text = scraper.find_elements_by_class_name("section-review-text")

    review_text = scraper.find_elements_by_class_name("section-review-text")
    for i in review_text:
        print(i.text)

    for i in stars:
        print(i.text)

    stars = scraper.find_elements_by_class_name("section-review-stars")
    review_text = scraper.find_elements_by_class_name("section-review-text")
    first_review_stars = stars[0]
    active_stars = first_review_stars.find_elements_by_class_name("section-review-star-active")

    #print('there are ' + len(first_review_stars) + ' 1 star review STARS')
    #print('there are ' + len(review_text) + ' 1 star review TEXT')

    for review in review_text:
        if user_id in review_map:
            review_map[user_id].append(review.text)
        else:
            review_map[user_id] = []
            review_map[user_id].append(review.text)

    # get_reviews_for_user("100145551853115296988", scraper)
    '''