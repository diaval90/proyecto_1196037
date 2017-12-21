from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Los modelos  estan listos.
NIVELES = (
		('basico','Basico'),
		('medio','Medio'),
		('dificil','Dificil'),
	)
TIPO = (
		('individual','Individual'),
		('grupal','Grupal'),
	)
ESTADO = (
		 ('activo','Activo'),
		 ('incativo','Inactivo'),
	)

ESTADO2  = (
		 ('calificado','Calificado'),
		 ('sin calificar','Sin Calificar'),
	)

class Categoria (models.Model):
	nombre          = models.CharField(max_length = 50  , unique = True)

	def __unicode__ (self):
		return self.nombre 

class Reto (models.Model):
	descripcion         = models.TextField()
	autor				= models.CharField(max_length = 50,null=True, blank=True)
	fecha_creacion      = models.DateTimeField(auto_now_add = True)
	fecha_publicacion   = models.DateField()
	hora_publicacion    = models.TimeField()
	fecha_limite        = models.DateField()
	hora_limite         = models.TimeField()
	tipo                = models.CharField(max_length = 50, choices = TIPO)
	dificultad          = models.CharField(max_length = 50, choices = NIVELES)
	archivo             = models.FileField(upload_to = 'media')
	categoria           = models.ForeignKey(Categoria)
	estado              = models.CharField(max_length = 50, choices = ESTADO, default="Activo")
	like                = models.IntegerField(default = 0)
	dis_like            = models.IntegerField(default = 0)
	premio              = models.FileField(upload_to = 'media', null=True, blank=True) 
	puntos_maximos      = models.IntegerField(null=True, blank=True)
	def clean(self):
		if self.fecha_publicacion:
			if self.fecha_limite < self.fecha_publicacion:
				raise ValidationError('La fecha limite no puede ser menor a la fecha de publicacion')
	def clean(self):
		if self.hora_limite:
			if self.hora_limite == self.hora_publicacion:
				raise ValidationError('la hora de publicacion no puede ser igual a la hora limite')

	def __unicode__ (self):
		return self.descripcion

class Persona (models.Model):
	imagen			= models.FileField(upload_to = 'media', null=True, blank=True)
	identificacion  = models.CharField(max_length = 50, unique=True)
	nombres         = models.CharField(max_length = 256)
	apellidos       = models.CharField(max_length = 256)
	ficha           = models.CharField(max_length = 30)
	correo          = models.EmailField(unique=True, null=True, blank=True)
	telefono        = models.CharField(max_length = 12 , null=True, blank=True)
	direccion       = models.CharField(max_length = 50, null=True, blank=True)
	puntaje         = models.IntegerField(null=True, blank=True, default=0)
	user            = models.OneToOneField(User)

	def __unicode__ (self):
		return self.nombres

class Persona_Reto (models.Model):
	persona         = models.ForeignKey(Persona)#,null= True, blank= True)
	reto            = models.ForeignKey(Reto)
	estado          = models.CharField(max_length = 50, null= True, blank= True, choices = ESTADO2)
	fecha_respuesta = models.DateTimeField(auto_now_add=True)
	calificacion    = models.IntegerField(null= True, blank= True)
	nombre_grupo    = models.CharField(max_length = 50, null= True, blank= True)
	archivo         = models.FileField(upload_to = 'respuestas')
	descripcion     = models.TextField(null= True, blank= True)


	def __unicode__ (self):
		return self.estado

class Like_Dislike (models.Model):
	reto           = models.ForeignKey(Reto)
	seleccion      = models.BooleanField()
	usuario		   = models.IntegerField()
