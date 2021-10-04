import requests
from bs4 import BeautifulSoup

courses = [
    'Besturingssystemen: hoorcollege',
    'Besturingssystemen: oefeningen (1Mcws)',
    'Declarative Languages: Lecture',
    'Declarative Languages: Exercises (Group A)',
    'Design of Software Systems: Lecture',
    'Design of Software Systems: Exercises',
    'Distributed Systems: Lecture',
    'Distributed Systems: Exercises (1McsA)',
    'Principles of Machine Learning: Lecture',
    'Principles of Machine Learning: Exercises (Group 1)',
    'Capita Selecta Computer Science: Artificial Intelligence'
]

URL = 'https://people.cs.kuleuven.be/~btw/roosters2122/cws_semester_1.html'

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
