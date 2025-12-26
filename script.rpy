
# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define judy = Character("Judy", color="#f5b7ff")
define p = Character("[player_name]", color="#c8ffc8")
define n = Character(None, what_color="#d0d0d0", window_tint=True) #внутренний монолог

#SAMURAI-BLUE SAMURAI-BW SAMURAI-RED


label start:

    show judy_neutral

    jump intro_01


label intro_01:

    scene bg blue
    with fade

    # Появляется Judy
    show judy neutral
    with dissolve

    judy "Привет."
    judy "Не волнуйся. Я здесь, чтобы немного помочь тебе разобраться."

    judy "История, в которую ты сейчас погружаешься, начинается с самого обычного парня."
    judy "Ему девятнадцать лет. Колледж, съёмная квартира, обычная жизнь."

    judy "По крайней мере… такой она была до сегодняшнего дня."

    judy "Но прежде чем мы продолжим, я должна знать, как тебя зовут."

    # Запрос имени
    $ player_name = renpy.input("Введите имя главного героя:")
    $ player_name = player_name.strip() or "Марк"

    judy "Хорошо, [player_name]."
    judy "Запомни это имя. Оно ещё не раз прозвучит."

    jump intro_02

label intro_02:

    # Фон комнаты
    scene bg red
    with fade

    # Внутренний монолог
    n "Я лежал на кровати и смотрел в потолок."
    n "Мысли снова и снова возвращались к Хлое."

    n "Мы знакомы уже давно."
    n "Она всегда была рядом, даже когда я этого не замечал."

    n "Интересно… что она сейчас думает обо всём этом?"

    # Звук уведомления
    play sound "phone_notification.mp3"

    n "Телефон завибрировал."

    # Сообщения появляются по очереди
    n "Мама: Ты видел новости? Пожалуйста, ответь."

    play sound "phone_notification.mp3"
    pause 0.4

    n "Мама: Это не шутка. Мужчины пропадают."

    play sound "phone_notification.mp3"
    pause 0.4

    n "Мама: Я волнуюсь за тебя."

    n "Я медленно вытащил телефон из кармана и уставился в экран."

    jump intro_03
