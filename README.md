# rookie-coffee
## Consideraciones BD:
En unidad_medida: _id es string ya que almacena el codigo, ejemplo "KG","ML","L","G"

En detalle_venta: precio_historico hace referencia al precio del producto a la fecha de compra


Las llaves foráneas tomarán el nombre de la tabla a la que hacen referencia, además de tener el mismo tipo de dato que la PK de dicha tabla.

## Consideraciones paquetes/carpetas

### Controlador
Aqui se maneja la lógica del negocio
### Modelo
Abstracción de las entidades identificadas
### Base-datos
Conexión a la base de datos