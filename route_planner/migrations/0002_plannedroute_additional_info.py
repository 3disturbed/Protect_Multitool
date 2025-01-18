# Generated by Django 5.1.5 on 2025-01-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plannedroute',
            name='additional_info',
            field=models.CharField(blank=True, help_text='Any further information that may be useful', max_length=1000, null=True, verbose_name='Additional information'),
        ),
    ]