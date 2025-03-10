# Generated by Django 5.0.6 on 2024-06-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=50, verbose_name='Maxsulot nomi')),
                ('photo', models.CharField(max_length=200, null=True, verbose_name='Rasm file_id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Narx')),
                ('description', models.TextField(max_length=3000, null=True, verbose_name='Tavsif')),
                ('category_code', models.CharField(max_length=20, verbose_name='Kategoriya kodi')),
                ('category_name', models.CharField(max_length=30, verbose_name='Kategoriya nomi')),
                ('subcategory_name', models.CharField(max_length=30, verbose_name='Ost-Kategoriya nomi')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True, verbose_name='Full name')),
                ('username', models.CharField(max_length=50, null=True, unique=True, verbose_name='Username')),
                ('telegram_id', models.PositiveBigIntegerField(unique=True, verbose_name='Telegram ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
