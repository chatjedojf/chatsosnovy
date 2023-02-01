import os
import openai
import telebot

openai.api_key = ("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")
bot = telebot.TeleBot("6120320046:AAFBt8ElUXNnXuxkxd_aKqCjNaEnRQh9w6g")

@bot.message_handler(func=lambda _: True)
def handle_message(message):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message.text,
  temperature=0.5,
  max_tokens=3500,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
)
  bot.send_message (chat_id=message.from_user.id,  text=response["choices"][0]["text"])

bot.polling()

