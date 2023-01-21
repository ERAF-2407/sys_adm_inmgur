from django.contrib import admin
from .models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Register, RegisterAdmin)

