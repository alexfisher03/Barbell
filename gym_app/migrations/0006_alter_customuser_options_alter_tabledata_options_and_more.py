# Generated by Django 4.2.4 on 2023-08-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0005_alter_tabledata_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'App user', 'verbose_name_plural': 'App users'},
        ),
        migrations.AlterModelOptions(
            name='tabledata',
            options={'verbose_name': 'Stat Data', 'verbose_name_plural': 'Stat Data'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
