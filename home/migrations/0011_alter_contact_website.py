# Generated by Django 4.0.6 on 2022-08-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_projects_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]