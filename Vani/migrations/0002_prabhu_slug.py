# Generated by Django 3.2.6 on 2021-09-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vani', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prabhu',
            name='slug',
            field=models.CharField(default='hare-krishna', max_length=60),
            preserve_default=False,
        ),
    ]