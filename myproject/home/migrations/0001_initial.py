# Generated by Django 4.2 on 2023-12-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=255)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
            ],
        ),
    ]