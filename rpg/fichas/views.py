from django.shortcuts import render, get_object_or_404, redirect
from .models import fichaRpgModel
from .forms import fichaRpgForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def viewFichas(request):
    fichas = fichaRpgModel.objects.filter(is_dead=False)
    
    dados = {
        'fichas': fichas
    }
    
    

    return render(request, 'fichas.html', dados)

@login_required
def infoFichas(request, id_fichas):
    ficha = get_object_or_404(fichaRpgModel, pk=id_fichas) 
    
    dados = {
        'ficha': ficha
    }
    
    return render(request, 'info-fichas.html', dados)

@login_required
def createFichas(request):
    context = {}
    
    form = fichaRpgForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("/")

    context["form"] = form
    
    return render(request, "forms_create.html", context)

@login_required
def infoFichas(request, id_fichas):
    ficha = get_object_or_404(fichaRpgModel, pk=id_fichas) 
    
    dados = {
        'ficha': ficha
    }
    
    return render(request, 'info-fichas.html', dados)

@user_passes_test(lambda u: u.is_superuser)
def deleteFicha(request, id_fichas):
    ficha = get_object_or_404(fichaRpgModel, pk=id_fichas) 
    
    dados = {}
    
    dados['ficha'] = ficha
    
    if request.method == 'POST':
        ficha.delete()
        # after deleting redirect to
        # home page
        return redirect("/fichas")
    
    return render(request, 'delete_ficha.html', dados)

@login_required
def changeFicha(request, id_fichas):
    ficha = get_object_or_404(fichaRpgModel, pk=id_fichas) 
    
    
    context = {}
    
    form = fichaRpgForm(request.POST or None, instance=ficha)
    
    if form.is_valid():
        form.save()
        return redirect("/fichas")

    context["form"] = form
    
    return render(request, "forms_create.html", context)

@login_required
def search(request):
    fichas = fichaRpgModel.objects.filter(is_dead=False)
    
    if 'search' in request.GET:
        nome_a_buscar = request.GET['search']
        if search:
            fichas = fichaRpgModel.objects.filter(nome_personagem__icontains=nome_a_buscar)

    dados = {
        'fichas': fichas
    }
    
    return render(request,'buscar.html', dados)