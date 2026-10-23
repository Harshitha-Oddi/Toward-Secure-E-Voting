first create database blockchain_voting_db; in my sql
then open cmd activate env voting_venv\Scripts\activate
then install req which is pip install -r requirements.txt
now install ganache app and open and quickstart
now open second cmd activate envi and run python test_ganache_connection.py
thin in the previous one continue with these steps
then python manage.py makemigrations
then python manage.py migrate
now run python check_users.py
now run python manage.py runserver

you must register all the voters you wont get predefined voters
admin id
admin123 pass
admin id
admin123 pass
