from django.contrib import admin
from .models import Usuario, Ciudadano, Tecnico, Administrativo, Ubicacion, TipoFalla, EstadoQueja, Queja, ComentarioQueja

admin.site.register(Usuario)
admin.site.register(Ciudadano)
admin.site.register(Tecnico)
admin.site.register(Administrativo)
admin.site.register(Ubicacion)
admin.site.register(TipoFalla)
admin.site.register(EstadoQueja)
admin.site.register(Queja)
admin.site.register(ComentarioQueja)
