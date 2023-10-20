from django.db import models

class Stand (models.Model):
    localizacao = models.CharField(max_length=300)
    valor = models.DecimalField(
        verbose_name=("valor"),
        decimal_places=2,
        max_digits=6
    )

    def __str__(self):
        return self.localizacao

class Reserva (models.Model):
    cnpj = models.CharField(max_length=150)
    nome_empresa = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=250)
    quitado = models.BooleanField()
    localizacao = models.ForeignKey(Stand, on_delete=models.CASCADE,  related_name='reservas_localizacao')

