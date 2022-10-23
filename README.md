# Django-Student-API
Added model form validation on task-2

# Installation

* install poetry
* run `poetry add django`
* run `poetry shell`
* run `python manage.py runserver`

# Usage

* `http://127.0.0.1:8000/student/` 
  * GET: retrieve all students
  * POST: create a new student (need to provide a json body for the student)

* `http://127.0.0.1:8000/student/x` 
  * GET: retrive student with id = x
  * PUT: Update studetnt with id = x (need to provide a json body for the student)
  * DELETE: delete student with id = x
