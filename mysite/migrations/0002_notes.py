# Generated by Django 3.1.3 on 2021-01-09 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('myfile', models.FileField(upload_to='upload')),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
    ]
