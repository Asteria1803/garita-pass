# GaritaPass — Prototipo B2B Navegable de Alta Fidelidad

> **Entorno demostrativo — Datos ficticios**  
> Oficina digital de cumplimiento documental y habilitaciones operativas para empresas contratistas (minería, oil & gas, energía e infraestructura).

Este prototipo interactivo fue construido para validar la propuesta de valor y modelo operativo de **GaritaPass** ante directores, gerentes de operaciones, responsables de Recursos Humanos, Seguridad e Higiene (HSE), jefes de flota y eventuales inversores o socios estratégicos.

---

## 🚀 Cómo Ejecutar y Visualizar el Prototipo

### Opción 1: Servidor Local (Recomendado)
Ejecutá el script de Python incluido en esta carpeta:
```bash
python serve.py
```
El prototipo se iniciará automáticamente en tu navegador en:
👉 `http://localhost:8080/index.html`

### Opción 2: Apertura Directa en Navegador
Hacé doble clic en el archivo `index.html` para abrirlo directamente en Chrome, Edge, Firefox o Safari. No requiere dependencias externas ni compilación previa.

---

## 🏢 Empresa Ficticia Precargada

* **Razón Social**: Andes Servicios Integrales SRL
* **Ubicación**: Av. Ignacio de la Roza 450 Oeste, Ciudad de San Juan, San Juan, Argentina
* **Actividad**: Mantenimiento electromecánico industrial, transporte de personal y asistencia técnica en faenas mineras
* **Proyectos Ficticios**:
  1. **Proyecto Cordillera** (Valle del Cura, Iglesia — 4.150 msnm — Preparación 91%)
  2. **Proyecto Cumbre** (Cordillera Frontal, Calingasta — 3.850 msnm — Preparación 76%)
  3. **Proyecto Andino** (Precordillera, Jáchal — 2.300 msnm — Preparación 84%)

---

## 🎯 Recorridos Funcionales Obligatorios Verificados

### 1. Recorrido de Juan Pérez (Examen Preocupacional)
1. En el **Dashboard (Resumen)**, localizá la sección **"Qué requiere atención hoy"**.
2. Hacé clic en la alerta: *"Examen preocupacional de Juan Pérez: vence en 7 días"*.
3. Se abrirá la **Ficha de Juan Pérez**, donde se observa que para Proyecto Cumbre su estado es **Observado**.
4. Hacé clic en el botón **"Actualizar documento"**.
5. Se abrirá el modal de extracción de IA con el archivo precargado. Hacé clic en **"Ejecutar extracción con IA"**.
6. Observá la animación de 7 pasos de escaneo. La IA detectará la nueva fecha de vencimiento (`02/10/2027`) emitida por Dr. Albarracín.
7. Hacé clic en **"Confirmar información"**. El documento pasará a estado *"Pendiente de revisión por HSE"*.
8. Hacé clic en **"Aprobar revisión documental y habilitar recurso"**.
9. **Resultado automático**:
   - Juan Pérez pasa a estado **Habilitado**.
   - El índice de preparación de Proyecto Cumbre sube de **76% a 79%**.
   - El índice general de la empresa sube de **82% a 84%**.
   - El contador de personas habilitadas sube de **42 a 43**.
   - Se muestra notificación de éxito y se asienta el evento en la bitácora de **Auditoría**.

---

### 2. Recorrido de Vehículo AB 123 CD (Póliza de Seguro Vencida)
1. Desde el menú lateral ingresá a **4. Vehículos** (o hacé clic en la alerta del Dashboard).
2. Abrí la ficha de la camioneta **Toyota Hilux AB 123 CD**.
3. Observá el cartel rojo de bloqueo en garita por seguro caducado.
4. Hacé clic en **"Cargar póliza renovada con IA"** y luego en **"Ejecutar extracción con IA"**.
5. La IA extraerá la póliza `#POL-MA-948102` con vencimiento `02/10/2027` y cláusula de no repetición.
6. Hacé clic en **"Confirmar información"** y luego en **"Aprobar revisión documental"**.
7. **Resultado automático**:
   - La Toyota Hilux pasa a estado **Habilitado**.
   - El contador de vehículos habilitados sube de **11 a 12** y los bloqueados bajan a **0**.
   - El índice general sube a **86%**.
   - Se emite notificación toast y se registra en **Auditoría**.

---

## 🗺️ Estructura Completa de Módulos (11 Pantallas)

1. **1. Resumen**: Dashboard operativo con diagnóstico en menos de 10 segundos, evolución de 6 meses y acciones inmediatas.
2. **2. Proyectos**: Tarjetas con los 3 proyectos mineros y botón *"Evaluar preparación para este proyecto"*.
3. **3. Personas**: Tabla de 12 colaboradores ficticios con buscador, filtros, fichas completas y botón *"Ver credencial QR"*.
4. **4. Vehículos**: Monitoreo de 8 móviles con kit de alta montaña (jaula antivuelco, pértiga LED, radio VHF).
5. **5. Equipos**: Registro de maquinarias (PEMP EQ-018, generadores, grúas) y ensayos de izaje.
6. **6. Documentos**: Bandeja con asistente de extracción OCR por IA y advertencia de validación humana obligatoria.
7. **7. Requisitos**: Matriz comparativa entre Cordillera, Cumbre y Andino, con simulador de movilización de personal.
8. **8. Alertas**: Centro de observaciones con clasificación crítica, asignación de responsables y posposición.
9. **9. Exportaciones**: Generador de carpetas digitales foliadas con índice y hash SHA-256.
10. **10. Auditoría**: Registro de trazabilidad inmutable con filtro por origen (Humano, IA OCR, Regla automática).
11. **11. Configuración**: Matriz de permisos para 7 roles y simulador de vista por rol activo.

