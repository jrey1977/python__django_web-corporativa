from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ''' CAMPOS A MOSTRAR '''
    list_display = ('title','author','published','post_categories')
    ''' EL ORDEN EN QUE LOS MUESTRO: PRIMERO AUTOR Y, 
    DENTRO DE AUTOR, POR FECHA DE PUBLICACIÓN '''
    ordering = ('author','published')
    ''' PUEDO PONER UN BUSCADOR Y DECIRLE LOS CAMPOS EN LOS QUE BUSCAR '''
    search_fields =('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)