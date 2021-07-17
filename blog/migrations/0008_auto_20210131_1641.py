# Generated by Django 3.1.2 on 2021-01-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210130_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Philosophy', 'philosophy'), ('Fotography', 'fotography'), ('Cinema', 'cinema'), ('Literature', 'literature'), ('Music', 'music'), ('Poetry', 'poetry'), ('Politics', 'politics'), ('Economics', 'economics'), ('Science', 'science'), ('Sports', 'sports'), ('Diversity', 'diversity')], default='Diversity', max_length=20),
        ),
    ]