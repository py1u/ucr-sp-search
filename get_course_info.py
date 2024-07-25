from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webSrapping import get_course_labels
import time
import json
import random
import re
import pandas as pd

def get_course_info(driver, course_labels):
    """
    获取课程信息并存储到字典中
    """
    course_info = {}

    try:
        # open the main webpage
        driver.get('https://www.coursicle.com/ucr/courses/')
        time.sleep(10)

        # read and save Cookie
        with open('cookiesMain.json', 'w') as file:
            json.dump(driver.get_cookies(), file)

        # go into every course
        for label in course_labels:
            # set URL
            course_url = f'https://www.coursicle.com/ucr/courses/{label}/'
            
            # clean Cookie
            driver.delete_all_cookies()

            # load Cookie
            driver.get('https://www.coursicle.com/ucr/courses/')
            with open('cookiesMain.json', 'r') as file:
                cookies = json.load(file)
            
            # add Cookie
            for cookie in cookies:
                driver.add_cookie(cookie)
            
            # access url
            driver.get(course_url)
            time.sleep(random.uniform(3, 7))  # set random waiting time to simulate human reaction
            
            # use BeautifulSoup
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            # get info
            course_texts = []
            elements = soup.find_all('a', class_='tileElement')
            for element in elements:
                # search for needed info
                course_name_elem = element.find('span', class_='tileElementText tileElementTextWithSubtext')
                course_name_full = course_name_elem.text.strip() if course_name_elem else ""
                
                # split the course name
                match = re.match(r'([A-Z]+)\s*(\w+)', course_name_full)
                if match:
                    course_name = match.group(1)
                    course_number = match.group(2)
                else:
                    course_name = course_name_full
                    course_number = ""
                
                # build new url
                if course_name and course_number:
                    # get detail info
                    course_detail_text = get_course_detail(driver, course_name, course_number)
                    
                    # add info to the list
                    course_texts.append((course_name, course_number, course_detail_text))
            
            # store into course_info
            course_info[label] = course_texts

    finally:
        return course_info

def get_course_detail(driver, course_name, course_number):
    
    # build url
    course_detail_url = f'https://www.coursicle.com/ucr/courses/{course_name}/{course_number}/'
    
    # access course detail url
    driver.get(course_detail_url)
    time.sleep(random.uniform(3, 7))  # random waiting time
    
    # get info
    detail_html_content = driver.page_source
    detail_soup = BeautifulSoup(detail_html_content, 'html.parser')
    
    # get needed info
    subitem_content_elem = detail_soup.find('div', class_='subItemContent')
    if subitem_content_elem:
        course_detail_text = subitem_content_elem.text.strip()
    else:
        course_detail_text = "No information found"
    
    return course_detail_text

# get course_labels
course_labels = get_course_labels()


# initialize ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-gpu")

# create webdriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # access course info
    course_info = get_course_info(driver, course_labels)

finally:
    # close chrome
    driver.quit()

# check output (use for testing)
for label, texts in course_info.items():
    print(f"Course Label: {label}")
    for name, number, detail in texts:
        print(f"Course Name: {name}")
        print(f"Course Number: {number}")
        print(f"Course Detail: {detail}")
        print("-" * 50)
    print("=" * 50)

# save as csv
rows = []
for label, texts in course_info.items():
    for name, number, detail in texts:
        rows.append([label, name, number, detail])

df = pd.DataFrame(rows, columns=["Course Label", "Course Name", "Course Number", "Course Detail"])
df.to_csv('course_info.csv', index=False)