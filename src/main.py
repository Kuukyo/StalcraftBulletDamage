import matplotlib.pyplot as plt
import gun
import ttk
import numpy as np


guns = ["WA2000", "FN SCAR SSR", "VSS-M Vintorez"]
bullet_res = 351.23
bullet_res2 = 392.83
vitality = 120
max_range = 120

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('TTK of Guns +15 using AP ammo')

for name in guns:
    weapon = gun.Gun(name)
    ttkc = ttk.TTKCalculator(weapon, vitality, bullet_res, True, "ceramic")
    ttkc2 = ttk.TTKCalculator(weapon, vitality, bullet_res2, True, "ceramic")
    x = np.arange(max_range)
    y = []
    y2 = []

    for d in x:
        y.append(ttkc.ttk(d))
        y2.append(ttkc2.ttk(d))

    ax1.plot(x, y, label=name)
    ax2.plot(x, y2, label=name)

ax1.set(xlabel="Distance In Meters", ylabel="Time To Kill In Seconds", title=f"Against {vitality} Vitality and {bullet_res} Bullet Resistance")
ax2.set(xlabel="Distance In Meters", ylabel="Time To Kill In Seconds", title=f"Against {vitality} Vitality and {bullet_res2} Bullet Resistance")

ax1.legend()
ax2.legend()
plt.show()
