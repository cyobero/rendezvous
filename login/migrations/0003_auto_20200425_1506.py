# Generated by Django 3.0.5 on 2020-04-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20200425_1313'),
        ('login', '0002_auto_20200425_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='appointments',
            field=models.ManyToManyField(blank=True, null=True, related_name='appointments', to='schedule.Appointment'),
        ),
    ]