from django.forms import ModelForm
from .models import Servico, CategoriaComercio


class FormServico(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class': 'form-control' })
        self.fields['titulo'].widget.attrs.update({'placeholder': 'titulo' })
        self.fields['categoria_comercio'].widget.attrs.update({'class': 'form-control' })
        self.fields['categoria_comercio'].widget.attrs.update({'placeholder': 'categoria_comercio' })
        
        choices = list()   
        for i, j in self.fields['categoria_comercio'].choices:
            categoria = CategoriaComercio.objects.get(titulo=j)
            choices.append((i.value, categoria.get_titulo_display()))
            
        self.fields['categoria_comercio'].choices = choices