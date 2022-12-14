# Generated by Django 4.0.6 on 2022-07-23 07:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_review_alter_projects_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 23, 0, 13, 22, 74854), null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image_2',
            field=models.ImageField(blank=True, help_text='This image will shown on list and feed preview', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image_3',
            field=models.ImageField(blank=True, help_text='This image will shown on list and feed preview', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 23, 0, 13, 22, 74854), null=True),
        ),
    ]
