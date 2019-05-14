# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Host(models.Model):
    ip = models.CharField( max_length=100,verbose_name='主机IP')
    os = models.CharField( max_length=100, verbose_name='系统')
    partition = models.CharField(max_length=100, verbose_name='分区')

    class Meta:
        verbose_name = "主机"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip