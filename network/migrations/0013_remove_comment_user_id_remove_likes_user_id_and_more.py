# Generated by Django 4.1.2 on 2022-12-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_rename_user_comment_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='likes',
            name='username',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.IntegerField(default=None),
        ),
    ]
