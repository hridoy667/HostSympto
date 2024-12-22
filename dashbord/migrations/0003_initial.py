# Generated by Django 5.1.2 on 2024-11-11 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bmiInput', '0012_bmisuggestion_sleep_suggestion_and_more'),
        ('dashbord', '0002_delete_bmidailyroutine'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wakeup', models.TextField()),
                ('breakfast', models.TextField()),
                ('midmeal', models.TextField()),
                ('lunch', models.TextField()),
                ('evening', models.TextField()),
                ('dinner', models.TextField()),
                ('bmi_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='diet_plan', to='bmiInput.bmisuggestion')),
            ],
        ),
        migrations.CreateModel(
            name='ProductivitySuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleep', models.TextField()),
                ('deep_work', models.TextField()),
                ('relaxation', models.TextField()),
                ('bmi_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='productivity_suggestion', to='bmiInput.bmisuggestion')),
            ],
        ),
    ]