from antlr4 import *
from PalabrasLexer import PalabrasLexer
from PalabrasParser import PalabrasParser
from evaluador import Evaluador

def procesar(texto):
    # 1. Crear flujo de entrada
    input_stream = InputStream(texto)

    # 2. Lexer
    lexer = PalabrasLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # 3. Parser
    parser = PalabrasParser(tokens)

    # 👉 IMPORTANTE: generar el árbol sintáctico
    # Cambia 'expr' por el nombre de tu regla inicial
    tree = parser.expr()

    # 4. Evaluador (visita el árbol)un
    evaluador = Evaluador()
    return evaluador.visit(tree)

if __name__ == "__main__":
    while True:
        txt = input("Ingresa operación en palabras: ")
        try:
            resultado = procesar(txt)
            print("Resultado:", resultado)
        except Exception as e:
            print("Error:", e)
