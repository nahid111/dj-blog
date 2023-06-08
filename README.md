# Blog Api using DRF

This repo contains the backend api part of the application.

- Backend: Django
- Frontend: React,
  Redux [<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/link.svg" width="20" height="20">](https://github.com/nahid111/react-redux-toolkit-blog)

## Getting Started

1. Install `python3-devel` on your local machine for `<python.h>` and other system headers.
   <br/><nbsp/>UBUNTU or Debian
   <br/><nbsp/>`sudo apt install python3-dev default-libmysqlclient-dev build-essential`
   <br/><nbsp/>Red Hat / CentOS
   <br/><nbsp/>`sudo dnf install python3-devel mysql-devel`
2. clone the repo & cd into it.
3. Create a virtual environment for installing dependencies:
   <br/><nbsp/>`python3 -m venv project_name_venv`
4. Source the virtual environment:
   <br/><nbsp/>`source project_name_venv/bin/activate`
5. Install the dependencies in the virtual environment:
   <br/><nbsp/>`pip install -r requirements.txt`

## Setting up DB

1. create the .env file in the project root directory and set the values:

   ```markdown
   SECRET_KEY=
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   ```

2. Run migrations
   <br/><nbsp/>`python manage.py migrate`

## Running the Server

1. Run the server:
   <br/><nbsp/>`python manage.py runserver`

## Running Unit Tests

<nbsp/>`./manage.py test backend`

## View api documentation

- Run <br/>`./manage.py runserver`
- Visit <br/>`http://127.0.0.1:8000/api/v1/swagger-ui`

## Note:

> A custom user model is used to make the email to be used as the username.
> <br/> ...

# Running with docker & docker-compose, gunicorn, nginx

1. Make sure you have docker and docker-compose installed
2. Set the following env vars in the .env file
   ```markdown
   DB_HOST=db   # should be same as the service name defined in docker-compose.yaml
   
   MYSQL_DATABASE=<YOUR_DB_NAME>
   MYSQL_ROOT_PASSWORD=<YOUR_DB_PASSWORD>
   
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   ```
3. Run <br/>
   `docker compose up` <br/> or <br/>
   `docker compose up -d` for running in the background
4. Visit <br/>
   `http://127.0.0.1:1337/api/v1/swagger-ui`
5. For clean up, run <br/>
   `docker compose down -v`
