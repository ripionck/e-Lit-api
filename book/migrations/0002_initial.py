# Generated by Django 5.0.1 on 2024-03-07 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.publisher'),
        ),
    ]
