# Generated by Django 5.1.2 on 2024-10-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=16)),
            ],
        ),
    ]
