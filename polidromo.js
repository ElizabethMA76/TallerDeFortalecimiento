const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function esPalindromo(cadena) {
    cadena = cadena.toLowerCase();
    return cadena === cadena.split("").reverse().join("");
}

rl.question("Ingresa una palabra o frase para verificar si es un palíndromo: ", function(input) {
    if (input.trim() === "") {
        console.log("No ingresaste ninguna cadena.");
    } else {
        const resultado = esPalindromo(input) ? "sí es un palíndromo" : "no es un palíndromo";
        console.log(`"${input}" ${resultado}.`);
    }
    rl.close();
});
