# Generated by Django 3.2.3 on 2021-06-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('article', '0003_articlepage_author_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='banner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wagtailimages.image'),
        ),
    ]
