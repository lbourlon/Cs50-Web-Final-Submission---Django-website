from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import BooleanField, CharField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


# Create your models here.
class User(AbstractUser):
    newsletter = BooleanField(default = False)

CATEGORY_CHOICES = (
        ('philosophy', 'Philosophy'),
        ('fotography', 'Fotography'),
        ('cinema','Cinema'),
        ('literature', 'Literature'),
        ('music', 'Music'),
        ("poetry",'Poetry'),
        ("politics","Politics"),
        ("economics",'Economics'),
        ("science",'Science'),
        ("sports",'Sports'),
        ("diversity",'Diversity')
    )

def list_categories():
    """Return a list of every category that have at least one article"""
    return [category for category,_ in CATEGORY_CHOICES if len(Article.objects.filter(category=category)) != 0]

class Article(models.Model, HitCountMixin):
    title = models.CharField(max_length=80, default='Change this text before publishing')
    lead_image = models.ImageField(upload_to = "images", default='no_image.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    body = RichTextUploadingField(blank=True)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES, default='diversity')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateField()
    preview_text = models.TextField(max_length=300, default='Change this text before publishing')


    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return f"{self.title}, by {self.author}, id : {self.id}, publish_date : {self.pub_date}"

    def serialize(self):
        return{
            "id": self.id,
            "title":self.title,
            "preview_text":self.preview_text,
            "author":self.author.username,
            "body":self.body,
            "pub_date":self.pub_date.strftime("%b %#d %Y, %-I:%M %p"),
            "category":self.category
        }


