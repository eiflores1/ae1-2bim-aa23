from django.shortcuts import render
from deportes.models import Futbol

def acciones(request):

   mis_acciones = Futbol.objects.all()
   numero_acciones = len(mis_acciones) 
   informacion_template ={"mi_futbol":mis_acciones, "numero_futbol":numero_acciones}
   return render(request, "acciones.html", informacion_template)