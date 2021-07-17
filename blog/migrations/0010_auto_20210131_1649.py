# Generated by Django 3.1.2 on 2021-01-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210131_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('philosophy', 'Philosophy'), ('fotography', 'Fotography'), ('cinema', 'Cinema'), ('literature', 'Literature'), ('music', 'Music'), ('poetry', 'Poetry'), ('politics', 'Politics'), ('economics', 'Economics'), ('science', 'Science'), ('sports', 'Sports'), ('diversity', 'Diversity')], default='diversity', max_length=20),
        ),
    ]
