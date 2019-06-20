# Generated by Django 2.2.2 on 2019-06-20 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0001_initial'),
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_accepted', models.NullBooleanField()),
                ('employer_accepted', models.NullBooleanField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_jobs', to='candidates.Candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_candidates', to='jobs.Job')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewInvitation',
            fields=[
                ('uuid', models.CharField(default='FQFUE', max_length=5, primary_key=True, serialize=False)),
                ('confirmed_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(-3, 'Revoked'), (-2, 'Candidate Cancelled'), (-1, 'Employer Cancelled'), (0, 'Request Open'), (1, 'Pending Confirmation'), (2, 'Confirmed'), (3, 'Completed')], default=0)),
                ('request_reminders_sent', models.IntegerField(default=0)),
                ('confirmation_reminders_sent', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=1)),
                ('result', models.CharField(blank=True, max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Exclusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField()),
                ('time_start', models.CharField(max_length=5)),
                ('time_end', models.CharField(max_length=5)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]