# Generated by Django 2.0 on 2020-03-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('thumbnial', models.FileField(upload_to='media')),
            ],
            options={
                'db_table': 't_article',
            },
        ),
    ]
