preguntas = {
    "hola":"Hola como estas?",
    "bien y tu":"tambien muy bien"
    "tiene cursos programacion":"si en talento tech tenemos cursos de programación"
    "donde estan ubicados": "en la carrera 29 # 50 20"
}


def respuesta(pregunta):
    if pregunta in preguntas:
        respuesta=preguntas[pregunta]
        else:
            respuesta="no entendi tu pregunta"
        return respuesta
    print(respuesta)

    print("Hola soy un chatbot Version 1")
    while true 