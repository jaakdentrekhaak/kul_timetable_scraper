import requests
from bs4 import BeautifulSoup

courses = [
    'Comparative Programming Languages: Lecture',
    'Comparative Programming Languages: Exercises (2McsA)',
    'Genetic Algorithms and Evolutionary Computing: Lecture',
    'Genetic Algorithms and Evolutionary Computing: Exercises',
    'Big Data Analytics Programming: Lecture',
    'Big Data Analytics: Exercises',
    'Religie, zingeving en levensbeschouwing',
    'Lessen voor de 21ste eeuw',
]

URL = 'https://people.cs.kuleuven.be/~btw/roosters2223/cws_semester_1.html'

r = requests.get(URL)

if not r.ok:
    raise Exception('Timetable could not be retrieved from the URL')

soup = BeautifulSoup(r.content, 'html.parser')

# Loop through all days
for day in soup.find_all('table'):
    for course in day.find_all('tr'):
        course_title = course.find_all('a')[0].text
        if course_title not in courses:
            course.decompose()

with open('result.html', 'w') as result_file:
    result_file.write(soup.prettify())
