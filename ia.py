
import sys
import ollama
from pathlib import Path

pergunta = sys.argv[1] if len(sys.argv) > 1 else "Explique o Alien RPG."
base = Path("base.txt").read_text(encoding="utf-8")

resposta = ollama.chat(model="llama3", messages=[
    {"role": "system", "content": "Você é a MÃE, a IA da nave do Alien RPG. Responda com base no texto do livro."},
    {"role": "user", "content": f"{base}\n\nPergunta: {pergunta}"}
])

print(resposta['message']['content'])
