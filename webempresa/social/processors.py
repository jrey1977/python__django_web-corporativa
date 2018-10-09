from .models import Link

def obtener_enlaces(request):
    arrayEnlaces = Link.objects.all()
    enlaces = { 'misEnlaces':arrayEnlaces}
    return enlaces
