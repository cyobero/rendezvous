# Generated by Django 3.0.5 on 2020-04-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200425_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='default-profile.png', null=True, upload_to='images/'),
        ),
    ]
