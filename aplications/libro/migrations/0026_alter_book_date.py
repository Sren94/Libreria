# Generated by Django 5.0.4 on 2024-05-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0025_alter_book_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(default=True, verbose_name='Fecha De Lanzamiento'),
        ),
    ]