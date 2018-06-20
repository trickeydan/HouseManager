# Generated by Django 2.0.6 on 2018-06-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('display_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('picture', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=20)),
                ('pronouns', models.CharField(max_length=30)),
                ('bio', models.TextField()),
            ],
        ),
    ]
