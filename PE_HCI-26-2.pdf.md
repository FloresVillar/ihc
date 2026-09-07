# PE_HCI-26-2.pdf
>python3 limpieza_datos/scripts/pdf_to_md.py PE_HCI-26-2.pdf

## PRUEBA DE ENTRADA - INTERACCIÓN HUMANO

## COMPUTADOR (CC451)

Nombres y Apellidos: ____________________ Código: ________ Fecha: 31-08-26

### 1. ¿Cuál de los siguientes describe mejor el concepto de "visibilidad" en el diseño de interfaces?

a) Ocultar elementos complejos para simplificar la interfaz

b) Hacer evidentes las funciones disponibles y el estado del sistema

De acuerdo a los principios de Don Norman , la visibilidad asegura que el usuario sepa de forma intuitiva que acciones puede realizar y cual es el estado actual de la interfaz sin tener que adivinar


c) Priorizar la velocidad de carga sobre la claridad visual

d) Usar colores llamativos para todos los elementos interactivos

### 2. En el contexto de usabilidad, ¿qué mide principalmente la "eficiencia"?

a) La satisfacción del usuario después de usar el sistema

b) La rapidez con que los usuarios completan tareas una vez familiarizados

La eficiencia evalua la productividad.Una vez que el usuario ha aprendido a usar la interfaz mide cuantos recursos (tiempo, clics,esfuerzo) le toma alcanzar sus objetivos

c) La cantidad de errores cometidos por usuarios novatos

d) El tiempo que toma aprender a usar el sistema por primera vez

### 3. ¿Cuál de las siguientes es una técnica de investigación de usuarios en la etapa de descubrimiento?

a) Prueba A/B

b) Entrevistas contextuales

En la fase de descubrimientos se busca comprender el problema y el entorno del usuario.Las entrevistas contextuales permiten observar y hablar con los usuarios en su propio entorno real, a diferencia de las pruebas A/B o heruristicas que evaluan soluciones ya propuestas 

c) Evaluación heurística

d) Pruebas de usabilidad remotas

### 4. En CSS Grid, ¿qué propiedad se utiliza para definir el tamaño de las filas en un grid?

a) grid-template-columns

b) grid-template-rows

Esta propiedad establece especificamente la altura y el numero de las filas explicitas en un contenedor Grid (por ejemplo: grid-template-rows: 100px auto 50px;)

c) grid-auto-flow

d) grid-gap

### 5. ¿Qué elemento HTML5 se utiliza para contenido que es independiente y tiene sentido por sí mismo, como publicaciones de blog o artículos de noticias?

a) <section>

b) <aside>

c) <article>

Semanticamente , el elemento <article> representa una seccion autocontenida que podria distribuirse o reutilizarse de forma completamente independiente del resto del sitio

d) <header>

### 6. Para lograr un diseño responsivo, ¿qué técnica CSS permite que los elementos se ajusten automáticamente al tamaño de la ventana gráfica usando porcentajes y unidades relativas?

a) Media Queries

b) Flexbox

c) Layout fluido (Fluid Layout)

El layout fluido reemplaza las medidas fijas (como pixeles) por porcentajes (%) o unidades de viewport (vw , vh) permitiendo un estiramiento o encogimiento proporcional constante.

d) Diseño fijo con pixeles

### 7. ¿Qué método de array en JavaScript transforma cada elemento de un array aplicando una función y devuelve un nuevo array del mismo tamaño?

a) filter()

b) forEach()

c) map()

El metodo .map() itera sobre cada elemento , aplica una funcion de callback con una transformacion y retorna un array resultante con exactamente la misma longitud

d) some()

### 8. Dado el siguiente código JavaScript, ¿cuál es el resultado?
```python
const numeros = [1, 2, 3, 4]; 
const [primero, , tercero] = numeros; 
console.log(primero + tercero);
```
Aplicando la desestructuracion de arreglos, se toman los valores de de los indice 0, obviar el de indice 1, indice 2
primero = 1, tercero =3
finalmente la suma , primero + tercero = 4

a) 3 b) 4 c) 6 d) Error de sintaxis

### 9. En JavaScript, ¿cuál de las siguientes es una forma correcta de manejar una promesa?

a) Usando try/catch con async/await

b) Usando .then() y .catch()

c) Ambas a) y b) son correctas

