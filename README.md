# Repositorio Abierto - Academia UPC & Ofitech.lat

¡Bienvenido al **Repositorio Abierto de Academia UPC**! Este espacio educativo contiene recursos didácticos de alta calidad científica e interactiva para la nivelación y formación universitaria.

Este proyecto ha sido diseñado e implementado por **Ofitech.lat** en colaboración con la cátedra de matemáticas de la **Academia UPC**.

---

## 📐 Trigonometría Interactiva para Nivelación Universitaria

Este directorio contiene un curso completo y dinámico que cubre la teoría y la práctica formal de la trigonometría plana e interactiva, preparado para la integración nativa en plataformas de aprendizaje LMS mediante el estándar educativo **SCORM**.

### 📁 Estructura del Proyecto

Todos los recursos se encuentran organizados dentro de la carpeta [`trigonometria-interactiva/`](./trigonometria-interactiva/):

1.  **`trig_solver.html`**:
    *   *Simulador y Solucionador Gráfico SPA*: Aplicación interactiva de última generación con estética Glassmorphic en Modo Oscuro.
    *   *Interactividad*: Arrastre táctil y clic de ángulos notables con cálculo analítico de las 6 razones trigonométricas exactas y decimales.
    *   *Evaluación*: Motor interno que genera ilimitadas preguntas aleatorias parametrizadas en 3 niveles de dificultad (Básico, Intermedio, Avanzado).
2.  **`trig_circle.svg`**:
    *   *Circunferencia Trigonométrica Vectorial*: Recurso de alta fidelidad con coordenadas de puntos notables y radianes exactos.
3.  **`trigonometricas.elpx`**:
    *   *Curso Nativo eXeLearning v4*: Archivo de exportación moderno ODE 2.0 que contiene la estructura pedagógica de 5 módulos teóricos científicos y 15 cuestionarios de autoevaluación inyectados localmente.
4.  **`generate_course.py`**:
    *   *Motor de Generación Paramétrica*: Código fuente en Python utilizado para compilar el curso, dibujar los triángulos y proyecciones SVG inline y serializar el cuestionario en formato XML compatible con eXeLearning.
5.  **`content.xml`** y **`content.dtd`**:
    *   *Esquema XML de Contenido*: Archivos descriptivos de navegación e iDevices `form` nativos validados frente al DTD oficial de eXeLearning v4.

---

## 🚀 Guía de Despliegue e Integración

### 1. Ejecución del Simulador Offline/Online
Puedes abrir el archivo [`trig_solver.html`](./trigonometria-interactiva/trig_solver.html) directamente en cualquier navegador moderno de forma offline para usar el visualizador y solucionador interactivo de ángulos en tiempo real. 

Si deseas alojarlo de manera remota, puedes subirlo a tu servidor de hosting web (ej. Namecheap) y referenciarlo.

### 2. Edición y Personalización en eXeLearning
1. Abre la aplicación **eXeLearning** (v4.0 o superior).
2. Abre el archivo [`trigonometricas.elpx`](./trigonometria-interactiva/trigonometricas.elpx) para editar o ampliar los temas trigonométricos.
3. El curso ya cuenta con las imágenes y el simulador web embebidos directamente en las páginas teóricas de manera local en `content/resources/`.

### 3. Publicación en Moodle (SCORM)
1. En eXeLearning, ve a **Archivo > Exportar > Estándar educativo > SCORM 1.2** o **SCORM 2004**.
2. Exporta el curso como un archivo `.zip`.
3. Sube este ZIP a tu plataforma **Moodle** añadiendo una actividad de tipo **Paquete SCORM**.
4. Ajusta la calificación en Moodle a *Calificación más alta* e *Intento más alto* para registrar automáticamente los resultados de los exámenes directamente en el **Libro de Calificaciones (Gradebook)** de Moodle.

---

## 🎓 Créditos y Autoría

*   **Creador de Contenidos**: Ofitech.lat
*   **Academia**: Academia UPC - Repositorio Abierto
*   **Licencia**: Recurso educativo abierto para uso formativo.
*   **Enlace de Clases**: Visita la academia y accede a tutorías personalizadas y clases magistrales en: [ofitech.lat/clases](https://ofitech.lat/clases)

---
*Desarrollado con pasión para impulsar la educación matemática universitaria abierta.*
