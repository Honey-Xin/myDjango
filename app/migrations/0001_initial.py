# Generated by Django 2.2.26 on 2023-02-04 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auThor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField(max_length=11, verbose_name='作者ID')),
                ('auThor_name', models.CharField(max_length=255, verbose_name='姓名')),
                ('auThor_sex', models.CharField(max_length=20, verbose_name='性别')),
                ('auThor_birthy', models.CharField(max_length=255, null=True, verbose_name='出生年月')),
                ('auThor_phone', models.IntegerField(max_length=11, verbose_name='纤细方式')),
            ],
        ),
        migrations.CreateModel(
            name='arTicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arTicle_id', models.IntegerField(max_length=11, verbose_name='剧本ID')),
                ('arTicle_name', models.CharField(max_length=255, verbose_name='剧本名')),
                ('arTicle_theme', models.CharField(max_length=255, verbose_name='剧本主题')),
                ('arTicle_content', models.CharField(max_length=10000, verbose_name='剧本内容')),
                ('arTicle_score', models.IntegerField(max_length=11, verbose_name='剧本得分')),
                ('arTicle_auThor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.auThor')),
            ],
        ),
    ]
