# Generated by Django 3.2 on 2024-10-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='event_date',
            field=models.DateField(),
        ),
    ]
