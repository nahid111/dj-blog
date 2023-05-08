# API using DRF
<hr/>

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
<nbsp/>`python manage.py test shop`