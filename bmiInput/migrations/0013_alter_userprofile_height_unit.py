# Generated by Django 5.1.2 on 2024-11-15 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiInput', '0012_bmisuggestion_sleep_suggestion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='height_unit',
            field=models.CharField(choices=[('m', 'Meters'), ('ft', 'Feet')], default='ft', max_length=5),
        ),
    ]