from matplotlib import pyplot as plt

racer1_v = 4.0
racer1_a = 0.01
racer1_vel = []

racer2_v = 2.0
racer2_a = 0.02
racer2_vel = []

frame_list = []

for i in range(0, 551):
    frame_list.append(i)


v1 = 0
v2 = 0

for t in range(len(frame_list)):
    # Acceleration Stage
    if v1 < racer1_v:
        v1 = racer1_a * t
        racer1_vel.append(v1)
    # Cruising Stage
    elif v1 >= racer1_v:
        racer1_vel.append(v1)

    # Acceleration Stage
    if v2 < racer2_v:
        v2 = racer2_a * t
        racer2_vel.append(v2)
    # Cruising Stage
    elif v2 >= racer2_v:
        racer2_vel.append(v2)

racer1_label = 'Racer 1 (maxV = {}, a = {})'.format(racer1_v, racer1_a)
racer2_label = 'Racer 2 (maxV = {}, a = {})'.format(racer2_v, racer2_a)

plt.plot(frame_list, racer1_vel, label=racer1_label)
plt.plot(frame_list, racer2_vel, label=racer2_label)

plt.title('Velocity vs Time')
plt.xlabel('Time (Frames)')
plt.ylabel('Velocity (Pixels/Frame)')
plt.legend()

plt.show()

