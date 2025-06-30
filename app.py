from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/mensaje', methods=['GET'])
def obtener_mensaje():
    texto_largo = (
        "Antes de sumergirnos en ARM64, establezcamos una base. ARM son las siglas de Advanced RISC Machine, un tipo de arquitectura de procesador conocida por su eficiencia y por centrarse en la Computación de Conjunto de Instrucciones Reducido (RISC). Los procesadores RISC dan prioridad a un conjunto más reducido de instrucciones más sencillas, lo que se traduce en un menor consumo de energía y un tamaño de chip más reducido. Esto los hace ideales para dispositivos móviles como teléfonos inteligentes y tabletas, donde la duración de la batería y la portabilidad son cruciales."

        "La propia arquitectura ARM engloba una amplia familia de conjuntos de instrucciones, con variaciones que responden a diferentes requisitos de rendimiento y potencia. Tradicionalmente, los procesadores ARM funcionaban en modo de 32 bits, lo que limitaba la cantidad de memoria que podían direccionar y el tamaño de los datos que podían manejar. Aquí es donde entra en escena ARM64."
        "Conclusión: ARM64: una fuerza a tener en cuenta"
        "En conclusión, ARM64 no es sólo una evolución de la arquitectura ARM; representa un cambio significativo en la informática. Su capacidad para ofrecer un rendimiento excepcional manteniendo la eficiencia energética la convierte en una opción convincente para una amplia gama de dispositivos, desde aparatos móviles a potentes servidores. A medida que el ecosistema de software siga madurando y los desarrolladores aprovechen el potencial de ARM64, podemos esperar que esta arquitectura desempeñe un papel aún más destacado en la configuración del futuro de la informática."
    )
    return jsonify({"mensaje": texto_largo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
