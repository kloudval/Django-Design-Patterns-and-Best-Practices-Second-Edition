# Generated by Django 2.0 on 2018-01-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('desc', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
