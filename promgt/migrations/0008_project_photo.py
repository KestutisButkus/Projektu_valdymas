# Generated by Django 5.1.4 on 2024-12-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgt', '0007_remove_employee_user_remove_invoice_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='project_photos/'),
        ),
    ]
