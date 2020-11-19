def Password():
    global User_Key, mode, Button_lock, Lock, Count
    User_Key = Temp
    serial.write_line("" + (User_Key))
    if User_Key == Key or User_Key == Hand:
        if Lock == 0:
            basic.show_icon(IconNames.YES)
            basic.pause(200)
            basic.clear_screen()
            mode = 4
            Button_lock = 1
            radio.send_number(8)
            basic.show_number(mode)
            basic.pause(100)
            Lock = 1
    elif (User_Key != Key or User_Key != Hand) and Unlock == 4:
        if Lock == 0:
            basic.show_icon(IconNames.NO)
            basic.pause(200)
            basic.clear_screen()
            Start()
            Count = Count + 1
            if Count > Try:
                control.wait_micros(250000)
                control.reset()

def my_function():
    global Mode_1, Mode_2, Mode_3, Mode_4, Mode_5, Mode_6
    if User_Key == Key and Lock == 1:
        radio.send_number(2)
        if mode == 1:
            Mode_1 = 2
        elif mode == 2:
            Mode_2 = 2
        elif mode == 3:
            Mode_3 = 2
        elif mode == 4:
            Mode_4 = 2
        elif mode == 5:
            Mode_5 = 2
        elif mode == 6:
            Mode_6 = 2
        control.wait_micros(100)
        modes()
touchbit.on(touchbit.TouchPad.B,
    touchbit.TouchEvent.PRESSED,
    my_function)

def Start():
    global Button_lock, Unlock, Screen, Speed, Key, Hand, Try, User_Key, Lock, Temp
    basic.clear_screen()
    radio.set_group(1)
    Button_lock = 0
    Unlock = 0
    Screen = 1
    Speed = 30
    Key = "ABBA"
    Hand = "BAAB"
    Try = 5
    User_Key = ""
    Lock = 0
    Temp = ""

def on_button_pressed_a():
    global Temp, Unlock
    if Lock == 0:
        Temp = "" + User_Key + "A"
        Unlock = Unlock + 1
        basic.show_string("A")
        basic.pause(100)
        basic.clear_screen()
        Password()
input.on_button_pressed(Button.A, on_button_pressed_a)

def my_function2():
    global Mode_1, Mode_2, Mode_3, Mode_4, Mode_5, Mode_6
    if User_Key == Key and Lock == 1:
        radio.send_number(4)
        if mode == 1:
            Mode_1 = 4
        elif mode == 2:
            Mode_2 = 4
        elif mode == 3:
            Mode_3 = 4
        elif mode == 4:
            Mode_4 = 4
        elif mode == 5:
            Mode_5 = 4
        elif mode == 6:
            Mode_6 = 4
        control.wait_micros(100)
        modes()
touchbit.on(touchbit.TouchPad.D,
    touchbit.TouchEvent.PRESSED,
    my_function2)

def Waiting2():
    if Temp == "":
        led.toggle(0, 4)
        if Temp == "":
            basic.pause(500)
            if Temp == "":
                if Temp == "":
                    led.toggle(1, 4)
                    if Temp == "":
                        basic.pause(500)
                        if Temp == "":
                            if Temp == "":
                                led.toggle(2, 4)
                                if Temp == "":
                                    basic.pause(500)
                                    if Temp == "":
                                        if Temp == "":
                                            led.toggle(3, 4)
                                            if Temp == "":
                                                basic.pause(500)
                                                if Temp == "":
                                                    led.toggle(4, 4)
                                                    if Temp == "":
                                                        basic.pause(500)
                                                        if Temp == "":
                                                            basic.clear_screen()
                                                            if Temp == "":
                                                                basic.pause(500)
                                                                if Temp == "":
                                                                    Waiting2()

def my_function3():
    global mode
    if User_Key == Key and Lock == 1:
        radio.send_number(6)
        mode = mode + 1
        if mode < 1:
            mode = 6
        elif mode > 6:
            mode = 1
        basic.show_number(mode)
touchbit.on(touchbit.TouchPad.RIGHT,
    touchbit.TouchEvent.PRESSED,
    my_function3)

def my_function4():
    global mode
    if User_Key == Key and Lock == 1:
        radio.send_number(5)
        mode = mode - 1
        if mode < 1:
            mode = 6
        elif mode > 6:
            mode = 1
        basic.show_number(mode)
