# Generated by Django 5.1.2 on 2024-11-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiInput', '0010_remove_bmisuggestion_diet_suggestion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dietsubcategory',
            name='bmi_subcategory',
        ),
        migrations.AddField(
            model_name='bmisuggestion',
            name='diet_suggestion',
            field=models.TextField(default='No diet suggestion available'),
        ),
        migrations.AddField(
            model_name='bmisuggestion',
            name='exercise_suggestion',
            field=models.TextField(default='No diet suggestion available'),
        ),
        migrations.AddField(
            model_name='bmisuggestion',
            name='other_health_tips',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bmisuggestion',
            name='water_intake_suggestion',
            field=models.TextField(default='No diet suggestion available'),
        ),
        migrations.DeleteModel(
            name='BMISubcategory',
        ),
        migrations.DeleteModel(
            name='DietSubcategory',
        ),
    ]