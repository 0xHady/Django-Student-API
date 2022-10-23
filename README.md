# Django-Student-API

# Installation

* install poetry
* run `poetry add django`
* run `poetry shell`
* run `python manage.py runserver`

# Usage

* `http://127.0.0.1:8000/api/` 
  * GET: retrieve all students 
  * POST: create a new student (need to provide a Json body for the student)

* `http://127.0.0.1:8000/api/x` 
  * GET: retrive student with id = x
  * PUT: Update studetnt with id = x
  * DELETE: delete student with id = x

Note: All CRUD operations are done on a Json file (student/db.json)
