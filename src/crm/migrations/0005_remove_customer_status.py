# Generated by Django 4.0.4 on 2022-04-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_remove_event_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='status',
        ),
    ]
