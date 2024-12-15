# Generated by Django 5.1.3 on 2024-12-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', max_length=254, verbose_name='Link')),
                ('icon', models.CharField(blank=True, default='', max_length=254, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Medias',
                'ordering': ['order'],
            },
        ),
    ]