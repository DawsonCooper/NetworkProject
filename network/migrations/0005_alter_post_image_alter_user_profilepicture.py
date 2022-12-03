# Generated by Django 4.1.2 on 2022-12-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='network/static/images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profilePicture',
            field=models.ImageField(blank=True, default='def_profile_pic.jpg', null=True, upload_to='network/static/images'),
        ),
    ]
