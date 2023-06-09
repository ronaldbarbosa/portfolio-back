# Generated by Django 4.2 on 2023-04-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('frontend', models.CharField(blank=True, max_length=150, null=True)),
                ('backend', models.CharField(blank=True, max_length=150, null=True)),
                ('devops', models.CharField(blank=True, max_length=150, null=True)),
                ('url', models.URLField()),
                ('image', models.URLField()),
                ('finished', models.BooleanField(default=True)),
            ],
        ),
    ]
