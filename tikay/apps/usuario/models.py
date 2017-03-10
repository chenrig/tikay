from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=15)
	celular = models.CharField(max_length=15)

	def __str__(self):
		return self.usuario.username