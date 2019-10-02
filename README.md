# Review-System
A simple review form using Django model forms to get comments from people visiting the site.

How to add this to your Project
1. Install django and django-admin and start a new django project 
  (Google how to start a new django project if you are new to this:  https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
2. Clone this repo by getting zip other using git clone. 
3. Copy the review folder into your project folder. 
4. Open settings.py file of your project and add review to INSTALLED_APPS. 
5. Copy urls from urls.py in review_form folder and add them to your projects urls.py or include review_form.urls to in your urls.py (You can name the urls according to your choice)
6. Makemigrations, and migrate and then runserver using following commands :
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  (if this gives any error, make sure you are in right directory and all the requirements are fullfilled, use python3 instead of python if you also have python2 installed in your system. 
7. Feel free to contact me, if you still have any difficulty runnning this. 
