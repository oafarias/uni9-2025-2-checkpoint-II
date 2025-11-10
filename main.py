# Importa as classes dos outros arquivos
from canais import WhatsApp, Telegram, Facebook, Instagram, ICanal
from mensagens import MensagemTexto, MensagemVideo, MensagemFoto, MensagemArquivo

# Importa 'List' para 'type hinting' (boa prática)
from typing import List

# --- PARTE 1: TESTE AUTOMÁTICO (O que você já tinha) ---
def rodar_demonstracao():
    """Função que roda todos os testes pré-definidos."""
    
    print("=" * 40)
    print("### INICIANDO DEMONSTRAÇÃO AUTOMÁTICA (TESTE) ###")
    print("=" * 40 + "\n")

    # Instanciando os canais
    canal_whatsapp = WhatsApp()
    canal_telegram = Telegram()
    canal_facebook = Facebook()
    canal_instagram = Instagram()

    # Instanciando as mensagens
    msg_texto = MensagemTexto("Olá! Este é o checkpoint II de POO.")
    msg_foto = MensagemFoto("Foto da equipe!", "equipe.jpg")
    msg_video = MensagemVideo("Tutorial de Python", "tutorial.mp4", "video/mp4", 300)
    msg_arquivo = MensagemArquivo("Documento de Requisitos", "requisitos.pdf", "application/pdf")

    # A. WhatsApp
    canal_whatsapp.enviar(msg_texto, "+5511999998888")

    # B. Telegram
    canal_telegram.enviar(msg_video, "@usuario_telegram")
    
    # C. Facebook
    canal_facebook.enviar(msg_foto, "usuario.facebook.123")

    # D. Instagram
    canal_instagram.enviar(msg_arquivo, "outro.user.insta")
    
    print("\n### FIM DA DEMONSTRAÇÃO AUTOMÁTICA ###")
    print("=" * 40 + "\n")


# --- PARTE 2: MENU INTERATIVO (Novo) ---
def menu_interativo():
    """Função que mostra um menu para o usuário escolher o que enviar."""
    
    print("=" * 40)
    print("### INICIANDO MODO INTERATIVO ###")
    print("=" * 40 + "\n")

    # Instanciamos os canais que o menu pode usar
    canais = {
        "1": WhatsApp(),
        "2": Telegram(),
        "3": Facebook(),
        "4": Instagram()
    }

    while True:
        # 1. Pergunta o Canal
        print("Para qual canal você quer enviar mensagem?")
        print("  1: WhatsApp")
        print("  2: Telegram")
        print("  3: Facebook")
        print("  4: Instagram")
        print("  0: Sair")
        
        escolha_canal = input("Escolha o canal (0 para Sair): ")

        if escolha_canal == "0":
            print("\nObrigado por usar o sistema! Saindo...")
            break
        
        if escolha_canal not in canais:
            print("\nOpção inválida! Tente novamente.\n")
            continue
        
        # Seleciona o objeto do canal (Polimorfismo!)
        canal_selecionado = canais[escolha_canal]
        
        # 2. Pergunta o Destinatário
        destinatario = input(f"Digite o destinatário para {canal_selecionado.__class__.__name__}: ")
        
        # 3. Pergunta o tipo de Mensagem
        print("\nQual tipo de mensagem?")
        print("  1: Texto")
        print("  2: Foto")
        print("  3: Vídeo")
        print("  4: Arquivo")
        
        escolha_tipo = input("Escolha o tipo de mensagem: ")
        texto_base = input("Digite o texto principal da mensagem: ")
        
        mensagem_para_enviar = None

        # Cria o objeto de mensagem correto (Polimorfismo!)
        if escolha_tipo == "1":
            mensagem_para_enviar = MensagemTexto(texto_base)
        elif escolha_tipo == "2":
            # Usamos nomes de arquivo fixos para simplificar o menu
            mensagem_para_enviar = MensagemFoto(texto_base, "foto_interativa.jpg")
        elif escolha_tipo == "3":
            mensagem_para_enviar = MensagemVideo(texto_base, "video_interativo.mp4", "video/mp4", 60)
        elif escolha_tipo == "4":
            mensagem_para_enviar = MensagemArquivo(texto_base, "documento_interativo.pdf", "app/pdf")
        else:
            print("\nTipo inválido. Enviando como texto simples.")
            mensagem_para_enviar = MensagemTexto(texto_base)
            
        # 4. Envia a Mensagem
        # Graças ao Polimorfismo, não importa qual canal ou qual mensagem
        # foi escolhida, o método .enviar() simplesmente funciona.
        try:
            canal_selecionado.enviar(mensagem_para_enviar, destinatario)
            print("--- Mensagem enviada com sucesso! --- \n")
        except Exception as e:
            print(f"Erro ao enviar: {e}\n")


# --- Ponto de entrada do script ---
# Bloco padrão para garantir que o script só rode quando executado diretamente
if __name__ == "__main__":
    
    # Loop para garantir que o usuário escolha 1 ou 2
    while True:
        print("Sistema de mensagens pronto.")
        print("-----")
        print("Pressione 1 para varrer o sistema (rodar testes).")
        print("-----")
        print("Pressione 2 para iniciar sem a varredura.")
        
        escolha_inicial = input("Sua escolha: ")
        
        if escolha_inicial == "1":
            # 1. Roda o teste automático primeiro
            rodar_demonstracao()
            
            # 2. Inicia o menu interativo
            menu_interativo()
            break # Sai do loop de inicialização
            
        elif escolha_inicial == "2":
            # 1. Pula os testes e vai direto para o menu
            menu_interativo()
            break # Sai do loop de inicialização
            
        else:
            print("\nOpção inválida! Pressione apenas '1' ou '2'.\n")
            # O loop vai repetir a pergunta