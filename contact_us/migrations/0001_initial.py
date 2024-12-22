# Generated by Django 5.1.2 on 2024-11-27 11:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the user providing feedback', max_length=100)),
                ('email', models.EmailField(help_text='Email of the user providing feedback', max_length=254)),
                ('message', models.TextField(help_text='Feedback message')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the feedback was submitted')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
                'ordering': ['-created_at'],
            },
        ),
    ]
