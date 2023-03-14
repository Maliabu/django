## Django Admin Login Credentials
- url:  http://127.0.0.1:8000/admin/
- username: admin
- password: admin@cyanase2023
## making migartion if you made changes to models
- python manage.py makemigrations
- python manage.py sqlmigrate api 0004 
- python manage.py migrate
Where `0004` is the migration code of the api app it will be generated automatically when you run `python manage.py makemigrations`
