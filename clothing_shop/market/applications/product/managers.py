from django.db import models
from django.db.models import Q, F, Count

class ProductManager(models.Manager):
    """ managers de productos """
    #def para filtrar los productos nuevos
    def list_product_new(self):
        return self.filter(
            offer=False,
        ).order_by('-created')[:3]
    

    #def para filtrar por productos en oferta
    def offer_list(self):
        return self.filter(
            offer=True,
        ).order_by('-created')[:3]

    
    #def para buscar producto 
    def search_product(self,kword, categoria, sub_categoria):
        

        if len(categoria) > 0 :
            return self.filter(
                category__name=categoria,
                name__icontains=kword
            )
        elif len(sub_categoria) > 0:
            return self.filter(
                category__sub_categoria__name=sub_categoria,
                name__icontains=kword
            )
        else:    
            return self.filter(
                name__icontains=kword
            )

        
    

class CategoryManager(models.Manager):

    def count_product_on_category(self):
        return self.annotate(
            num_products=Count('category_product')   
        )
        
        