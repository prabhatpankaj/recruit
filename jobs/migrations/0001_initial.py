# Generated by Django 2.2.2 on 2019-06-20 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employers', '0001_initial'),
        ('recruiters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, choices=[('onsite', 'On-site'), ('remote', 'Remote')], max_length=50, null=True)),
                ('weekly_hours', models.IntegerField()),
                ('salary_high', models.IntegerField()),
                ('salary_low', models.IntegerField()),
                ('accommodation_included', models.BooleanField()),
                ('accommodation_stipend', models.CharField(max_length=100)),
                ('travel_stipend', models.CharField(max_length=100)),
                ('insurance_included', models.BooleanField()),
                ('insurance_stipend', models.CharField(max_length=100)),
                ('contract_length', models.IntegerField()),
                ('contract_renew_bonus', models.IntegerField(blank=True, null=True)),
                ('contract_completion_bonus', models.IntegerField(blank=True, null=True)),
                ('compensation_type', models.CharField(choices=[('One-time', 'One-time'), ('Monthly', 'Monthly')], max_length=25)),
                ('compensation_amount', models.CharField(max_length=25)),
                ('compensation_terms', models.CharField(max_length=250)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='employers.Employer')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='recruiters.Recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='JobRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_high', models.IntegerField()),
                ('age_low', models.IntegerField()),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True)),
                ('citizenship', models.ManyToManyField(blank=True, to='jobs.Country')),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
        ),
    ]
