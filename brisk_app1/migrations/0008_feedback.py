# Generated by Django 4.1.6 on 2023-04-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brisk_app1', '0007_remove_couponactive_payment_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(blank=True, max_length=70)),
                ('Customer_Email', models.CharField(blank=True, max_length=70)),
                ('Feedbacks', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
