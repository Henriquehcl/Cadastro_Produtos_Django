from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import ProdutosForm
from app.models import Produtos
from django.core.paginator import Paginator # responsável pela paginação


# Create your views here.


"""
#função para testar o server
def home(request):  # função home que é chamado na urls.py
    return HttpResponse('Hello World')

"""

""" Enviando para a página inicial as informações do DB através do dicionário data """


def home(request):
    data = {}
    search = request.GET.get('search')  # recebe os dados do campo de busca
    if search:
        data['db'] = Produtos.objects.filter(descricao__icontains=search)
        """ o texto antes do underscore é o nome da coluna no DB """
        
    else:
        data['db'] = Produtos.objects.all()
        all = Produtos.objects.all()
        paginator = Paginator(all, 5)  # quantia de registros por página, neste caso 5 registros
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = ProdutosForm
    return render(request, 'form.html',data)


def create(request):
    form = ProdutosForm(request.POST or None)  # recebendo a requisição via post do forms.py
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):  # pk é o ID do DB, que está sendo capturado no botão visulizar no index.html
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')
