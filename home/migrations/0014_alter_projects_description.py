# Generated by Django 4.0.6 on 2022-08-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_technology_rename_image_2_projects_mobile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(),
        ),
    ]
