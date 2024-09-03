# CompiScript 🧑🏻‍💻

CompiScript is a compiler project that implements a basic programming language.

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

### Var declaration

```
var myString = "string";
var myBool = true;
var myInt = 1;
```

### Function declarations
```
fun sumator(a, b) {
    var result = a + b;
    return result;
}
```

### Class declaration
```
class Person {
  init(name, age) {
    this.name = name;
    this.age = age;
    this.favoriteColor = "red";
  }

  greet() {
    var message = "Hello, my name is " + this.favoriteColor;
    return message;
  }

}
```

### Class inheritance
```
class Person {
  init(name, age) {
    this.name = name;
    this.age = age;
    this.favoriteColor = "red";
  }

  greet() {
    print "Hello world! my name is" + this.name;
  }

}

class Student extends Person {
  init(name, age, grade) { 
    super.init(name, age);
    this.grade = grade;
  } 

  study() {
    print "Im studying! Im " + super.age + " years old";
  }

}
```

### If, if else, else, for & while
```
var x = 0; 
var y = 2;
var z = 0;
var w = "lol";

if ((x > 10 and y < 20) or (z == 0 and w != "null")){
    print "Complex condition met!";

    if (x % 2 == 0 and y % 2 != 0) {
        print "x is even and y is odd";
    } else if (x % 2 != 0 and y % 2 == 0) {
        print "x is odd and y is even";
    } else {
        print "x and y are either both odd or both even";
    }

    while (x > 0 and y > 0) {
        x = x - 1;
        y = y - 1;
        if (x == y) {
            print "x and y are equal";
            break;
        }
    }
} else {
    print "Complex condition not met";
}
```

### Manage of global and local states
```
var a = 1;

fun sumator() {
    var b = 10;
    var result = a + b;
}
```

### Non declare variables
```
myString = "string";
myBool = true;
myInt = 1;
var a = b + 1;
```

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

### Complex example
```
class Person {
  init(name, age) {
    this.name = name;
    this.age = age;
    this.favoriteColor = "red";
  }

  greet() {
    var message = "Hello, my name is " + this.favoriteColor;
    return message;
  }

}

class Student extends Person {
  init(name, age, grade) { 
    super.init(name, age);
    this.grade = grade;
  } 

  performAction() { // UNION return type: string, int or boolean
    if (super.age > 18) {
        return "You are a not a child."
    } else {
        return 0;
    }
    return true;
  }

  study() {
    var nameVariable = this.name;
    var actionResult = this.performAction() // string, int or boolean
    var parentAge = super.age; 
    var parentGreeting = super.greet()
    print this.name + " is studying in grade " + this.grade + ".";
  }

} 

var name = "Alexander";

// class instances
var personInstance = new Person(name, 20);
var studentInstance = new Student(name, 20, 3);

// accesing to class attributes & methods
var grade = studentInstance.name;
var greetingResult = studentInstance.greet(); // return a string, int or boolean.
studentInstance.greet();    // Output: Hello, my name is red
studentInstance.study();    // Output: Alexander is studying in grade 3

```
