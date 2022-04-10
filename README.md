# lab-manager
An University Laboratory Management tool developed in Python/Flask

## _A Laboratory Management Web Application based in Flask_
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=blue)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![](https://img.shields.io/badge/Framework-Flask-informational?style=flat&logo=flask&logoColor=white&color=blue)
![](https://img.shields.io/badge/Tools-Bootstrap-informational?style=flat&logo=bootstrap&logoColor=white&color=blue)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=blue)

I created this app based on the needs of the Laboratório de Máquinas Térmicas at the Federal University of Paraná.

There is a lot of different users in the lab, on different projects (Engineering Projects, such as Formula SAE, Baja SAE, Aerodesing, etc), so the idea is to create a simple way for the students to create their account with basic data, and allow for the Professors responsible for each projects to validate their accounts.

Further down the road, the idea is to connect directly to the Access Point API (A biometric lock) to create the users account and to allow the users to create their biometric key (after the permission of the leader of the project).

![ProfilePage](/imgs/admin_profile.png "Users Profile Page")

![UsersAdmPage](/imgs/admin_users.png "Users Admin Page")

## Objectives

Develop a Laboratory Manager using Flask to develop some skills with, and work with the following technology or programming solutions:

* Work with Web Development in Python
* Development of a full stack web application
* Implement Elasticsearch
* Work with form validation in Flask
* Work with HTML and Bootstrap
* Work with DataTables.js together with Flask
* Work with GIT
* Work with relational database (SQL)
* Configure and use DB Migrations

## To-do

- Deploy the final app 
- Implement Unity Testing

## Dependencies

* Flask
* SQLAlchemy
* FlaskLogin
* WTForms
* Werkzeug
* Flask-Migrate
* Elasticsearch

## Database Schema

![LabManager Database](/imgs/db_schema.png "LabManager Database Schema")

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

Run Elasticsearch Docker Container (For DEV mode)
    
```sh
docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
```

Run Flask server (In DEV mode)
    
```sh
export FLASK_ENV=development; flask run
```

Run Tests
```sh
python -m pytest
```

## Docker Commands

Build Docker Container

```sh
docker build -t lab_manager:latest .
```

Run MySQL Docker Container

```sh
 docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=lab_manager -e MYSQL_USER=lab_manager \
    -e MYSQL_PASSWORD=MYSQL_PASSWORD_GOES_HERE \
    mysql/mysql-server:latest
```

Run Elasticsearch Docker Container

```sh
docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2
```

Run Docker Container

```sh
docker run --name lab_manager -d -p 8000:5000 --rm -e SECRET_KEY=my-super-secret-key \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://lab_manager:MYSQL_PASSWORD_GOES_HERE@dbserver/lab_manager \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    lab_manager:latest
```

View Docker Container Logs

```sh
docker logs lab_manager
```
