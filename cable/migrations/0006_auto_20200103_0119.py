# Generated by Django 3.0.1 on 2020-01-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0005_auto_20200103_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residencdimens',
            name='tensa_va',
            field=models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Tensão (VA)'),
        ),
    ]
