# Generated by Django 3.1.3 on 2020-11-28 14:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0001_initial'),
        ('triagem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triagem',
            name='resultado',
        ),
        migrations.AddField(
            model_name='triagem',
            name='local',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Unidade', to='unidade.unidade', verbose_name='Unidade de Pronto Atendimento *'),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='data',
            field=models.DateField(default=datetime.date.today, help_text='dd/mm/aaaa', max_length=11, verbose_name='Data do atendimento *'),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='hora',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='hh:mm', max_length=5, verbose_name='Hora do atendimento *'),
        ),
    ]
