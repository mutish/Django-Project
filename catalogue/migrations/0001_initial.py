# Generated by Django 4.1.7 on 2023-03-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_image', models.ImageField(upload_to='')),
                ('product_price', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'catalogue',
            },
        ),
    ]