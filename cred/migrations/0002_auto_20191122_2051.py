# Generated by Django 2.2.6 on 2019-11-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cred', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cred',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='not required'),
        ),
        migrations.AddField(
            model_name='cred',
            name='ssh_key',
            field=models.FileField(blank=True, null=True, upload_to='not required'),
        ),
    ]