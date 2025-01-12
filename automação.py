#É necessário primeiro importar as libs em um ambiente virtual (*env)


import pywhatkit #Instalar com o comando: pip install pywhatkit
from datetime import datetime 



numero_phone = "+55..." #Insira o telefone com o ddd e o número.


mensagem = "Olá contato, 🤳✌ esta é uma mensagem automática enviada via Python! 🚀👨🏾‍💻. Essa é apenas uma automação em teste. *APENAS DESCONSIDERE ESTA MENSAGEM 😉✔*"


# Obter o horário atual
hora_atual = datetime.now()
hora = hora_atual.hour
minuto = hora_atual.minute + 1  # Agendar para 1 minuto no futuro


# Agendar o envio da mensagem
try:
    pywhatkit.sendwhatmsg(numero_phone, mensagem, hora, minuto)
    print("Mensagem agendada com sucesso!")
except Exception as e:
    print(f"Erro ao agendar a mensagem: {e}")
    
    
    
#Após chamar o programa no terminal, abra o site https://web.whatsapp.com/ e aguarde a mensagem ser enviada.
