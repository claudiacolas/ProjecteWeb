# Generated by Django 4.2.1 on 2023-05-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alcohol_date_alcohol_user_brand_date_brand_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='combination',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mycombinations'),
        ),
    ]
