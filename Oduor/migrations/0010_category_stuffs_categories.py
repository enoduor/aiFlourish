# Generated by Django 4.2.4 on 2024-01-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oduor', '0009_alter_stuffs_ad_alter_stuffs_website_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='stuffs',
            name='categories',
            field=models.ManyToManyField(to='Oduor.category'),
        ),
    ]