touchbit.on(touchbit.TouchPad.LEFT,
    touchbit.TouchEvent.PRESSED,
    my_function4)

def my_function5():
    global Mode_1, Mode_2, Mode_3, Mode_4, Mode_5, Mode_6
    if User_Key == Key and Lock == 1:
        radio.send_number(3)
        if mode == 1:
            Mode_1 = 3
        elif mode == 2:
            Mode_2 = 3
        elif mode == 3:
            Mode_3 = 3
        elif mode == 4:
            Mode_4 = 3
        elif mode == 5:
            Mode_5 = 3
        elif mode == 6:
            Mode_6 = 3
        control.wait_micros(100)
        modes()
touchbit.on(touchbit.TouchPad.C,
    touchbit.TouchEvent.PRESSED,
    my_function5)

def on_button_pressed_ab():
    global Speed
    if Lock == 1 and Key == User_Key:
        radio.send_number(7)
        if mode == 1:
            basic.clear_screen()
            Speed = Speed + 10
            basic.show_number(Speed)
        elif mode == 2:
            basic.clear_screen()
            Speed = Speed - 10
            basic.show_number(Speed)
        elif mode == 3:
            basic.clear_screen()
            Speed = Speed + 10
            basic.show_number(Speed)
        elif mode == 4:
            control.wait_micros(100)
            Start()
        elif mode == 5:
            pass
        elif mode == 6:
            pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def modes():
    global mode
    basic.clear_screen()
    control.wait_micros(100)
    if mode == 1:
        if Mode_1 == 1:
            for index in range(2):
                turtle.set_position(2, 4)
                turtle.forward(2)
                turtle.turn_left()
                turtle.forward(2)
                turtle.turn_right()
                basic.clear_screen()
        elif Mode_1 == 2:
            for index2 in range(2):
                turtle.set_position(2, 4)
                turtle.forward(4)
                basic.clear_screen()
        elif Mode_1 == 3:
            basic.show_leds("""
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                """)
        elif Mode_1 == 4:
            for index3 in range(2):
                turtle.set_position(2, 4)
                turtle.forward(2)
                turtle.turn_right()
                turtle.forward(2)
                turtle.turn_left()
                basic.clear_screen()
        elif Mode_1 == 5:
            pass
        elif Mode_1 == 6:
            pass
    elif mode == 2:
        if Mode_2 == 1:
            for index4 in range(2):
                turtle.set_position(2, 0)
                turtle.back(2)
                turtle.turn_right()
                turtle.back(2)
                turtle.turn_left()
                basic.clear_screen()
        elif Mode_2 == 2:
            for index5 in range(2):
                turtle.set_position(2, 0)
                turtle.back(4)
                basic.clear_screen()
        elif Mode_2 == 3:
            basic.show_leds("""
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                """)
        elif Mode_2 == 4:
            for index6 in range(2):
                turtle.set_position(2, 0)
                turtle.back(2)
                turtle.turn_left()
                turtle.back(2)
                turtle.turn_right()
                basic.clear_screen()
        elif Mode_2 == 5:
            pass
        elif Mode_2 == 6:
            pass
    elif mode == 3:
        if Mode_3 == 1:
            pass
        elif Mode_3 == 2:
            pass
        elif Mode_3 == 3:
            basic.show_leds("""
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                """)
        elif Mode_3 == 4:
            pass
        elif Mode_3 == 5:
            pass
        elif Mode_3 == 6:
            pass
    elif mode == 4:
        if Mode_4 == 1:
            mode = 1
        elif Mode_4 == 2:
            mode = 2
        elif Mode_4 == 3:
            mode = 3
        elif Mode_4 == 4:
            mode = 4
        elif Mode_4 == 5:
            mode = 5
        elif Mode_4 == 6:
            mode = 6
    control.wait_micros(100)
    basic.show_number(mode)

def on_button_pressed_b():
    global Temp, Unlock
    if Lock == 0:
        Temp = "" + User_Key + "B"
        Unlock = Unlock + 1
        basic.show_string("B")
        basic.pause(100)
        basic.clear_screen()
        Password()
input.on_button_pressed(Button.B, on_button_pressed_b)

