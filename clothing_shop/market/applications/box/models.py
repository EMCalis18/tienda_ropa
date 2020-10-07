from django.db import models
from django.conf import settings

#
from model_utils.models import TimeStampedModel



#
# from .managers import SaleDetailManager


class CloseBox(TimeStampedModel):
    """
        Representa los cierres de caja
    """

    date_close = models.DateTimeField(
        'Fecha de Cierre',
    )
    count = models.PositiveIntegerField(
        'Cantidad de ventas'
    )
    amount = models.DecimalField(
        'Monto total en ventas', 
        max_digits=10, 
        decimal_places=2
    )
    

    class Meta:
        verbose_name = 'Cierre Caja'
        verbose_name_plural = 'Cirres de Caja'

    def __str__(self):
        return  str(self.date_close)
