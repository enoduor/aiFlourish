# Generated by Django 4.2.4 on 2024-01-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oduor', '0008_alter_stuffs_website_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuffs',
            name='ad',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='stuffs',
            name='website_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
