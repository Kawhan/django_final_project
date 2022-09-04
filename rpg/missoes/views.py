from django.shortcuts import render
from .models import missoesModel
from .forms import MissoesForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
@login_required
def viewMissoes(request):
    missoes = missoesModel.objects.all().filter(aberta=True)
    
    dados = {}
    
    dados['missoes'] = missoes
    
    return render(request, 'missoes/viewMissoes.html', dados)

@login_required
def missoesCreate(request):
    context = {}
    
    form = MissoesForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("view_missoes")

    context["form"] = form
    
    return render(request, "forms_create.html", context)

@login_required
def missoesEdit(request, missao_id):
    missao = get_object_or_404(missoesModel, pk=missao_id) 

    context = {}
    
    form = MissoesForm(request.POST or None, instance=missao)
    
    if form.is_valid():
        form.save()
        return redirect("view_missoes")

    context["form"] = form
    
    return render(request, "forms_create.html", context)

@user_passes_test(lambda u: u.is_superuser)
def missoesDelete(request, missao_id):
    missao = get_object_or_404(missoesModel, pk=missao_id) 
    
    dados = {}
    
    dados['missao'] = missao
    
    if request.method == 'POST':
        missao.delete()
        # after deleting redirect to
        # home page
        return redirect("view_missoes")
    
    return render(request, 'missoes/delete_missao.html', dados)