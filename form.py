class Form:
    
    def __init__(self, tituloFormulario, preguntas, tamanoFuente=True, saltosDeLinea=1, espaciosDerecha =1, estilo="", estiloTitulo=""):
        self.tituloFormulario = tituloFormulario
        self.preguntas = preguntas
        self.tamanoFuente = tamanoFuente
        self.saltosDeLinea = saltosDeLinea
        self.espaciosDerecha = espaciosDerecha
        self.estilo = estilo
        self.estiloTitulo = estiloTitulo

    def mostrarForm(self):
        respuestas = []
        saltosDeLinea = self.darFormato(self.saltosDeLinea, "\n")
        espaciosDerecha = self.darFormato(self.espaciosDerecha, "\t")
        titulo = self.devolverTitulo()
        print(titulo)
        for indice in range(len(self.preguntas)):
            estilos = self.estilo
            if self.tamanoFuente == True:
                formatoPregunta = f"{saltosDeLinea}{espaciosDerecha}{estilos}{self.preguntas[indice]}: ".upper()
                respuestaPregunta = input(formatoPregunta)
                datoExacto = self.obtenerDatoExacto(respuestaPregunta)
                respuestas.append(datoExacto)
            else:
                formatoPregunta = f"{saltosDeLinea}{espaciosDerecha}{estilos}{self.preguntas[indice]}: "
                respuestaPregunta = input(formatoPregunta)
                datoExacto = self.obtenerDatoExacto(respuestaPregunta)
                respuestas.append(datoExacto)
        print("\n\n")
        return respuestas

    def devolverTitulo(self):
        saltosDeLinea = self.darFormato(self.saltosDeLinea, "\n")
        espaciosDerecha = self.darFormato(self.espaciosDerecha, "\t")
        if self.tamanoFuente == True:
            return f"{saltosDeLinea}{espaciosDerecha}{self.estiloTitulo}{self.tituloFormulario}\n".upper()
        else:
            return f"{saltosDeLinea}{espaciosDerecha}{self.estiloTitulo}{self.tituloFormulario}\n".title()

    def darFormato(self, cantidad, caracter):
        formato = ""
        for indice in range(cantidad):
            formato += f"{caracter}"
        return formato

    def obtenerDatoExacto(self, valor):
        try:
            nuevoValor = 0
            if int(valor):
                nuevoValor = int(valor)
            elif float(valor):
                nuevoValor = float(valor)
            return nuevoValor
        except (TypeError, ValueError):
            return valor

    def limpiar(self):
        from os import system
        system("cls")

    def mensajeMal(self, mensaje="Has rellenado mal alguno/s campos.", estilo=""):
        if estilo == "":
            estilo = "ಠ_ಠ  "
        print(f"\n\n\t{estilo}{mensaje} \n\n")


