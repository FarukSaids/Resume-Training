# Generated by Django 5.1.3 on 2024-12-23 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_document_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ('order',), 'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'ordering': ('order',), 'verbose_name': 'Social Media', 'verbose_name_plural': 'Social Medias'},
        ),
    ]
