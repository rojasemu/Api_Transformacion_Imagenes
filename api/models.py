from django.db import models

# Create your models here.

class Images(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Nombre')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to ="images", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')  
    
    
    
class Logs(models.Model):
    
   image=models.ForeignKey(Images, on_delete=models.CASCADE, null=True, blank=True)
   error =models.CharField(max_length=100, verbose_name='Errores')
   description= models.CharField(max_length=100, verbose_name='Descripcion')
   
class Step(models.Model):
    
    name = models.CharField(max_length=100, verbose_name='Pasos')
    
class History(models.Model):
    step=models.ForeignKey(Step, on_delete=models.CASCADE, null=True, blank=True)  
    image=models.ForeignKey(Images, on_delete=models.CASCADE, null=True, blank=True)    
    status =models.CharField(max_length=50, verbose_name='estado')
    star_time=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    end_time=models.DateTimeField(auto_now=True, verbose_name='Editado el')
    



    