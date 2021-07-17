# Cs50web Final Project : ColetivoAmador

## What is it and why?

The idea was to make a site to replace a blog a few friends of mine use to run.
(this one: https://umcoletivoamador.blogspot.com/)

In this blog a group of authors write and publish articles on many subjects.
Among those : music, politics, philosophy, interviews, etc.

## Distinctivenes requirement

The javascript code used to load the article previews into the index was implemented in the same way as the network project. But other than that,
this project is very different from the previous one.

Context processors were used to load the most visited article of the week and the
latest music recommendation.

The django-hitcount library was used to keep track of how many visits a given
article receives.

The django-ckeditor library was used to allow authors to write articles with complex formatting and display images.

The django-crontab was used to check for new posts every day to send an email
to users subscribed to the newsletter. This functionality couldn't be fully tested
because django-crontab requires unix systems to work.

## What is in each file (inside the blog app)

Index.js is the javascript file that runs most of the application's front-end.
It is in charge of loading previews, full articles and animations.

layout.html defines the site's base structure, navbar and loads featured articles.
Index.html defines the site's heading and it is where the article_previews are loaded.

Also created in the blog app, "cron.py" contains the cronjob that sends
emails to subscribed users. And "context_processor.py" adds context processors
for featured articles and article categories on the navbar.

Util.py defines the "get_method_required" wrapper as well as "search_articles" and "send_email" functions.

## Instalation and how to run

Python-version : 3.6.9
run : "pip -r requirements.txt" to install the required packages
then : "python manage.py runserver" to run the application

## Final thoughts and considerations

I tried my best to make a responsive site and easy to navigate.
Also I decided to keep the article creation in the admin site as it would be
run by close friends. In any case an "Authors" group with the right permissions
was created to distinguish them from the admins.

One thing to keep in mind is that the version I'll submit won't be able to
send emails since it requires a gmail account and password to be saved in the source code.
