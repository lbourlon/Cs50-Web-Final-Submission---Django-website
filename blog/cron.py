from . import util
from .models import Article, User
import datetime

def check_for_new_articles():
    print("Checking for new Articles:", end=" ")
    today = datetime.date.today()
    todays_articles = Article.objects.filter(pub_date = today)

    if(len(todays_articles) != 0):
        print("Articles found! Sending Emails to the subscribed users")
        subscribed_users = User.objects.filter(newsletter = True)
        for user in subscribed_users:
            util.send_mail(user.email)
    else:
        print("No new Articles released today")