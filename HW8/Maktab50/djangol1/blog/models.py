from django.db import models


class Post(models.Model):

    created_data = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    title = models.CharField(verbose_name='عنوان اسلاید', max_length=100)
    creator = models.ForeignKey('auth.User', verbose_name='کاربر', on_delete=models.PROTECT)
    content = models.TextField(verbose_name='متن اسلاید')
    # email = models.EmailField(max_length=254)
    # slide_show = models.TextField(verbose_name='متن اسلاید')
    # head = models.CharField(verbose_name='عنوان اسلاید', max_length=110)
