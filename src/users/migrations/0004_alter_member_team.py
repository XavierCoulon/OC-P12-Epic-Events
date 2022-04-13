# Generated by Django 4.0.4 on 2022-04-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_member_is_admin_alter_member_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.CharField(choices=[('P', 'Support'), ('S', 'Sales'), ('A', 'Admin')], max_length=64),
        ),
    ]