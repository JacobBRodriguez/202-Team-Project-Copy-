# Generated by Django 3.0.5 on 2020-11-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team_5', '0007_auto_20201124_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='Team_5.Listing'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]