# Generated by Django 5.1.2 on 2024-11-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiInput', '0011_remove_dietsubcategory_bmi_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmisuggestion',
            name='sleep_suggestion',
            field=models.TextField(default='No sleep suggestion available'),
        ),
        migrations.AlterField(
            model_name='bmisuggestion',
            name='exercise_suggestion',
            field=models.TextField(default='No exercise suggestion available'),
        ),
        migrations.AlterField(
            model_name='bmisuggestion',
            name='water_intake_suggestion',
            field=models.TextField(default='No water intake suggestion available'),
        ),
    ]