from __future__ import unicode_literals

import os

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

import datetime
from django.utils import timezone

from utils.gerador_hash import gerar_hash

def defhora():
    hora = str(timezone.localtime())
    return hora.split(" ")[1][:5]

class Triagem(models.Model):
    data = models.DateField(_('Data do atendimento *'), max_length=11, help_text='dd/mm/aaaa', default=datetime.date.today)
    hora = models.CharField(_('Hora do atendimento *'), help_text='hh:mm', max_length=50, default=defhora())
    local = models.ForeignKey('unidade.Unidade', verbose_name= 'Unidade de Pronto Atendimento *', on_delete=models.PROTECT, related_name='Unidade', null=True, blank=True)
    nome_paciente = models.CharField(_('Nome completo do paciênte *'), max_length=50)
    idade = models.PositiveIntegerField(_('Idade'))
    altura = models.FloatField(_('Altura (m)'), max_length=3, help_text='Favor inserir em metros')
    peso = models.FloatField(_('Peso (KG)'), max_length=4, help_text='Em quilograma (Ex.: 45.5)')
    
    
    #febre, dorcabeca, secrecao, garganta, tosse, respiracao, dorcorpo, diarreia, viagem, contatoinfectado
    febre = models.BooleanField(_('Tem febre?'), default=False)
    dorcabeca = models.BooleanField(_('Tem dores de cabeça?'), default=False)
    secrecao = models.BooleanField(_('Tem secreção nasal ou espirros?'), default=False)
    garganta = models.BooleanField(_('Tem dor/irritação na garganta?'), default=False)
    tosse = models.BooleanField(_('Tem tosse seca?'), default=False)
    respiracao = models.BooleanField(_('Tem dificuldade respiratória?'), default=False)
    dorcorpo = models.BooleanField(_('Tem dores no corpo?'), default=False)
    diarreia = models.BooleanField(_('Tem diarréia?'), default=False)
    viagem = models.BooleanField(_('Viajou nos últimos 14 dias para algum local com casos confirmados de COVID19?'), default=False)
    contatoinfectado = models.BooleanField(_('Teve contato nos últimos 14 dias com algum infectado por COVID19?'), default=False)
    
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['nome_paciente','-data','-hora','idade']
        verbose_name        =   ('triagem')
        verbose_name_plural =   ('triagens')
        unique_together     =   ['nome_paciente', 'data', 'hora'] #criando chave primária composta no BD

    def __str__(self):
        return "Paciente: %s. Data: %s. Hora: %s" % (self.nome_paciente, self.data, self.hora)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        #self.codigo = self.codigo.upper()
        super(Triagem, self).save(*args, **kwargs)

    @property
    def imc(self):
        return self.peso/(self.altura*self.altura)
        
    @property
    def pontos(self):
        total=0
        if self.febre:
            total+=5
        if self.dorcabeca:
            total+=1
        if self.secrecao:
            total+=1
        if self.garganta:
            total+=1
        if self.tosse:
            total+=3
        if self.respiracao:
            total+=10
        if self.dorcorpo:
            total+=1
        if self.diarreia:
            total+=1
        if self.viagem:
            total+=3
        if self.contatoinfectado:
            total+=10
        return total

    @property
    def get_absolute_url(self):
        return reverse('triagem_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('triagem_delete', args=[str(self.id)])
    
    @property
    def get_visualiza_url(self):
        return reverse('triagem_detail', args=[str(self.id)])

