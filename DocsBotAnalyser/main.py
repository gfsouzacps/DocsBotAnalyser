from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6322969440:AAHQTqMrKDdD3BdnaXmfS75DHVgYDMXWRps'
BOT_USERNAME: Final = '@DocsAnalyserBot'


# Commands - Funcoes que podem ser chamadas pelo bot utilizando "/nome_do_comando". Cada comando deve ser registrado
# no Telegram, utilizando o command "/setcommands" no BotFather
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o Optimus, seu bot de analise de documentos!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o Optimus, seu bot de analise de documentos! Por favor, diga-me o "
                                    "que precisa.")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o Optimus, seu bot de analise de documentos! Esse é o comando "
                                    "customizado.")


# Responses - Diferente das funcoes, o handle_response analisa o texto recebido e gera uma resposta

def handle_response(text: str) -> str:
    lower: str = text.lower()

    if 'olá' in lower:
        return 'Olá, seja bem vindo!'

    if 'oi' in lower:
        return 'Olá, seja bem vindo!'

    if 'como vai voce?' in lower:
        return 'Eu estou bem, obrigado!'

    return 'Eu nao entendi oq que você escreveu'


# Verifica se a mensagem e de um grupo, remove o nome de usuario do bot caso exista e gera uma resposta.
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'O update {update} causou um erro {context.error}')


if __name__ == '__main__':
    print('Bot sendo iniciado')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Intervalo de leitura de texto
    print('Intervalo de leitura...')
    app.run_polling(poll_interval=3)
