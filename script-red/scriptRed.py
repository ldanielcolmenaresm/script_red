#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import telebot
import os
import locale
import smtplib
import datetime

hora = datetime.datetime.now()
hora = hora.strftime('%H:%M  %d|%m|%Y')

bot = telebot.TeleBot("1905982141:xxxxxxxxxx-xxxxxxxx") # id bot telegram

cid = 99999999 # numero id asociado al telegram

time.sleep(2)

with open("/home/dc/tools/red_bot/device_home.txt") as devi:
    device = set(devi.readlines())

with open("/home/dc/tools/red_bot/device_oth.txt") as temp:
    tempo = set(temp.readlines())

resto = tempo-device
resto_len = len(resto)

if resto_len == 0:
    print ('🟢🔐 No hay diferencias 🔐 ✅\n',hora)
    #  msj0 = ('🟢No hay diferencias✅\n\n   🔐 Red Segura! 🔐\n\n' + hora)
    #  bot.send_message(cid, msj0)
# bot.send_message(cid, '✅ No hay intrusos')

else:

    time = "".join(hora)

    text = "".join(resto)
    msj = ('\n🚨 ⚠️INTRUSOS⚠️ 🚨 \n\n  --> ' + hora + '\n\nDispositivos desconocidos:\n\n' + text + '----------------------------\n\n')
    print(msj)
    # print (mensaje)
    bot.send_message(cid, msj)

    # send Email
    messageMail = '----->> !! INTRUSOS !! <<-----\n\nDISPOSITIVOS DESCONOCIDOS:\n\n' + text + '\n\n' + hora
    subject = '!!ALERTA!! Nuevo dispositivo conectado a la red'
    messageMail = 'Subject: {}\n\n{}'.format(subject, messageMail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('correo@gmail.com','contrasenia ****')
    server.sendmail('correosalida@gmail.com','correoRecibido@gmail.com', messageMail)
    server.quit()
    print("🔴-------------------------------------------------------🔴\n Se ha enviado un correo con los dispositivos sospechosos")

    file = open('seguimiento.log', 'a')
    file.write(msj)
    file.close()

