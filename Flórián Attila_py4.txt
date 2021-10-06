pont = None
pont = int(input("Adja meg a pontot"))
while pont == 50 or pont > 50:
    pont = int(input("Adja meg a pontot"))
    print("ötös")
else:
    print("nem ös")