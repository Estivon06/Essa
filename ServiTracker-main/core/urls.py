from django.urls import path
from .views import (
    index, nosotros, contacto, servicios,
    dashboard, crear_queja, panel_empleados,
    cambiar_estado, agregar_comentario,
    error_404_test, error_500_test,
    admin_gestion_usuarios, admin_reportes,
    admin_crear_usuario, admin_editar_usuario, admin_eliminar_usuario,
    admin_panel_quejas, admin_asignar_tecnico, admin_editar_queja, admin_eliminar_queja
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

    # Gestión de usuarios y reportes (panel personalizado)
    path('gestion/usuarios/', admin_gestion_usuarios, name='admin_gestion_usuarios'),
    path('gestion/usuarios/nuevo/', admin_crear_usuario, name='admin_crear_usuario'),
    path('gestion/usuarios/<int:usuario_id>/editar/', admin_editar_usuario, name='admin_editar_usuario'),
    path('gestion/usuarios/<int:usuario_id>/eliminar/', admin_eliminar_usuario, name='admin_eliminar_usuario'),
    path('gestion/reportes/', admin_reportes, name='admin_reportes'),

    # Panel administrativo de PQR y acciones
    path('gestion/quejas/', admin_panel_quejas, name='admin_panel_quejas'),
    path('gestion/quejas/<int:queja_id>/asignar/', admin_asignar_tecnico, name='admin_asignar_tecnico'),
    path('gestion/quejas/<int:queja_id>/editar/', admin_editar_queja, name='admin_editar_queja'),
    path('gestion/quejas/<int:queja_id>/eliminar/', admin_eliminar_queja, name='admin_eliminar_queja'),

    # Gestión de PQR (vistas existentes)
    path('queja/<int:queja_id>/cambiar-estado/', cambiar_estado, name='cambiar_estado'),
    path('queja/<int:queja_id>/comentario/', agregar_comentario, name='agregar_comentario'),

    # Errores
    path('test-404/', error_404_test),
    path('test-500/', error_500_test),
]
