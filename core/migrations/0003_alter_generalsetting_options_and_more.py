# Generated by Django 5.0.2 on 2024-05-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameter',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