Las promesas modernas pueden gestionarse con la sintaxis clasica de encadenamiento (.then().cath()) o mediante la estructura sincronica simulada de bloques try/catch combinada con funciones async/await

d) Usando bucles while para esperar la respuesta

### 10. ¿Qué hace el siguiente código en Python?
```python
frutas = ["manzana", "banana", "cereza", "dátil"] 
resultado = {fruta: len(fruta) for fruta in frutas}
```
a) Crea una lista con la longitud de cada fruta

b) Crea un diccionario donde las claves son las frutas y los valores son sus longitudes

Una estructura de comprension de diccionarios (dictionary comprehension).Genera pares claves-valor transformando la lista `{'manzana': 7, 'banana': 6, ...}`

c) Filtra las frutas con longitud mayor a 5

d) Genera un error de sintaxis

### 11. En Python, ¿cuál es la diferencia entre una tupla y una lista?

a) Las tuplas son mutables, las listas son inmutables

b) Las listas son mutables, las tuplas son inmutables

c) Las tuplas pueden contener solo números

d) No hay diferencia significativa

### 12. ¿Qué resultado produce el siguiente código Python?
```python
def calcular(operacion): 
    def aplicar(a, b): 
        if operacion == "suma": 
            return a + b 
        elif operacion == "multiplica": 
            return a * b 
    return aplicar

sumar = calcular("suma") 
print(sumar(5, 3))
```
a) 8 b) 15 c) None d) Error: operacion no está definido

Es un concepto de clausura (closure) la funcion `calcular("suma")` retorna la definicion interna de `aplicar`. Al invocar ``sumar(5,3)` se evalua internamente el bloque de la suma dando.

### 13. ¿Qué código de estado HTTP indica que el servidor no puede procesar la solicitud debido a un error en la sintaxis del cliente?

a) 400 Bad Request

El codigo 400 significa expresamente que la peticion del cliente esta mal formada o corrupta y el servidor no la comprende

b) 401 Unauthorized

c) 403 Forbidden

d) 500 Internal Server Error

### 14. En el diseño de APIs RESTful, ¿qué método HTTP se utiliza típicamente para eliminar un recurso?

a) POST b) PUT c) DELETE d) OPTIONS

Siguiendo las convenciones estandar del protocolo REST , `DELETE` es el verbo semantico dedicado a remover un recurso del servidor mediante su URI.

### 15. En Git, ¿qué comando se usa para crear una nueva rama y cambiar a ella simultáneamente?

a) git branch nueva-rama

b) git checkout -b nueva-rama

c) git switch nueva-rama

d) git branch -m nueva-rama

### 16. ¿Cuál de las siguientes es una buena práctica para mejorar la accesibilidad de imágenes en la web?

a) Usar imágenes sin texto alternativo para agilizar la carga

b) Proporcionar texto alternativo (alt) descriptivo y significativo

El atributo `alt` describe el contenido de la imagen de forma textual para los lectores de pantalla utilizados por personas con discapacion visual

c) Usar imágenes de fondo para todos los elementos visuales

d) Evitar imágenes en sitios web accesibles

### 17. ¿Qué técnica ayuda a los usuarios con discapacidad visual a navegar por una página web estructurada?

a) Usar encabezados jerárquicos (h1, h2, h3...) correctamente

Una jerarquia correcta de encabezados permite que lectoores de pantalla generen un "mapa" navegable de la pagina, dejando que el usuario salte entre seccion sin leer todo el contenido literalmente.

b) Usar solo divs con clases para todo el contenido

c) Eliminar todos los enlaces de la página

d) Usar fuentes muy pequeñas

### 18. Escribe código JavaScript que permita filtrar un arreglo de objetos representando empleados, mostrando solo aquellos con salario mayor a 3000 y que pertenezcan al departamento de "TI", ordenados de mayor a menor salario.

Estructura del objeto empleado:

{ id: 1, nombre: "Carlos", salario: 3500, departamento: "TI" }

Espacio para respuesta:

```bash
const empleados = [
    {id: 1, nombre="Carlos", salario: 3500, departamente: "TI"},
    {id: 2, nombre="Ana", salario: 3500, departamente: "TI"},
    {id: 3, nombre="Luis", salario: 3500, departamente: "TI"},
    {id: 4, nombre="Maria", salario: 3500, departamente: "Ventas"}
]

const resultado = empleados.filter(emp => emp.salario > 3000 && emp.departamento === "TI").sort((a,b) => b.salario - a.salario);
```