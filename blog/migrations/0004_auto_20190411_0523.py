# Generated by Django 2.1.7 on 2019-04-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date_added',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='blog',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
