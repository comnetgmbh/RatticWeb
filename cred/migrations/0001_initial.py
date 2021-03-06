# Generated by Django 2.2.2 on 2019-11-12 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('url', models.URLField(blank=True, db_index=True, null=True)),
                ('username', models.CharField(blank=True, db_index=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('descriptionmarkdown', models.BooleanField(default=False, verbose_name='Markdown Description')),
                ('description', models.TextField(blank=True, null=True)),
                ('iconname', models.CharField(default='Key.png', max_length=64, verbose_name='Icon')),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('modified', models.DateTimeField(db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ssh_key_name', models.CharField(blank=True, max_length=64, null=True)),
                ('attachment_name', models.CharField(blank=True, max_length=64, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('groups', models.ManyToManyField(blank=True, default=None, related_name='child_creds', to='auth.Group')),
                ('latest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='cred.Cred')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CredChangeQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cred', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cred.Cred')),
            ],
        ),
        migrations.CreateModel(
            name='CredAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audittype', models.CharField(choices=[('A', 'Added'), ('C', 'Changed'), ('M', 'Only Metadata Changed'), ('V', 'Only Details Viewed'), ('X', 'Exported'), ('D', 'Deleted'), ('S', 'Scheduled For Change'), ('P', 'Password Viewed')], max_length=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('cred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='cred.Cred')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credlogs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-time',),
                'get_latest_by': 'time',
            },
        ),
        migrations.AddField(
            model_name='cred',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='child_creds', to='cred.Tag'),
        ),
    ]
