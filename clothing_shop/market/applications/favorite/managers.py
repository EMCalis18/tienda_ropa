from django.db import models

class FavotitosManager(models.Manager):
    

    def favoritos_user(self, usuario):
        return self.filter(
            product__anulate=False,
            user=usuario,
              
        ).order_by('-created')