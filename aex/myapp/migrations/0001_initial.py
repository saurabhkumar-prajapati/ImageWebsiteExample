# Generated by Django 3.1.7 on 2021-03-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
