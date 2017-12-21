from django.conf.urls import url
from.views import * 

urlpatterns = [
		#aprendices
		url(r'^agregar_aprendiz/$', registrar_aprendices, name='registrar_aprendices'),#ya instrcutor
		url(r'^buscar/$', buscar_ap, name='buscar'),#ya instructor
		url(r'^lista_aprendiz/$', aprendices, name='aprendices'),#ya instructor
		url(r'^editar_aprendiz/(?P<pk>[0-9]+)/edit/$', editar, name='post_edit'),#ya instructor
		url(r'^ranking/$', ranking, name='ranking'),#ya ambos
		url(r'^eliminar_ap/(?P<pk>[0-9]+)/$', eliminar_ap, name='eliminar_ap'),#ya instructor
		url(r'^ranking_aprendices_retos_mas_realizados/$', ranking_aprendices_retos_mas_realizados, name='ranking_aprendices_retos_mas_realizados'),#ya ambos
		url(r'^excel$', importar_view, name='excel'),#ya instructor
		#login
		url(r'^login/$', login_view, name='vista_login'),#ya ambos
		url(r'^logout/$', logout_view, name='vista_logout'),#ya ambos
		url(r'^ver_perfil/$',perfil, name='ver_mi_perfil'),
		url(r'^like_dislike/(?P<pk>[0-9]+)/$', like_dislike, name='like_dislike'),#pendiente aprendiz


		#categorias
		url(r'^agregar_categoria/$',agregar_categoria, name='agregar_categoria'),#ya instructor
		url(r'^lista_categoria/$', lista_categoria, name='lista_categorias'),#ya instructor
		url(r'^editar_categoria/(?P<pk>[0-9]+)/$', editar_categoria, name='editar_categoria'),#ya instrcutor
		url(r'^eliminar_categoria/(?P<pk>[0-9]+)/$', eliminar_categoria, name='eliminar_categorias'),#ya instructor

		#reto
		url(r'^buscar_reto/$',buscar_reto, name='buscar_retos'),
		url(r'^crear_reto/$',crear_reto, name='crear_reto'),#ya instructor
		url(r'^listar_reto/$', ver_retos, name='lista_reto'),#ya ambos
		url(r'^editar_reto/(?P<pk>[0-9]+)/$', editar_reto, name='editar_retos'),#ya instructor
		url(r'^detalle_reto/(?P<pk>[0-9]+)/$', detalle_reto, name='ver_detalle_reto'),#ya ambos
		url(r'^eliminar_reto/(?P<pk>[0-9]+)/$', eliminar_reto, name='eliminar_reto'),#ya instructor
		url(r'^listar_reto_por_calificar/$', lista_sin_c, name='lista_reto_sin_c'),#ya instructor
		url(r'^lista_retos_calificado/$', lista_retos_calificados, name='lista_retos_calificados'),#ya instructor
		url(r'^calificar_reto/(?P<pk>[0-9]+)/$', calificar_reto, name='calificar_reto'),#ya instructor
		url(r'^solucionar_reto_i/(?P<pk>[0-9]+)/$', solucionar_reto_i, name='solucionar_reto_individual'),#ya aprendiz
		url(r'^lista_mis_retos$',lista_mis_retos, name='lista_mis_retoss'),#ya ambos
		url(r'^retos_popular/$',retos_popular, name='retos_popular'),#ya ambos
		#instructores
		url(r'^agregar_instructor/$', registrar_instructor, name='registrar_instructores'),#ya instructor
		url(r'^lista_instructor/$', lista_instructor, name='lista_instructores'),#ya instructor
		url(r'^editar_instructor/(?P<pk>[0-9]+)/$', editar_instructor, name='edit_intructor'),#ya administrador
		url(r'^eliminar_instructor/(?P<pk>[0-9]+)/$', eliminar_instructor, name='eliminar_instructor'),#ya administrador
		url(r'^inhabilitar_user/(?P<pk>[0-9]+)/$',inhabilitar_user, name='inhabilitar'),#ya instructor

		#vista principal 
		url(r'^$', vista_principal, name='index'),

]