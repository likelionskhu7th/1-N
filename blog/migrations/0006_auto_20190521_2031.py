# Generated by Django 2.2.1 on 2019-05-21 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
    ]