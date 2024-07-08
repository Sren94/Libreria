# Generated by Django 5.0.4 on 2024-05-04 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0002_alter_author_options'),
        ('libro', '0014_alter_book_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autor.author'),
        ),
    ]