# Generated by Django 4.0.2 on 2022-03-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
    ]
