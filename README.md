# django-jwt-user
Basic default user with JWT authentication. You can download this code and use as it is in any large scale project with less configuration.


Project Setup
------------------
1. Required Python Version
    1. `Python 3.6 or later`
2. Install required python3 packages
    1. `python3.# -m pip install -r requirements.txt`
3. Migrate Database
    1. `python3.# manage.py makemigrations`
    2. `python3.# manage.py migrate`
4. Create superuser to use admin panel(optional)
    1. `python3.# manage.py createsuperuser`
5. Run Django server (default host is 127.0.0.1 and port is 8000)
    1. `python3.# manage.py runserver`
6. Change EMAIL settings `project/project/settings.py` to register using the API.


API Endpoints
------------------
1. `admin/` - to access admin panel
2. `api/user/token` - to login (generates access-token and refresh-token)
3. `api/user/token/refresh` - to generate a new access-token from refresh-token
4. `api/user/token/verify` - verifies the access-token (optional)
5. `api/user/logout` - to logout the user from application
6. `api/user/register` - to register a new user in the application
7. `api/user/details` - to get the user details


Production Settings
------------------
Settings file location `project/project/settings.py`

Set **DEBUG** to *False* when deploying in production server.

Change the **SECRET_KEY** values with random strings.

If your front-end is running from different host add the host name in **ALLOWED_HOSTS**.

Feel free to change access-token and refresh-token expire time in *ACCESS_TOKEN_LIFETIME* and *REFRESH_TOKEN_LIFETIME* in **SIMPLE_JWT**.

If your frontend is running from a different domain, add your domain in **CORS_ORIGIN_WHITELIST** and **CSRF_TRUSTED_ORIGINS** to whitelist your domain from CORS restrictions.

You can allow `cache-control` header from browser by adding `cache-control` to the **CORS_ALLOW_HEADERS** list.

Allow or restrict HTTP request methods by modifying **CORS_ALLOW_METHODS** list.

Change *DEFAULT_FROM_EMAIL*, *SERVER_EMAIL*, *EMAIL_BACKEND*, *EMAIL_HOST*, *EMAIL_USE_TLS*, *EMAIL_PORT*, *EMAIL_HOST_USER*, *EMAIL_HOST_PASSWORD* to setup your email.


LICENSE
------------------
This software is licenced under Apache License Version 2.0, January 2004.
http://www.apache.org/licenses/
