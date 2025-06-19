1. Definición de la Paleta de Colores
Establecí una paleta de colores utilizando variables CSS para mantener la coherencia visual:

css
:root {
    --gold: #D4AF37;       /* Tono dorado principal */
    --dark-gold: #B8860B;  /* Variación oscura del dorado */
    --black: #000000;      /* Negro sólido */
    --white: #FFFFFF;      /* Blanco puro */
    --light-gray: #F5F5F5; /* Gris claro para fondos */
    --dark-gray: #333333;  /* Gris oscuro para texto */
}


2. Configuración Base de la Página
Apliqué los estilos fundamentales para el documento:

css
body {
    font-family: 'Montserrat', sans-serif;
    margin: 0;
    padding: 0;
    background-color: var(--white);
    color: var(--black);
}


Esto configura:

La tipografía Montserrat como fuente principal

Elimina los márgenes y rellenos por defecto

Establece un fondo blanco con texto negro



3. Diseño del Encabezado
Implementé un encabezado con contraste alto:

css
.header {
    background-color: var(--black);
    color: var(--gold);
    padding: 15px 0;
    text-align: center;
    border-bottom: 3px solid var(--gold);
}


Características:

Fondo negro con texto dorado

Alineación centralizada

Borde inferior decorativo en dorado

Espaciado interno equilibrado

4. Contenedor Principal del Chat
Diseñé el área de conversación con las siguientes propiedades:

css
.chat-container {
    max-width: 800px;
    margin: 30px auto;
    border: 1px solid var(--gold);
    border-radius: 8px;
    box-shadow: 0 0 15px rgba(0,0,0,0.1);
}


Especificaciones:

Ancho máximo controlado

Centrado automático en la página

Borde en dorado

Esquinas redondeadas

Sombra para profundidad

5. Estilización de Mensajes
Diferencié visualmente los mensajes del sistema y del usuario:

Para mensajes del bot:

css
.bot-message span {
    background-color: var(--white);
    border: 1px solid var(--gold);
}
Para mensajes del usuario:

css
.user-message span {
    background-color: var(--gold);
    color: var(--black);
}


Distinciones:

Mensajes del sistema: fondo blanco con borde dorado

Mensajes del usuario: fondo dorado con texto negro

Ancho limitado al 80% para mejor legibilidad

Espaciado vertical adecuado entre mensajes

6. Área de Composición de Mensajes
Implementé el área de entrada de texto:

css
#message-form {
    display: flex;
    padding: 15px;
    background-color: var(--black);
}

#message-input {
    border: 2px solid var(--gold);
    border-radius: 30px;
}


Características funcionales:

Diseño flexible para adaptabilidad

Fondo negro para contraste

Campo de texto con borde dorado

Esquinas completamente redondeadas

Integración visual con el diseño general

7. Personalización de la Barra de Desplazamiento
Añadí estilos personalizados al scroll:

css
#chat-box::-webkit-scrollbar {
    width: 8px;
}

#chat-box::-webkit-scrollbar-thumb {
    background-color: var(--gold);
}


Detalles implementados:

Anchura reducida

Color dorado para el control deslizante

Fondo gris claro para el canal del scroll

Integración con el esquema de color general