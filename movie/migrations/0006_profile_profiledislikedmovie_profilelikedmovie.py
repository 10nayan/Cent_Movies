# Generated by Django 3.1 on 2020-08-31 04:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0005_auto_20200807_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileLikedMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Liked_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_later', to='movie.movies')),
                ('ProfileLinked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userliked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDislikedMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dislike_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dislike_later', to='movie.movies')),
                ('ProfileLinked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdisliked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfileLinked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('Watch_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watch_later', to='movie.movies')),
            ],
        ),
    ]
