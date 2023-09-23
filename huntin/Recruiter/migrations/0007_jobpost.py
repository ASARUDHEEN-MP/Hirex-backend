# Generated by Django 4.2.3 on 2023-08-30 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recruiter', '0006_recruiterdetails_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desgination', models.CharField(blank=True)),
                ('skills', models.TextField(blank=True)),
                ('vaccancies', models.IntegerField(blank=True, null=True)),
                ('location', models.TextField(blank=True)),
                ('Type', models.CharField(blank=True)),
                ('workmode', models.CharField(blank=True)),
                ('experience_from', models.CharField(blank=True)),
                ('experience_to', models.CharField(blank=True)),
                ('job_description', models.TextField()),
                ('criteria', models.CharField(blank=True)),
                ('payscale_from', models.CharField(blank=True)),
                ('payscale_to', models.CharField(blank=True)),
                ('hired_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
