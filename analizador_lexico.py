from string import ascii_letters
def evaluar(lista):#expresion [int, a;]
  if(lista[0]=="int" or lista[0]=="double"):
    if(len(lista)>2):
      #int , a, = ,5;
      #int _a = 5;
     
      # _a = 5;
      lista2=list("_")
      abc=list(ascii_letters)+lista2 #abc...ABC....._

      #_a;
      sub_lista_=lista[1] # _ , a , ;
    
      for i in range(len(abc)):
        if(sub_lista_[0]==abc[i]):
          valido= True
          break
        else:
          valido=False

      if(lista[2]=="="):
        valido2=True
      else:
        valido2=False

      numero= (lista[len(lista)-1]) # 5;
      numero_final = numero[0]
      
      rango_numeros = range(10)
      lista_numeros = str(list(rango_numeros))
      
      for m in range(len(lista_numeros)):
        
        if(numero_final == lista_numeros[m]):
          
          valido3=True
          break;
        else:
          valido3 = False

      sub_lista=lista[len(lista)-1] #expresion  
      sub_2 = sub_lista[len(sub_lista)-1] # ;
      #print(sub_2) # ;
      
      if(valido==True and valido2==True and valido3==True and sub_2==";"):#_a ;
        print(lista)
        print("valida: fin de expresion")
      else:
        print("invalida: estructura invalida")

    else : #es una declaracion de variable sin valor
      #_a;
      #int _a;
      lista2=list("_")
      abc=list(ascii_letters)+lista2 #abc...ABC....._

      #_a;
      sub_lista_=lista[1] # _ , a , ;
    
      for i in range(len(abc)):
        if(sub_lista_[0]==abc[i]):
          valido= True
          break
        else:
          valido=False

     
      sub_lista=lista[len(lista)-1] #expresion  
      sub_2 = sub_lista[len(sub_lista)-1] # ;
      #print(sub_2) # ;
      if(valido==True and sub_2==";"):#_a ;
        print(lista)
        print("valida: fin de expresion")
      else:
        print("estructura invalida")
  else:
    print("no es una expresion")


e="int a6 = 5;"
e1="int a;"
e2="double a4 = 3;"
e3="double _5;"
e4 ="int a"


lista_separada=e4.split(" ")
evaluar(lista_separada)
