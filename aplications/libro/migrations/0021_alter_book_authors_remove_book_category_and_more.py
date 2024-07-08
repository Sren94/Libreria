# Generated by Django 5.0.4 on 2024-05-04 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_alter_author_options'),
        ('libro', '0020_remove_book_authors_alter_book_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='categoria_autor', to='autor.author'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_libro', to='libro.category'),
        ),
    ]
