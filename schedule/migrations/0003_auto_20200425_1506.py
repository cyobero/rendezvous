# Generated by Django 3.0.5 on 2020-04-25 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200425_1506'),
        ('schedule', '0002_auto_20200425_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='rendezvous',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserProfile'),
        ),
    ]
