# Generated by Django 4.2.4 on 2023-08-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0004_alter_tabledata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabledata',
            name='date',
            field=models.DateField(default='2023-08-24'),
            preserve_default=False,
        ),
    ]
