# Generated by Django 3.2.6 on 2021-08-07 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default=' ', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
