# Generated by Django 4.1.7 on 2023-03-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0002_alter_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Возраст'),
            preserve_default=False,
        ),
    ]
