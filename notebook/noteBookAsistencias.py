import pandas as pd
#Leyendo los datos de asistencias
asistenciaDataFrame = pd.read_csv("./data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)
#Obteniendo informacion basica del dataframe
#print(asistenciaDataFrame.info())
#print(asistenciaDataFrame.tail(20))
#print(asistenciaDataFrame.head(20))
#print(asistenciaDataFrame.describe())
#print(asistenciaDataFrame.isnull().sum())
#print(asistenciaDataFrame['estado'].value_counts())
#print(asistenciaDataFrame['estrato'].value_counts().head())

#FILTROS O CONSULTAS DETALLADAS


#1.Necesito encontrar los estudiantes que si asistieron
estudiantesQueAsistieron= asistenciaDataFrame.query('estado=="asistio"')

#2.Necesito encontrar los estudiantes que faltaron
estudiantesQueFaltaron= asistenciaDataFrame.query('estado=="inasistencia"')

#3. Necesito encontrar los estudiantes que llegaron tarde(Justificaron)
estudiantesConJustificacion= asistenciaDataFrame.query('estado=="justificado"')

#4. Necesito encontrar a los estudiantes de estrato 1
estudiantesEstrato1= asistenciaDataFrame.query('estrato== 1')

#5. Necesito encontrar a los estudiantes de estratos altos
estudiantesEstratoAlto= asistenciaDataFrame.query('estrato== 5 or estrato== 6')

#6. Necesito encontrar estudiants que llegan en metro
estudiantesMetro= asistenciaDataFrame.query('medio_transporte=="metro"')

#7. Necesito encontrar que llegaron en bicileta
estudiantesConBicicleta = asistenciaDataFrame.query('medio_transporte=="bicicleta"')

#8. Necesito encontrar todos los estudiantes menos los que llegaron a pie
estudiantesConTransporte = asistenciaDataFrame.query('medio_transporte !="a pie"')

#9. Necesito todos los registros de asistencia de junio
asistenciaEnJunio = asistenciaDataFrame[asistenciaDataFrame['fecha'].str.contains(r"-06-", na=False)]

#10. Necesito todos los estudiantes que usan transporte ecologico
estudiantesConTransporteEcologico = asistenciaDataFrame.query('medio_transporte =="a pie" or medio_transporte== "bicicleta"')


#11. Necesito usan bus y son estratos alto
estudiantesBusEstratoAlto = asistenciaDataFrame.query('medio_transporte == "bus" and estrato >= 5 ')

#12. Necesito usan bus y son de estrato bajo
estudiantesBusEstratoBajo = asistenciaDataFrame.query('medio_transporte == "bus" and estrato <= 3')

#13. Necesito estudiantes que caminan para llegar a clases
estudiantesQuecaminan = asistenciaDataFrame.query('medio_transporte == "a pie"')

#CONTEOS POR AGUPACIONES

#14. Necesito el conteo de resgistros por estado de asistencia
conteo=asistenciaDataFrame.groupby('estado').size()

#15. Necesito obtener el numero de registro por estrato
numeroRegistroPorEstrato = asistenciaDataFrame.groupby('estrato').size()

#16. Cantidad de estudiantes por medio de transporte
conteoMedioTransporte= asistenciaDataFrame.groupby('medio_transporte').size()

#17. Promedio de estrato por estado de asistencia
promedioAsistenciaPorEstrato= asistenciaDataFrame.groupby('estado')['estrato'].mean()

#18. Maximo estrato por estado
maximoEstratoPorEstado = asistenciaDataFrame.groupby('estado')['estrato'].max()

#19. Minimo estrato por estado
minimoEstratoPorEstado = asistenciaDataFrame.groupby('estado')['estrato'].min()

#20. Conteo de asistencias por grupo y estado
conteoPorGrupoEstado = asistenciaDataFrame.groupby(['id_grupo', 'estado']).size()
print(conteoPorGrupoEstado)