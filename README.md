# Blockchain Analytics tool using Django

## Installation
#### Clone the repository to your local machine:
``git clone your-git-repo``  
#### Install Python 3, if you don't have it installed:
* https://www.python.org/downloads/
#### Create and activate a virtual environment:
* `python3 -m venv env`
* `source env/bin/activate`
#### Install necessary packages:
* `pip install -r requirements.txt`
#### Create PostgreSQL database:
* https://www.postgresqltutorial.com/postgresql-getting-started/
* https://docs.djangoproject.com/en/4.0/ref/settings/#databases
### Create chart js
* https://www.jsdelivr.com/package/npm/chart.js
* https://www.chartjs.org/docs/latest/
#### Configure database in settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_pasword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
#### Run database migrations:
* `python manage.py migrate`
## Usage
1. #### Run the application
    `python manage.py runserver` 
2. #### Go to browser and type `localhost:8000`
## Examples
