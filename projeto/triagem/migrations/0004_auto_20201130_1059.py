# Generated by Django 3.1.3 on 2020-11-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triagem', '0003_auto_20201130_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='hora',
            field=models.CharField(default='13:59', help_text='hh:mm', max_length=50, verbose_name='Hora do atendimento *'),
        ),
    ]
