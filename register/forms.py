from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        exclude = ('created', 'datecompleted', 'user',)
        widgets = {
            
            # IDENTIFICACIÓN DEL REGISTRO            
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un nombre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripción'}),
            'urgente': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),

            # 1. IDENTIFICACIÓN DEL CASO
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un municipio'}),
            'parroquia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un parroquia'}),
            'referido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre del referido'}),
            'ci_referido': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la cédula del referido'}),
            
            # 2. DATOS DE IDENTIFICACIÓN
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el apellido'}),
            'ci': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la cédula'}),
            'fecha_n': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Selecciona la fecha de nacimiento', 'type': 'date'}),
            'lugar_n': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe donde nacio'}),
            'est_civil': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona el estado cívil'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la dirección'}),
            'sabe_leer_escribir': forms.CheckboxInput(), 
            'ocupacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la cédula del referido'}),
            
            # 3. DATOS FAMILIAR
            'nombre_apellido_f': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el nombre y apellido del familiar'}),
            'edad_f': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la edad del familiar'}),
            'ci': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la cédula del familiar'}),
            'est_civil_f': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Estado civíl del familiar'}),
            'ocupacion_f': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ocupación del famliar'}),

            # 4. CONDICIONES DE VIVIENDA
            'vivienda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de vivienda'}),
            'parades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describa las paredes'}),
            'piso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describa el piso'}),
            'techo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describa el techo'}),
            'cuartos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuántos cuartos tiene?'}),
            'comedor': forms.CheckboxInput(), 
            'sala': forms.CheckboxInput(), 
            'cocina': forms.CheckboxInput(), 

            # 5. SITUACIÓN SOCIO-ECONÓMICA

            'sueldo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuánto gana?'}),
            'subsidios': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Recibe subsubsidios'}),
            'becas_pen_jub': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Recibe becas?'}),
            'ayudas_familiares': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuenta con alguna ayuda familiar?'}),
            'otros': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Qué otro tipo de ingreso percibe?'}),
            'total_ingresos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
            'vivienda': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuánto gasta en vivienda?'}),
            'servicios': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuánto gasta en servicios?'}),
            'transporte': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuánto gasta en transporter?'}),
            'medicinas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuánto gasta en medicinas?'}),
            'total_egresos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),

            # 6. ÁREA DE SALUD
            'enf_padecidas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Padecidas'}),
            'enf_actuales': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Actuales'}),
            'medico_tratante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Médico'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre donde se ha atendido'}),
            
            # 7. OBSERVACIONES
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agregue alguna observación'}),
        }