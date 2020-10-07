from django.db import models
# third-party
from model_utils.models import TimeStampedModel
from .managers import ProductManager, CategoryManager


class Provider(TimeStampedModel):
    """Model definition for Provider."""
    name = models.CharField(
        'Nombre del proveedor',
         max_length=20,
    )
    email = models.EmailField(
        'email proveedor',
        max_length=100,
    )
    phone = models.CharField(
        'telefonos',
        max_length=40,
        blank=True,
    )

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Provedores'

    def __str__(self):
        return self.name

        
   


class SubCategoria(models.Model):
    """Model definition for Sub_Categoria."""

    name = models.CharField(
        'Nombre de la sub-categoria',
         max_length=20,
    )
    
    class Meta:
        verbose_name = 'Sub_Categoria'
        verbose_name_plural = 'Sub_Categorias'

    def __str__(self):
        return self.name



class Category(TimeStampedModel):
    """Model definition for category."""
    
    name = models.CharField(
        'Nombre de la categoria',
         max_length=20,
    )
    description = models.TextField(
        'Descripcion de la categoria',
        blank=True,
    )
    sub_category = models.ManyToManyField(SubCategoria)
    
    objects = CategoryManager()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'

    def __str__(self):
        return self.name


class Marca(TimeStampedModel):
    """Model definition for marca."""

    name = models.CharField(
        'Nombre de la marca',
         max_length=20,
    )
    provider = models.ForeignKey(
        Provider, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name
        
class Colors(models.Model):
    """ Representa color de un producto """

    color = models.CharField(
        'color', 
        max_length=30, 
        unique=True
    )
    
    class Meta:
        verbose_name = 'Color Producto'
        verbose_name_plural = 'Colores'

    def __str__(self):
        return str(self.id) + ' - ' + (self.color)

class Size(models.Model):
    """Model definition for Size."""

    
    size = models.CharField(
        'size ',  
        max_length=4,  
    )


    class Meta:
        """Meta definition for Size."""

        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return  self.size
        

class SizeNumber(models.Model):
    """Model definition for SizeNumber."""

    size_number = models.PositiveIntegerField(
        'size number',    
    )

    class Meta:
        """Meta definition for SizeNumber."""

        verbose_name = 'SizeNumber'
        verbose_name_plural = 'SizeNumbers'

    def __str__(self):
        return  str(self.size_number)



class Product(TimeStampedModel):
    """Model Product """
    # GENEROS
    MEN = 'M'
    WOMEN = 'F'
    UNISEX = 'U'
    # SIZE
    SIZE_NUMBER = 'Numero'
    SIZE = 'Letra'
    

    UNIT_CHOICES = (
        (SIZE_NUMBER, 'Numero'),
        (SIZE, 'Letra'),
    )
    GENDER_CHOICES = [
        (MEN, 'Masculino'),
        (WOMEN, 'Femenino'),
        (UNISEX, 'Unisex'),
    ]
    barcode = models.CharField(
        max_length=13,
        unique=True,
        default=0,
    )
    name = models.CharField(
        'Nombre del producto',
         max_length=50,
        )
    description = models.TextField(
        'Descripcion del producto',
        blank=True,
    )
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.CASCADE
    )
    unit = models.CharField(
        'Unidad de medida',
        max_length=20,
        choices=UNIT_CHOICES, 
    )
    size = models.ManyToManyField(
        Size,
        blank=True,
    )
    sizeNumber = models.ManyToManyField(
        SizeNumber,
        blank=True,
    )
    gender = models.CharField(
        'Genero',
        max_length=1,
        choices=GENDER_CHOICES, 
    )
    stock = models.PositiveIntegerField(
        'Cantidad en almacen',
        default=0
    )
    purchase_price = models.DecimalField(
        'Precio compra',
        max_digits=7, 
        decimal_places=2
    )
    sale_price = models.DecimalField(
        'Precio venta',
        max_digits=7, 
        decimal_places=2
    )
    num_sale = models.PositiveIntegerField(
        'Numero de ventas',
        default=0
    )
    main_image = models.ImageField(
        'imagen principal',
        upload_to='producto',
    ) # imagen principal del producto
    image1 = models.ImageField('Imagen 1', blank=True, null=True, upload_to='producto')
    image2 = models.ImageField('Imagen 2', blank=True, null=True, upload_to='producto')
    image3 = models.ImageField('Imagen 3', blank=True, null=True, upload_to='producto')
    image4 = models.ImageField('Imagen 4', blank=True, null=True, upload_to='producto')
    
    color = models.ManyToManyField(Colors)
    anulate = models.BooleanField(
        'Eliminado',
        default=False
    )
    offer = models.BooleanField(
        'En oferta',
        default=False,
        blank=True,
    )
    discount = models.PositiveIntegerField(
        'Descuento',
        default=0,
        blank=True,

    )
    price_discount = models.PositiveIntegerField(
        'precio de Descuento',
        default=0,  
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='category_product'
    )
    comment = models.TextField(
        'comentarios del producto',
        blank=True,
        max_length=150,
    )

    
    objects = ProductManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def save(self, *args ,**kwargs,):
        
        if self.offer:
            total = (self.sale_price * self.discount ) / 100
            total = self.sale_price - total
            self.price_discount = total


        super(Product ,self).save(*args , **kwargs)
        
    def __str__(self):
        return str(self.id) + ' - ' + self.name

