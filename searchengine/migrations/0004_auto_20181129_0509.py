# Generated by Django 2.1.3 on 2018-11-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0003_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='page',
            name='pagetitle',
            field=models.CharField(default='', max_length=100),
        ),
    ]
