from rest_framework import viewsets, filters
from .models import Contact
from .serializers import ContactSerializer
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from django.http import HttpResponse
from django.shortcuts import render


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone_number']

def export_contacts(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contacts.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter  

    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.black)
    p.drawString(200, height - 40, "Contact List")
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, height - 60, 'ID')
    p.drawString(100, height - 60, 'Name')
    p.drawString(250, height - 60, 'Phone Number')
    p.drawString(400, height - 60, 'Email')
    p.drawString(550, height - 60, 'Created At')

    y_position = height - 80
    contacts = Contact.objects.all()

    for contact in contacts:
        p.setFont("Helvetica", 10)
        p.drawString(50, y_position, str(contact.id))
        p.drawString(100, y_position, contact.name)
        p.drawString(250, y_position, contact.phone_number)
        p.drawString(400, y_position, contact.email)
        p.drawString(550, y_position, str(contact.created_at))

        y_position -= 20
        if y_position < 100:
            p.showPage()
            p.setFont("Helvetica-Bold", 10)
            p.drawString(50, height - 60, 'ID')
            p.drawString(100, height - 60, 'Name')
            p.drawString(250, height - 60, 'Phone Number')
            p.drawString(400, height - 60, 'Email')
            p.drawString(550, height - 60, 'Created At')
            y_position = height - 80

    p.showPage()
    p.save()

    return response


def show_export_page(request):
    return render(request, 'export.html')
