# Generated by Django 4.0.6 on 2022-08-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_projects_case_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='case_study',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
