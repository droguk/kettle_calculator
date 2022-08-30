# Usage: python3 kettlecost.py
import time
import os
mytimer = 0
# costs based on OFGEM price cap values
kw_cost_now = 28
kw_cost = 51
number_of_kw = 3
for mytimer in range(500):
    # this clear is for Linux OS, if running in Windows, change 'clear' to 'cls'
    clear = lambda: os.system('clear')
    clear()
    cost_counter = mytimer * number_of_kw * kw_cost / 3600
    # per year calculation based on 2 boils per day and then displayed in £ rather than p.
    year_counter = 2 * 365 * cost_counter / 100
    print ("kW per hour:", number_of_kw, "Cost per unit (p):", kw_cost)
    print ("Time (s):", mytimer, "Cost (p):", format(cost_counter,".1f"), "Cost over year (£):", format(year_counter,".2f"))
    time.sleep(1)
