La Casa del Código
La Casa del Código es una aplicación web diseñada para gestionar cursos, profesores y estudiantes. Este proyecto incluye funcionalidades para crear, editar y visualizar cursos a través de una interfaz web intuitiva.

Características
Gestión de Cursos: Crear, visualizar y buscar cursos, porfesores o estudiantes.

Formulario Dinámico: Añadir nueva informacion mediante un formulario interactivo.

Protección CSRF: Implementación de tokens CSRF para seguridad en formularios.

Tecnologías Utilizadas
Django: Framework principal del proyecto.

Bootstrap: Estilos CSS para una interfaz amigable y responsiva.

SQLite: Base de datos para almacenamiento de datos.

Instalación
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

Clona el repositorio con los siguientes pasos:

1-
git clone https://github.com/ZaftheR/app_coder.git
Navega al directorio del proyecto:

2-
cd la-casa-del-codigo
Crea y activa un entorno virtual:

3-
python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate
Instala las dependencias del proyecto:

4-
pip install -r requirements.txt
Aplica las migraciones para configurar la base de datos:

5-
python manage.py makemigrations
python manage.py migrate
Ejecuta el servidor de desarrollo:

6-
python manage.py runserver
Abre tu navegador y visita http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

Uso
Gestión de Cursos
Visualizar Cursos: En la página de inicio, puedes ver una lista de todos los cursos disponibles.

Buscar Cursos: Utiliza la barra de búsqueda para encontrar cursos específicos.

Añadir Cursos: Llena el formulario para añadir nuevos cursos.

Seguridad
Tokens CSRF: Los formularios incluyen tokens CSRF para prevenir ataques de falsificación de solicitudes entre sitios.
