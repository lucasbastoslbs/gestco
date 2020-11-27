# Generated by Django 3.1.3 on 2020-11-27 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome da Unidade de Pronto Atendimento *')),
                ('endereco', models.CharField(help_text='Rua, número, bairro, cep', max_length=130, verbose_name='Endereço *')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade *')),
                ('telefone', models.CharField(help_text='Ex.: 55 3221-2303', max_length=12, verbose_name='Telefone de contato *')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo? *')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='coordenador', to=settings.AUTH_USER_MODEL, verbose_name='Coordenador da Unidade de Atendimento *')),
            ],
            options={
                'verbose_name': 'unidade',
                'verbose_name_plural': 'unidades',
                'ordering': ['nome'],
                'unique_together': {('nome', 'cidade')},
            },
        ),
    ]
