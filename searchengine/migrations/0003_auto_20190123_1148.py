# Generated by Django 2.2.dev20181228003414 on 2019-01-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0002_book_numpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='books_download',
            field=models.FileField(blank='True', upload_to='books_dataset'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]