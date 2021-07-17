from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

import datetime

from hitcount.models import HitCount
from hitcount.views import HitCountMixin


from . import util
from .models import User, Article

def index(request):
    return render(request, "blog/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "blog/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blog/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "blog/register.html")


def article(request, article_id):
    """Render an article"""
    article = Article.objects.filter(pk = article_id).first()

    increment_view(request, article_id)

    return render(request,"blog/article.html", {
        "article":article,
    })

@util.get_method_required
def load_article(request, article_id):
    article = Article.objects.filter(pk = article_id).first()
    return JsonResponse(article.serialize())


@util.get_method_required
def load_articles(request, category, page, search_str):
    """takes in a category and page, returns the articles"""

    start_date = datetime.date(2005,1,1)
    end_date = datetime.date.today()

    if(search_str == "no-search"):
        articles = Article.objects.all()
    
    else:
        articles = util.search_articles(search_str)
        
    if(category != "all"): articles = articles.filter(category = category)

    #don't return the articles that aren't yet published
    articles = articles.filter(pub_date__range = (start_date, end_date))

    #order by reverse publish date (most recent articles on top)
    articles = articles.order_by('-pub_date')

    if(len(articles) == 0):
        return JsonResponse({"error":"No such articles"}, status = 404)

    paginator = Paginator(articles, 5)
    return_articles = paginator.page(page)

    return JsonResponse({
        'number_of_pages':paginator.num_pages,
        'articles':[article.serialize() for article in return_articles]
    })

@util.get_method_required
def increment_view(request, article_id):
    article = Article.objects.filter(pk=article_id).first()
    hit_count = HitCount.objects.get_for_object(article)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    
    return JsonResponse(hit_count_response, status = 200, safe = False)




def newsletter(request):
    # user = User.objects.get(pk=user_id)

    user = request.user
    
    if (user.newsletter == False):
        user.newsletter =  True
        user.save()
        return JsonResponse({"success":'You are now subscribed to the newsletter'}, status =200)

    else:
        user.newsletter = False
        user.save()
        return JsonResponse({"success":'You are now unsubscribed to the newsletter'}, status =200)
