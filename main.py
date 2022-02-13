import requests
from bs4 import BeautifulSoup

courses_old = [
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

courses = [
    'Fundamentals for Computer Science: Lecture',
    'Fundamentals for Computer Science: Exercises (Group A)',
    'Modelling of Complex Systems',
    'Modelling of Complex Systems: Exercises (1McsA)',
    'Software Architecture: Lecture',
    'Software Architecture: Project (1McsA)',
    'Machine Learning: Project',
    'Information Retrieval and Search Engines: Lecture',
    'Information Retrieval and Search Engines: Lecture (6 ECTS 6 ECTS)',
    'Information Retrieval and Search Engines: Exercises (6 STP 6 STP)',
    'Computer Vision: Lecture',
    'Capita Selecta Computer Science: Artificial Intelligence'
]

URL_old = 'https://people.cs.kuleuven.be/~btw/roosters2122/cws_semester_1.html'
URL = 'https://people.cs.kuleuven.be/~btw/roosters2122/cws_semester_2.html'

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
