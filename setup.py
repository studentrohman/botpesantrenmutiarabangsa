# -*- coding: utf-8 -*-

# here we create the simplest possible bot
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']


import telebot

API_TOKEN = '1625321618:AAENq9YhPJOe-qkfRXVPHFz9dQWgvjEx2oA'
bot = telebot.TeleBot(API_TOKEN)


# Handle /start and /help
@bot.message_handler(commands=['mulai'])
def command_help(message):
    bot.reply_to(
        message,
        "Assalamualaikum wr wb, kenalin aku  santri senior Pesantren Mutiara bangsa.  coba ketik ngaji untuk melihat list ngaji di Pesantren Mutiara Bangsa"
    )


@bot.message_handler(regexp='mulai')
def command_help(message):
    bot.reply_to(
        message,
        "Assalamualaikum wr wb, kenalin aku  santri senior Pesantren Mutiara bangsa.  coba ketik ngaji untuk melihat list ngaji di Pesantren Mutiara Bangsa"
    )



@bot.message_handler(regexp='assalamualaikum')
def command_help(message):
    bot.reply_to(message, "Waalaikumussalam wr wb")
@bot.message_handler(regexp='salam')
def command_help(message):
    bot.reply_to(message, "Waalaikumussalam wr wb")


@bot.message_handler(regexp='ngaji')
def command_help(message):
    bot.reply_to(
        message,
        "santri dapat mengaji dipesantren Online lo, coba donwload dulu aplikasi androidnya di link pesantrenmutiarabangsa.com/aplikasi atau langsung ke website aku di pesantrenmutiarabangsa.com. ketika 'macam kitab' ngaji kamu akan mendapatkan pilihan ngajinya"
    )

@bot.message_handler(regexp='macam')
def command_help(message):
    bot.reply_to(
        message,
        "santri bisa belajar beberapa pelajaran pondok pesantren lo di di aplikasi kami coba pilih dibawah ini:1. fikih 2. akhlak 3. tasawuf 4. kisah nabi. pilih salah satu yak nanti aku kasih rekomendasi untuk belajarnya "
    )

@bot.message_handler(regexp='fikih')
def command_help(message):
    bot.reply_to(
        message,
        "mau belajar kitab fikih mnihajud tholibin bersama gus baha langsung klik link : https://pesantrenmutiarabangsa.com/courses/ngaji-minhajud-thalibin-bersama-gus-baha/, kalau kitab Syarifatullah bisa klik disini https://pesantrenmutiarabangsa.com/courses/ngaji-syariatullah-al-kholidah-bersama-gus-baha/"
    )


@bot.message_handler(regexp='tasawuf')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://pesantrenmutiarabangsa.com/courses/ngaji-al-hikam-bersama-gus-baha/"
    )


@bot.message_handler(regexp='akhlaq')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://pesantrenmutiarabangsa.com/courses/ngaji-al-hikam-bersama-gus-baha/"
    )


@bot.message_handler(regexp='akhlaq')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://pesantrenmutiarabangsa.com/courses/murattal-alquran-sheikh-abdulrahman-al-ossi/"
    )


@bot.message_handler(regexp='akhlak')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://pesantrenmutiarabangsa.com/courses/murattal-alquran-sheikh-abdulrahman-al-ossi/"
    )


@bot.message_handler(regexp='kisah nabi')
def command_help(message):
    bot.reply_to(
        message,
        "coba Klik link berikut untuk ngaji https://pesantrenmutiarabangsa.com/courses/shirah-nabi-muhammad-bersama-gusbaha/"
    )


@bot.message_handler(
    regexp='((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
def command_url(message):
    bot.reply_to(message, " Maaf  aku nggak bisa membuka link tersebut")


@bot.message_handler(regexp='seneng')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk")


@bot.message_handler(regexp='terima kasih')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk")


@bot.message_handler(regexp='mantab')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk")

@bot.message_handler(regexp='makasih')
def command_url(message):
    bot.reply_to(
        message,
        "terima kasih Banyak yakk, jangan lupa ikuti sosial media kita yakk")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "maaf yak,   saya belum paham yang kau maksd, coba tanyakan tentang ngaji insyaallah saya bisa memberikan rekomendasi")


# and here we actually run it
bot.polling()