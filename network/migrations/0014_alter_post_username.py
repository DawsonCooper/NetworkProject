# Generated by Django 4.1.2 on 2022-12-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_remove_comment_user_id_remove_likes_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(default=None, max_length=24, null=True),
        ),
    ]
