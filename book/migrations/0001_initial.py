# Generated by Django 4.0.2 on 2022-03-04 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('numberOfPage', models.IntegerField()),
                ('language', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookStats',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('importPrice', models.FloatField()),
                ('quantityLeft', models.IntegerField()),
                ('createAt', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('barcode', models.TextField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.publisher'),
        ),
    ]
