# Generated by Django 5.1.2 on 2024-11-15 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiInput', '0014_userprofile_disease_history'),
        ('dashbord', '0008_remove_timebasedsuggestion_deep_work_suggestion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timebasedsuggestion',
            name='bmi_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmiInput.bmisuggestion'),
        ),
        migrations.DeleteModel(
            name='BMICategory',
        ),
    ]
