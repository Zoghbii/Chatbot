1. Estructura HTML (index.html)
DOCTYPE y Encabezado
html

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zoghbi Jeans - Asistente Virtual</title>


Propósito: Define el documento como HTML5 en español
Funcionalidad:

meta charset="UTF-8" → Soporte para caracteres especiales

viewport → Hace la página responsive en dispositivos móviles

title → Título que aparece en la pestaña del navegador

Enlaces a Hojas de Estilo
html

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">

Propósito: Importa los estilos visuales
Funcionalidad:

Primer link → Carga el CSS personalizado desde Flask

Segundo link → Importa Font Awesome para íconos

Estructura del Cuerpo
html

<body>
    <div class="header">
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Zoghbi Jeans" class="logo">
        <h1>Asistente Virtual</h1>
    </div>

Propósito: Cabecera de la aplicación
Funcionalidad:

Muestra el logo de la marca

Presenta el título del asistente

Contenedor del Chat
html

    <div class="chat-container">
        <div id="chat-box">
            <div class="bot-message">
                <i class="fas fa-robot"></i>
                <span>¡Hola! Soy el asistente de Zoghbi Jeans...</span>
            </div>
        </div>

Propósito: Área de visualización de mensajes
Funcionalidad:

Contenedor principal (chat-container)

Área de mensajes (chat-box)

Mensaje inicial del bot con ícono de robot

Formulario de Mensajes
html

        <form id="message-form">
            <input type="text" id="message-input" placeholder="Escribe tu consulta..." required>
            <button type="submit"><i class="fas fa-paper-plane"></i></button>
        </form>

Propósito: Interfaz para que el usuario envíe mensajes
Funcionalidad:

Formulario con identificador para JavaScript

Campo de texto con marcador de posición

Botón de envío con ícono de avión de papel

2. Código JavaScript
Selección de Elementos
javascript

const form = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const chatBox = document.getElementById('chat-box');
Propósito: Obtener referencias a elementos del DOM

Funcionalidad:

Prepara los elementos para manipulación posterior

Manejador de Eventos del Formulario
javascript

form.addEventListener('submit', function(e) {
    e.preventDefault();
    const message = messageInput.value;
    
    if(message.trim() === '') return;

Propósito: Interceptar el envío del formulario
Funcionalidad:

Previene el envío tradicional (recarga de página)

Obtiene el valor del mensaje

Valida que no esté vacío

Renderizado del Mensaje del Usuario
javascript

    chatBox.innerHTML += `
        <div class="user-message">
            <i class="fas fa-user"></i>
            <span>${message}</span>
        </div>
    `;

Propósito: Mostrar el mensaje del usuario en el chat
Funcionalidad:

Añade HTML dinámico al contenedor

Usa template literals para interpolación

Muestra ícono de usuario junto al mensaje

Comunicación con el Backend
javascript

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(message)}`
    })

Propósito: Enviar la consulta al servidor
Funcionalidad:

Usa Fetch API para comunicación asíncrona

Configura método POST y cabeceras

Codifica el mensaje para URL

Procesamiento de la Respuesta
javascript

    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `
            <div class="bot-message">
                <i class="fas fa-robot"></i>
                <span>${data.response}</span>
            </div>
        `;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

Propósito: Manejar la respuesta del servidor
Funcionalidad:

Convierte respuesta a JSON

Añade la respuesta del bot al chat

Ajusta el scroll para mostrar el último mensaje

Evento para Tecla Enter
javascript

messageInput.addEventListener('keypress', function(e) {
    if(e.key === 'Enter') {
        form.dispatchEvent(new Event('submit'));
    }
});

Propósito: Permitir envío con Enter
Funcionalidad:

Detecta pulsación de tecla

Dispara evento submit al presionar Enter

3. Flujo Completo de Operación
Inicialización:

El navegador carga HTML y CSS

Se muestra el mensaje inicial del bot

Interacción del Usuario:

Escribe mensaje en el campo de texto

Presiona enviar (click o Enter)

Procesamiento Frontend:

JavaScript valida y muestra el mensaje

Envía la consulta al backend

Comunicación Backend (implícito):

El servidor recibe la consulta en /get_response

Procesa y genera una respuesta

Devuelve JSON con la respuesta

Visualización de Respuesta:

JavaScript recibe y muestra la respuesta

Ajusta el scroll del chat

Repetición:

El ciclo se repite para cada mensaje nuevo

