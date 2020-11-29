from __future__ import unicode_literals

import os

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash

class Unidade(models.Model):
    nome = models.CharField(_('Nome da Unidade de Pronto Atendimento *'), max_length=80)
    endereco = models.CharField(_('Endereço *'), max_length=130, help_text='Rua, número, bairro, cep')
    cidade = models.CharField(_('Cidade *'), max_length=30)
    coordenador = models.ForeignKey('usuario.Usuario', verbose_name= 'Coordenador da Unidade de Atendimento *', on_delete=models.PROTECT, related_name='coordenador')
    telefone = models.CharField(_('Telefone de contato *'), max_length=12, help_text='Ex.: 55 3221-2303')
    is_active = models.BooleanField(_('Ativo? *'), default=True)
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)
    
    objects = models.Manager()
    
    class Meta:
        ordering            =   ['nome']
        verbose_name        =   ('unidade')
        verbose_name_plural =   ('unidades')
        unique_together     =   ['nome', 'cidade'] #criando chave primária composta no BD

    def __str__(self):
        return "Unidade: %s - %s. Coordenador: %s" % (self.nome, self.cidade, self.coordenador.nome)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        super(Unidade, self).save(*args, **kwargs)
        

    @property
    def get_absolute_url(self):
        return reverse('unidade_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('unidade_delete', args=[str(self.id)])
    
    @property
    def get_visualiza_url(self):
        return reverse('unidade_detail', args=[str(self.id)])