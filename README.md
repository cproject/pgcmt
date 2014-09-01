pgcmt
=====

Change Management Tool For PostgreSQL by using Django framework.
Aim of this application is to keep all DDL Changes, when and who did it.
This is easy to follow and find all changes you're applied in production databases if you are faced with a problem.

### Usage

* First, edit database settings for this project in ***settings.py***
* Then, sync with database and create a super user
```python manage.py syncdb```
* Run your Django application
``` manage.py runserver 0.0.0.0:8000```
* Add your database as project (**Create Project**)
* Create responsible people who requests DDL changes (**Create Responsible**)
* Add your DDL Changes or anything (**Create Ticket**)
