# Generated by Django 4.0 on 2023-03-14 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userprofile_languag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='languag',
            new_name='language',
        ),
    ]