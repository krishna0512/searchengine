# Generated by Django 2.2.dev20181228003414 on 2019-01-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0004_auto_20190123_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='books_download',
        ),
        migrations.AddField(
            model_name='book',
            name='book_pdf',
            field=models.FileField(blank=True, upload_to='book_pdf'),
        ),
    ]
