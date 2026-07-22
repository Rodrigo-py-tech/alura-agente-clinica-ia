from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")

print(repr(api_key))
print("Inicio:", api_key[:10])
print("Longitud:", len(api_key))


cliente = Groq(
    api_key=api_key
)


respuesta = cliente.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Responde solamente: OK"
        }
    ]
)


print(respuesta.choices[0].message.content)