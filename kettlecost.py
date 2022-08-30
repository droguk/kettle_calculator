import time
import os
mytimer = 0
kw_cost_now = 28
kw_cost = 51
number_of_kw = 3
for mytimer in range(500):
    clear = lambda: os.system('clear')
    clear()
    cost_counter = mytimer * number_of_kw * kw_cost / 3600
    year_counter = 2 * 365 * cost_counter / 100
    print ("kW per hour:", number_of_kw, "Cost per unit (p):", kw_cost)
    print ("Time (s):", mytimer, "Cost (p):", format(cost_counter,".1f"), "Cost over year (£):", format(year_counter,".2f"))
    time.sleep(1)