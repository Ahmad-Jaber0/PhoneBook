# Generated by Django 5.0.4 on 2025-01-25 11:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?[0-9]{7,15}$')])),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='Invalid email address.')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
