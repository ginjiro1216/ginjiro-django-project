from django.db import models

from django.conf import settings


class FoodKind(models.Model):
    kind = models.CharField('種類', max_length=128)

    def __str__(self):
        return self.kind


# Create your models here.
class FoodShop(models.Model):
    shop = models.CharField('おみせ', max_length=128)
    food_kind = models.ForeignKey(FoodKind,
                                  verbose_name='しゅるい',
                                  on_delete=models.CASCADE)
    description = models.TextField('せつめい', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name='とうこうしゃ',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.shop


