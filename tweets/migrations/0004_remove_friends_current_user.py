# Generated by Django 2.2.2 on 2019-08-05 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_friends_current_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='current_user',
        ),
    ]
