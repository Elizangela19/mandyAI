# MandyAI

---

## **🛠️ Requisitos Previos**
Asegúrate de tener instalado lo siguiente:

- Python 3.8+
- Administrador de paquetes pip
- Entorno virtual (opcional pero recomendado)
- ngrok (para exponer el servidor local)

---

## **📌 Instalación**

### **1️⃣ Clonar el Repositorio**
```bash
 git clone [https://github.com/your-repo/fastapi-ai-chatbot.git](https://github.com/Elizangela19/mandyAI.git)
```

### **2️⃣ Configurar el Entorno Virtual (Opcional)**
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### **3️⃣ Instalar Dependencias Requeridas**
```bash
pip install -r requirements.txt
```

### **4️⃣ Extraer y Cargar el Modelo Universal Sentence Encoder**
Descarga el **Universal Sentence Encoder v2** y extráelo en el directorio `model/`.
```bash
mkdir -p model/universal-sentence-encoder
# Extrae el modelo manualmente en model/universal-sentence-encoder/
```
Asegúrate de que la carpeta del modelo contenga lo siguiente y añade la carpeta del drive en la carpeta del modelo:
```
https://drive.google.com/drive/folders/1WB8OtetgQSFXPAfYNa3sbI7sE2wS6p35?usp=sharing
model/universal-sentence-encoder/
 ├── saved_model.pb
 ├── variables/
```

---

## **🚀 Ejecutando MandyAI**

### **5️⃣ Iniciar el Servidor de la API**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
Si se ejecuta con éxito, deberías ver:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### **6️⃣ Probar la API Localmente**
#### **Usando cURL:**
```bash
curl -X 'POST' \
  'http://localhost:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{"query": "Tell me about budgeting"}'
```
#### **Usando Postman:**
- **Método:** `POST`
- **URL:** `http://localhost:8000/chat`
- **Encabezados:** `{ "Content-Type": "application/json" }`
- **Cuerpo (JSON):**
  ```json
  { "query": "Tell me about budgeting" }
  ```

---

## **🌎 Exponer la API Públicamente con ngrok**
Si necesitas que Typebot acceda a tu API, expónla usando **ngrok**.

### **7️⃣ Configurar ngrok** Para configurar el authToken, crea una cuenta en ngrok.
```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
ngrok http 8000
```
Esto generará una URL como:
```
https://random-url.ngrok.io -> http://localhost:8000
```
Copia esta URL para el siguiente paso.

---

## **🔗 Conectando con Typebot**

### **8️⃣ Configurar Webhook en Typebot**
1. Abre **[Typebot.io](https://typebot.io/)** y crea un nuevo bot.
2. Arrastra y suelta un bloque **Webhook**.
3. Configura:
   - **Método:** `POST`
   - **URL:** `https://random-url.ngrok.io/chat`
   - **Encabezados:** `{ "Content-Type": "application/json" }`
   - **Cuerpo:**
     ```json
     { "query": "{{input}}" }
     ```
4. **Mapear Respuesta:**
   - Asigna `{{response.response}}` a la variable `ai_response`.
   - Muestra `{{ai_response}}` en un mensaje de texto.

### **9️⃣ Probar Typebot**
- Ejecuta el chatbot e ingresa una consulta financiera.
- Verifica que la IA responda correctamente.

---

## **📌 Despliegue**
Para producción, despliega tu aplicación FastAPI usando **Render, AWS, DigitalOcean o Heroku**.

---

## **💡 Solución de Problemas**
### **🔹 ¿La API no responde?**
- Asegúrate de que FastAPI esté corriendo: `uvicorn app:app --host 0.0.0.0 --port 8000`
- Revisa los registros de la API en busca de errores.
- Usa Postman para probar manualmente la API.

### **🔹 ¿Problemas con el Webhook en Typebot?**
- Asegúrate de que la URL del webhook sea correcta (`https://random-url.ngrok.io/chat`)
- Verifica que Typebot reciba una respuesta `200 OK`.
- Imprime `{{ai_response}}` para depurar el mapeo de la respuesta.

---

## **🎯 Mejoras Futuras**
✅ Expandir las respuestas de la IA para más temas financieros.  
✅ Desplegar la API en un servidor en la nube.  
✅ Mejorar el flujo de Typebot con lógica avanzada.  

---

## **📜 Licencia**
Este proyecto es **de código abierto**. ¡Siéntete libre de modificarlo y usarlo!
