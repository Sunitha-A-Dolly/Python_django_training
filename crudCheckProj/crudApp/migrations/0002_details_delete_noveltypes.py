# Generated by Django 4.1.3 on 2022-12-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='NovelTypes',
        ),
    ]
