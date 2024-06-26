# Generated by Django 4.2.11 on 2024-03-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]
