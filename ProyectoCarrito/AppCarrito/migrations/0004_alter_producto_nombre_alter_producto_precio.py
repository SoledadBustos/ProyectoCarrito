# Generated by Django 4.0.5 on 2022-07-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCarrito', '0003_rename_tienda_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
