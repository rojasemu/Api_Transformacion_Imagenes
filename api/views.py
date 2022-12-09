import json
import os
import time
from django.http import JsonResponse
from django.views import View
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageChops




#log


# Create your views here.

class ProcesarView(View):
    
    # para saltarse el CSRF token 
    @method_decorator(csrf_exempt) #   con el decorador y el parametro que recibe es para saltar la restriccion de CSRF
    def dispatch(self, request, *args, **kwargs): # metodo que se ejecuta cada vez que hacemos una peticion
        return super().dispatch(request, *args, **kwargs)
        
    #Consultar
    def get(self, request, id=0):
        
        if  id >0:
           imagenes =list(Images.objects.filter(id=id).values())
           history= History.objects.get(id=id)                
           star_history =history.star_time
           end_history=history.end_time
           status=history.status
           
           if len(imagenes)>0:
               img =imagenes[0]
               datos ={'message': "Success", 'img':img, 'Historial_imagen':'Historia', 'Star_time':star_history, 'end_history':end_history, 'status':status } 
           else:
               datos = {'message': "Image not found..."}
           return JsonResponse (datos)           
        
        else:
                 
            imagenes = list(Images.objects.values())        
            if len (imagenes)>0:
                datos = {'message': "Success", 'imagenes':imagenes}        
            else:
                datos = {'message': "Image not found..."}        
            return JsonResponse (datos)       
       
   
    #Agregar
    def post(self, request):
        
        jd =json.loads(request.body)# convierto lo json a diccionario para que lo pueda entender python
        Images.objects.create (name=jd['name'], image=jd['image'])
        #tomo los datos del diccionario y los registro en la base de datos
        
        datos ={'message':"Success"}  
        return JsonResponse (datos)   
    
    
    
    #Actualizar
    def put(self, request, id, id_step):
        
        jd =json.loads(request.body)
        imagenes =list(Images.objects.filter(id=id).values())
        
        ima= Images.objects.get(id=id)
        
        paso= Step.objects.get(id=id_step)
        
        step =paso.id
  
              
            
        for diccionario in imagenes:
               #print(diccionario['image'])           
           archivo=diccionario['image']
           
           ruta_comprobar =os.path.abspath("./") + "/media/"+archivo
           print(ruta_comprobar)
        if len(imagenes) >0:
           step =paso.id
           ima=ima.id
           
           if os.path.isfile(ruta_comprobar) and paso.name == "Pasar a Blanco y Negro":
                img = Image.open(ruta_comprobar)
                imgGray = img.convert('L')
                #imgGray.show()
                imgGray.save(os.path.abspath("./media") + "/images/"  + str(id) + "blanco_negro_new.png")
                Images.objects.filter(id=id).update(image="images/" + str(id) + "blanco_negro_new.png")
                History.objects.create(step_id=step, image_id=ima, status='proccess')
                history= History.objects.get(id=id)
                
                star_history =history.star_time
                end_history=history.end_time     
                datos = {'id_imagen':id,
                         'status': "Success",
                         'step': "Se Cambio la Imagen a Blanco y Negro.",'Star_time':star_history, 'end_history':end_history} 
                
           if os.path.isfile(ruta_comprobar) and paso.name == "Invertir los colores":
               
                img = Image.open(ruta_comprobar)                
                inv_img = ImageChops.invert(img)                 
                #inv_img.show()
                inv_img.save(os.path.abspath("./media") + "/images/"  + str(id) + "invertir_color.png")
                Images.objects.filter(id=id).update(image="images/" + str(id) + "invertir_color.png")
                History.objects.create(step_id=step, image_id=ima, status='proccess') 
                history= History.objects.get(id=id)
                
                star_history =history.star_time
                end_history=history.end_time
                datos = {'id_imagen':id,
                         'status': "Success",
                         'step': "Se Invertio el color de la Imagen.",'Star_time':star_history, 'end_history':end_history} 
                
           if os.path.isfile(ruta_comprobar) and paso.name == "Rotal la imagen 90 grados":
               
                Original_Image = Image.open(os.path.join(ruta_comprobar))
                rotated_image= Original_Image.transpose(Image.ROTATE_90)  
                #rotated_image1.show()                
                rotated_image.save(os.path.abspath("./media") + "/images/"  + str(id) + "new90.png")
                Images.objects.filter(id=id).update(image="images/" + str(id) + "new90.png") 
                History.objects.create(step_id=step, image_id=ima, status='proccess')
                history= History.objects.get(id=id)
                
                star_history =history.star_time
                end_history=history.end_time                
                
                datos = {'id_imagen':id,
                         'status': "Success",
                         'step': "Se Roto la imgan a  90 grados.",'Star_time':star_history, 'end_history':end_history} 
                
           if os.path.isfile(ruta_comprobar) and paso.name == "E invertir la sobre el eje vertical":
               
                Original_Image = Image.open(os.path.join(ruta_comprobar))
                rotated_image1 = Original_Image.transpose(Image.TRANSVERSE) 
                a =rotated_image1.transpose(Image.ROTATE_90)
                #a.show()             
                a.save(os.path.abspath("./media") + "/images/"  + str(id) + "eje_vertical.png")
                Images.objects.filter(id=id).update(image="images/" + str(id) + "eje_vertical.png")
                History.objects.create(step_id=step, image_id=ima, status='proccess')
                history= History.objects.get(id=id)
                
                star_history =history.star_time
                end_history=history.end_time
                
                
                datos = {'id_imagen':id,
                         'status': "Success",
                         'step': "Se invirtio la imagen sobre el eje vertical.", 'Star_time':star_history, 'end_history':end_history}  
                 
        else:
            datos = {'message': "Image  not found..."}    
 
  
        return JsonResponse (datos)    
  
    
    

    
    


