# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from reportlab.pdfgen import canvas
from .models import Ressource
from django.core.files.storage import FileSystemStorage

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()

NOM_FICHIER_PDF = "Programme_OSMJ.pdf"


Title = "Observatoire en santé menatle justice"
pageinfo = " Description des programmes "

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Helvetica',10)
    canvas.drawString(inch, 0.75 * inch, "OSMJ / %s" % pageinfo)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica',10)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()


def some_pdf(request, pk):
    fichier = 'QID_' + str(pk) + '_' + NOM_FICHIER_PDF
    doc = SimpleDocTemplate("/tmp/{}".format(fichier))

#    Story = [Spacer(1,2*inch)]
    Story = []
    style = styles["Normal"]
#    articles_list =Ressource.objects.all()
#    for article in articles_list:

    ressource = Ressource.objects.get(pk=pk)

    ptext = '<b>Vérification des informations qui seront publiées sur notre site web </b>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 0.1 * inch))

    f = Ressource._meta.get_field('nom')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.nom
    p = Paragraph(bogustext, style,bulletText="\x80")
    Story.append(p)

    f =Ressource._meta.get_field('acronyme')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.acronyme
    p = Paragraph(bogustext, style,bulletText="\x80")
    Story.append(p)

    f = Ressource._meta.get_field('siteweb')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.siteweb
    p = Paragraph(bogustext, style, bulletText="\x80")
    Story.append(p)

    Story.append(Spacer(1, 0.1 * inch))

    f =Ressource._meta.get_field('descriptif')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.descriptif
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Spacer(1, 0.1 * inch))

    f =Ressource._meta.get_field('popcible')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.popcible
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Spacer(1, 0.1 * inch))

    if ressource.confidentiel == 1:
        ptext = '<b>Informations qui vont rester confidentielles :</b>'
        Story.append(Paragraph(ptext, styles["Normal"]))
    else:
        ptext = '<b>Contacts</b>'
        Story.append(Paragraph(ptext, styles["Normal"]))

    f = Ressource._meta.get_field('nompersress')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.nompersress
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Ressource._meta.get_field('adresse')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.adresse
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Ressource._meta.get_field('courriel')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.courriel
    p = Paragraph(bogustext, style)
    Story.append(p)

    f = Ressource._meta.get_field('telephone')
    bogustext = "<b>" + f.verbose_name + " : </b>"
    bogustext += ressource.telephone
    p = Paragraph(bogustext, style)
    Story.append(p)

    doc.build(Story, onFirstPage=myLaterPages, onLaterPages=myLaterPages)

    fs = FileSystemStorage("/tmp")
    with fs.open(fichier) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(fichier)
    return response


def extractionb(request):
    ressources =Ressource.objects.all()
    return render(request, 'listeb.html',  {'ressources': ressources})



