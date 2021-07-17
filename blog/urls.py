from django.urls import path
from django.urls.conf import include, re_path
from . import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import include, re_path


urlpatterns = [

    #auth views:
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),


    #alternative routes
    path("article/<int:article_id>", views.article, name ="article"),

    #api routes:
    path("articles/<str:category>/<int:page>/<str:search_str>", views.load_articles, name = "load_articles"),
    path("single_article/<int:article_id>", views.load_article, name ="load_article"),
    path("increment_view/<int:article_id>", views.increment_view, name ="increment_view"),
    path('newsletter/', views.newsletter, name = 'newsletter'),

   
    #others:
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/images/favicon.ico'))),
    path(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    ]