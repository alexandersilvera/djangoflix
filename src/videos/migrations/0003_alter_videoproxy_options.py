# Generated by Django 3.2.6 on 2021-08-13 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videoproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoproxy',
            options={'verbose_name': 'Video Publicado', 'verbose_name_plural': 'Videos Publicados'},
        ),
    ]