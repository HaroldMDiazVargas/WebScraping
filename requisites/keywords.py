


InfoEntidad = [
    ['funciones y deberes'],                                                                                                                                #01
    ['organigrama', 'estructura orgánica'],                                                                                                                                        #02 
    ['mapas y cartas descriptivas de los procesos'],                                                                                                        #03
    ['directorio institucional'],                                                                                                                           #04
    ['información de servidores públicos', 'directorio de servidores públicos'],                                                                            #05
    ['directorio de entidades'],                                                                                                                            #06
    ['directorio de asociaciones, agremiaciones', 'directorio de agremiaciones'],                                                                           #07
    ['procedimientos que se siguen para tomar decisiones', 'procesos y procedimientos'],                                                                    #08
    ['mecanismos para presentar quejas y reclamos', 'mecanismo de presentación directa de solicitudes'],                                                    #09
    ['calendario de actividades'],                                                                                                                          #10
    ['decisiones que pueden afectar al público', 'decisiones que puede afectar al público'],                                                                #11
    ['autoridades que lo vigilan', 'entes de control que vigilan a la entidad','entes de control'],                                                         #12
    ['publicación de hojas de vida'],                                                                                                                       #13
    ['servicio al público, normas, formularios y protocolos de atención', 'servicio al público, normas'],                                                   #14
]
  

Normatividad = [
    ['normativa de la entidad', 'normatividad'],        #1                                                                                                         
    ['vinculo al diario o gaceta oficial'],             #2
    ['políticas, lineamientos y manuales'],             #3
    ['búsqueda de normas'],                             #4                                                                                                                
    ['proyectos de normas para comentarios']            #5
]


Contratacion = [
    ['plan anual de adquisiciones'],                                                                        #1
    ['información contractual'],                                                                            #2
    ['ejecución de contratos'],                                                                             #3
    ['manual de contratación, adquisición y/o compras', 'políticas en materia de adquisición y compras'],   #4     
    ['formatos o modelos de contratos'],                                                                    #5
]

Planeacion = [
    ['presupuesto general'],                                                                        #1
    ['ejecución presupuestal', 'histórica anual' ],                                                 #2
    ['plan de acción'],                                                                             #3
    ['proyectos de inversión','programas y proyectos en ejecución'],                                #4
    ['informes de empalme'],                                                                        #5
    ['informacion pública y/o relevante'],                                                          #6
    ['informes de gestión, evaluación y auditoría'],                                                #7
    ['informes de la oficina de control interno', 'reportes de control interno'],                   #8
    ['informe sobre defensa pública y prevención del daño antijurídico', 'defensa judicial'],       #9
    ['informes trimestrales sobre acceso a información, quejas y reclamos'],                        #10
]

Tramites = [
     ['trámites y servicios','trámites'],    #1
]

Participa = [
    ['descripción general del menú participa', 'descripción general'],      #1
    ['diagnóstico e identificación de problemas'],                          #2
    ['consulta ciudadana'],                                                 #3
    ['planeación y presupuesto participativo'],                             #4
    ['control ciudadano', 'control social'],                                #5
    ['rendición de cuentas']                                                #6
]


DatosAbiertos = [
    ['instrumentos de gestión de la información'],        #1
    ['sección de datos abiertos', 'publicación de datos abiertos']                         #2
]

GrupoInteres = [
    ['información para niños, niñas y adolescentes'],     #1
    ['información para mujeres'],                         #2
    ['información adicional']                             #3
]

InfoTributaria = [
    ['procesos de recaudo de rentas locales'],                              #1
    ['tarifas de liquidación del impuesto de industria y comercio']         #2
]




Atencion = [
    ["atención"]
]


ParticipaMenu = [
    ["participa"]
]


Noticias = [
    ["noticias"]
]

NormatividadMenu = [
    ["normatividad"]
]

keywordsTransparencia = {
    "InfoEntidad": InfoEntidad,
    "Normatividad": Normatividad,
    "Contratacion": Contratacion,
    "Planeacion": Planeacion,
    "Tramites": Tramites,
    "Participa": Participa,
    "DatosAbiertos": DatosAbiertos,
    "GrupoInteres": GrupoInteres,
    "InfoTributaria": InfoTributaria,
    
}

keywordsAtencion = {
    "Atención": Atencion
}

keywordsParticipa = {
    "Participa":ParticipaMenu
}
keywordsNoticias = {
    "Noticias": Noticias
}

keywordsNormatividad = {
    "Normatividad": NormatividadMenu
}

keywordsDict = {

    "Transparencia":keywordsTransparencia,
    "Atención":keywordsAtencion,
    "Participa":keywordsParticipa,
    "Noticias":keywordsNoticias,
    "Normatividad":keywordsNormatividad,
}
