# Generated by Django 3.2.2 on 2021-07-01 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
