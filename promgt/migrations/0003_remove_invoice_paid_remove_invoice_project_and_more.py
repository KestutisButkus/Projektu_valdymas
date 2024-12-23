# Generated by Django 5.1.4 on 2024-12-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgt', '0002_remove_project_invoices_remove_project_tasks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='project',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='invoices',
            field=models.ManyToManyField(related_name='project_invoices', to='promgt.invoice'),
        ),
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.ManyToManyField(related_name='project_tasks', to='promgt.task'),
        ),
    ]
