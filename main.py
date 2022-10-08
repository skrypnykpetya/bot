import telebot
import config
import random
from telebot import types

NUMBER = 0

bot = telebot.TeleBot(config.TOKEN)

MESSAGE = "Enter a number from 1 to 100: "
INVALID_NUMBER = "Please enter a correct number"
CORRECT_GUESS_MESSAGE = "Congrats, you guess !!!"
LESS_MESSAGE = "number is less then NUMBER i wish"
GREAT_MESSAGE = "number is great then NUMBER i wish"
NEW_GAME_MESSAGE = "You want one more game ? OK let's do it "


@bot.message_handler(commands=["start"])
def welcome(message):
    global NUMBER
    NUMBER = random.randint(1, 100)
    print(NUMBER)
    bot.send_message(
        message.chat.id,
        "Hello, {0.first_name} {0.last_name}. \n"
        "I am a guess number bot.\n"
        "Try to guess number what i wish. \n"
        "GOOG LUCK !!!!".format(message.from_user)
    )

    bot.send_message(message.chat.id, MESSAGE)


@bot.message_handler(content_types=["text"])
def echo(message):
    global NUMBER

    if NUMBER == 0:
        return bot.send_message(message.chat.id, "To start new game enter command: /start")

    number = valid_number(message.text)
    if not number:
        return bot.send_message(message.chat.id, INVALID_NUMBER)
    text = check_number_guess(number)

    if text == CORRECT_GUESS_MESSAGE:
        NUMBER = 0

    bot.send_message(message.chat.id, text)


def check_number_guess(number: int):
    if number == NUMBER:
        return CORRECT_GUESS_MESSAGE
    elif number < NUMBER:
        return LESS_MESSAGE
    elif number > NUMBER:
        return GREAT_MESSAGE


def valid_number(number: str) -> int:
    if number.isnumeric():
        number = int(number)
        if 0 < number < 100:
            return number
    return 0


def main():
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()



