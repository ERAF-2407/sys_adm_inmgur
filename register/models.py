from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  """
  # 1. IDENTIFICACIÓN DEL CASO
  municipio = models.CharField(max_length=50)
  parroquia = models.CharField(max_length=50)
  referido = models.CharField(max_length=50)
  ci_referido = models.CharField(max_length=50)

  # 2. DATOS DE IDENTIFICACIÓN
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  ci = models.CharField(max_length=50)
  fecha_nacimiento = models.DateTimeField(auto_now_add=True)
  lugar_nacimiento = models.CharField(max_length=50)
  estado_civil_soltera = models.BooleanField(default=False)
  estado_civil_casada = models.BooleanField(default=False)
  estado_civil_divorsiada = models.BooleanField(default=False)
  estado_civil_viuda = models.BooleanField(default=False)
  direccion = models.CharField(max_length=50)
  sabe_leer_escribir = models.BooleanField(default=False)
  ocupacion = models.CharField(max_length=50)

  # 3. GRUPO FAMILIAR
  nombre_apellido_familiar = models.CharField(max_length=50)
  edad =
  """



  def __str__(self):
    return self.title + ' - ' + self.user.username

