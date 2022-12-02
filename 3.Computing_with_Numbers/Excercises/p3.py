def main():

    distance = float(input("Please enter distance from ligning: "))

    speedOfsound = 1100

    mile = 5280

    distanceTomile = distance/mile
    speedOfSoundAsMile = mile/speedOfsound


    print(f"You should ear sound in: { distance / speedOfsound} seconds.")

main()