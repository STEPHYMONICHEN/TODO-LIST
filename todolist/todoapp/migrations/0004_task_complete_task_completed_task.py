# Generated by Django 5.0.4 on 2024-04-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_task_edited_at_alter_task_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='completed_task',
            field=models.BooleanField(default=False),
        ),
    ]
