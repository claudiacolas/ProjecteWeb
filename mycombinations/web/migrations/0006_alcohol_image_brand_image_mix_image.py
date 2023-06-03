# Generated by Django 4.2.1 on 2023-06-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_combination_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcohol',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mycombinations'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mycombinations'),
        ),
        migrations.AddField(
            model_name='mix',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mycombinations'),
        ),
    ]