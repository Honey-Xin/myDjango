# Generated by Django 2.2.26 on 2023-02-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='arTicle_id',
        ),
        migrations.RemoveField(
            model_name='author',
            name='author_id',
        ),
        migrations.AlterField(
            model_name='author',
            name='auThor_phone',
            field=models.IntegerField(max_length=11, null=True, verbose_name='联系方式'),
        ),
    ]
