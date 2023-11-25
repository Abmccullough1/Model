# Generated by Django 4.2.6 on 2023-11-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('release_year', models.IntegerField()),
                ('main_genre', models.TextField()),
                ('developer', models.TextField()),
                ('main_character', models.TextField()),
            ],
        ),
    ]
