# Generated by Django 5.0.1 on 2024-03-07 15:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
