
from webwhatsapi import WhatsAPIDriver
import time
import subprocess

print("Iniciando o driver do WhatsApp...")
driver = WhatsAPIDriver()
print("Escaneie o QR Code com o WhatsApp")

while not driver.is_logged_in():
    time.sleep(2)

print("Bot da MÃE iniciado.")

while True:
    time.sleep(3)
    for contato in driver.get_unread():
        for mensagem in contato.messages:
            if mensagem.type == 'chat' and ("mãe" in mensagem.content.lower()):
                pergunta = mensagem.content.lower().replace("mãe", "").strip()
                if pergunta:
                    print(f"Pergunta recebida: {pergunta}")
                    resposta = subprocess.run(
                        ['python', 'ia.py', pergunta],
                        capture_output=True,
                        text=True
                    )
                    contato.reply(resposta.stdout.strip())
