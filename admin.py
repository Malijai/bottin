# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Ressource, Document,Interception,Secteur,Programme


#class DocumentInline(admin.StackedInline):
class DocumentInline(admin.TabularInline):
    model = Document

    fields = ['docfile','description']


class RessourceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': ['nom', 'acronyme']}),
        ('Description', {'fields': ['depuis', 'descriptif']}),
        ('Métadonnées', {'fields': ['interception','popcible','region','programmetype','secteurtype']}),
        ('Contact', {'fields': ['siteweb']}),
        ('Informations pouvant être confidentielles', {'fields': ['confidentiel','adresse', 'nompersress','telephone','courriel'], }),
    ]

    inlines = [DocumentInline,]

    list_display = ('acronyme', 'nom', 'domaine')

    list_filter = ['domaine',]

def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Ressource, RessourceAdmin)
admin.site.register(Secteur)
admin.site.register(Programme)
admin.site.register(Interception)

