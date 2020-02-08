# django-jwt-user
Basic default user with JWT authentication. You can download this code and use as it is in any large scale project with less configuration.


Project Setup
--------------
1. Required Python Version
    1. `Python 3.6 or later`
2. Install required python3 packages
    1. `python3.# -m pip install -r requirements.txt`
3. Migrate Database
    1. `python3.# manage.py makemigrations`
    2. `python3.# manage.py migrate`
4. Create superuser to use admin panel(optional)
    1. `python3.# manage.py createsuperuser`
7. Run Django server (default host is 127.0.0.1 and port is 8000)
    1. `python3.# manage.py runserver`


API Endpoints
----------------
1. `admin/` - to access admin panel
2. `api/user/token` - to login (generates access-token and refresh-token)
3. `api/user/token/refresh` - to generate a new access-token from refresh-token
4. `api/user/token/verify` - verifies the access-token (optional)
5. `api/user/logout` - to logout the user from application
6. `api/user/register` - to register a new user in the application
7. `api/user/details` - to get the user details


LICENSE
------------------
This software is licenced under Apache License Version 2.0, January 2004.
http://www.apache.org/licenses/
