import asyncio
from app.gemini_service import chat_completion

async def chat_loop():
    print("Tutor IA conectado. Pode começar a conversar!")
    print("Dica: diga o que quer aprender e a IA conduz o papo.\n")

    contexto = "Você é um tutor paciente e prático. Ajude o usuário a aprender o que ele quiser. Faça perguntas, conduza o papo e ensine passo a passo.\n\n"

    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando conversa. Valeu!")
            break

        contexto += f"Usuário: {user_input}\n"

        resposta = await chat_completion(contexto)

        print(f"\nIA: {resposta}\n")

        contexto += f"IA: {resposta}\n"

if __name__ == "__main__":
    asyncio.run(chat_loop())