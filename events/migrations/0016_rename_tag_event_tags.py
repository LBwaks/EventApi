# Generated by Django 4.1 on 2022-10-07 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_alter_event_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='tag',
            new_name='tags',
        ),
    ]