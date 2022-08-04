# Generated by Django 4.0.6 on 2022-08-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_contact_created_at_alter_projects_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='type',
            field=models.CharField(choices=[('Website', 'Website'), ('Application', 'Application')], default='Website', max_length=500),
            preserve_default=False,
        ),
    ]
