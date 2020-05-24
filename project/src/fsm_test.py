from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    slowdown = green.to(yellow)
    stop = yellow.to(red)
    go = red.to(green)


traffic_light = TrafficLightMachine()
print(traffic_light.current_state)
for i in range(100):
    traffic_light.slowdown()
    print(traffic_light.current_state)
    traffic_light.stop()
    print(traffic_light.current_state)
    traffic_light.go()
    print(traffic_light.current_state)