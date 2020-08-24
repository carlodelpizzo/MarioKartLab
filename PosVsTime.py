from matplotlib import pyplot as plt

racer1_v = 4.0
racer1_a = 0.01
racer1_pos = []

racer2_v = 2.0
racer2_a = 0.02
racer2_pos = []

frame_list = []

for i in range(0, 551):
    frame_list.append(i)


d1 = 0
d2 = 0
v1 = 0
v2 = 0

for t in range(len(frame_list)):
    # Acceleration Stage
    if v1 < racer1_v:
        d1 = (racer1_a * (t * t)) / 2
        v1 = racer1_a * t
        racer1_pos.append(d1)
        d1a = d1
        t1 = t
    # Cruising Stage
    elif v1 >= racer1_v:
        d1 = d1a + v1 * (t - t1)
        racer1_pos.append(d1)

    # Acceleration Stage
    if v2 < racer2_v:
        d2 = (racer2_a * (t * t)) / 2
        v2 = racer2_a * t
        racer2_pos.append(d2)
        d2a = d2
        t2 = t
    # Cruising Stage
    elif v2 >= racer2_v:
        d2 = d2a + v2 * (t - t2)
        racer2_pos.append(d2)

racer1_label = 'Racer 3 (maxV = {}, a = {})'.format(racer1_v, racer1_a)
racer2_label = 'Racer 2 (maxV = {}, a = {})'.format(racer2_v, racer2_a)

finish = []

for i in range(len(frame_list)):
    finish.append(1000)

plt.plot(frame_list, finish, '--', color='black')
plt.plot(frame_list, racer2_pos, label=racer2_label)
plt.plot(frame_list, racer1_pos, label=racer1_label, color='red')


plt.title('Position vs Time')
plt.xlabel('Time (Frames)')
plt.ylabel('Position (Pixels)')
plt.legend()

plt.show()
