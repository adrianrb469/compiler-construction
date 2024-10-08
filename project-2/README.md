# Three Address Code for CompiScript 🧑🏻‍💻

This project consists on translate CompiScript code to Three Address Code. The purpose is to generate intermediate code mips assembly.

## Team Members 👥

- Adrian Rodriguez 21691
- Daniel Gomez 21429

## Project Demo 🎥

https://youtu.be/4A6uMO9N_bY?si=N88NDmuTJpjkNVIW

[![CompiScript Demo](https://img.youtube.com/vi/4A6uMO9N_bY/0.jpg)](https://www.youtube.com/watch?v=4A6uMO9N_bY)

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
