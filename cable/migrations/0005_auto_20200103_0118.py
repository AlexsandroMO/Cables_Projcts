# Generated by Django 3.0.1 on 2020-01-03 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cable', '0004_auto_20200103_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tensao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volts', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Tensão (VA)')),
            ],
        ),
        migrations.AlterField(
            model_name='residencdimens',
            name='tensa_va',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cable.Tensao', verbose_name='Tensão (VA)'),
        ),
    ]
