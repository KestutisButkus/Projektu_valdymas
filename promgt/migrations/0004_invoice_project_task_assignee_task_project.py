# Generated by Django 5.1.4 on 2024-12-17 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgt', '0003_remove_invoice_paid_remove_invoice_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_projects', to='promgt.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_assignees', to='promgt.employee'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_projects', to='promgt.project'),
        ),
    ]
