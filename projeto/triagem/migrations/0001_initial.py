# Generated by Django 3.1.3 on 2020-11-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Triagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='dd/mm/aaaa', max_length=11, verbose_name='Data do atendimento *')),
                ('hora', models.DateTimeField(help_text='hh:mm', max_length=5, verbose_name='Hora do atendimento *')),
                ('nome_paciente', models.CharField(max_length=50, verbose_name='Nome completo do paciênte *')),
                ('idade', models.CharField(max_length=3, verbose_name='Idade')),
                ('altura', models.FloatField(help_text='Favor inserir em metros', max_length=3, verbose_name='Altura (m)')),
                ('peso', models.FloatField(help_text='Em quilograma (Ex.: 45.5)', max_length=4, verbose_name='Peso (KG)')),
                ('febre', models.BooleanField(default=False, verbose_name='Tem febre?')),
                ('dorcabeca', models.BooleanField(default=False, verbose_name='Tem dores de cabeça?')),
                ('secrecao', models.BooleanField(default=False, verbose_name='Tem secreção nasal ou espirros?')),
                ('garganta', models.BooleanField(default=False, verbose_name='Tem dor/irritação na garganta?')),
                ('tosse', models.BooleanField(default=False, verbose_name='Tem tosse seca?')),
                ('respiracao', models.BooleanField(default=False, verbose_name='Tem dificuldade respiratória?')),
                ('dorcorpo', models.BooleanField(default=False, verbose_name='Tem dores no corpo?')),
                ('diarreia', models.BooleanField(default=False, verbose_name='Tem diarréia?')),
                ('viagem', models.BooleanField(default=False, verbose_name='Viajou nos últimos 14 dias para algum local com casos confirmados de COVID19?')),
                ('contatoinfectado', models.BooleanField(default=False, verbose_name='Teve contato nos últimos 14 dias com algum infectado por COVID19?')),
                ('resultado', models.IntegerField(blank=True, null=True, verbose_name='Resultado da triagem')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'triagem',
                'verbose_name_plural': 'triagens',
                'ordering': ['nome_paciente', '-data', '-hora', 'idade'],
                'unique_together': {('nome_paciente', 'data', 'hora')},
            },
        ),
    ]
