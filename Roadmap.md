# Roadmap del Módulo Selector de Región

Aquí se detallan las posibles futuras mejoras y características para el módulo `mmc_region_selector`.

### Completado

* **[Frontend] v16.0.1.0.4:** El selector de región se muestra fuera del contenedor (hamburger) del navbar para que el usuario pueda identificar fácilmente en qué sitio se encuentra sin necesidad de abrir el menú.

---

### Próxima Versión (v16.0.2.0)

#### Futuras Ideas 🚀

* **[Característica] Detección por IP (GeoIP):** Añadir una opción para sugerir o redirigir automáticamente al usuario al sitio web de su región basándose en su dirección IP.
* **[Característica] Selector de Idioma Integrado:** Combinar el selector de región con el selector de idioma para ofrecer una experiencia de localización completa en un solo dropdown.
* **[Característica] Múltiples Unidades de Negocio:** Permitir que el dropdown muestre todas las unidades de negocio como sub-secciones, no solo la actual.
    * Ejemplo:
        * **Retail**
            * Guatemala
            * El Salvador
        * **Distribución**
            * Panamá
            * Costa Rica
* **[UI/UX]** Permitir la personalización del estilo del selector (colores, tamaño) desde las opciones de configuración del backend, sin necesidad de modificar el código.
* **[Backend]** Mejorar la vista de configuración para que sea posible ordenar las regiones mediante drag-and-drop.