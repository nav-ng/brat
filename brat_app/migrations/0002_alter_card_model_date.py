# Generated by Django 4.2 on 2023-05-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brat_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card_model", name="date", field=models.IntegerField(),
        ),
    ]
