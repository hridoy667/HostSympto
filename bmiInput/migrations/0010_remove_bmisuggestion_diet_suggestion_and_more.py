# Generated by Django 5.1.2 on 2024-11-10 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiInput', '0009_bmisuggestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmisuggestion',
            name='diet_suggestion',
        ),
        migrations.RemoveField(
            model_name='bmisuggestion',
            name='exercise_suggestion',
        ),
        migrations.RemoveField(
            model_name='bmisuggestion',
            name='other_health_tips',
        ),
        migrations.RemoveField(
            model_name='bmisuggestion',
            name='water_intake_suggestion',
        ),
        migrations.CreateModel(
            name='BMISubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion_type', models.CharField(choices=[('Diet', 'Diet'), ('Exercise', 'Exercise'), ('Deep Work', 'Deep Work'), ('Sleep', 'Sleep'), ('Water Intake', 'Water Intake')], max_length=20)),
                ('content', models.TextField()),
                ('bmi_suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='bmiInput.bmisuggestion')),
            ],
        ),
        migrations.CreateModel(
            name='DietSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_day', models.CharField(choices=[('Morning', 'Morning'), ('Breakfast', 'Breakfast'), ('Mid-Morning', 'Mid-Morning'), ('Lunch', 'Lunch'), ('Mid-Afternoon', 'Mid-Afternoon'), ('Dinner', 'Dinner'), ('Evening', 'Evening')], max_length=15)),
                ('details', models.TextField()),
                ('bmi_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet_times', to='bmiInput.bmisubcategory')),
            ],
        ),
    ]
