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
        }
    }
}
touchbit.on(touchbit.TouchPad.b, touchbit.TouchEvent.pressed, function () {
    if (true) {
    	
    }
})
input.onButtonPressed(Button.A, function () {
    Temp = "" + User_Key + "A"
    basic.showString("A")
    Password()
})
touchbit.on(touchbit.TouchPad.d, touchbit.TouchEvent.pressed, function () {
    if (true) {
    	
    }
})
input.onGesture(Gesture.TiltLeft, function () {
	
})
touchbit.on(touchbit.TouchPad.right, touchbit.TouchEvent.pressed, function () {
    if (true) {
    	
    }
})
touchbit.on(touchbit.TouchPad.left, touchbit.TouchEvent.pressed, function () {
    if (true) {
    	
    }
})
touchbit.on(touchbit.TouchPad.c, touchbit.TouchEvent.pressed, function () {
    if (true) {
    	
    }
})
input.onButtonPressed(Button.AB, function () {
	
})
input.onButtonPressed(Button.B, function () {
    Temp = "" + User_Key + "B"
    basic.showString("B")
    Password()
})
input.onGesture(Gesture.Shake, function () {
	
})
input.onGesture(Gesture.TiltRight, function () {
	
})
touchbit.on(touchbit.TouchPad.a, touchbit.TouchEvent.pressed, function () {
    if (true) {
    	
    }
})
input.onGesture(Gesture.ThreeG, function () {
	
})
let Temp = ""
let Lock = 0
let User_Key = ""
let Hand = ""
let Key = ""
radio.setGroup(1)
Key = "ABBA"
Hand = "BAAB"
User_Key = ""
Lock = 0
basic.forever(function () {
    if (Lock == 0) {
        led.toggle(0, 4)
        led.toggle(1, 4)
        led.toggle(2, 4)
        led.toggle(3, 4)
        basic.pause(200)
    }
})
