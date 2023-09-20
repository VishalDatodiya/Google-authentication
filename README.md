# React setup

## create the client id and secret key console.developers.google.com

    npx create-react-app react-google-auth

    cd react-google-auth

    npm install @react-oauth/google@latest --force

## put the url in google authenticate uurl in console.developers.google.com

    http://localhost:3000
    http://localhost

    npm start

# DRF project setup

    python -m venv env
    env\scripts\activate

    pip install django djangorestframework djangorestframework-simplejwt requests
    django-admin startproject DRFGoogleAuth
    cd DRFGoogleAuth

    python manage.py startapp authapi

    python manage.py makemigrations
    python manage.py migrate

    python manage.py runserver

# Testing in postman

    http://localhost:8000/api/google-auth/

    method : POST

    body -> raw -> JSON

    {
        "token" : "from browser inspect-> console and copy token and past here"
    }

    You will get email, name and user_id
