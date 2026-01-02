# DjangoDemo

Phase 1: Environment Setup (Windows Edition)
This was the trickiest part due to operating system differences.

Directory Creation: You ran mkdir Dev -> cd Dev -> mkdir trydjango.

Virtual Environment:

Video: Used virtualenv.

You: Used python -m venv . (The built-in Python tool, which is better for Windows).

Activation:

Video: Used source bin/activate.

You: Used Scripts\activate (Confirmed by the (trydjango) prefix in your terminal).

Phase 2: Project Creation (Skeleton)
Installing Django:

You encountered errors (No module named 'distutils' and 'cgi') because your Python version (3.13) was too new for the older Django version.

Solution: pip install --upgrade django (Upgraded to Django 5.x to fix compatibility).

Initializing the Project:

Command: django-admin startproject trydjango .

Key Detail: The dot . at the end was crucial to create manage.py in the current folder, avoiding nested directories.

Navigating Paths:

You successfully located manage.py by navigating into the src folder using cd src.

Phase 3: Database & Admin
First Migration:

Command: python manage.py migrate.

Result: Django generated the db.sqlite3 database file and set up the foundation (like user tables).

Creating a Superuser:

Command: python manage.py createsuperuser.

Note: The password input was invisible for security, which is normal behavior.

Phase 4: Developing Features (App & Models)
This is where the actual coding began.

Creating an App:

Command: python manage.py startapp products.

Result: Created a dedicated module for managing "products".

Defining the Model:

You wrote class Product... inside products/models.py.

Purpose: Told Django that a "Product" consists of a title, price, etc.

Syncing to Database:

python manage.py makemigrations (Created the blueprints).

python manage.py migrate (Built the actual tables in the database).


