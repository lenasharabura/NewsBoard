# News board API

## Simple REST API build with Django-rest-framework
- API allows you to authenticate your users with Token authentication.
- Authenticated users can add posts to news board. Every such post has title, link and upvotes count (which initialized with zero value), author name and time of publication setted automatically.
- Users can edit and delete own posts.
- Authenticated users can leave comments for posts. Comment contain author name, time of publication(setted automatically) and text of comment.
- Users can edite own comments.
- Authenticated users can upvote posts (for each post once)

### Check Postman documentation:
https://documenter.getpostman.com/view/18107741/UV5f8E9M

### Currently running on Heroku:

It uses WhiteNoise for static files, Gunicorn as wsgi server, Heroku Postgres as DB, Redis cloud from redislabs.com as message broker.

#

## Running locally:

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example.env):
and change file name to .env:

`SECRET_KEY`<br />

`DB_NAME`<br />
`DB_USER`<br />
`DB_PASSWORD`<br />

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Run app:

`python3 manage.py runserver`
