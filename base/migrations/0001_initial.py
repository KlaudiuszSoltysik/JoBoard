# Generated by Django 4.1.2 on 2022-10-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_and_surname', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]