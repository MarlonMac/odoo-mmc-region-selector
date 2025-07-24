# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

### [16.0.1.0.3] - 2025-07-23

#### Corregido

* **Herencia de Plantilla:** Se corrigió la herencia de la vista para apuntar a `website.navbar_nav` y se ajustó el XPath a `//ul[@id='top_menu']` para asegurar la máxima compatibilidad con diferentes temas y estructuras de Odoo 16. Este cambio resuelve el error persistente "no se puede localizar en la vista padre".

#### Añadido

* **Banderas de País Dinámicas:** El selector ahora intenta usar la bandera oficial del país (`/base/static/img/country_flags/`) asociada a la compañía del sitio web antes de recurrir a la imagen personalizada (`flag_icon`).
* **Mejoras Visuales:** Se ajustó el HTML y CSS para una mejor alineación vertical de las banderas y el texto.

### [16.0.1.0.2] - (Fecha estimada)

#### Añadido

* **Lógica de Unidad de Negocio:** Se refina la lógica del frontend para mostrar únicamente los sitios que pertenecen a la misma Unidad de Negocio (`business_unit_id`) del sitio web actual.
* **Encabezado de Dropdown:** El menú desplegable ahora muestra el nombre de la Unidad de Negocio actual como un encabezado.

### [16.0.1.0.1] - (Fecha estimada)

#### Añadido

* **Modelo `mmc.business.unit`:** Se introduce el modelo de "Unidad de Negocio" para permitir la agrupación de diferentes sitios/regiones.
* **Relación en Modelo `region.selector`:** Se añade el campo `business_unit_id` al modelo principal para vincular cada región a una unidad de negocio.
* **Vistas de Backend para Unidades de Negocio:** Se crean las vistas de formulario, árbol y menú para gestionar las Unidades de Negocio desde el backend.

### [16.0.1.0.0] - (Fecha estimada)

#### Añadido

* **Versión Inicial:** Creación del módulo `mmc_region_selector`.
* **Modelo Principal:** Creación del modelo `res.company.region.selector` con los campos básicos (nombre, compañía, sitio web, bandera, etc.).
* **Vistas de Configuración:** Creación de las vistas de backend para configurar las regiones.
* **Plantilla Inicial:** Primera versión del template QWeb para mostrar el selector en el header.
* **Permisos de Acceso:** Definición inicial de los permisos de acceso para los nuevos modelos.