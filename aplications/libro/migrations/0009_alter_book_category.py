# Generated by Django 5.0.4 on 2024-05-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0008_remove_book_category_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='category_author', to='libro.category'),
        ),
    ]
