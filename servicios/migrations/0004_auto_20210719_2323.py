# Generated by Django 3.2.5 on 2021-07-19 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_auto_20210702_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='imagen2',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='imagen3',
        ),
    ]
