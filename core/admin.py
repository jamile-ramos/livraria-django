from django.contrib import admin
from core.models import Autor, Categoria, Editora, Livro, Compra, ItensCompra

admin.site.register(Categoria)
admin.site.register(Editora)    
admin.site.register(Autor)
admin.site.register(Livro)  

# Isso é só para melhorar a forma de visualizacao no admin para que itens e compras fiquem na mesma página
class ItensInline(admin.TabularInline): 
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
