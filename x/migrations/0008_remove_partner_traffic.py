# Generated by Django 4.0.4 on 2022-11-06 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0007_alter_partner_options_alter_quota_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='traffic',
        ),
    ]