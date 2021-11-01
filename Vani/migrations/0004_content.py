# Generated by Django 3.2.6 on 2021-09-01 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vani', '0003_prabhu_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9000)),
                ('image', models.ImageField(upload_to='photos/')),
                ('prabhu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vani.prabhu')),
            ],
        ),
    ]
