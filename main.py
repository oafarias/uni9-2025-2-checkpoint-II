# Importa as classes dos outros arquivos
from canais import WhatsApp, Telegram, Facebook, Instagram, ICanal
from mensagens import MensagemTexto, MensagemVideo, MensagemFoto, MensagemArquivo

# Importa 'List' para 'type hinting' (boa prática)
from typing import List

def rodar_demonstracao():
    """Função principal para executar a demonstração."""
    
    # --- 1. Instanciando os Canais ---
    # (Todos podem ser tratados como 'ICanal' graças ao polimorfismo)
    canal_whatsapp = WhatsApp()
    canal_telegram = Telegram()
    canal_facebook = Facebook()
    canal_instagram = Instagram()

    # --- 2. Instanciando as Mensagens ---
    # (Todas podem ser tratadas como 'Mensagem' graças à herança)
    msg_texto = MensagemTexto("Olá! Este é o checkpoint II de POO.")
    msg_foto = MensagemFoto("Foto da equipe!", "equipe.jpg")
    msg_video = MensagemVideo("Tutorial de Python", "tutorial.mp4", "video/mp4", 300)
    msg_arquivo = MensagemArquivo("Documento de Requisitos", "requisitos.pdf", "application/pdf")

    print("### INICIANDO DEMONSTRAÇÃO DE ENVIO ###\n")

    # --- 3. Demonstração de Envio (Polimorfismo em Ação) ---
    # O método .enviar() é o mesmo, mas a mensagem e o canal se comportam
    # de forma diferente.

    # A. WhatsApp (espera número)
    canal_whatsapp.enviar(msg_texto, "+5511999998888")

    # B. Telegram (pode ser número ou usuário)
    canal_telegram.enviar(msg_video, "@usuario_telegram")
    canal_telegram.enviar(msg_texto, "+5511911112222") # Telegram também aceita número

    # C. Facebook (espera usuário)
    canal_facebook.enviar(msg_foto, "usuario.facebook.123")

    # D. Instagram (espera usuário)
    canal_instagram.enviar(msg_foto, "user.insta") # Instagram envia foto
    canal_instagram.enviar(msg_arquivo, "outro.user.insta") # Instagram envia "arquivo" (ex: DM)


    # --- 4. Demonstração Avançada (Polimorfismo) ---
    # Podemos tratar todos os canais da mesma forma,
    # sem saber qual é qual, graças à interface ICanal.

    print("\n\n### DEMONSTRAÇÃO DE POLIMORFISMO AVANÇADO ###")
    print("Enviando uma mensagem de arquivo para TODOS os canais.")

    # Criamos uma lista do tipo ICanal
    todos_os_canais: List[ICanal] = [canal_whatsapp, canal_telegram, canal_facebook, canal_instagram]
    destinatarios = ["+551155555", "@admin_grupo", "fb.suporte", "ig.suporte"]

    # O loop não se importa se o canal é WhatsApp ou Facebook,
    # ele apenas chama .enviar() (Polimorfismo)
    for i, canal in enumerate(todos_os_canais):
        canal.enviar(msg_arquivo, destinatarios[i])

    print("### FIM DA DEMONSTRAÇÃO ###")


# --- Ponto de entrada do script ---
# Bloco padrão para garantir que o script só rode quando executado diretamente
# (e não quando importado por outro script)
if __name__ == "__main__":
    rodar_demonstracao()
