

import imagesearch as ims
from caminos.caminos import caminos
import random
import time
import math,sys


import datetime
import dateutil.relativedelta


from pynput.mouse import Button, Controller
mouse=Controller()



def fun_error(e):
   return 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e

class Acciones:
    def __init__(self,camino=[],path="img/"):
        self.camino=camino
        self.path = path
        self.posiciones_arena = [(696, 180),(575, 314),(809, 314),(458, 442),(698, 456),(924, 439),(349, 577),(565, 578),(809, 580),(1048, 585)]
        self.ciclo=0

        #CAMINO
        self.tiempo_inicial= datetime.datetime.now()
        self.tiempo_faltante= 0
        self.tiempo_final = datetime.datetime.now()        
        self.tiempo_ejecucion=3 #TIEMPO EN MINUTOS QUE DEBERIA DURAR EL CAMINO


        #ARENAS
        self.arenas_variables = {"pos_oponente":-1,"turno":0,"arena_resultados":[0,0],"no_atacar":[]}
        self.arenas_defecto = {"pos_oponente":-1,"turno":0,"arena_resultados":[0,0],"no_atacar":[]}
        self.camino_actual=""
        
        self.info= {}
    
    def imprimir_info(self):
        self.calcular_tiempo_faltante()
        self.info={}
        self.info["ciclo"] = self.ciclo
        self.info["tiempo_faltante"] = self.tiempo_faltante
        self.info["camino_actual"] = self.camino_actual
        if(self.camino_actual=="jugar_arena_adentro"):
            self.info["arenas_variables"]=self.arenas_variables
        print(self.info)
    
    def calcular_tiempo_faltante(self):
        """ Tiempo faltante en minutos"""
        self.tiempo_faltante = (self.tiempo_inicial.hour-self.tiempo_final.hour)*60 \
            + (self.tiempo_inicial.minute-self.tiempo_final.minute)


    # @classmethod
    def ejecutar_accion(self,item,data={}):
        try:
            accion_ar = []
            img= self.path+item["img"]


            if(type(item["accion"]) ==list ):
                accion_ar = item["accion"]
                # print("es array")
            else:
                accion_ar.append(item["accion"]) 
            
            
            pos = ims.imagesearch(img)
            res = {"correcto":0,"config":item}
            ##########################
            # LISTAS DE ACCIONES
            ###############################
            
            
            for i, accion in enumerate(accion_ar):
                
                if(pos[0]!=-1):

                    if(accion=="click"):
                        ims.click_image(img,pos,"left")
                    elif(accion=="doble"):
                        ims.click_image(image=img,clicks=2,pos=pos,action="left")
                    elif(accion=="ARENA"):
                        self.jugar_arena()
                    elif(accion=="elegir_oponente"):
                        res["pos_oponente"],res["estrategia"]= self.elegir_oponente(data)
                        op= self.posiciones_arena[res["pos_oponente"]]
                        self.done_click(op[0],op[1])
                        self.arenas_variables["pos_oponente"] = res["pos_oponente"]

                    elif(accion=="arena_resultados" ):
                        if(item["resultado"]=="victoria"):
                            self.arenas_variables["arena_resultados"][0]+=1
                        else:
                            self.arenas_variables["arena_resultados"][1]+=1
                        res["arena_resultados"]=self.arenas_variables["arena_resultados"]
                    elif(accion=="final_batalla"):
                        self.arenas_variables["turno"]+=1
                        self.arenas_variables["no_atacar"] = []
                        self.imprimir_info()
                    elif(accion=="final_arena"):
                        self.arenas_variables = self.arenas_defecto
                    elif(accion=="esperar"):
                        time.sleep(item["esperar"])
                    elif(accion=="arena_no_atacar"):
                        self.arenas_variables["no_atacar"].append(self.arenas_variables["pos_oponente"])


                    res["correcto"]=1
                    # print(accion)
                    # print(res)
                    # return res
                else:
                    if "accion_no_encuentra" in item:
                        accion=item["accion_no_encuentra"]
                        if(accion=="add_no_atacar"):
                            self.arenas_variables["no_atacar"].append(self.arenas_variables["pos_oponente"])
                
                
            return res
        except Exception as e:
            print(item)
            print(fun_error(e))

    @classmethod
    def jugar_arena(cls): 
        ja =Acciones()
        ja.ejecutar_camino("jugar_arena_adentro")       
        # self.ejecutar_camino("jugar_arena_adentro")
        # ejecutar=caminos[] 
        




    def ejecutar_camino(self,camino="jugar_arena"):

        """
        config
         """
        self.camino_actual = camino
        ejecutar=caminos[camino]["pasos"]


        ################################
        # TIEMPO ENTRE PASOS
        #################################### 
        tiempo_pasos=1
        if "tiempo_pasos" in caminos[camino]["config"]:
            tiempo_pasos= caminos[camino]["config"]["tiempo_pasos"]
        

        ###############################
        # TIEMPO EJECUCION PROCESO
        ###############################
        
        if("tiempo_ejecucion" in caminos[camino]["config"]):
            self.tiempo_ejecucion= caminos[camino]["config"]["tiempo_ejecucion"]
        
        self.tiempo_inicial = datetime.datetime.now()
        self.tiempo_final  = self.tiempo_inicial + dateutil.relativedelta.relativedelta(minutes=self.tiempo_ejecucion)       
        
        
        
        ###########################################
        # CICLOS
        ###################################
        ciclos=1
        if("ciclos" in caminos[camino]["config"]):
            ciclos= caminos[camino]["config"]["ciclos"]
        
        
        terminar=0



        while(  (terminar<ciclos)   and (self.tiempo_final>self.tiempo_inicial)):    
            for i, item in enumerate(ejecutar):        
                time.sleep(0.2)
                resultado = self.ejecutar_accion(item)
                

                if resultado["correcto"]==1:
                    
                    
                    if "final" in resultado["config"] :                      
                        terminar+=1
                        print("terminar por llegar al final")

                    time.sleep(tiempo_pasos)

                
                        



            self.tiempo_inicial = datetime.datetime.now()
            if((self.tiempo_final<self.tiempo_inicial)):
                
                print("terminar por tiempo")



    def done_click(self, position1, position2):
        mouse.position=(position1,position2)
        mouse.click(Button.left,1)


    def posicion_calcerbero(self):
        pos = ims.imagesearch(self.path+"calcerbero.PNG")
        
        puntos=[]
        minimo = 1000
        p_minimo = -1
        for i,item in enumerate(self.posiciones_arena):
            distancia = math.sqrt(  math.pow(pos[0] - item[0],2)  + math.pow(pos[1] - item[1],2) )
            if(distancia <minimo):
                minimo=distancia
                p_minimo= i
            puntos.append(distancia)


        return p_minimo

    
    def elegir_oponente(self, data={}):
        """pos_calcerbero
        no_atacar: array de las posiciones que no se deben atacar
        v_d: victorias y derrotas
        turno: que turno esta
        """

        no_atacar=[]
        if "no_atacar" in data:
            no_atacar =data["no_atacar"]
        
        
        pos_calcerbero = self.posicion_calcerbero()
        self.arenas_variables["no_atacar"].append(pos_calcerbero)

        print(self.arenas_variables)
        atacar=0
        terminar = 0
        estrategia = -1
        while(terminar == 0):
            if(self.arenas_variables["turno"]==0):
                atacar = random.randint(5,9)
                estrategia = 0

            ##################################
            #IR POR PODIO
            ##################################    
            elif(  (pos_calcerbero not in [0,1]) and (self.arenas_variables["arena_resultados"][1]==0) ):
                atacar=random.randint(0, 5)
                estrategia = 1
                
            
            ##################################
            #GUARDAR PODIO
            ##################################
            elif(pos_calcerbero in [0,1]):
                atacar=random.randint(6, 9)
                estrategia = 2
                
            
            ##########################################
            # TRATAR DE ATACAR 
            #########################################
            elif( self.arenas_variables["arena_resultados"][0]> 0           ):
                atacar = random.randint(4, 9)
                estrategia = 3
            
            
            
            ###################################
            # NINGUNA ESTRATEGIA
            #################################
            else:
                atacar= random.randint(0, 9)
                estrategia = -2

            if(atacar not in self.arenas_variables["no_atacar"]):
                terminar= 1
        

        
        return atacar,estrategia


    
class Pruebas:
    def fun_arrastrar_img_a_otra():
        pos = im.imagesearch(path+"excel.PNG")
        pos2= im.imagesearch(path+"carpeta.PNG")
        
        if(pos[0]!=-1 and pos2[0]!=-1):
            pyautogui.moveTo(pos[0], pos[1], 2, pyautogui.easeInOutQuad)
            pyautogui.mouseDown() #sostener
            pyautogui.moveTo(pos2[0], pos2[1], 2, pyautogui.easeInOutQuad)
            pyautogui.mouseUp()
            
            
        print(pos)
        print(pos2)
    
fun_arrastrar_img_a_otra()



if __name__ == "__main__":
    ac = Acciones()
    ac.ejecutar_camino("jugar_arena")
    
