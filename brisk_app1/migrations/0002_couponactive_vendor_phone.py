# Generated by Django 4.1.6 on 2023-03-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brisk_app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponactive',
            name='Vendor_Phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
