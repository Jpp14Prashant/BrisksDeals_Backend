# Generated by Django 4.1.6 on 2023-04-04 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brisk_app1', '0005_remove_vendorrequest_vendor_id_vendorrequest_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorbusinessdetails',
            name='vendor_token',
        ),
    ]
