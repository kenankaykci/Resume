# Generated by Django 5.0.2 on 2024-05-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='job_information',
            field=models.CharField(blank='', default='', max_length=254, verbose_name='Job Information'),
        ),
    ]