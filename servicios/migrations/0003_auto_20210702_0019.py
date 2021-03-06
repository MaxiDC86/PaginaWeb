# Generated by Django 3.2.2 on 2021-07-02 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_servicio_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen2',
            field=models.ImageField(default=1, upload_to='servicios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='imagen3',
            field=models.ImageField(default=1, upload_to='servicios'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
