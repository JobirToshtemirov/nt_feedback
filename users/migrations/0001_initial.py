# Generated by Django 5.1.2 on 2024-10-13 13:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Organization Name')),
                ('location', models.CharField(blank=True, max_length=64, null=True, verbose_name='Location')),
                ('linkedin_link', models.CharField(blank=True, max_length=64, null=True, verbose_name='Linkedin')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='users/', verbose_name='Avatar')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
