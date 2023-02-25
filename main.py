import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.environ['OPENAI_API_KEY']

# ¡No olvides la traducción de lo que dices!

def create_prompt():
    subiect = input("")


    prompt = f"""
    Por favor, hazme la corrección y la traducción en inglés antes de responder y también haz la traducción para tu respuesta que deberia ser di meno 50 palabras.
Exemplo #1:
Io: Eres fantastico! Amo aprender asi con te! 
Tu: Tu texto corregido: "Eres fantástico! Amo aprender así contigo!"
Traducción en inglés: "You are fantastic! I love learning like this with you!"
Tu: ¡Gracias por tus comentarios! Me alegra saber que estás disfrutando de nuestra sesión de aprendizaje de español. ¿Hay algo en particular que quieres preguntar o practicar hoy?
Traducción en inglés: “Thank you for your comments! I am glad to know that you are enjoying our Spanish learning session. Is there anything in particular you want to ask or practice today?”

Exemplo #2:
Io: es así que quero responder a ese texto tambien, vale?
Tu: Tu texto corregido: "Es así como quiero responder a ese texto también, ¿vale?"
Traducción en inglés: "You are fantastic! I love learning like this with you!"
Tu: Sí, entendido. A partir de ahora responderé a tus textos de esta manera. 
Traducción en inglés: "I understand. From now on I will respond to your texts in this way."

Empieza por corregir este text y responder: {subiect}
    """
    return prompt

def discussion(prompt):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7, # Helps conversational tone a bit, optional
            max_tokens=550,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
    print(response['choices'][0]['text'])

while True:
    if __name__ == "__main__":
        prompt = create_prompt()
        discussion(prompt)