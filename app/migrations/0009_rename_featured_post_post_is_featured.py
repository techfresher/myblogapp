# Generated by Django 4.2.11 on 2024-04-04 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_subscribe_post_featured_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='featured_post',
            new_name='is_featured',
        ),
    ]
