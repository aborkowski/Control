input.onGesture(Gesture.TiltRight, function () {
    if (User_Key == Key && Lock == 1) {
    	
    }
})
function Password () {
    User_Key = Temp
    serial.writeLine(User_Key)
    if (User_Key == Key || User_Key == Hand) {
        if (Lock == 0) {
            basic.showIcon(IconNames.Yes)
            basic.pause(200)
            basic.clearScreen()
            radio.sendNumber(9)
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
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    if (User_Key == Hand && Lock == 1) {
    	
    }
})
input.onGesture(Gesture.ScreenUp, function () {
    if (User_Key == Hand && Lock == 1) {
    	
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (User_Key == Hand && Lock == 1) {
    	
    }
})
input.onButtonPressed(Button.A, function () {
    if (Lock == 0) {
        Temp = "" + User_Key + "A"
        basic.showString("A")
        basic.pause(1000)
        basic.clearScreen()
        Password()
    }
})
input.onGesture(Gesture.Shake, function () {
    if ((User_Key == Key || User_Key == Hand) && Lock == 1) {
        radio.sendNumber(8)
    }
})
touchbit.on(touchbit.TouchPad.d, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(4)
    }
})
touchbit.on(touchbit.TouchPad.right, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(6)
    }
})
touchbit.on(touchbit.TouchPad.left, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(5)
    }
})
input.onGesture(Gesture.ScreenDown, function () {
    if (User_Key == Hand && Lock == 1) {
    	
    }
})
input.onGesture(Gesture.LogoDown, function () {
    if (User_Key == Key && Lock == 1) {
    	
    }
})
touchbit.on(touchbit.TouchPad.c, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(3)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(7)
    }
})
input.onButtonPressed(Button.B, function () {
    if (Lock == 0) {
        Temp = "" + User_Key + "B"
        basic.showString("B")
        basic.pause(1000)
        basic.clearScreen()
        Password()
    }
})
touchbit.on(touchbit.TouchPad.a, touchbit.TouchEvent.pressed, function () {
    if (User_Key == Key && Lock == 1) {
        radio.sendNumber(1)
    }
})
input.onGesture(Gesture.ThreeG, function () {
    if (User_Key == Hand && Lock == 1) {
    	
    }
})
let Count = 0
let Temp = ""
let Lock = 0
let User_Key = ""
let Try = 0
let Hand = ""
let Key = ""
radio.setGroup(1)
Key = "ABBA"
Hand = "BAAB"
Try = 5
User_Key = ""
Lock = 0
Temp = ""
basic.forever(function () {
    if (Temp == "") {
        led.toggle(0, 4)
        basic.pause(500)
        basic.clearScreen()
        led.toggle(1, 4)
        basic.pause(500)
        basic.clearScreen()
        led.toggle(2, 4)
        basic.pause(500)
        basic.clearScreen()
        led.toggle(3, 4)
        basic.pause(500)
        basic.clearScreen()
        led.toggle(4, 4)
        basic.pause(500)
        basic.clearScreen()
    }
})
