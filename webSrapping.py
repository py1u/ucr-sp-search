import requests
from bs4 import BeautifulSoup
import json

def get_course_labels(cookies_file='cookiesMain.json'):
    # Load cookies
    with open(cookies_file, 'r') as file:
        cookies = json.load(file)

    # Initialize session
    session = requests.Session()

    # Set up user-agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    session.headers.update(headers)

    # Set up cookies
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    # Try to access the URL
    url = 'https://www.coursicle.com/ucr/courses'
    response = session.get(url)
    html_content = response.text

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all('span', class_='tileElementText subjectName')

    # Extract course labels
    course_labels = [element.text.strip() for element in elements]

    return course_labels
