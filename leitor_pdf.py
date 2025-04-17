
from PyPDF2 import PdfReader

leitor = PdfReader("ALIEN-RPG-PTBR.pdf")
texto = ""

for pagina in leitor.pages:
    texto += pagina.extract_text() + "\n"

with open("base.txt", "w", encoding="utf-8") as arq:
    arq.write(texto)

print("Texto extraído para base.txt com sucesso.")
