from __future__ import unicode_literals

import os

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
#from datetime.date.today()

from utils.gerador_hash import gerar_hash
    
#data, hora, nome completo do paciente, idade, altura, peso, IMC (índice de massa corpórea que deverá ser calculado e armazenado automaticamente), resultado da triagem

class Triagem(models.Model):
    class Pontos(models.IntegerChoices):
        total = 0
        Q1 = 1
        return total
    data = models.DateField(_('Data do atendimento *'), max_length=11, help_text='dd/mm/aaaa')#, default=date.today
    hora = models.DateTimeField(_('Hora do atendimento *'), max_length=5, help_text='hh:mm') #, default=timezone.now
    nome_paciente = models.CharField(_('Nome completo do paciênte *'), max_length=50)
    idade = models.CharField(_('Idade'), max_length=3)
    altura = models.FloatField(_('Altura (m)'), max_length=3, help_text='Favor inserir em metros')
    peso = models.FloatField(_('Peso (KG)'), max_length=4, help_text='Em quilograma (Ex.: 45.5)')
    imc = models.FloatField(_('IMC'), peso/(altura*altura), editable=False)
    resultado = models.IntegerField(_('Resultado da triagem'), null=True, blank=True,value = Pontos)
    
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
        self.codigo = self.codigo.upper()
        super(Triagem, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('triagem_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('triagem_delete', args=[str(self.id)])
    
    @property
    def get_visualiza_url(self):
        return reverse('triagem_detail', args=[str(self.id)])
    

#triggers para limpeza dos arquivos apagados ou alterados. No Django é chamado de signals
#deleta o arquivo fisico ao excluir o item da pasta midias
@receiver(models.signals.post_delete, sender=Triagem)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.arquivo_anexo1:
        if os.path.isfile(instance.arquivo_anexo1.path):
            os.remove(instance.arquivo_anexo1.path)

#deleta o arquivo fisico ao alterar o arquivo da pasta midia
@receiver(models.signals.pre_save, sender=Triagem)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        obj = Triagem.objects.get(pk=instance.pk)

        if not obj.arquivo_anexo1:
            return False

        old_file = obj.arquivo_anexo1
    except Triagem.DoesNotExist:
        return False

    new_file = instance.arquivo_anexo1
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
