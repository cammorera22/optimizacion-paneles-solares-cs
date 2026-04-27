# optimizacion-paneles-solares-cs
Optimizador LP Paneles solares- UCR
Este proyecto es una herramienta diseñada para evaluar la viabilidad técnica y económica de instalar paneles solares en hogares. El sistema utiliza modelos de programación lineal para minimizar la inversión inicial cumpliendo con la demanda energética y restricciones de area.

Descripcion del modelo
Variables de Decisión: Cantidad de paneles Tipo A, B y C por vivienda.
Función Objetivo: min Z = 190x + 205y + 255z.
Restricciones principales:
  Demanda Energética: La generación mensual debe ser mayor/igual al gasto en $kWh/mes$ de la casa.
  Espacio Físico: El área total de los paneles debe ser menor/igual al área del techo disponible en metros cuadrados.
Premisas: Se asumen 4.5 horas pico solares diarias y meses de 30 días.

Instrucciones
  1. Haga clic en el enlace de la aplicación (ubicado en la descripción del repositorio).
  2. Ajuste los parámetros: En el panel lateral, puede modificar la demanda de energía o el área disponible del techo para cada una de las 3 casas.
  3. Para este modelo las horas solares por dia se mantienen constantes en 4.5h, asi que no hay que modificar este parametro, sin embargo, si desea trabajar bajo otros supuestos debe modificarlo
  4. Optimizar: Presione el botón "Optimizar" para que el modelo calcule automáticamente la combinación de paneles A, B y C que minimiza su inversión.
  5. Revise los indicadores: La aplicación mostrará de inmediato si el proyecto es viable físicamente y su rentabilidad financiera.

Por:
  Camila Morera C35393
  Sebastian Solano C4k112
