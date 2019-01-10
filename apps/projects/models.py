from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=32, verbose_name="项目名")


class Module(models.Model):
    name = models.CharField(max_length=32, verbose_name="模块名")
    description = models.TextField(verbose_name="描述")
    port = models.IntegerField(verbose_name="端口", blank=True, null=True)
    charger = models.CharField(default="", max_length=64, blank=True, verbose_name="负责人")
    package_name = models.CharField(max_length=32, blank=True, null=True, verbose_name="包名")
    project = models.ForeignKey(Project, on_delete="CASCADE")







