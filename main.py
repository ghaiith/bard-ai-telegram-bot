import google.generativeai as palm
import telebot

TOKEN = '6398171667:AAF_vYASuarTjlvgJQpfZjKuBv14ghTw-LI'
palm.configure(api_key="AIzaSyBVvIdH4sMIWbAH3aIXKaMtBYJeUti--qQ")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Hello {name}! Ask me About anything")


@bot.message_handler(func=lambda message: True)
def handle_search_product(message):
    name = message.from_user.first_name
    msg = message.text
    if msg == "":
        bot.reply_to(message, "Sorry, You mustn't write a empty message")
    try:
        bot.reply_to(message, f"Wait a Seconds {name} before send another message")
        defaults = {
            'model': 'models/chat-bison-001',
            'temperature': 0.25,
            'candidate_count': 1,
            'top_k': 40,
            'top_p': 0.95,
        }
        context = ""
        examples = [
            [
                " ",

            ]

        ]
        examples[0].append(str(msg))
        messages = []
        messages.append("NEXT REQUEST")
        response = palm.chat(
            **defaults,
            context=context,
            examples=examples,
            messages=messages
        )
        bot.reply_to(message, response.last)
    except Exception as e:
        bot.reply_to(message, "Sorry, an error occurred while processing your request.")


if __name__ == "__main__":
    bot.polling()

