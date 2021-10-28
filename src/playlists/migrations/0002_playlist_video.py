# Generated by Django 3.2.6 on 2021-08-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_alter_video_video_id'),
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.video'),
        ),
    ]
