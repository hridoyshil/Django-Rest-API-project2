# Generated by Django 4.2.6 on 2023-10-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiquest',
            name='course_duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='aiquest',
            name='seat',
            field=models.IntegerField(),
        ),
    ]
