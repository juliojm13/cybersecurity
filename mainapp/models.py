from django.db import models


class Organisation(models.Model):
    org_name = models.CharField(verbose_name='nombre de la organización', max_length=256, blank=False)

    def __str__(self):
        return self.org_name


class Diagnostic(models.Model):
    created = models.DateTimeField(verbose_name='fecha del diagnostico', auto_now_add=True)
    gr = models.BigIntegerField(verbose_name='gestion de riesgos', default=0)
    ga = models.BigIntegerField(verbose_name='gestion de activos', default=0)
    gia = models.BigIntegerField(verbose_name='gestion de identidad y acceso', default=0)
    gav = models.BigIntegerField(verbose_name='gestion de amenazas y vulnerabilidades', default=0)
    cea = models.BigIntegerField(verbose_name='conciencia del estado actual', default=0)
    iic = models.BigIntegerField(verbose_name='intercambio de informacion y comunicaciones', default=0)
    ri = models.BigIntegerField(verbose_name='respuesta a incidentes', default=0)
    gde = models.BigIntegerField(verbose_name='gestion de dependencias externas', default=0)
    cp = models.BigIntegerField(verbose_name='capacitacion del personal', default=0)
    gpc = models.BigIntegerField(verbose_name='gestion de programa de ciberseguridad', default=0)
    total = models.BigIntegerField(verbose_name='puntaje total', default=0)
    id_organization = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Diagnóstico {self.created}'
