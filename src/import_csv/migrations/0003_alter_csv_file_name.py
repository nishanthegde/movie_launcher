# Generated by Django 4.0.6 on 2022-08-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_csv', '0002_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to=''),
        ),
    ]
