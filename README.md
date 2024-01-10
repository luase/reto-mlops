# 4 Ejemplos de cómo chatear con tus archivos CSV

Este repositorio contiene 4 (5, considerando la solución de paga) distintas soluciones para interactuar con tus archivos CSV sin código, solamente hablando con un chatbot.

## Cómo hacer el setup de la app

- Clona el repositorio

  `git clone https://github.com/luase/reto-mlops.git`

- Instala Ollama: [Instrucciones Oficiales](https://ollama.ai/download)
- Crea un entorno virtual y activalo
  
  `python -m venv .venv`

  `source .venv/bin/activate`

- Instala los requerimientos

  `pip install -r requirements.txt`

- Prueba los notebooks!

  ## Qué encontraras
  Primero me gustaría que revisara lo que se puede conseguir con herramientas de paga, como lo es una cuenta de paga de ChatGPT
  - [Asesor Inmobiliario Reto AI](https://chat.openai.com/g/g-Mpzzcl7EB-asesor-inmobiliario-reto-ai)
 
  El propósito del repositorio es conseguir resultados similares o mejores a los que ofrecen los LLM de paga, utilizando únicamente herramientas Open Source.

  Dentro de la notebook [`QnA_With_RAG.ipynb`](https://github.com/luase/reto-mlops/blob/main/QnA_With_RAG.ipynb) verás cómo agregar un archivo de CSV o un Dataframe de Pandas al conocimiento de un LLM de manera que pueda consultarlo como referencia de su base de conocimiento. Así como as ventajas y desventajas de hacerlo de este modo.

  
  En la segunda notebook [`QnA_With_RAG_w_CodeExecution.ipynb`](https://github.com/luase/reto-mlops/blob/main/QnA_With_RAG_w_CodeExecution.ipynb) encontrarás cómo no enseñarle directamente todo el CSV o Dataframe a tu LLM, si no cómo darle las herramientas para que este pueda generar código que le ayude a consultar el documento, así como las ventajas y desventajas también.
