# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Interception(models.Model):
    #1 Law Enforcement/Emergency Services, 2 Post-Arrest Initial Detention/Initial Hearings; 3 Post-Initial Hearings: Jail/Prison, Courts, Forensic Evaluations & Forensic;
    # 4 Re-Entry From Jails, State Prisons, & Forensic Hospitalization #5 Community Corrections & Community Support
    description = models.CharField(max_length=100, verbose_name="Niveau d'interception")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description

class Programme(models.Model):
    #1 Law Enforcement/Emergency Services, 2 Post-Arrest Initial Detention/Initial Hearings; 3 Post-Initial Hearings: Jail/Prison, Courts, Forensic Evaluations & Forensic;
    # 4 Re-Entry From Jails, State Prisons, & Forensic Hospitalization #5 Community Corrections & Community Support
    description = models.CharField(max_length=100, verbose_name="Niveau d'interception")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Secteur(models.Model):
    #1 Law Enforcement/Emergency Services, 2 Post-Arrest Initial Detention/Initial Hearings; 3 Post-Initial Hearings: Jail/Prison, Courts, Forensic Evaluations & Forensic;
    # 4 Re-Entry From Jails, State Prisons, & Forensic Hospitalization #5 Community Corrections & Community Support
    description = models.CharField(max_length=100, verbose_name="Niveau d'interception")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Ressource(models.Model):
    nom = models.CharField(max_length=250, verbose_name="Nom du programme")
    acronyme = models.CharField(max_length=50, default='-', verbose_name="Acronyme")
    depuis = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ressource / programme existant depuis")
    descriptif = models.TextField(verbose_name="Brève description")
    interception = models.ManyToManyField(Interception, verbose_name="Niveau d'intercetion")
    domaine = models.CharField(max_length=250, blank=True, null=True,verbose_name="Domaines d'intervention / pratiques")
    siteweb = models.CharField(max_length=250, blank=True, null=True,verbose_name="Site web")
    courriel = models.CharField(max_length=250, blank=True, null=True,verbose_name="Courriel")
    telephone = models.CharField(max_length=250, blank=True, null=True,verbose_name="Téléphone")
    secteurtype = models.ManyToManyField(Secteur, verbose_name="Secteurs")
    programmetype = models.ManyToManyField(Programme, verbose_name="Type de programme")
    confidentiel = models.BooleanField(verbose_name="Cliquer si les informations de contact sont confidentielles")
    nompersress = models.CharField(max_length=250, verbose_name="Nom de la personne ressource", blank=True, null=True)
    adresse = models.CharField(max_length=250, verbose_name="Adresse", blank=True, null=True)
    author = models.ForeignKey(User, related_name='AssistantRessource',blank=True, null=True, on_delete=models.DO_NOTHING)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    region = models.CharField(max_length=250, blank=True, null=True,verbose_name="Province, région, ville ...")
    popcible = models.TextField(verbose_name="Population cible", blank=True, null=True)
    testdeplus = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '{}, {}'.format(self.acronyme.upper(), self.nom)

    def __unicode__(self):
        return u'{}'.format(self.__str__())


class Document(models.Model):
    docfile = models.FileField(upload_to='DocsRessources', verbose_name="Documentation utile", blank=True, null=True)
    description = models.CharField(max_length=100, verbose_name="Brève description", blank=True, null=True, help_text="Nom explicite et court du fichier (par exemple rapport annuel)")
    ressource = models.ForeignKey(Ressource, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, related_name='AssistantDocument', blank=True, null=True, on_delete=models.DO_NOTHING)
    posted = models.DateTimeField(auto_now_add=True)



