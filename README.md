# Motor_De_Busqueda

1. Preparación de los Datos (Paso 1)
   
Definimos una lista en Python llamada articulos_reglamento que actúa como nuestro corpus (conjunto de documentos). Esta lista contiene 10 artículos reales extraídos 

del reglamento estudiantil, cubriendo temas de becas, faltas y cancelaciones.

2. Procesamiento de Lenguaje Natural Básico (Limpieza)
   
Antes de hacer matemáticas, el texto pasa por la función limpiar_texto. Esta función utiliza expresiones regulares (re.sub) para eliminar signos de puntuación 

(puntos, comas) y convierte todo a minúsculas. Esto es vital para que el algoritmo entienda que "Beca." y "beca" son exactamente la misma palabra.

3. Cálculo del TF (Frecuencia del Término)
   
La función calcular_tf mide qué tan frecuente es una palabra dentro de un artículo específico. La lógica es simple:

Fórmula: (Número de veces que aparece la palabra) / (Total de palabras en ese artículo).

Esto nos dice qué tan importante es la palabra dentro de ese documento en particular.

4. Cálculo del IDF (Frecuencia Inversa de Documento)
   
Aquí es donde entra la magia de numpy con la función calcular_idf.

Fórmula: Logaritmo natural de (Total de documentos / Documentos que contienen la palabra).

¿Para qué sirve? Penaliza las palabras muy comunes (como "el", "la", "estudiante") que aparecen en todos los artículos, y le da un peso o valor mucho mayor a palabras raras o específicas (como "vulnerabilidad" o "fraude").

Caso 1: 
<img width="1074" height="286" alt="image" src="https://github.com/user-attachments/assets/fb324d5b-c58d-4722-b307-488ce7454b0c" />

Caso 2:
<img width="1092" height="380" alt="image" src="https://github.com/user-attachments/assets/747343d7-a24f-4050-9b45-218c9a65aabb" />

Caso 3: 
<img width="568" height="161" alt="image" src="https://github.com/user-attachments/assets/4ad03e67-7175-48bf-aff5-f2a157c50956" />


