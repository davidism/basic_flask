Basic Flask
===========

This sample project shows how I organize a project to use Flask,
Flask-SQLAlchemy, and Alembic together.  It demonstrates the application
factory pattern and is organized using blueprints.

Demonstrating migration generation
----------------------------------

I used Alembic to autogenerate a migration and then tweaked the results.  If you
want to see autogeneration in action, just delete
`alembic/versions/35b593d48d6a_user_models.py`, then run
`alembic revision --autogenerate -m "user models"`.

Set up the database
-------------------

Change `basic_app.config.SQLALCHEMY_DATABASE_URI` to what you want.  By default
it points to a sqlite file called `app.db` in the project folder.

Then run `alembic upgrade head` to set up the database through migrations.

Or, permform the following from a Python shell.

    In [1]: from basic_app import create_app, db
    In [2]: create_app().app_context().push()
    In [3]: db.create_all()

Then run `alembic stamp head` to mark migrations as current.

Origin
------

Created in answer to this question on /r/flask and StackOverflow:

* [\[AF\] Has anyone ever gotten Alembic to work with Flask Blueprints? \[SQLAlchemy\]](http://www.reddit.com/r/flask/comments/1h1k5g/af_has_anyone_ever_gotten_alembic_to_work_with/)
* [Alembic autogenerates empty Flask-SQLAlchemy migrations](http://stackoverflow.com/questions/17201800/alembic-autogenerates-empty-flask-sqlalchemy-migrations)
