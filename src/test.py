import gun
import ttk


weap = gun.Gun("FN F2000")
ttkc = ttk.TTKCalculator(weap, 0.08, 100, 250, True, "ceramic")
print(ttkc.bullet_damage_at_distance(100))
print(ttkc.bullets_needed_to_kill(100))
print(ttkc.ttk(100))