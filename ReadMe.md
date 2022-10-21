# SaveMySnippet Web App (Back-end)

A web app to save and manage daily use code snippets. Snippets can be organized into folders. It contains Sort and Filter functionality to access Snippets.

Front-end repository can be found [here](https://github.com/ujjaval-shah/save-my-snippet).

## Environment

```
Python                      3.7.7
djangorestframework         3.11.1
Django                      2.2.11
```

## Setup

- Download the repository.
- Steps to create the database are as follows.

```cmd
python manage.py makemigrations
python manage.py makemigrations snips
python manage.py migrate
```

- If you want to create the superuser (optional)

```cmd
python manage.py createsuperuser
```

- When you open the app (ui) for the first time: Go to Edit Languages tab and Add all languages at once.

## Run

```cmd
python manage.py runserver
```
