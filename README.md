backstg_demo
===========

A sample calc app with django-rest-framework 

It will return (1 + 2 +...+ N)**2 - (1**2 + 2**2 +...+ N**2) where N between 1 and 100
and the number of times the service was called for the number N in JSON format

Installation:

git clone https://github.com/vlad2012/backstg_demo.git

cd backstg_demo

virtualenv venv

source venv/bin/activate

pip install -r requirements.pip

cd backstg_main

./manage.py syncdb

start the server:

./manage.py runserver

It has two endpoints:

http://localhost:8000/difference/          
this lists all the computed differences so far

http://localhost:8000/difference/100/      
with GET will show the difference value and how many times was called
with PUT will increment the 'occurences' counter
with DELETE will delete the entry

