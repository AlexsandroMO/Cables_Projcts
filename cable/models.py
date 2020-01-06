
from django.db import models
from django.contrib.auth import get_user_model


class TabelaCondutor(models.Model):
    secao = models.CharField(verbose_name='Seção Transversão', max_length=5)
    capacidade_conducao = models.DecimalField(verbose_name='Capacidade de Condução', max_digits=5, decimal_places=2)
    queda_tesao = models.DecimalField(verbose_name='Queda de Tensão', max_digits=4, decimal_places=2)

    def __str__(self):
        return self.secao


class TipoCircuito(models.Model):
    ckt = models.CharField(verbose_name='Tipo de Circuito', max_length=50)

    def __str__(self):
        return self.ckt


class Disjuntor(models.Model):
    dj = models.CharField(verbose_name='Mini DJ Schneider', max_length=4)

    def __str__(self):
        return self.dj


class Tensao(models.Model):
    #volts = models.IntegerField(blank=True, null=True)
    volts = models.CharField(max_length=10)

    def __str__(self):
        return self.volts 


class Project(models.Model):
    project = models.CharField(verbose_name='Nome do Projeto', max_length=100)
    description = models.TextField(verbose_name='Descrição do Projeto', blank=True, null=False)
    create_project = models.DateTimeField(auto_now_add=True)
    update_project = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project


class ResidencDimens(models.Model):
    projeto = models.ForeignKey(Project, verbose_name='Nome do Projeto', on_delete=models.CASCADE)
    local = models.CharField(verbose_name='Local da Instalação', max_length=50)
    tipo = models.ForeignKey(TipoCircuito, verbose_name='Tipo de Instalação', on_delete=models.CASCADE)
    tensa_va = models.ForeignKey(Tensao, verbose_name='Tensão (VA)', on_delete=models.CASCADE)
    quant = models.DecimalField(verbose_name='Quantidade', max_digits=3, decimal_places=0)
    potencia_va = models.DecimalField(verbose_name='Potência (VA)', max_digits=7, decimal_places=2)
    total_va = models.DecimalField(verbose_name='Total (VA)', max_digits=8, decimal_places=2, blank=True)
    corrente_a = models.DecimalField(verbose_name='Corrente (A)', max_digits=8, decimal_places=2, blank=True)
    comprimento = models.DecimalField(verbose_name='Comprimento do Circuito (m)', max_digits=7, decimal_places=0)
    sessao_condutor = models.ForeignKey(TabelaCondutor, verbose_name='Sessão Transversal do Condutor (mm²)', on_delete=models.CASCADE)
    queda_tensao_ckt = models.DecimalField(verbose_name='Queda de Tensão do Circuito (%)', max_digits=2, decimal_places=2, blank=True)
    queda_tensao_perm = models.DecimalField(verbose_name='Queda de Tensão Permitida (%)', max_digits=4, decimal_places=2)
    queda_tensao_test = models.CharField(verbose_name='Queda de Tensão', max_length=3, blank=True)
    capacidade_corrente = models.CharField(verbose_name='Capacidade de Corrente', max_length=3, blank=True)
    numero_polos = models.DecimalField(verbose_name='Número de Polos', max_digits=4, decimal_places=0)
    corrente_nominal = models.ForeignKey(Disjuntor, verbose_name='Corrente Nominal', on_delete=models.CASCADE)
    verifica_dj = models.CharField(verbose_name='Verifica Disjuntor', max_length=3, blank=True)
    update_resid = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.local


