# Generated by Django 3.2.7 on 2021-09-13 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FriendApp', '0003_auto_20210913_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]