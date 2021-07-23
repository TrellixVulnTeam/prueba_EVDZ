# Generated by Django 3.2.5 on 2021-07-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('paternal_last_name', models.CharField(max_length=200)),
                ('maternal_last_name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField()),
                ('rfc', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'management_persons',
            },
        ),
    ]
