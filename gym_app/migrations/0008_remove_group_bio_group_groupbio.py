# Generated by Django 4.2.4 on 2023-09-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0007_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='bio',
        ),
        migrations.AddField(
            model_name='group',
            name='groupbio',
            field=models.TextField(blank=True, null=True),
        ),
    ]