# Generated by Django 3.0.5 on 2020-04-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20200425_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='details',
            field=models.CharField(blank=True, default='No details provided.', max_length=150, null=True),
        ),
    ]
