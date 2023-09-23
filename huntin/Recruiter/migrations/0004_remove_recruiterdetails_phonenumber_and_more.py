# Generated by Django 4.2.3 on 2023-08-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0003_alter_recruiterdetails_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiterdetails',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='recruiterdetails',
            name='about_us',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='recruiterdetails',
            name='companyregno',
            field=models.IntegerField(default=0),
        ),
    ]
