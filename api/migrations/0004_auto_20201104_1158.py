# Generated by Django 3.1.1 on 2020-11-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201103_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_status',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public', max_length=10, verbose_name='Profile status'),
        ),
    ]