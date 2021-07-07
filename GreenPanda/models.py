from django.db import models

# Create your models here.


class TipoMoneda(models.Model):
    idMoneda = models.IntegerField(primary_key=True, verbose_name="Id de Moneda")
    MonedaDePago = models.CharField(max_length=15, verbose_name="Pesos o Dólares")
    

    def __str__(self):
        return self.MonedaDePago

class RegistroP(models.Model):
    NumeroId = models.IntegerField(primary_key=True, verbose_name="Numero de identificación")
    fotoLogoP = models.ImageField(upload_to="Fotografía/logo del proveedor", null=True, verbose_name="Fotografía/logo del proveedor")
    NombreC = models.CharField(max_length=40, verbose_name="Nombre Completo del Proveedor")
    Telefono = models.IntegerField(verbose_name="Número telefonico")
    Direccion = models.CharField(max_length=50,verbose_name="Dirección")
    Email = models.CharField(max_length=30, verbose_name="Email")
    Pais = models.CharField(max_length=15, verbose_name="País")
    MonedaPago = models.ForeignKey(TipoMoneda, on_delete=models.CASCADE)


    def __str__(self):
        return self.NumeroId
