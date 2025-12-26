define judy = Character("Judy", color="#f5b7ff")
define p = Character("[player_name]", color="#c8ffc8")
define n = Character(None, what_color="#d0d0d0", window_tint=True)

init python:
    phone_channels = {}
    active_channel = None

    def create_channel(channel_id, display_name):
        if channel_id not in phone_channels:
            phone_channels[channel_id] = {"name": display_name, "messages": []}

    create_channel("mom_channel", "Мама")
    create_channel("judy_channel", "Judy")
    create_channel("friend_channel", "Друг")
    create_channel("celebrity_channel", "Знаменитость")
    create_channel("scientist_channel", "Учёный")
    create_channel("fan1_channel", "Фанатка1")
    create_channel("fan2_channel", "Фанатка2")

    def send_message(sender, text_or_image, channel_id, side="left", summary_alt=None):
        msg = {}
        if text_or_image.lower().endswith((".png", ".jpg", ".webp")):
            msg["image"] = text_or_image
            if summary_alt:
                msg["text"] = summary_alt
        else:
            msg["text"] = f"{sender}: {text_or_image}"
        msg["side"] = side
        phone_channels[channel_id]["messages"].append(msg)

    def show_phone_channel(channel_id):
        """Показать телефон сразу с выбранным каналом"""
        global active_channel
        active_channel = channel_id
        renpy.show_screen("phone_channel_view")

    def hide_phone_channel():
        renpy.hide_screen("phone_channel_view")

label start:
    show judy_neutral
    jump intro_01

label intro_01:
    scene bg blue
    with fade
    show judy neutral
    with dissolve

    judy "Привет."
    judy "Не волнуйся. Я здесь, чтобы немного помочь тебе разобраться."
    judy "История, в которую ты сейчас погружаешься, начинается с самого обычного парня."
    judy "Ему девятнадцать лет. Колледж, съёмная квартира, обычная жизнь."
    judy "По крайней мере… такой она была до сегодняшнего дня."
    judy "Но прежде чем мы продолжим, я должна знать, как тебя зовут."

    $ player_name = renpy.input("Введите имя главного героя:")
    $ player_name = player_name.strip() or "Марк"

    judy "Хорошо, [player_name]."
    judy "Запомни это имя. Оно ещё не раз прозвучит."

    jump intro_02

label intro_02:
    scene bg red
    with fade

    n "Я лежал на кровати и смотрел в потолок."
    n "Мысли снова и снова возвращались к Хлое."
    n "Интересно… что она сейчас думает обо всём этом?"

    # --- Сообщение от мамы ---
play sound "audio/phone_notification.mp3"
$ send_message("Мама", "Ты видел новости? Пожалуйста, ответь.", "mom_channel")
$ show_phone_channel("mom_channel")

n "Я потянулся к телефону и увидел сообщение от мамы."

$ hide_phone_channel()

pause 0.5
play sound "audio/phone_notification.mp3"
$ send_message("Мама", "Это не шутка. Мужчины пропадают.", "mom_channel")
$ show_phone_channel("mom_channel")

n "Что за бред? Похоже на розыгрыш."

$ hide_phone_channel()

pause 0.5
play sound "audio/phone_notification.mp3"
$ send_message("Мама", "Я волнуюсь за тебя.", "mom_channel")
$ show_phone_channel("mom_channel")

n "Никогда бы не подумал, что стану перепроверять подобную ерунду."

$ hide_phone_channel()

n "Надо собраться с мыслями и лечь спать"

jump intro_03

label intro_03:
    scene bg black
    with fade
