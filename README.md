# App movies

## Run project

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

## App Features

1. [x] include a RESTful API
2. [X] A User can SIGN UP
3. [X] When a User SIGNS UP, it should create a new USER for the APPLICATION
4. [X] A User can LOG IN
5. [X] A User can LOG OUT
6. [X] A User can CREATE a new Movie
7. [X] A User can RETRIEVE a SINGLE
8. [X] A User can RETRIEVE a LIST of Movies
9. [X] A User can UPDATE a Movie
10. [X] A User can DELETE a Movie
11. [] A User can RETRIEVE a List of Recommended Movies