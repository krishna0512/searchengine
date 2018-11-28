How to change from sqlite3 to postgresql
Reference Link: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
Make sure postgresql is installed in your ubuntu system, then
$ sudo su - postgres
$ psql
<postgres $> CREATE DATABASE searchengine;
<postgres $> CREATE USER krishna WITH PASSWORD 'kkrishna';
<postgres $> ALTER ROLE krishna SET client_encoding TO 'utf8';
<postgres $> ALTER ROLE krishna SET default_transaction_isolation TO 'read committed';
<postgres $> ALTER ROLE krishna SET timezone TO 'UTC';
<postgres $> GRANT ALL PRIVILEGES ON DATABASE searchengine TO krishna;
<postgres $> \q
$ pip install psycopg2
If this is giving the warning then install
$ pip install psycopg2-binary
Change the DATABASES dict in SETTINGS.py to 
	DATABASES = {
	    'default': {
	        'ENGINE': 	'django.db.backends.postgresql_psycopg2',
	        'NAME': 	'searchengine',
	        'USER': 	'krishna',
	        'PASSWORD': 'kkrishna',
	        'HOST': 	'localhost',
	        'PORT': 	'',
	    }
	}
