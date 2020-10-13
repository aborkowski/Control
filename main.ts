function Password () {
    User_Key = Temp
    serial.writeLine("" + (User_Key))
    if (User_Key == Key || User_Key == Hand) {
        if (Lock == 0) {
            basic.showIcon(IconNames.Yes)
            basic.pause(200)
            basic.clearScreen()
            mode = 4
            radio.sendNumber(8)
        }
        basic.pause(100)
        Lock = 1
    } else if (User_Key.length > Key.length || User_Key.length > Hand.length) {
        if (Lock == 0) {
            basic.showIcon(IconNames.No)
            basic.pause(200)
            basic.clearScreen()
            User_Key = ""
            Temp = ""
            Count = Count + 1
            if (Count > Try) {
                control.waitMicros(25000)
                control.reset()
            }
        }
    }
}
touchbit.on(touchbit.TouchPad.b, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(2)
        if (mode == 1) {
            Mode_1 = 2
        } else if (mode == 2) {
            Mode_2 = 2
        } else if (mode == 3) {
            Mode_3 = 2
        } else if (mode == 4) {
            Mode_4 = 2
        }
        control.waitMicros(100)
        modes()
    }
})
function Button_B () {
    Temp = "" + User_Key + "B"
    basic.showString("B")
    basic.pause(100)
    basic.clearScreen()
    Password()
}
function Start () {
    radio.setGroup(1)
    Screen = 1
    Key = "ABBA"
    Hand = "BAAB"
    Try = 5
    User_Key = ""
    Lock = 0
    Temp = ""
    Waiting()
}
input.onButtonPressed(Button.A, function () {
    if (Lock == 0) {
        Button_A()
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (User_Key == Hand && Lock == 1) {
        radio.sendNumber(0)
    }
})
touchbit.on(touchbit.TouchPad.d, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(4)
        if (mode == 1) {
            Mode_1 = 4
        } else if (mode == 2) {
            Mode_2 = 4
        } else if (mode == 3) {
            Mode_3 = 4
        } else if (mode == 4) {
            Mode_4 = 4
        }
        control.waitMicros(100)
        modes()
    }
})
function Button_A () {
    Temp = "" + User_Key + "A"
    basic.showString("A")
    basic.pause(100)
    basic.clearScreen()
    Password()
}
input.onGesture(Gesture.TiltLeft, function () {
    if (User_Key == Hand && Lock == 1) {
        radio.sendNumber(0)
    }
})
input.onGesture(Gesture.ScreenUp, function () {
    if (User_Key == Hand && Lock == 1) {
        radio.sendNumber(0)
    }
})
touchbit.on(touchbit.TouchPad.right, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(6)
        mode = mode + 1
    }
})
touchbit.on(touchbit.TouchPad.left, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(5)
        mode = mode - 1
    }
})
input.onGesture(Gesture.ScreenDown, function () {
    if (User_Key == Hand && Lock == 1) {
        radio.sendNumber(0)
    }
})
touchbit.on(touchbit.TouchPad.c, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(3)
        if (mode == 1) {
            Mode_1 = 3
        } else if (mode == 2) {
            Mode_2 = 3
        } else if (mode == 3) {
            Mode_3 = 3
        } else if (mode == 4) {
            Mode_4 = 3
        }
        control.waitMicros(100)
        modes()
    }
})
input.onButtonPressed(Button.AB, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(7)
        if (mode == 4) {
            control.waitMicros(1000)
            Start()
        }
    }
})
function modes () {
    basic.clearScreen()
    if (mode == 1) {
        Screen = 0
        control.waitMicros(100)
        if (Mode_1 == 1) {
            for (let index = 0; index < 2; index++) {
                turtle.setPosition(2, 4)
                turtle.forward(2)
                turtle.turnLeft()
                turtle.forward(2)
                turtle.turnRight()
                basic.clearScreen()
            }
        } else if (Mode_1 == 2) {
            for (let index = 0; index < 2; index++) {
                turtle.setPosition(2, 4)
                turtle.forward(3)
                basic.clearScreen()
            }
        } else if (Mode_1 == 3) {
            basic.showLeds(`
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                `)
        } else if (Mode_1 == 4) {
            for (let index = 0; index < 2; index++) {
                turtle.setPosition(2, 4)
                turtle.forward(2)
                turtle.turnRight()
                turtle.forward(2)
                turtle.turnLeft()
                basic.clearScreen()
            }
        }
        control.waitMicros(100)
        Screen = 1
    } else if (mode == 2) {
        Screen = 0
        control.waitMicros(100)
        if (Mode_2 == 1) {
        	
        } else if (Mode_2 == 2) {
            for (let index = 0; index < 2; index++) {
                turtle.setPosition(2, 4)
                turtle.back(3)
                basic.clearScreen()
            }
        } else if (Mode_2 == 3) {
        	
        } else if (Mode_2 == 4) {
        	
        }
        control.waitMicros(100)
        Screen = 1
    } else if (mode == 3) {
        Screen = 0
        control.waitMicros(100)
        if (Mode_3 == 1) {
        	
        } else if (Mode_3 == 2) {
        	
        } else if (Mode_3 == 3) {
        	
        } else if (Mode_3 == 4) {
        	
        }
        control.waitMicros(100)
        Screen = 1
    } else if (mode == 4) {
        if (Mode_4 == 1) {
            mode = 1
        } else if (Mode_4 == 2) {
            mode = 2
        } else if (Mode_4 == 3) {
            mode = 3
        } else if (Mode_4 == 4) {
            mode = 4
        }
    }
}
input.onButtonPressed(Button.B, function () {
    if (Lock == 0) {
        Button_B()
    }
})
input.onGesture(Gesture.Shake, function () {
    if (User_Key == Hand && Lock == 1) {
        radio.sendNumber(7)
    }
})
input.onGesture(Gesture.TiltRight, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(0)
    }
})
input.onGesture(Gesture.LogoDown, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(0)
    }
})
touchbit.on(touchbit.TouchPad.a, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(1)
        if (mode == 1) {
            Mode_1 = 1
        } else if (mode == 2) {
            Mode_2 = 1
        } else if (mode == 3) {
            Mode_3 = 1
        } else if (mode == 4) {
            Mode_4 = 1
        }
        control.waitMicros(100)
        modes()
    }
})
input.onGesture(Gesture.ThreeG, function () {
    if (User_Key == Hand && Lock == 1) {
        radio.sendNumber(0)
    }
})
function Waiting () {
    if (Temp == "") {
        led.toggle(0, 4)
        if (Temp == "") {
            basic.pause(500)
            if (Temp == "") {
                basic.clearScreen()
                if (Temp == "") {
                    led.toggle(1, 4)
                    if (Temp == "") {
                        basic.pause(500)
                        if (Temp == "") {
                            basic.clearScreen()
                            if (Temp == "") {
                                led.toggle(2, 4)
                                if (Temp == "") {
                                    basic.pause(500)
                                    if (Temp == "") {
                                        basic.clearScreen()
                                        if (Temp == "") {
                                            led.toggle(3, 4)
                                            if (Temp == "") {
                                                basic.pause(500)
                                                if (Temp == "") {
                                                    basic.clearScreen()
                                                    if (Temp == "") {
                                                        led.toggle(4, 4)
                                                        if (Temp == "") {
                                                            basic.pause(500)
                                                            if (Temp == "") {
                                                                basic.clearScreen()
                                                                if (Temp == "") {
                                                                    Waiting()
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
let Screen = 0
let Mode_4 = 0
let Mode_3 = 0
let Mode_2 = 0
let Mode_1 = 0
let Try = 0
let Count = 0
let mode = 0
let Lock = 0
let Hand = ""
let Key = ""
let Temp = ""
let User_Key = ""
Start()
led.setBrightness(255)
basic.forever(function () {
    while (Lock == 1) {
        while (Screen == 1) {
            basic.showNumber(mode)
            if (mode < 1) {
                mode = 4
            } else if (mode > 4) {
                mode = 1
            }
        }
    }
})
