import matplotlib.pyplot as plt
import gun
import ttk
import numpy as np


guns = ["FN F2000", "AEK-971", "HK G36C", "ASh-12", "Worn VSS Vintorez", "Worn PKP"]
bullet_res = 300

for name in guns:
    weapon = gun.Gun(name)
    ttkc = ttk.TTKCalculator(weapon, 100, bullet_res, True, "ceramic")
    x = np.arange(150)
    y = []
    for d in x:
        y.append(ttkc.ttk(d))

    plt.plot(x, y, label=name)

plt.xlabel("Distance In Meters")
plt.ylabel("Time To Kill In Seconds")
plt.title(f"TTK Of Guns + 0 against 100 Vitality and {bullet_res} Bullet Resistance")

plt.legend()
plt.show()
