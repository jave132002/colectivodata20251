import pandas as pd

usuariosDataFrame= pd.read_excel("./data/usuarios_sistema_completo.xlsx")


#1Necesito solo una tabla con los estudiantes
tablaEstudiantes = usuariosDataFrame.query('tipo_usuario=="estudiante"')
print(tablaEstudiantes)

#2Necesito un listado de solo instructores o profesores
listadoDocentes = usuariosDataFrame.query('tipo_usuario== "docente"')
print(listadoDocentes)

#3Necesito un listado de especialistas en desarrollo web o sistemas
ListadoEspecialistasSistemas = usuariosDataFrame.query('especialidad=="Ingenieria de Sistemas"')
print(ListadoEspecialistasSistemas)

#4Necesito un listado de solo usuarios con direcciones en Medellín
lisadoUsuariosMedellin = usuariosDataFrame[usuariosDataFrame['direccion'].str.contains("Medellin", case=False, na=False)]
if lisadoUsuariosMedellin.empty:
    print("No hay datos con esta direccion")
else:    
    print(lisadoUsuariosMedellin)

#5Necesito un listado de solo usuarios cuyas direcciones terminen en SUR
listadoUsuariosTerminadosEnSur = usuariosDataFrame[usuariosDataFrame['direccion'].str.endswith("Sur", na=False)]
if listadoUsuariosTerminadosEnSur.empty:
    print("No hay usuarios con direccion terminada en Sur")
else:
    print(listadoUsuariosTerminadosEnSur)    
 
#6Necesito un listado de especialistas que contengan la palabra 'datos'
listaEspecialistaDatos = usuariosDataFrame[usuariosDataFrame['especialidad'].str.contains("datos", case=False, na=False)]
if listaEspecialistaDatos.empty:
    print("No hay especialidad con la palabra datos")
else:
    print(listaEspecialistaDatos)   

#7Necesito docentes de Itagui
docentesItagui = usuariosDataFrame[(usuariosDataFrame['tipo_usuario'].str.contains("docente")) & (usuariosDataFrame["direccion"].str.contains("Itagui"))]
if docentesItagui.empty:
    print("No hay docentes que vivan en Itagui")
else:
    print(docentesItagui)    

#8Necesito una lista de nacidos en los 90 o antes
usuariosDataFrame['fecha_nacimiento'] = pd.to_datetime(usuariosDataFrame["fecha_nacimiento"])
nacidosNoventaoAntes = usuariosDataFrame[usuariosDataFrame['fecha_nacimiento'] <= pd.to_datetime("1990-12-31")]
if nacidosNoventaoAntes.empty:
    print("No hay personas nacidas en estos años")
else:
    print(nacidosNoventaoAntes)    

#9Necesito un listado de profesores mayores
usuariosDataFrame['fecha_nacimiento'] = pd.to_datetime(usuariosDataFrame['fecha_nacimiento'])
DocentesMayore = usuariosDataFrame[(usuariosDataFrame['tipo_usuario'].str.contains("docente")) & (usuariosDataFrame['fecha_nacimiento'] <= pd.to_datetime("1970-12-31"))]
if DocentesMayore.empty:
    print("No hay docentes mayores")
else:
    print(DocentesMayore)    
  
#10Necesito un listado de profesores y estudiantes nacidos en el nuevo milenio
usuariosDataFrame['fecha_nacimiento'] = pd.to_datetime(usuariosDataFrame['fecha_nacimiento'], errors='coerce')

docentesEstudiantesNuevoMilenio = usuariosDataFrame[
    usuariosDataFrame['tipo_usuario'].str.contains("docente|estudiante", case=False, na=False) & 
    (usuariosDataFrame['fecha_nacimiento'] >= pd.to_datetime("2000-01-01"))
]

if docentesEstudiantesNuevoMilenio.empty:
    print("No hay docentes o estudiantes nacidos en el nuevo milenio")
else:
    print(docentesEstudiantesNuevoMilenio)