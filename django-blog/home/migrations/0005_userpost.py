# Generated by Django 3.0 on 2020-05-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_books_homeintro'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
