# Generated by Django 3.2.3 on 2021-06-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210603_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
