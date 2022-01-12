from django.forms import ModelForm
from app.models import Produtos  # alterar o nome de myapp.models para app.models e chamar a classe criada em models.py

# Create the form class.


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos  # mesmo nome da classe
        fields = ['produto', 'descricao', 'quantidade', 'preco']  # nome dos campos criados na classe em models.py
