from django import forms
from .models import *
from django.contrib.auth.models import User
class busqueda(forms.Form):
	buscar = forms.CharField()

class busqueda_reto(forms.Form):
	busca = forms.CharField()	

class PersonaForm(forms.ModelForm):
	class Meta:
			model = Persona
			fields = ('identificacion','nombres','apellidos','ficha', 'telefono',)		


class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))


class aprendicesForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ('nombres', 'apellidos','ficha','telefono',)

class instructorForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ('nombres', 'apellidos','telefono',)		

class Agregar_Categoria_Forms(forms.ModelForm):
	class Meta:
		model= Categoria
		fields= '__all__'

class Crear_Reto_Form (forms.ModelForm):
	class Meta: 
		model = Reto
		fields	 = '__all__'
		exclude = ('like', 'dis_like', 'autor', 'estado')
		widgets= {
			'fecha_publicacion': forms.DateInput(attrs={'class':'datepicker'}),
			# 'hora_publicacion': forms.TimeInput(attrs={'class':'timepicker'}),
			'fecha_limite': forms.DateInput(attrs={'class':'datepicker'}),
			# 'hora_limite': forms.TimeInput(attrs={'class':'timepicker'}),
		}

class RegisterForm(forms.Form):	
	username 	= forms.CharField(label = "ingresa tu correo", widget = forms.EmailInput())
	# email 		= forms.EmailField(label = "Correo Electronico", widget = forms.TextInput())
	password_one = forms.CharField(label = "identificacion", widget = forms.PasswordInput(render_value = False))
	# password_two = forms.CharField(label = "Confirmar Password", widget = forms.PasswordInput(render_value = False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username = username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya Existe')

	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	try:
	# 		u = User.objects.get(email = email)
	# 	except User.DoesNotExist:
	# 		return email
	# 	raise forms.ValidationError('Email ya registrado')

	# def clean_password_two(self):
	# 	password_one = self.cleaned_data['password_one']
	# 	password_two = self.cleaned_data['password_two']

	# 	if password_one == password_two:
	# 		pass
	# 	else:
	# 		raise forms.ValidationError('Password no coinciden')

class editar_user_form(forms.ModelForm):
	# clave = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length= 140)
	class Meta:
		model   = User
		fields = ('username', )			

class persona_reto(forms.ModelForm):
	class Meta: 
		model = Persona_Reto
		fields	 = [
		'calificacion'
		]


class solucion_reto_i(forms.ModelForm):
	class Meta: 
		model = Persona_Reto
		fields	 = [
		'descripcion',
		'archivo'
		]

class importar_form(forms.Form):
	#Nombres = forms.CharField(max_length=100)
	docfile = forms.FileField(
		label='Selecciona un archivo'
	)
