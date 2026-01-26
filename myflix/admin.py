from django.contrib import admin
from myflix.models import user, stream

class users(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'cpf', 'data de nascimento', 'celular')
    lisy_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(user, users)

class streams(admin.ModelAdmin):
    list_display = ('id','codigo', 'descricao')
    lisy_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(streams, streams)