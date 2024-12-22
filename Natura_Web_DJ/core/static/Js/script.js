
// Constantes Hamburguesa
const hamburguesa = document.querySelector('.hamburguesa');
const menu_hamburguesa = document.querySelector('.menu_hamburguesa');

// Constantes Busqueda
const iconoBuscar = document.querySelector('.contenedor_buscar');
const menu_buscar = document.querySelector('.menu_buscar');

const buscarInput = document.querySelector('.buscar_input');

const contenedor_filtro_categoria = document.getElementById("ordenMenuCategoria")
const contenedor_filtro_orden = document.getElementById("ordenMenuFiltro");

// Seleccionamos el overlay
const overlay_filtro_orden = document.getElementById("overlay_filtro_orden");
const overlay_filtro_categorias = document.getElementById("overlay_filtro_categoria");




// Funcion hamburguesa
hamburguesa.addEventListener('click', () => {
    // Alterna el estado del menú hamburguesa
    hamburguesa.classList.toggle('active');
    menu_hamburguesa.classList.toggle('active');

    // Si el menú de búsqueda está abierto, lo cierra
    if (menu_buscar.classList.contains('active')) {
        menu_buscar.classList.remove('active');
    }
});


// Funcion menu de busqueda 
iconoBuscar.addEventListener('click', () => {
    
    // Alterna el estado del menú de búsqueda
    menu_buscar.classList.toggle('active');

    contenedor_filtro_orden.classList.remove("active");
    contenedor_filtro_categoria.classList.remove("active");
    

    // Solo hace scroll si no está ya en la parte superior de la página
    if (window.scrollY !== 0) {
        // Devuelve el scroll al inicio de la pantalla
        window.scrollTo({
            top: 0, // Devuelve al inicio
            behavior: 'smooth' // Efecto suave de desplazamiento
        });
    }


    // Si el menú hamburguesa está abierto, lo cierra
    if (menu_hamburguesa.classList.contains('active')) {
        menu_hamburguesa.classList.remove('active');
        hamburguesa.classList.remove('active');
    }
});



// SCROLL

let lastScrollTop = 0; // Variable para almacenar la posición de scroll anterior
window.addEventListener('scroll', () => {
    let currentScroll = window.scrollY; // Obtiene la posición actual del scroll

    menu_hamburguesa.classList.remove('active');
    hamburguesa.classList.remove('active');
    contenedor_filtro_orden.classList.remove("active");
    contenedor_filtro_categoria.classList.remove("active");

    // Si el usuario hace scroll hacia abajo, ocultamos el menú
    if (currentScroll > lastScrollTop) {
        menu_buscar.classList.remove('active');
        
        contenedor_filtro_categoria.classList.remove("active");
        overlay_filtro_categorias.classList.remove("active")
        
        contenedor_filtro_orden.classList.remove("active");
        overlay_filtro_orden.classList.remove("active");
    }
    // Si el usuario hace scroll hacia arriba, mantenemos el menú visible
    else if (currentScroll < lastScrollTop) {
        
    }

    lastScrollTop = currentScroll; // Actualizamos la posición anterior del scroll
});


// Funcion FILTRO_ORDEN

function toggleOrdenMenu() {

    // Alternar el overlay
    overlay_filtro_orden.classList.toggle("active");

    // Cerrar el menú de categorías si está abierto
    if (contenedor_filtro_categoria.classList.contains("active")) {
        contenedor_filtro_categoria.classList.remove("active");
    }

    // Alternar la visibilidad del menú de orden
    contenedor_filtro_orden.classList.toggle("active");

    // Ocultar el overlay si cerramos el menú
    if (!contenedor_filtro_orden.classList.contains("active")) {
        overlay_filtro_orden.classList.remove("active");
    }
}


overlay_filtro_orden.addEventListener("click", () => {
    contenedor_filtro_orden.classList.remove("active");
    overlay_filtro_orden.classList.remove("active");
});


function ordenar(tipo) {
    console.log("Orden seleccionado:", tipo);
    // Aquí puedes añadir la lógica para actualizar los datos
    toggleOrdenMenu(); // Cerrar el menú
}


// Funcion FILTRO_CATEGORIA

function toggleCategorias() {
    
    // Cerrar el menú de orden si está abierto
    if (contenedor_filtro_orden.classList.contains("active")) {
        contenedor_filtro_orden.classList.remove("active");
        overlay_filtro_orden.classList.remove("active");
    }

    // Alternar el overlay y el contenedor de categorías
    overlay_filtro_categorias.classList.toggle("active");
    contenedor_filtro_categoria.classList.toggle("active");

    // Ocultar el overlay si cerramos el menú
    if (!contenedor_filtro_categoria.classList.contains("active")) {
        overlay_filtro_categorias.classList.remove("active");
    }
}


overlay_filtro_categorias.addEventListener("click", () => {
    contenedor_filtro_categoria.classList.remove("active");
    overlay_filtro_categorias.classList.remove("active");
});

function seleccionarCategoria(categoria) {
    console.log('Categoría seleccionada:', categoria);
    toggleCategorias(); // Cerrar el menú
}

