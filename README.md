# ⛱️ Vamos a la Playa - Sistema de Gestión Distribuida

[![Universidad de Cádiz](https://img.shields.io/badge/Universidad%20de%20C%C3%A1diz-UCA-blue.svg)](https://www.uca.es/)
[![Grado](https://img.shields.io/badge/Grado-Ingenier%C3%ADa%20Inform%C3%A1tica%20(GII)-yellowgreen.svg)](#)
[![Curso Académico](https://img.shields.io/badge/Curso-2018%2F2019-red.svg)](#)
[![Asignatura](https://img.shields.io/badge/Asignatura-Sistemas_Distribuidos_(SD)-red)](https://guiasdocentes.uca.es/)
[![Estado](https://img.shields.io/badge/Estado-Finalizado-success)](https://github.com/JordiGM/Vamos_a_la_playa-SD-GII-ESI-UCA/commits/main)

---

## 📝 Descripción del Proyecto

**Vamos a la Playa** es una aplicación que simula un **sistema de gestión de recursos distribuidos** para una zona costera. El objetivo principal es la implementación y el estudio de un sistema con arquitectura Cliente-Servidor que utiliza la tecnología **Java Remote Method Invocation (RMI)** para coordinar las peticiones de acceso, reserva de sombrillas o gestión de aforo, poniendo especial énfasis en la **concurrencia** y la **sincronización** de los datos compartidos.

Este proyecto se enmarca en la asignatura de **Sistemas Distribuidos (SD)** del Grado en Ingeniería Informática (GII) de la Escuela Superior de Ingeniería (ESI) de la Universidad de Cádiz (UCA).

### 🎯 Objetivos de la Implementación

* Implementar una arquitectura de **Sistema Distribuido** robusta.
* Demostrar el uso de **Java RMI** para la comunicación entre procesos.
* Garantizar la **exclusión mutua** en el acceso a recursos compartidos (e.g., el inventario de sombrillas o el contador de aforo).
* Manejar la **concurrencia** de múltiples clientes simulando usuarios que acceden al sistema simultáneamente.

---

## 🛠️ Tecnologías y Dependencias

El proyecto ha sido desarrollado utilizando las siguientes tecnologías y herramientas:

| Tecnología | Versión Requerida | Uso Principal |
| :--- | :--- | :--- |
| **Java Development Kit (JDK)** | 11 o superior | Lenguaje de programación principal. |
| **Java RMI** | Incluido en el JDK | Comunicación remota entre Cliente y Servidor. |
| **Maven** (Opcional) | 3.6 o superior | Gestión de dependencias y compilación del proyecto. |

### 📋 Requisitos Previos

Asegúrate de tener instalado en tu sistema:

1.  **Java JDK (versión 11+):**
    ```bash
    java -version
    ```
2.  Un **Entorno de Desarrollo Integrado (IDE)** como IntelliJ IDEA, Eclipse o VS Code con soporte para Java.

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para obtener una copia operativa del proyecto en tu máquina local.

### 1. Clonar el Repositorio

Abre una terminal y clona el proyecto:

```bash
git clone [https://github.com/JordiGM/Vamos_a_la_playa-SD-GII-ESI-UCA.git](https://github.com/JordiGM/Vamos_a_la_playa-SD-GII-ESI-UCA.git)
cd Vamos_a_la_playa-SD-GII-ESI-UCA
```
2. Compilación

El proyecto se estructura en al menos tres componentes clave: InterfazRemota, Servidor y Cliente. Debes compilar los archivos Java.

Usando javac (método manual):
```bash
# Ejemplo de compilación (ajustar rutas de packages si es necesario)
javac -d bin src/**/*.java
```

Usando Maven (si se ha configurado pom.xml):

```bash
mvn clean install
```

Este comando generará los archivos .class necesarios y, posiblemente, un fichero .jar ejecutable.

▶️ Uso y Ejecución del Sistema

Para que el sistema distribuido funcione, debes iniciar los componentes en el siguiente orden:

    1. Registro RMI (rmiregistry)
    2. Servidor
    3. Clientes

1. Iniciar el Registro RMI

El registro RMI es esencial para que los clientes puedan buscar la implementación remota del servidor.

```bash
# Ejecutar en el directorio donde se encuentran los archivos .class (e.g., ./bin)
rmiregistry [PUERTO_RMI]
```
    Nota: El puerto por defecto es 1099. Si se omite, se usará este puerto.

2. Iniciar el Servidor

El Servidor es el componente principal que implementa la interfaz remota, gestiona la lógica de negocio (reserva de recursos) y publica el objeto remoto en el registro RMI.

```bash
# Ejemplo de ejecución del Servidor (ajustar CLASSPATH y nombre de clase)
java -classpath bin es.uca.sd.playa.servidor.ServidorPlayas [PUERTO_RMI]
```
    Asegúrate de que la clase ServidorPlayas se encuentra en tu CLASSPATH y que el registro RMI ya está activo.

3. Iniciar los Clientes

Los clientes son las aplicaciones que solicitan servicios al Servidor a través de la Interfaz Remota. Puedes ejecutar varios clientes para simular la concurrencia.

```bash
# Ejemplo de ejecución del Cliente
java -classpath bin es.uca.sd.playa.cliente.ClientePlayas [IP_SERVIDOR] [PUERTO_RMI]
```
Ejecuta el comando anterior varias veces para iniciar múltiples clientes concurrentes. Cada cliente intentará realizar una operación de gestión de recursos.

📂 Estructura del Repositorio

La organización del código sigue una estructura estándar para proyectos RMI:

.
├── src/
│   ├── es/uca/sd/playa/
│   │   ├── cliente/             # Código fuente de las clases Cliente (interfaz de usuario o simulación)
│   │   ├── servidor/            # Código fuente de las clases Servidor (lógica de negocio e implementación remota)
│   │   └── interfaz/            # Interfaz Remota (métodos a exponer a los clientes)
├── bin/                       # Directorio de clases compiladas (.class)
├── lib/                       # Librerías externas (si las hubiera, e.g., JARs)
└── README.md                  # Este documento
## 🤝 Colaboradores

Este proyecto fue desarrollado en colaboración por:

* **[sheratanAlde](https://github.com/sheratanAlde)**
* **[groutwo](https://github.com/groutwo)**

📜 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo LICENSE (si existe) para más detalles.

Universidad de Cádiz - ESI | Grado en Ingeniería Informática | Sistemas Distribuidos (SD)
