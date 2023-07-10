from django.db import models

MARCA_CHOICE = [
    ('FIAT', 'Fiat'),
    ('CHEVROLET', 'Chevrolet'), 
    ('FORD', 'Ford'),
    ('TOYOTA', 'Toyota')
]

CATEGORIA_CHOICE = [
    ('PARTICULAR', 'Particular'), 
    ('TRANSPORTE', 'Transporte'),
    ('CARGA', 'Carga'),
]

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20, choices=MARCA_CHOICE, verbose_name='Marca', default='Ford')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    s_carroceria = models.CharField(max_length=50, verbose_name='Serial Carrocería')
    s_motor =  models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICE, verbose_name='Categoría', default='Particular')
    precio = models.IntegerField(null=False, verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def save(self, *args, **kwargs):
        super(Vehiculo, self).save(*args, **kwargs)

    def __str__(self):
        return self.modelo
    
    class Meta:
        permissions = (
            ("visualizar_catalogo", "visualizar_catalogo"),
            ("can_add_vehiculo", "can_add_vehiculo"),
        )