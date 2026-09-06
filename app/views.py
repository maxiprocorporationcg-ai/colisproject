from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterParcelForm
from .models import Parcel

#liste colis
#colis_data = ["Colis1","Colis2","Colis3","Colis4","Colis5",]
# Create your views here.
def home_page(request):
  #  nb_colis = len(colis_data)
    nb_colis = len(Parcel.objects.all())
    Nom_entrepo = "OneEntrepo"
    context = {
        'nb_colis': nb_colis,
        'Nom_entrepo': Nom_entrepo
    }
    return render(request, 'index.html', context=context)

def parcels_page(request):
    return render(request, "parcels.html", context={'colis': Parcel.objects.all()})

def add_parcel_page(request):
    
    if request.method == 'POST':
        form = RegisterParcelForm(request.POST)
        if form.is_valid():
            form.save() #Enregistrement dans la base
            return HttpResponse("Enregistrement ok ---"+"<a href='/'>Retour à l'accueil</a>")
    else:
        form = RegisterParcelForm
        return render(request, "add_parcel.html", context={'form': form})

def tracking_page(request):
     parcel = None
     error = None
     if request.method == 'POST':
            tracking_number = request.POST.get('tracking_number')
            try:
                 parcel = Parcel.objects.get(tracking_number = tracking_number)
            except Parcel.DoesNotExist:
                 error = "Aucun colis n'existe avec ce numéro"
     return render(request, "tracking.html", { "parcel":parcel, "error": error})
     