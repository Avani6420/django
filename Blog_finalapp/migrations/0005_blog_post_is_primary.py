# Generated by Django 3.2.7 on 2021-09-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_finalapp', '0004_alter_blog_post_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='is_primary',
            field=models.BooleanField(default=False),
        ),
    ]
