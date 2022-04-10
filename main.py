# from table 1, Pwi = Peak Load (%) * Panual
# from table 2, p_day = Day of week * Pwi
p_day = 0.93*.862*85
# from table 3, b is the hourly peak load from 12 am to 12 PM, 24 Hours
b = [0.67, 0.63, 0.60, 0.59, 0.59, 0.60, 0.74, 0.86, 0.95, 0.95, 0.96, 0.95, 0.95, 0.95, 0.93, 0.94, 0.99, 1, 1, 0.96, 0.91, 0.83, 0.73, 0.63]

x = ()
i = ()

for i in range(24):

    x = b[i]*p_day
    print(f"{i+1}H = {x} MW")
    i += 1
