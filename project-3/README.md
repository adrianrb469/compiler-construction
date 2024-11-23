# Three Address Code for CompiScript 🧑🏻‍💻

This project consists on translate CompiScript code to Three Address Code and finally to Mips code.

## Team Members 👥

- Adrian Rodriguez 21691
- Daniel Gomez 21429

## Project Demo 🎥

[https://youtu.be/BW47YvWrBx8](https://youtu.be/BW47YvWrBx8)

[![CompiScript Demo](https://img.youtube.com/vi/BW47YvWrBx8/0.jpg)](https://youtu.be/BW47YvWrBx8)

Click the image above to watch our project demo on YouTube.

## Installation 💻

To install our CompiScript IDE, you need to have Python installed on your system. Then, you can install the required dependencies using pip:

```

pip install streamlit

```

## Running CompiScript IDE 🛠️

To run the CompiScript IDE, use the following command:

```

streamlit run ide.py

```

## Features 🚀

#### Arithmetic operations
- Addition
- Substraction
- Multiplication
- Division

#### If, else if, else statements
- Supports if statements
- Supports if & else if statements
- Supports if, else if & else statements

#### Loops
- While statements
- For statements

## Examples 💥

### Arithmetic operations

```
var x = 5 - 4 * 8;
var y = x + 6 / 2;
var z = x * y + 7;
```

### If statement

```
var x = 10;
if (x > 5) {
    x = x - 1;
}
```

### If else statement

```
var x = 10;
if (x > 5) {
    x = x - 1;
} else {
    x = x + 1;
}
```

### If, else if, else statement
```
var x = 10;
if (x > 5) {
    x = x - 1;
} else if (x == 5) {
    x = x + 5;  
} else if (x == 4) {
    x = x + 4;  
} else if (x == 3) {
    x = x + 3;  
} else {
    x = x + 1;
}
```

### While statement

```
var x = 0;

while (x<5) {
    print "Hola mundo!";
    var y = 6;
}
```

### For statements

```
for(var x = 0; x < 10; x++) {
    print "Hello world!";
}
```

```
for(var x = 0; x < 10; x--) {
    print "Hello world!";
}
```

```
for(var x = 0; x < 10; x += 3) {
    print "Hello world!";
}
```

```
for(var x = 0; x < 10; x -=21) {
    print "Hello world!";
}
```

```
for(var x = 0; x < 10; x++) {
    print "Hello world!";
    for(var y = 0; y < 10; y += 2) {
        print "Hello world nested!";
    }
}
```

### Classes
```
class Persona {
  init(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }

  saludar() {
    print "Hola, mi nombre es " + this.nombre;
  }

  incrementarEdad(anos) {
    this.edad = this.edad + anos;
    print "Ahora tengo " + this.edad + " años.";
  }
  
  getName() {
      return this.nombre;
  }
}

fun main() {
    var nombre = "Ronald";
    var ronald = new Persona(nombre, 40);
    
    var age = ronald.edad;
    var name = ronald.getName();
    ronald.incrementarEdad(1);
}
```

### Complex example
```
// Without arrays
class Producto {
  init(nombre, precio, cantidad) {
    this.nombre = nombre;
    this.precio = precio;
    this.cantidad = cantidad;
  }

  calcularValorInventario() {
    var valor = this.precio * this.cantidad;
    print "Valor del inventario de " + this.nombre + ": " + valor;
    return valor;
  }

  vender(cantidadVendida) {
    if (cantidadVendida <= this.cantidad) {
      this.cantidad = this.cantidad - cantidadVendida;
      print "Se vendieron " + cantidadVendida + " unidades de " + this.nombre;
    } else {
      print "No hay suficiente inventario para vender " + cantidadVendida + " unidades de " + this.nombre;
    }
  }

  restock(cantidadAgregada) {
    this.cantidad = this.cantidad + cantidadAgregada;
    print "Se añadieron " + cantidadAgregada + " unidades de " + this.nombre + " al inventario.";
  }
}

class Categoria {
  init(nombre) {
    this.nombre = nombre;
    this.producto1 = nil;
    this.producto2 = nil;
    this.producto3 = nil;
  }

  agregarProducto(nombre, precio, cantidad, posicion) {
    var nuevoProducto = new Producto(nombre, precio, cantidad);

    if (posicion == 1) {
      this.producto1 = nuevoProducto;
    } 
    if (posicion == 2) {
      this.producto2 = nuevoProducto;
    } 
    if (posicion == 3) {
      this.producto3 = nuevoProducto;
    }

    print "Producto " + nombre + " añadido a la categoría " + this.nombre;
  }

  // Método recursivo para calcular el valor total sin arrays
  calcularValorTotalRecursivo(posicion) {
    if (posicion > 3) {
      return 0;
    }

    var valorProducto = 0;

    if (posicion == 1 and this.producto1 != nil) {
      valorProducto = this.producto1.calcularValorInventario();
    } 
    if (posicion == 2 and this.producto2 != nil) {
      valorProducto = this.producto2.calcularValorInventario();
    }
    if (posicion == 3 and this.producto3 != nil) {
      valorProducto = this.producto3.calcularValorInventario();
    }

    return valorProducto + this.calcularValorTotalRecursivo(posicion + 1);
  }

  mostrarValorTotal() {
    var valorTotal = this.calcularValorTotalRecursivo(1);
    print "El valor total de la categoría " + this.nombre + " es: " + valorTotal;
  }
}

// Ejemplos de uso
var electronica = new Categoria("Electrónica");
electronica.agregarProducto("Laptop", 1000, 10, 1);
electronica.agregarProducto("Smartphone", 500, 20, 2);
electronica.agregarProducto("Tablet", 300, 15, 3);

// Operaciones con productos
electronica.producto1.vender(3);
electronica.producto2.restock(10);

// Calcular el valor total
electronica.mostrarValorTotal();
```
