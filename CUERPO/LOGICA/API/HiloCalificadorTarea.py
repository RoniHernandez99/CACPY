from PyQt5.QtCore import QThread
import os.path
import os
import io
from googleapiclient.http import MediaIoBaseDownload


# para convertir a pdf y para saber el sistema operativo
import pdfkit
import platform

from apiclient.http import MediaFileUpload




class HiloCalificadorTarea(QThread):
    def __init__(self,configuracionCalificador,nbGrader_control,classroom_control):
        super().__init__()

        self.configuracionCalificador=configuracionCalificador
        self.nbGrader_control=nbGrader_control
        self.classroom_control=classroom_control

        self.courseWork_id=None
        self.courseWork_name=None

        self.noMaxEstudiantesCalificar=5 # valor default


        # variable bandera
        self.CALIFICANDO_TAREA=False



    def setDatosTareaCalificar(self,nuevoCourseWork_id,nuevoCourseWork_name):
        self.courseWork_id=nuevoCourseWork_id
        self.courseWork_name=nuevoCourseWork_name

    def setNoMaxEstudiantesCalificar(self,nuevoValor):
        self.noMaxEstudiantesCalificar=nuevoValor

# def calificarEstudiantes(self, courseWork_id, courseWork_name, noMaxEstudiantesCalificar=5):

    def run(self):

        if self.courseWork_name and self.courseWork_id:

            courseWork_name=self.courseWork_name
            courseWork_id=self.courseWork_id



            print("Coursework_name",courseWork_name)
            print("Coursework_id",courseWork_id)


            ############################################################################################
            # DATOS DE LA CARPETA EN DONDE SE ADJUNTARAN LAS RETROALIMENTACIONES
            ###########################################################################################

            folder_id = '1W5StOtU4tJERcsRtUjj2lLhkJ8ybdbW1'
            nombreCarpetaCurso = 'israel_mejia'  # sera el id del curso

            drive_service = self.classroom_control.service_drive
            page_token = None

            ############################################################################################################################################
            # SI EXISTE EN DRIVE LA CARPETA DEL CURSO, AHI SE SUBIRAN LAS TAREAS DEL ESTUDIANTE PERO SI NO EXISTE SE VA A CREAR
            ############################################################################################################################################

            # Lo que se busca es una CARPETA, la carpeta que se busca NO SE ENCUENTRA en la papelera de reciclaje
            # la carpeta que se busca se encuentra dentro de la carpeta  cuyo id es igual a un id especifico
            query = "trashed=False and mimeType='application/vnd.google-apps.folder' and name='{}'   and  '{}' in parents".format(
                nombreCarpetaCurso, folder_id)
            # print("QUERY=",query)
            listaResultados = []
            while True:
                response = drive_service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name)',
                    pageToken=page_token).execute()

                for file in response.get('files', []):
                    # Process change
                    print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
                    listaResultados.append([file.get('name'), file.get('id')])
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break

            if listaResultados != []:
                # Si solo existe una carpeta con dicho nombre y especificaciones se obtiene su ID
                if len(listaResultados) == 1:
                    print("Si existe la carpeta")
                    ID_SUPREMO = listaResultados[0][1]
                # Si existe mas de una carpeta con dicho nombre y especificaciones entonces hay un error
                else:
                    print("ERROR de repeticion de dos carpeta, arreglar cuanto antes")

            # Si no existe ninguna carpeta con dicho nombre y especificaciones entonces se crea y posteriormente
            # se obtiene su ID
            else:
                print("No existe la carpeta")
                file_metadata = {
                    'name': nombreCarpetaCurso,
                    'parents': [folder_id],
                    'mimeType': 'application/vnd.google-apps.folder'
                }
                file = drive_service.files().create(body=file_metadata,
                                                    fields='id').execute()
                print('Folder ID: %s' % file.get('id'))
                ID_SUPREMO = file.get('id')
                print("")

            # YA QUE SE TIENE EL ID DE LA CARPETA EN DONDE SE SUBIRAN LAS RETROALIMENTACIONES...

            # formato del diccionario: dictEntregas[user_id] = [url, asignacion_id]
            dictEntregas = self.classroom_control.list_submissions(
                course_id=self.configuracionCalificador.curso_api_id,
                coursework_id=courseWork_id,
            )

            RUTA_ASIGNACIONES = self.get_rutaAsignaciones()

            if len(dictEntregas) > 0:
                for user_id, url_or_idAsignacion in dictEntregas.items():
                    url, idAsignacion = url_or_idAsignacion

                    ####################################################################################
                    #  OBTENIENDO EL NOMBRE EN DONDE SE DESCARGARA LA TAREA ENTREGADA POR EL USUARIO
                    ####################################################################################

                    print("RUTA ASIGNACIONES",RUTA_ASIGNACIONES)
                    print("USER ID: ",user_id)
                    print("COUSEWORK NAME",courseWork_name)


                    RUTA_TAREA = RUTA_ASIGNACIONES + user_id + '/' + courseWork_name + '/'
                    os.makedirs(RUTA_TAREA, exist_ok=True)
                    nombreArchivo = RUTA_TAREA + courseWork_name + '.ipynb'

                    ####################################################################################
                    #  DESCARGANDO LA ASIGNACION DEL ESTUDIANTE EN LA RUTA DEBIDA
                    ####################################################################################

                    # FORMATO DE LINK: 'https://drive.google.com/file/d/1m-LNYFiQeNKeeGRxo03dPg5HMrzQI3Wl/view?usp=drive_web'
                    # si el archivo ya existe en la ruta debida, se eliminara de ahi
                    archivo_id = url.split('/')[-2]
                    if os.path.exists(nombreArchivo):
                        print("YA EXISTE :DDDD")
                        os.remove(nombreArchivo)

                    # Descargando el archivo en la ruta debida
                    request = self.classroom_control.service_drive.files().get_media(fileId=archivo_id)
                    fh = io.BytesIO()
                    downloader = MediaIoBaseDownload(fh, request)
                    done = False
                    while done is False:
                        status, done = downloader.next_chunk()
                        print("Download %d%%." % int(status.progress() * 100))

                    fh.seek(0)
                    with open(nombreArchivo, 'wb') as f:
                        f.write(fh.read())
                        f.close()

                    ####################################################################################
                    #  CALIFICANDO LA TAREA CON NBGRADER
                    ####################################################################################

                    resultadoAlCalificar = self.nbGrader_control.autograde(assignment_id=courseWork_name,
                                                                           student_id=user_id)

                    calificacionFinal = 0
                    puntosTotales = 0
                    if resultadoAlCalificar['success'] is True:
                        calif = self.nbGrader_control.get_submission(assignment_id=courseWork_name, student_id=user_id)
                        puntosObtenidos = calif['score']
                        puntosTotales = calif['max_score']
                        print(puntosObtenidos, '/', puntosTotales)
                        calificacionFinal = puntosObtenidos / puntosTotales

                        # Si hubo exito al calificar la tarea entonces se puede crear la reotroalimentacion
                        # estatus_retroalimentacion=self.nbGrader_control.generate_feedback(assignment_id=courseWork_name,student_id=user_id,force=True)

                        nombreCopletoRetro = self.get_rutaRetroalimentacion() + user_id + '/' + courseWork_name + '/' + courseWork_name
                        huboExito_crearRetro = self.generarRetraolimentacionTarea_pdf(courseWork_name=courseWork_name,
                                                                                      idEstudiante=user_id,
                                                                                      nombreCompletoRetro=nombreCopletoRetro)

                        if huboExito_crearRetro:

                            ############################################################################################################################################
                            # SUBIENDO EL ARCHIVO A LA CARPETA DEL CURSO, OBTENIENDO SU LINK DE ACCESO Y POSTERIORMENTE MODIFICANDO SUS PERMISOS PARA UN ACCESO PUBLICO
                            ############################################################################################################################################

                            print("ID_SUPREMO:", ID_SUPREMO)
                            nombreGuardaraArchivo = '{}_{}'.format(user_id,
                                                                   courseWork_id)  # Id de los archivos   alumnoId_topicId_courseworkId_numeroVersion

                            #############################################################################################
                            # ADJUNTANDO EL NUMERO DE VERSION AL NOMBRE DEL ARCHIVO QUE SE DESEA SUBIR
                            #############################################################################################

                            # Se busca la existencia de archivos con la palabra 'nombreGuardaraArchivo' contenida
                            # trashed=False and mimeType!='application/vnd.google-apps.folder' and
                            # fullText contains 'hello'
                            query = "trashed=False and mimeType!='application/vnd.google-apps.folder' and fullText contains '{}'  and  '{}' in parents".format(
                                nombreGuardaraArchivo, ID_SUPREMO)
                            print("QUERY=", query)
                            listaResultados = []
                            while True:
                                # " mimeType = 'application/vnd.google-apps.folder'    '{}' in parents ".format(folder_id)
                                response = drive_service.files().list(
                                    q=query,
                                    spaces='drive',
                                    fields='nextPageToken, files(id, name)',
                                    pageToken=page_token).execute()

                                for file in response.get('files', []):
                                    # Process change
                                    print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
                                    listaResultados.append([file.get('name'), file.get('id')])
                                page_token = response.get('nextPageToken', None)
                                if page_token is None:
                                    break

                            numeroVersionArchivo = len(listaResultados)
                            nombreGuardaraArchivo += ('_{}.pdf'.format(numeroVersionArchivo))

                            #############################################################################################
                            # SUBIENDO EL ARCHIVO Y OBTENIENDO SU LINK DE VISTA
                            #############################################################################################

                            file_metadata = {
                                'name': nombreGuardaraArchivo,  # nombre que tendra en el archivo que se subira
                                'parents': [ID_SUPREMO]
                            }
                            media = MediaFileUpload(nombreCopletoRetro + '.pdf',
                                                    # nombre completo en donde se encuentra el archivo
                                                    mimetype='application/pdf',
                                                    # pdf=application/pdf   jpg=image/jpeg   html=application/json
                                                    resumable=True)
                            file = drive_service.files().create(body=file_metadata,
                                                                media_body=media,
                                                                fields='id,name,webContentLink,webViewLink'
                                                                ).execute()

                            # caracteristicas: https://developers.google.com/drive/api/v3/reference/files
                            print('File ID: %s' % file.get('id'))
                            print('File webView: %s' % file.get('webViewLink'))

                            URL_RETROALIMENTACION = file.get('webViewLink')

                            ID_RETROALIMENTACION = file.get('id')

                            #############################################################################################
                            # DANDOLE ACCESO PUBLICO AL ARCHIVO COMPARTIDO
                            #############################################################################################

                            ID_ARCHIVO_COMPARTIR = ID_RETROALIMENTACION

                            def callback(request_id, response, exception):
                                if exception:
                                    # Handle error
                                    print(exception)
                                else:
                                    print("Permission Id: %s " % response.get('id'))
                                    print('File webView: %s' % response.get('webViewLink'))
                                    print(response)
                                    print(request_id)

                            batch = drive_service.new_batch_http_request(callback=callback)
                            user_permission = {
                                'type': 'anyone',  # compartir para cualquier persona
                                'role': 'reader',  # los permisos compartidos seran unicamente de lector
                            }
                            batch.add(drive_service.permissions().create(
                                fileId=ID_ARCHIVO_COMPARTIR,
                                body=user_permission,
                                fields='id'
                            ))
                            batch.execute()

                            #############################################################################################
                            # SUBIENDO LOS RESULTADOS AL USUARIO
                            #############################################################################################

                            # RESPUESTA AL USUARIO
                            studentSubmission = {
                                'assignedGrade': puntosObtenidos,
                                'draftGrade': puntosObtenidos,
                                'state': 'RETURNED',
                            }

                            print("Id sudmision:", idAsignacion)
                            self.classroom_control.service_classroom.courses().courseWork().studentSubmissions().patch(
                                courseId=self.configuracionCalificador.curso_api_id,
                                courseWorkId=courseWork_id,
                                id=idAsignacion,
                                updateMask='assignedGrade,draftGrade',
                                # updateMask='assignedGrade,draftGrade',
                                body=studentSubmission).execute()

                            request = {
                                'addAttachments': [
                                    {
                                        'link': {
                                            "url": URL_RETROALIMENTACION
                                        }
                                    }
                                ]
                            }
                            coursework = self.classroom_control.service_classroom.courses().courseWork()
                            coursework.studentSubmissions().modifyAttachments(
                                courseId=self.configuracionCalificador.curso_api_id,
                                courseWorkId=courseWork_id,
                                id=idAsignacion,
                                body=request).execute()

                            print("ESTUDIANTE: ", user_id, " TEMRINADO DE CALIFICAR")


                    # no hubo exito al calificar...
                    else:
                        print("PROBLEMAS AL CALIFICAR AUTOMATICAMENTE")
                        print('ERROR:\n', '\t', resultadoAlCalificar['error'])
                        print('LOG:\n', '\t', resultadoAlCalificar['log'])


    def get_rutaAsignaciones(self):
        if self.nbGrader_control:
            ubicacionCurso=self.nbGrader_control.config.CourseDirectory.root
            print("UBICACION DEL CURSO...",ubicacionCurso)
            ubicacionCurso+='submitted/'
            return ubicacionCurso

    def get_rutaRetroalimentacion(self):
        if self.nbGrader_control:
            ubicacionCurso=self.nbGrader_control.config.CourseDirectory.root
            print("UBICACION DEL CURSO...",ubicacionCurso)
            ubicacionCurso+='feedback/'
            return ubicacionCurso


    def generarRetraolimentacionTarea_pdf(self, courseWork_name, idEstudiante, nombreCompletoRetro):
        estatus_retroalimentacion = self.nbGrader_control.generate_feedback(assignment_id=courseWork_name,
                                                                            student_id=idEstudiante, force=True)

        # hubo exito al crear el feedbak
        if estatus_retroalimentacion['success']:

            sistema = platform.system()
            # print("Estamos en {}".format(sistema))

            urlpath = nombreCompletoRetro + '.html'
            pdffilepath = nombreCompletoRetro + '.pdf'
            print("RUTA DEL ARCHIVO A COPIAR...", urlpath)
            print("RUTA DEL ARCHIVO A CREAR...", pdffilepath)

            # C:\Users\ronal\Desktop\proyectos\calificadorRoni\NB_GRADER\course_1\feedback\114283316418743255552\tarea_2
            if sistema == 'Windows':
                path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
                config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
                pdfkit.from_url(url=urlpath, output_path=pdffilepath, configuration=config)
                return True

            elif sistema == 'Linux':
                pdfkit.from_url(url=urlpath, output_path=pdffilepath)
                return True
            elif sistema == 'Darwin':  # sistema operativo mac
                return False

        else:
            print("PROBLEMAS AL GENERAR LA RETROALIMENTACION")
            print('ERROR:\n', '\t', estatus_retroalimentacion['error'])
            print('LOG:\n', '\t', estatus_retroalimentacion['log'])
            return False