def my_function6():
    global Mode_1, Mode_2, Mode_3, Mode_4, Mode_5, Mode_6
    if User_Key == Key and Lock == 1:
        radio.send_number(1)
        if mode == 1:
            Mode_1 = 1
        elif mode == 2:
            Mode_2 = 1
        elif mode == 3:
            Mode_3 = 1
        elif mode == 4:
            Mode_4 = 1
        elif mode == 5:
            Mode_5 = 1
        elif mode == 6:
            Mode_6 = 1
        control.wait_micros(100)
        modes()
touchbit.on(touchbit.TouchPad.A,
    touchbit.TouchEvent.PRESSED,
    my_function6)

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
Speed = 0
Screen = 0
Mode_6 = 0
Mode_5 = 0
Mode_4 = 0
Mode_3 = 0
Mode_2 = 0
Mode_1 = 0
Try = 0
Count = 0
Button_lock = 0
mode = 0
Lock = 0
Unlock = 0
Hand = ""
Key = ""
Temp = ""
User_Key = ""
basic.clear_screen()
Waiting2()
Start()
led.set_brightness(255)

def on_forever():
    global Speed, mode, Mode_1, Mode_2, Mode_3, Mode_4, Mode_5, Mode_6
    if Lock == 1 and Hand == User_Key:
        if input.is_gesture(Gesture.SHAKE):
            radio.send_number(7)
            if mode == 1:
                basic.clear_screen()
                Speed = Speed + 10
                basic.show_number(Speed)
            elif mode == 2:
                basic.clear_screen()
                Speed = Speed - 10
                basic.show_number(Speed)
            elif mode == 3:
                basic.clear_screen()
                Speed = Speed + 10
                basic.show_number(Speed)
            elif mode == 4:
                control.wait_micros(100)
                Start()
            elif mode == 5:
                pass
            elif mode == 6:
                pass
        elif input.is_gesture(Gesture.TILT_RIGHT):
            radio.send_number(6)
            mode = mode + 1
            if mode < 1:
                mode = 6
            elif mode > 6:
                mode = 1
            basic.show_number(mode)
        elif input.is_gesture(Gesture.TILT_LEFT):
            radio.send_number(5)
            mode = mode - 1
            if mode < 1:
                mode = 6
            elif mode > 6:
                mode = 1
            basic.show_number(mode)
        elif input.is_gesture(Gesture.SCREEN_DOWN):
            radio.send_number(1)
            if mode == 1:
                Mode_1 = 1
            elif mode == 2:
                Mode_2 = 1
            elif mode == 3:
                Mode_3 = 1
            elif mode == 4:
                Mode_4 = 1
            elif mode == 5:
                Mode_5 = 1
            elif mode == 6:
                Mode_6 = 1
            control.wait_micros(100)
            modes()
        elif input.is_gesture(Gesture.SCREEN_UP):
            radio.send_number(4)
            if mode == 1:
                Mode_1 = 4
            elif mode == 2:
                Mode_2 = 4
            elif mode == 3:
                Mode_3 = 4
            elif mode == 4:
                Mode_4 = 4
            elif mode == 5:
                Mode_5 = 4
            elif mode == 6:
                Mode_6 = 4
            control.wait_micros(100)
            modes()
        elif input.is_gesture(Gesture.LOGO_UP):
            radio.send_number(3)
            if mode == 1:
                Mode_1 = 3
            elif mode == 2:
                Mode_2 = 3
            elif mode == 3:
                Mode_3 = 3
            elif mode == 4:
                Mode_4 = 3
            elif mode == 5:
                Mode_5 = 3
            elif mode == 6:
                Mode_6 = 3
            control.wait_micros(100)
            modes()
        elif input.is_gesture(Gesture.LOGO_DOWN):
            radio.send_number(2)
            if mode == 1:
                Mode_1 = 2
            elif mode == 2:
                Mode_2 = 2
            elif mode == 3:
                Mode_3 = 2
            elif mode == 4:
                Mode_4 = 2
            elif mode == 5:
                Mode_5 = 2
            elif mode == 6:
                Mode_6 = 2
            control.wait_micros(100)
            modes()
basic.forever(on_forever)

def on_forever2():
    global Speed
    if Speed > 100:
        Speed = 30
    elif Speed < 30:
        Speed = 100
basic.forever(on_forever2)
