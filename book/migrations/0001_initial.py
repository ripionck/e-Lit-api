# Generated by Django 5.0.1 on 2024-02-17 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('publisher', '0002_alter_publisher_is_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('cover', models.ImageField(default='default.jpg', upload_to='book/covers/')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('edition', models.CharField(max_length=100)),
                ('page_count', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publisher.publisher')),
            ],
        ),
    ]
