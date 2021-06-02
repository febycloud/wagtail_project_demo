# Generated by Django 3.2.3 on 2021-06-02 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorpage',
            name='author_pic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wagtailimages.image'),
        ),
        migrations.DeleteModel(
            name='AuthorImage',
        ),
    ]
