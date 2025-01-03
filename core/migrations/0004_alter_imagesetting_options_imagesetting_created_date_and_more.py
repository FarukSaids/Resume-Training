# Generated by Django 5.1.3 on 2024-11-27 20:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_imagesetting_alter_generalsetting_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesetting',
            options={'ordering': ['name'], 'verbose_name': 'Image Setting', 'verbose_name_plural': 'Image Settings'},
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesetting',
            name='updated_date',
            field=models.DateField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AlterField(
            model_name='imagesetting',
            name='file',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image'),
        ),
    ]
