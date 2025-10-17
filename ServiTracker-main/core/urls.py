from django.urls import path
from .views import (
    index, nosotros, contacto, servicios,
    dashboard, crear_queja, panel_empleados,
    cambiar_estado, agregar_comentario,
    error_404_test, error_500_test, admin_gestion_usuarios, admin_reportes,
    admin_crear_usuario, admin_editar_usuario
    )

urlpatterns = [
    # Páginas públicas
    path('', index, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('servicios/', servicios, name='servicios'),

    # Dashboard y funcionalidades
    path('dashboard/', dashboard, name='dashboard'),
    path('crear-queja/', crear_queja, name='crear_queja'),
    path('panel-empleados/', panel_empleados, name='panel_empleados'),
    path('gestion/usuarios/', admin_gestion_usuarios, name='admin_gestion_usuarios'),
    path('gestion/reportes/', admin_reportes, name='admin_reportes'), 
    path('gestion/usuarios/nuevo/', admin_crear_usuario, name='admin_crear_usuario'),
    path('gestion/usuarios/<int:usuario_id>/editar/', admin_editar_usuario, name='admin_editar_usuario'),

    # Gestión de PQR
    path('queja/<int:queja_id>/cambiar-estado/', cambiar_estado, name='cambiar_estado'),
    path('queja/<int:queja_id>/comentario/', agregar_comentario, name='agregar_comentario'),

    # Errores
    path('test-404/', error_404_test),
    path('test-500/', error_500_test),
]
