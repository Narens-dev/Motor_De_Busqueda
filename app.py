import numpy as np
import re

# ==========================================
# PASO 2: Implementar las funciones TF e IDF
# ==========================================

def limpiar_texto(texto):
    """
    Convierte el texto a minúsculas y elimina signos de puntuación.
    Devuelve una lista de palabras exactas.
    """
    texto_limpio = re.sub(r'[^\w\s]', '', texto.lower())
    return texto_limpio.split()

def calcular_tf(palabra, documento):
    """
    Calcula el TF: frecuencia_palabra / total_palabras_doc
    """
    palabras_doc = limpiar_texto(documento)
    if len(palabras_doc) == 0:
        return 0
    
    frecuencia = palabras_doc.count(palabra.lower())
    return frecuencia / len(palabras_doc)

def calcular_idf(palabra, corpus):
    """
    Calcula el IDF usando Numpy: np.log(Total_Docs / Docs_con_la_palabra)
    """
    N = len(corpus) # Total de documentos
    
    # Contamos en cuántos documentos aparece la palabra exacta
    df = sum(1 for doc in corpus if palabra.lower() in limpiar_texto(doc))
    
    # Evitar división por cero si la palabra no está en ningún texto
    if df == 0:
        return 0 
        
    # Aplicamos el logaritmo natural de la librería numpy
    return np.log(N / df)

def calcular_score_final(consulta, documento, corpus):
    """
    Calcula el Score Final: Suma el TF-IDF de CADA palabra de la consulta.
    """
    palabras_consulta = limpiar_texto(consulta)
    score_total = 0
    
    for palabra in palabras_consulta:
        tf = calcular_tf(palabra, documento)
        idf = calcular_idf(palabra, corpus)
        
        # Multiplicamos y sumamos al acumulador
        score_total += (tf * idf)
        
    return score_total

def motor_de_busqueda(consulta, corpus):
    """
    Evalúa todos los documentos y los ordena del más al menos relevante.
    """
    resultados = []
    for i, doc in enumerate(corpus):
        score = calcular_score_final(consulta, doc, corpus)
        
        # Solo agregamos los documentos que tengan alguna coincidencia (score > 0)
        if score > 0:
            resultados.append({'articulo': i + 1, 'score': score, 'texto': doc})
            
    # Ordenar de mayor a menor relevancia
    resultados.sort(key=lambda x: x['score'], reverse=True)
    return resultados


# ==========================================
# PASO 1: Dataset sugerido (10 artículos del reglamento)
# ==========================================

articulos_reglamento = [
    "La universidad otorgará becas de excelencia a los estudiantes que obtengan un promedio ponderado acumulado superior a cuatro punto cinco.",
    "Se consideran faltas disciplinarias graves el fraude académico, la suplantación y la alteración de documentos oficiales de la institución.",
    "El estudiante podrá solicitar la cancelación de asignaturas únicamente dentro de las fechas establecidas en el calendario académico oficial.",
    "La inasistencia injustificada superior al veinte por ciento de las sesiones programadas en una asignatura causará la pérdida de la misma.",
    "Para conservar cualquier tipo de beca, el estudiante no debe haber incurrido en faltas disciplinarias durante su permanencia en la institución.",
    "La renovación de la matrícula académica estará sujeta a no tener sanciones disciplinarias vigentes ni obligaciones financieras pendientes.",
    "La cancelación total del semestre académico debe solicitarse por escrito ante la decanatura del programa justificando los motivos.",
    "Para optar al título profesional, el estudiante debe aprobar la totalidad de los créditos académicos y el requisito de segundo idioma.",
    "Las faltas disciplinarias leves serán sancionadas con amonestación verbal o escrita directamente por parte del director del programa.",
    "Las becas por vulnerabilidad socioeconómica requieren un estudio previo aprobado por el departamento de bienestar universitario."
]


# ==========================================
# PASO 3: Búsqueda Interactiva (TOP 3)
# ==========================================

print("=== MOTOR DE BÚSQUEDA TF-IDF ===")
print("Escribe las palabras que deseas buscar.")
print("Escribe 'salir' para terminar el programa.")
print("=" * 32)

while True:
    # Pedir al usuario que ingrese la consulta
    consulta_usuario = input("\n🔍 Ingresa tu búsqueda: ")
    
    # Condición para salir del ciclo
    if consulta_usuario.lower() == 'salir':
        print("Saliendo del motor de búsqueda. ¡Éxitos con el proyecto!")
        break
        
    print(f"\nResultados para: '{consulta_usuario}'")
    print("-" * 60)

    # Ejecutar el motor de búsqueda
    resultados_busqueda = motor_de_busqueda(consulta_usuario, articulos_reglamento)

    # Seleccionar solo el Top 3
    top_3 = resultados_busqueda[:3]

    if not top_3:
        print("No se encontraron artículos que coincidan con la búsqueda.")
    else:
        print("🏆 TOP 3 ARTÍCULOS MÁS RELEVANTES 🏆\n")
        # Mostrar los resultados enumerados del 1 al 3
        for i, res in enumerate(top_3, 1):
            print(f"Top {i} -> Artículo {res['articulo']} | Score TF-IDF: {res['score']:.4f}")
            print(f"Fragmento: {res['texto']}\n")