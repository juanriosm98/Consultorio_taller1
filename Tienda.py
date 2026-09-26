Cuantos_productos_va_a_llevar = input ("Cuantos productos va a llevar")
Cuantos_productos_va_a_llevar = int (Cuantos_productos_va_a_llevar)
Total_compra = 0

for i in range (Cuantos_productos_va_a_llevar ):
    nombre_del_producto = input(f"nombre del producto { i + 1 } ")
    if nombre_del_producto == "":
        print ("ERROR: el nombre del producto no puede estar vacio")
    else:
     precio_del_producto = input(f"precio del producto { i + 1 } ")
    if precio_del_producto == "" :
     print ("ERROR: El precio del producto no puede estar vacio")
    else: 
     precio_del_producto = float(precio_del_producto)
     if precio_del_producto < 0:
       print ("ERROS: El precio del producto no puede ser negativo")
     else: 
      descuento_del_producto = input ("ingrese el descuento del producto ")
      if descuento_del_producto == "" :
        print ("ERROR: El descuento del producto no puede estar vacio")
      else:

       descuento_del_producto = float (descuento_del_producto)
       if descuento_del_producto < 0: 
         print ("ERROR: El descuento del producto no puede ser un valor negativo")
       else:
        if descuento_del_producto > precio_del_producto:
          print ("ERROR: El descuento no puede ser mayor al precio")
        else:
         total_producto = precio_del_producto - descuento_del_producto 
         print (f"el precio final del producto {i + 1} es: {nombre_del_producto} es: {total_producto} pesos.")
         Total_compra = Total_compra + total_producto
print(f"el total a pagar es: {Total_compra}")         