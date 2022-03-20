# lab-manager
An University Laboratory Management tool developed in Python/Flask

## _A Laboratory Management Web Application based in Flask_
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)


I created this app based on the needs of the Laboratório de Máquinas Térmicas at the Federal University of Paraná.

There is a lot of different users in the lab, on different projects (Engineering Projects, such as Formula SAE, Baja SAE, Aerodesing, etc), so the idea is to create a simple way for the students to create their account with basic data, and allow for the Professors responsible for each projects to validate their accounts.

Further down the road, the idea is to connect directly to the Access Point API (A biometric lock) to create the users account and to allow the users to create their biometric key (after the permission of the leader of the project).

![UsersAdmPage](/imgs/admin_users.png "Users Admin Page")

![ProfilePage](/imgs/admin_profile.png "Users Profile Page")

## Objectives

Develop a Laboratory Manager using Flask to develop some skills with, and work with the following technology or programming solutions:

* Work with Web Development in Python
* Development of a full stack web application
* Work with form validation in Flask
* Work with HTML and Bootstrap
* Work with DataTables.js together with Flask
* Work with GIT
* Work with relational database (SQL)
* Configure and use DB Migrations

## To-do

- Deploy the final app 
- Implement Unity Testing
- Implement Elasticsearch

## Dependencies

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

* Flask
* SQLAlchemy
* FlaskLogin
* WTForms
* Werkzeug
* Flask-Migrate
* Elasticsearch

## Usage

Prepare the virtual environment (Using Linux):

```sh
python -m venv .venv
source .venv/bin/activate
```

Install all dependencies:

```sh
pip install -r requirements.txt
```

Run Flask server (In DEV mode)
    
```sh
export FLASK_ENV=development; flask run
```