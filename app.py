from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de conocimiento del chatbot para Zoghbi Jeans
respuestas = {
    "hola": "¡Hola! Bienvenido a Zoghbi Jeans. ¿En qué podemos ayudarte hoy?",
    "modelos": "Tenemos una amplia variedad: skinny, rectos, bootcut, en colores clásicos y tendencia. ¿Algún modelo en particular?",
    "que jeans tienen": "Tenemos una amplia variedad: skinny, rectos, bootcut, en colores clásicos y tendencia. ¿Algún modelo en particular?",
    "precios": "Nuestros jeans tienen un rango de precios entre $50 y $120, dependiendo del modelo y materiales.",
    "tallas": "Trabajamos tallas del 28 al 42, y también tenemos opciones especiales para tallas grandes.",
    "envios": "Realizamos envíos a todo el país con costo según ubicación. En Valencia es gratis en compras mayores a $100.",
    "promociones": "Actualmente tenemos 2x1 en jeans básicos los martes y 15% off pagando con transferencia bancaria.",
    "donde estan": "Nuestro local está en Av. Corrientes 1234, Valencia. Abrimos de lunes a sábados de 10 a 20hs.",
    "calidad": "Usamos mezclilla premium de 12oz con elastano para mayor comodidad, costuras reforzadas y terminaciones de lujo.",
    "adios": "¡Gracias por contactarte con Zoghbi Jeans! Vuelve pronto por tus jeans de calidad.",
    "default": "Disculpa, no entendí tu consulta. ¿Podrías reformularla? Estamos para ayudarte con: modelos, tallas, precios, envíos o promociones."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message'].lower()
    response = respuestas.get(user_message, respuestas['default'])
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)