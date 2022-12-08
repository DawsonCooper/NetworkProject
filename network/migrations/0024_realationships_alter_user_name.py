# Generated by Django 4.1.2 on 2022-12-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_user_name_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realationships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followerId', models.IntegerField()),
                ('followingId', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='Incognito', max_length=24),
        ),
    ]
