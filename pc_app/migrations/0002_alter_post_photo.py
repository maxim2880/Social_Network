# Generated by Django 4.1.7 on 2023-03-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='Изображение к посту'),
        ),
    ]