---

## 💡 Modos de Demostración para Clientes e Inversores

### 1. ▶ Modo Presentación (5 minutos) — Caso Proyecto Cumbre
Ubicado en el encabezado superior (botón violeta), en la pantalla de acceso o en el banner superior del Dashboard:
* **Objetivo**: Guiar una reunión ejecutiva de 5 minutos ante gerentes de operaciones, responsables de RRHH, Seguridad e Higiene (HSE), jefes de flota y socios/inversores.
* **Narrativa**: *“Andes Servicios Integrales SRL necesita incorporar personal y vehículos al Proyecto Cumbre. La empresa cree que está preparada, pero GaritaPass encuentra cinco brechas documentales que podrían demorar la incorporación.”*
* **Recorrido en 8 Pasos**:
  1. **Situación Inicial**: Diagnóstico consolidado en Resumen y filtro en Proyecto Cumbre (76%). *(“Toda la información operativa, en un solo lugar”)*.
  2. **Detección de Brechas**: Alertas críticas en garita: aptitud médica de Juan Pérez, póliza de Hilux AB 123 CD, izaje de PEMP EQ-018 y 2 capacitaciones. *(“El sistema detecta las brechas antes de una presentación”)*.
  3. **Reglas por Proyecto**: Matriz de exigencias: por qué lo admitido en Cordillera no alcanza en Cumbre (>4.100 msnm). *(“Cada requisito puede variar según el proyecto”)*.
  4. **Legajo Único**: Ficha técnica de Juan Pérez sin duplicar archivos. *(“Los documentos se cargan una vez y se reutilizan”)*.
  5. **Extracción y Validación**: Carga asistida del nuevo apto médico laboral con validación humana profesional. *(“Las fechas pueden extraerse automáticamente y luego validarse”)*.
  6. **Trazabilidad**: Cambio de estado inmediato a Habilitado, subida del índice al 79% y asiento inmutable en Auditoría. *(“Cada modificación queda registrada”)*.
  7. **Dossier Listo**: Generación en Exportaciones del paquete digital foliado y con índice. *(“La empresa puede preparar su carpeta con anticipación”)*.
  8. **Pantalla de Cierre y Validación**: Pregunta clave: *“¿Este flujo refleja cómo trabaja actualmente tu empresa?”*, con bloc interactivo para registrar respuestas a las 6 preguntas estratégicas y botón para copiar la minuta de la reunión.

### 2. Botón "Recorrido Guiado" (Básico)
Ubicado también en el encabezado superior, ofrece un tutorial breve de 5 pasos por las secciones centrales del sistema.

---

## ✨ Asistente Contextual “Asistente GaritaPass”

Ubicado en el encabezado superior (`[✨ Asistente GaritaPass]`) o mediante el botón flotante inferior derecho:
* **Naturaleza**: Panel lateral opcional (no reemplaza la interfaz).
* **Base de Conocimiento**: Opera exclusivamente sobre los datos ficticios precargados de *Andes Servicios Integrales SRL*.
* **Principios de Respuesta**:
  - **Concreción**: Datos precisos y sin rodeos técnicos ni promesas exageradas.
  - **Diferenciación neta**: Separa *Hechos constatados (Sistema)* de *Recomendaciones operativas*.
  - **Trazabilidad y Fuentes**: Cita siempre la fuente o registro utilizado (`Ficha PER-01`, `Alerta ALT-01`, `Matriz REQ-CUMBRE`, etc.).
  - **Acceso directo**: Proporciona botones para saltar con un clic al registro, ficha o proyecto correspondiente.
  - **Límites éticos y legales**: No inventa requisitos, no aprueba documentos de forma autónoma y no emite juicios legales definitivos.
  - **Advertencias**: Avisa si falta información y recuerda que opera en entorno demostrativo.
* **Preguntas Sugeridas y Consultas Libres**:
  - *"¿Qué falta para presentar la empresa en Proyecto Cumbre?"*
  - *"¿Qué documentos vencen durante los próximos 30 días?"*
  - *"¿Qué personas están bloqueadas y por qué?"*
  - *"¿Qué vehículos no cumplen los requisitos de Proyecto Cordillera?"*
  - *"¿Qué debería resolver primero?"*
  - *"¿Qué cambió durante la última semana?"*
  - *"¿Qué documentación tiene Juan Pérez?"*
  - *"¿Puedo asignar el equipo EQ-018 al Proyecto Cumbre?"*
  - *Preguntas libres por colaborador, matrícula, equipo o documento.*


