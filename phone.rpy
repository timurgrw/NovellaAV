# --- phone.rpy ---

default phone_unlocked = True
default active_channel = None

image phone_bg = "phone_bg.webp"

# --- Экран списка каналов ---
screen phone_hub():
    modal False
    zorder 100
    add "phone_bg" xalign 0.5 yalign 0.5

    frame:
        xalign 0.5
        yalign 0.5
        xsize 435
        ysize 675
        background None

        viewport:
            draggable True
            mousewheel True
            vbox:
                spacing 8
                for channel_id, channel in phone_channels.items():
                    if channel["messages"]:
                        textbutton channel["name"]:
                            style "phone_channel_button"
                            action [
                                SetVariable("active_channel", channel_id),
                                Show("phone_channel_view")
                            ]

# --- Экран сообщений канала ---
screen phone_channel_view():
    modal False
    zorder 110
    add "phone_bg" xalign 0.5 yalign 0.5

    frame:
        xalign 0.5
        yalign 0.5
        xsize 250
        ysize 400
        background None

        viewport:
            id "phone_messages_vp"
            draggable True
            mousewheel True
            yinitial 1.0   # <<< автоскролл вниз
            vbox:
                spacing 6
                for msg in phone_channels[active_channel]["messages"]:
                    if "image" in msg:
                        add msg["image"]
                    else:
                        if msg.get("side", "left") == "left":
                            text wrap_text(msg["text"], 32) style "phone_message_left"
                        else:
                            text wrap_text(msg["text"], 32) style "phone_message_right"

# --- HUD ---
screen hud():
    if phone_unlocked:
        imagebutton:
            idle "phone_icon.webp"
            hover "phone_icon_hover.webp"
            xpos 1820
            ypos 40
            action Show("phone_hub")

# --- Стили ---
style phone_channel_button:
    size 16
    color "#ffffff"
    xalign 0.0

style phone_message_left:
    size 14
    color "#ffffff"
    xalign 0.0
    italic True
    bold True

style phone_message_right:
    size 14
    color "#a8ffb0"
    xalign 1.0
    italic True
    bold True

# --- Python ---
init python:
    import textwrap

    def wrap_text(text, max_chars):
        return "\n".join(textwrap.wrap(text, max_chars))
