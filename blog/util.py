from django.http.response import JsonResponse
from django.db.models import Q
from django.utils.html import escape

from .models import Article
import datetime

import smtplib, ssl

def get_method_required(function):
    """decorator to make sure the incomming request if of type GET"""
    def wrapper(request, *args, **kwargs):
        if request.method != 'GET':
            return JsonResponse({"error": "GET request required!"}, status = 400)
        else:
            return function(request, *args, **kwargs)

    return wrapper



def search_articles(search_str):
    """Search the articles by title or by author"""
    safe_search_str = escape(search_str)

    results  = Article.objects.filter(Q(title__icontains = safe_search_str) | Q(author__username__icontains = safe_search_str))

    return results




#source : https://realpython.com/python-send-email/
def send_mail(receiver_email):
    """Sends an email to a receiver with the newest article"""
    print("got here")

    smtp_gmail_port = 465

    password = "Obviously not The Actual Password"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", smtp_gmail_port, context=context) as server:
        server.login("django.projeto.123@gmail.com", password)

        sender_email = "django.projeto.123@gmail.com"
        receiver_email = receiver_email

        message = """\
        Subject: There is a new article in the ColetivoAmador Site!

        Come and check it out!
        link : site link...

        """

        server.sendmail(sender_email, receiver_email, message)

        server.quit()
