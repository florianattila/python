pest = int(input("Hány fok van Budapesten?"))
becs = int(input("Hány fok van Bécsben?"))
if pest < becs:
    print(f"Budapesten van hűvösebb, {pest} fokot mértek. ")
elif pest > becs:
    print(f"Bécsben van hűvösebb, {becs} fokot mértek. ")
else:
    print("Budapesten és Bécsben is ugyanannyi fokot mértek")