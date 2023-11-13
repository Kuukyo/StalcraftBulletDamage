import matplotlib.pyplot as plt
import gun
import ttk
import numpy as np


guns = ["VSS Vintorez", "PKP Pecheneg", "A-545", "FN F2000 Tactical", "ASh-12", "HK G3A1", "SA-58 CTC"]
bullet_res = 302.29
vitality = 115

for name in guns:
    weapon = gun.Gun(name)
    ttkc = ttk.TTKCalculator(weapon, vitality, bullet_res, True, "ceramic")
    x = np.arange(150)
    y = []

    for d in x:
        y.append(ttkc.ttk(d))

    plt.plot(x, y, label=name)

plt.xlabel("Distance In Meters")
plt.ylabel("Time To Kill In Seconds")
plt.title(f"TTK Of Guns +10 against {vitality} Vitality and {bullet_res} Bullet Resistance using AP Ammo")

plt.legend()
plt.show()
