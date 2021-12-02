Submarine := Object clone do(
    horizontal := 0
    depth := 0
    aim := 0

    value := method(message, message at(0) asString asNumber)

	forward := method(
        if(call message name == "forward",
            horizontal = horizontal + value(call message arguments);
            depth = depth + aim * value(call message arguments))

        if(call message name == "down", aim = aim + value(call message arguments))

        if(call message name == "up", aim = aim - value(call message arguments))
    )
)

s := File with(System args at(1)) openForReading contents
Submarine doString(s)
(Submarine horizontal * Submarine depth) println
