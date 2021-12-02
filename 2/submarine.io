Submarine := Object clone do(
	  horizontal := 0
	  depth := 0

	  value := method(message, message at(0) asString asNumber)

	  forward := method(
	  	  if(call message name == "forward", horizontal = horizontal + value(call message arguments)) 
		  if(call message name == "down", depth = depth + value(call message arguments))
		  if(call message name == "up", depth = depth - value(call message arguments))
	  )
)

s := File with(System args at(1)) openForReading contents
Submarine doString(s)
(Submarine horizontal * Submarine depth) println
