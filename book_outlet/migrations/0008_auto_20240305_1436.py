# Generated by Django 2.2.12 on 2024-03-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0007_auto_20240305_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='published_country',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
    ]
