# Search Engine

Search Engine is a local project for OCR portal (IIITH) , collection of data of different languages.

## Installation


First step is to download elasticsearch and then django.
Main motto was to integrate the effective search by django and elasticsearch together.
Elasticsearch is an open source search engine which is known for its fast indexing , page ranking and ability to retrieve different languages like urdu , hindi , german , french , punjabi etc...

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Configuring Database

Install postgres using apt or yum
then, follow following steps to configure the postgres database.

Or to host it use dbsqlite3(preon)

```bash
sudo su - postgres
psql
```

```sql
CREATE DATABASE searchengine;
CREATE USER username WITH PASSWORD 'password';
ALTER ROLE username SET client_encoding TO 'utf8';
ALTER ROLE username SET default_transaction_isolation TO 'read committed';
ALTER ROLE username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE searchengine TO username;
\q
```

```bash
pip install psycopg2
```

If there is a warning stating while launching the django server then,

```bash
pip install psycopg2-binary
```

Change the DATABASE dict in settings.py to
```python
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'searchengine', 'USER': 'username', 'PASSWORD': 'password', 'HOST': 'localhost', 'PORT': '', } }
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
