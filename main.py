def on_gesture_tilt_right():
    if User_Key == Key and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def Password():
    global User_Key, Lock, Temp, Count
    User_Key = Temp
    serial.write_line(User_Key)
    if User_Key == Key or User_Key == Hand:
        if Lock == 0:
            basic.show_icon(IconNames.YES)
            basic.pause(200)
            basic.clear_screen()
            music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
            radio.send_number(8)
        basic.pause(100)
        Lock = 1
    elif len(User_Key) > len(Key) or len(User_Key) > len(Hand):
        if Lock == 0:
            basic.show_icon(IconNames.NO)
            basic.pause(200)
            basic.clear_screen()
            music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
                MelodyOptions.ONCE)
            User_Key = ""
            Temp = ""
            Count = Count + 1
            if Count > Try:
                control.wait_micros(25000)
                control.reset()

def my_function():
    if User_Key == Key and Lock == 1:
        radio.send_number(2)
touchbit.on(touchbit.TouchPad.B,
    touchbit.TouchEvent.PRESSED,
    my_function)

def on_gesture_tilt_left():
    if User_Key == Hand and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    if User_Key == Hand and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def Button_B():
    global Temp
    Temp = "" + User_Key + "B"
    basic.show_string("B")
    basic.pause(100)
    basic.clear_screen()
    Password()
def Start():
    global Key, Hand, Try, User_Key, Lock, Temp
    radio.set_group(1)
    Key = "ABBA"
    Hand = "BAAB"
    Try = 5
    User_Key = ""
    Lock = 0
    Temp = ""
    Waiting()

def on_gesture_logo_up():
    if User_Key == Hand and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_a():
    if Lock == 0:
        Button_A()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    if User_Key == Hand and Lock == 1:
        radio.send_number(7)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def my_function2():
    if User_Key == Key and Lock == 1:
        radio.send_number(4)
touchbit.on(touchbit.TouchPad.D,
    touchbit.TouchEvent.PRESSED,
    my_function2)

def Button_A():
    global Temp
    Temp = "" + User_Key + "A"
    basic.show_string("A")
    basic.pause(100)
    basic.clear_screen()
    Password()

def my_function3():
    if User_Key == Key and Lock == 1:
        radio.send_number(6)
touchbit.on(touchbit.TouchPad.RIGHT,
    touchbit.TouchEvent.PRESSED,
    my_function3)

def my_function4():
    if User_Key == Key and Lock == 1:
        radio.send_number(5)
touchbit.on(touchbit.TouchPad.LEFT,
    touchbit.TouchEvent.PRESSED,
    my_function4)

def on_gesture_screen_down():
    if User_Key == Hand and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_logo_down():
    if User_Key == Key and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def my_function5():
    if User_Key == Key and Lock == 1:
        radio.send_number(3)
touchbit.on(touchbit.TouchPad.C,
    touchbit.TouchEvent.PRESSED,
    my_function5)

def on_button_pressed_ab():
    if User_Key == Key and Lock == 1:
        radio.send_number(7)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if Lock == 0:
        Button_B()
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function6():
    if User_Key == Key and Lock == 1:
        radio.send_number(1)
touchbit.on(touchbit.TouchPad.A,
    touchbit.TouchEvent.PRESSED,
    my_function6)

def on_gesture_three_g():
    if User_Key == Hand and Lock == 1:
        radio.send_number(0)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def Waiting():
    if Temp == "":
        led.toggle(0, 4)
        if Temp == "":
            basic.pause(500)
            if Temp == "":
                basic.clear_screen()
                if Temp == "":
                    led.toggle(1, 4)
                    if Temp == "":
                        basic.pause(500)
                        if Temp == "":
                            basic.clear_screen()
                            if Temp == "":
                                led.toggle(2, 4)
                                if Temp == "":
                                    basic.pause(500)
                                    if Temp == "":
                                        basic.clear_screen()
                                        if Temp == "":
                                            led.toggle(3, 4)
                                            if Temp == "":
                                                basic.pause(500)
                                                if Temp == "":
                                                    basic.clear_screen()
                                                    if Temp == "":
                                                        led.toggle(4, 4)
                                                        if Temp == "":
                                                            basic.pause(500)
                                                            if Temp == "":
                                                                basic.clear_screen()
                                                                if Temp == "":
                                                                    Waiting()
Try = 0
Count = 0
Hand = ""
Temp = ""
Lock = 0
Key = ""
User_Key = ""
Start()