# Generated by Django 2.2.dev20181228003414 on 2019-01-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0007_book_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_pdf',
            field=models.FileField(blank=True, upload_to='book_pdf'),
        ),
    ]