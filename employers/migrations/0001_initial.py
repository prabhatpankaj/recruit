# Generated by Django 2.2.2 on 2019-06-20 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('name_english', models.CharField(max_length=200)),
                ('name_local', models.CharField(max_length=200)),
                ('address_english', models.CharField(max_length=200)),
                ('address_local', models.CharField(max_length=200)),
                ('business_license', models.ImageField(upload_to='employer/%Y/%m/%d')),
                ('business_license_thumb', models.ImageField(blank=True, upload_to='employer/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployerRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, choices=[('', ''), ('High School', 'High School'), ('Vocational School', 'Vocational School'), ('Community College', 'Community College'), ("Bachelor's Degree", "Bachelor's Degree"), ("Master's Degree", "Master's Degree"), ('MBA', 'MBA'), ('PhD', 'PhD')], max_length=25)),
                ('education_major', models.CharField(blank=True, max_length=50)),
                ('age_range_low', models.IntegerField(blank=True)),
                ('age_range_high', models.IntegerField(blank=True)),
                ('years_of_experience', models.IntegerField(blank=True)),
                ('citizenship', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employers.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='employer/%Y/%m/%d')),
                ('thumb', models.ImageField(blank=True, upload_to='employer/%Y/%m/%d')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='employers.Employer')),
            ],
        ),
    ]