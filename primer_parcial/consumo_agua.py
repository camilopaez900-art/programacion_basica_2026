# ingresar el nombre del usuario 
#ingresar el consumo mensual del agua en metros cubicos 
# determinar en que categoria esta su consumo de agua
# mostrar el nombre sel usuario, su categoria y su mensaje de la categoria en el que se encuntra 
# y si al final el cponsumo es 0 o es negativo se mostrara el mensaje de error correspondiente  

nombre = input("ingresa el nombre del usuario")
consumo = int(input ("el consumo mensual de agua en m³"))
if consumo >15:
    print("✅ Bajo consumo")
elif consumo <30:
    print(	"📊 Consumo normal" )
elif consumo >30:
    print( "Alto consumo")   
else: 
  print ( "Dato inválido")
