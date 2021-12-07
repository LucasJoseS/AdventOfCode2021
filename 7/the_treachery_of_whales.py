from sys import argv

_input = [ int(_str) for _str in open(argv[1]).readline().split(",") ]

_max = max(_input)
_min = min(_input)
fuel_costs = dict() #[go_to_pos] cost fuel

for go_to_pos in range(_min, _max):
    fuel_cost = 0
    
    for actual_pos in _input:
        fuel_cost += sum(range(abs(actual_pos - go_to_pos) + 1))

    fuel_costs[go_to_pos] = fuel_cost

print([ (key, value) for key, value in fuel_costs.items() if value == min(fuel_costs.values()) ])
