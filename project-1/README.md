# CompiScript 🧑🏻‍💻

CompiScript is a custom programming language and compiler project.

## Team Members 👥

- Adrian Rodriguez 21691
- Daniel Gomez 21429

## Project Demo 🎥

[![CompiScript Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

Click the image above to watch our project demo on YouTube.

## Installation 💻

To install our CompiScript IDE, you need to have Python installed on your system. Then, you can install the required dependencies using pip:

```

pip install streamlit

```

## Running CompiScript IDE 🏃🏻‍♂️

To run the CompiScript IDE, use the following command:

```

streamlit run ide.py

```

## Features 🚀

#### Sistema de Tipos
- Verificacion de tipos en operaciones aritmeticas y logicas.
- Control de tipos en asignaciones y declaraciones de variables.
- Compatibilidad de tipos en expresiones de comparacion.

#### Manejo de  Ambito
- Correcta resolucion de nombres de variables y funciones segun el ambito.
- Deteccion de variables no declaradas.
- Control de acceso a variables globales y locales.

#### Funciones y Procedimientos
- Verificacion de la cantidad y tipo de argumentos en llamadas a funciones.
- Validacion del tipo de retorno en funciones.

#### Control de Flujo
- Asegurar que las condiciones de los ciclos y estructuras condicionales sean de tipo booleano

## Examples 💣

### Anonymous Functions

CompiScript supports anonymous functions and closures. Here's an example:

```
fun sumator(a) { 
    return fun(b) { 
        return a + b; 
    }; 
}

var add = sumator(5); 
var a = add(10); 
var b = add(20);
```

This example demonstrates creating a function that returns another function, effectively creating a closure.

### [Additional Example Title]

```
[Additional example code here]
```
