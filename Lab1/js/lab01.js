// Mensaje en la consola
console.log("Lab01 - Estilos con HTML, CSS y JavaScript cargados correctamente.");

// Cambiar el color del título al pasar el mouse
document.getElementById("heading").addEventListener("mouseover", function() {
    this.style.color = "darkred";
});

document.getElementById("heading").addEventListener("mouseout", function() {
    this.style.color = "black";
});
