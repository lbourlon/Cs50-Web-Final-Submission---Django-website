from .models import list_categories
from .models import Article 
import datetime 

def categories(request):
    categories = list_categories()
    return {'categories':categories}

def featured_articles(request):
    today = datetime.date.today()
    last_week = today + datetime.timedelta(days = -7)

    article_list = Article.objects.filter(pub_date__range = (last_week, today))

    #if no articles were published this week get the higest of all time
    if(len(article_list) == 0):
        article_list = Article.objects.all()

    highest_hit = 0
    return_article = Article.objects.filter(pk=1).first()

    for art in article_list:
        if(art.hit_count.hits > highest_hit):
            return_article = art
            highest_hit = art.hit_count.hits

    #most recent music article:
    music = Article.objects.filter(category="music").order_by('-pub_date').first()
    return {
        'article_of_the_week':return_article,
        'music_recom':music,
        }

