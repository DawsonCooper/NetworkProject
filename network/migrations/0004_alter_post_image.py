# Generated by Django 4.1.2 on 2022-12-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_alter_user_bio_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images'),
        ),
    ]
