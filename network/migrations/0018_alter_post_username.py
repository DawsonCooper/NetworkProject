# Generated by Django 4.1.2 on 2022-12-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_alter_post_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, default='None', max_length=24, null=True),
        ),
    ]
