from math import pow
from tabulate import tabulate


def wind_chill():

    wind_speed = 0
    temp = -40
    wind_chill_table = []

    while wind_speed <= 50 and temp <= 50:

        formula = 35.74 + 0.6214*temp - 35.75 * \
            pow(wind_speed, 0.16) + 0.4275*temp*(pow(wind_speed, 0.16))

        wind_chill_table.append(
            [temp, wind_speed, formula])

        wind_speed += 5
        temp += 10

    print(tabulate(wind_chill_table, headers=[
          "Temp", "Wind", "Wind_Chill"], tablefmt="simple_grid"))


wind_chill()
