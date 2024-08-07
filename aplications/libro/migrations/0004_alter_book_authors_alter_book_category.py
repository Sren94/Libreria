# Generated by Django 5.0.4 on 2024-05-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_alter_author_options'),
        ('libro', '0003_alter_category_options_alter_book_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='author_book', to='autor.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='category_book', to='libro.category'),
        ),
    ]
