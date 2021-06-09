from django.db import models
from . import enums
from django.utils.translation import ugettext as _


class Product(models.Model):
    """
    Represents a single product
    """
    name = models.CharField(max_length=200, verbose_name='نام', db_index=True)
    description = models.TextField(verbose_name=_('Description'), help_text='متن نمایشی برای توصیف محصول')
    price = models.PositiveIntegerField(default=0, db_index=True)
    intro_image2 = models.ImageField(verbose_name='عکس محصولات', blank=True, null=True)
    qty_in_stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(
        default=False,
        help_text='آیا این محصول فروخته می شود؟'
    )
    type = models.CharField(
        max_length=100,
        choices=enums.ProductType.choices
    )

    def __str__(self):
        return self.name
