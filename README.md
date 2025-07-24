# Módulo Selector de Región para Odoo 16

## Resumen

Este módulo para Odoo 16 CE proporciona un **selector de región dinámico** en el encabezado del sitio web. Permite a los visitantes navegar fácilmente entre diferentes sitios web de la misma organización, que están agrupados lógicamente por "Unidades de Negocio".

El selector es visible tanto en la navegación de escritorio como en la **barra principal móvil**, garantizando una excelente experiencia de usuario en cualquier dispositivo.

## Características Principales ✨

* **Agrupación por Unidad de Negocio:** Organiza múltiples sitios web (compañías) bajo entidades lógicas como "Retail", "Distribución", "Servicios", etc.
* **Selector Inteligente y Dinámico:** El selector solo se muestra si hay otros sitios para ofrecer. Muestra el nombre y la bandera de la región actual y un menú desplegable con las demás.
* **Diseño Responsivo:** Totalmente visible y funcional en la barra de navegación móvil, fuera del menú de hamburguesa, para una identificación rápida de la región.
* **Banderas de País Estándar:** Utiliza automáticamente las banderas de país predeterminadas de Odoo (`/base/static/img/country_flags/`) basadas en el país de la compañía asociada al sitio web.
* **Ícono de Fallback:** Si no se encuentra una bandera de país o no se ha subido una personalizada, muestra un ícono global genérico.
* **Configuración desde el Backend:** Proporciona menús en el backend de Odoo para que los administradores puedan:
    * Crear y gestionar Unidades de Negocio.
    * Configurar cada sitio regional, asociándolo a una Compañía, un Sitio Web de Odoo y una Unidad de Negocio.
* **Permisos Detallados:** Define permisos de acceso para administradores y usuarios.

## Instalación

1.  Copia la carpeta `mmc_region_selector` a tu directorio de addons de Odoo.
2.  Reinicia el servicio de Odoo.
3.  Ve a **Aplicaciones** en tu dashboard de Odoo.
4.  Haz clic en **Actualizar lista de Aplicaciones**.
5.  Busca "Region Selector" y haz clic en **Instalar**.

## Configuración ⚙️

Una vez instalado el módulo, sigue estos pasos para configurarlo:

1.  **Crear Unidades de Negocio:**
    * Ve a **Sitio Web ‣ Regiones ‣ Unidades de Negocio**.
    * Crea las unidades de negocio que necesites (ej: "Centroamérica Retail", "Sudamérica Distribución").

2.  **Configurar las Regiones:**
    * Ve a **Sitio Web ‣ Regiones ‣ Configurar Regiones**.
    * Haz clic en **Crear** para añadir una nueva región.
    * **Nombre en Selector:** El texto que verá el usuario (ej: "Guatemala").
    * **Unidad de Negocio:** Asigna la región a una de las unidades creadas.
    * **Compañía:** Selecciona la `res.company` de Odoo que corresponde a esta región. El país se tomará automáticamente de aquí para la bandera.
    * **Sitio Web:** Selecciona el `website` específico al que se redirigirá.
    * **Activo en selector:** Marca esta casilla para que la región aparezca en el selector.
    * **Ícono/Bandera (Opcional):** Sube una imagen si quieres usar una bandera personalizada en lugar de la bandera del país por defecto.
    * Repite el proceso para todos los sitios que deseas incluir.

Una vez configurado, el selector aparecerá automáticamente en el frontend del sitio web si se cumplen las condiciones.

## Dependencias

* `website`

## Licencia

LGPL-3

## Autor

* Marlon Macario
* Website: `link-gt.com`