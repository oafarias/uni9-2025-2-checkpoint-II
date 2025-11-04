# **Uni9 \- Checkpoint II \- Estrutura de Mensagens POO**

Este repositório contém a solução para o Checkpoint II da disciplina de Programação Orientada a Objetos.

**Autor:**

$$Seu Nome Aqui$$

Repositório: https://github.com/oafarias/uni9-2025-2-checkpoint-II

## **1\. Problema**

O desafio consiste em criar uma estrutura de código com orientação a objetos capaz de enviar mensagens em diferentes formatos (texto, vídeo, foto, arquivo) para diversos canais de comunicação (WhatsApp, Telegram, Facebook, Instagram), respeitando os diferentes tipos de destinatários que cada canal aceita (Número de Telefone ou Usuário).

## **2\. Solução e Conceitos de POO**

A solução foi implementada em **Python** e dividida em módulos para organizar as responsabilidades, aplicando os conceitos fundamentais de POO solicitados:

### **Herança**

O conceito de herança é a base da estrutura de mensagens.py:

* Uma classe base abstrata Mensagem define o contrato inicial.  
* A classe MensagemComArquivo herda de Mensagem e adiciona atributos comuns a mídias (arquivo, formato).  
* As classes MensagemFoto, MensagemVideo e MensagemArquivo herdam de MensagemComArquivo, cada uma implementando seu comportamento específico (como a duracao no vídeo).  
* MensagemTexto herda diretamente de Mensagem.

### **Encapsulamento**

Todos os atributos das classes são "protegidos" (por convenção em Python, prefixados com \_, como \_mensagem\_base). Isso significa que eles não devem ser acessados ou modificados diretamente de fora da classe, protegendo o estado interno dos objetos.

### **Polimorfismo**

O polimorfismo é aplicado de duas formas centrais:

1. **Nos Canais (canais.py):** Uma "interface" (Classe Base Abstrata) ICanal define um método enviar(). Todas as classes de canal (WhatsApp, Telegram, Facebook, Instagram) implementam este método. Isso permite que o código principal (main.py) chame canal.enviar() sem precisar saber qual é o tipo específico de canal, como demonstrado no loop final do main.py.  
2. **Nas Mensagens (mensagens.py):** A classe base Mensagem define uma propriedade abstrata conteudo. Cada classe filha (MensagemTexto, MensagemVideo, etc.) implementa essa propriedade de forma diferente para se formatar corretamente. Quando o canal chama mensagem.conteudo, ele renderiza a mensagem correta (seja um texto simples ou uma estrutura de vídeo) sem que o canal precise saber o tipo de mensagem.

## **3\. Estrutura de Arquivos**

* mensagens.py: Contém todas as classes de Mensagem (Base, Texto, Foto, Vídeo, Arquivo).  
* canais.py: Contém a interface ICanal e as implementações de cada canal (WhatsApp, Telegram, etc.).  
* main.py: Script principal que importa as classes, cria instâncias e executa a demonstração de envio, provando que a estrutura funciona.

## **4\. Como Executar**

O projeto utiliza apenas bibliotecas padrão do Python, não sendo necessária a instalação de dependências.

1. Clone este repositório:  
   git clone \[https://github.com/oafarias/uni9-2025-2-checkpoint-II.git\](https://github.com/oafarias/uni9-2025-2-checkpoint-II.git)  
   cd uni9-2025-2-checkpoint-II

2. Execute o arquivo main.py para rodar a demonstração:  
   python main.py

O terminal exibirá a saída de todas as simulações de envio, demonstrando os diferentes canais e formatos de mensagem em ação.