# Generated by Django 4.1.7 on 2023-02-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_author_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
