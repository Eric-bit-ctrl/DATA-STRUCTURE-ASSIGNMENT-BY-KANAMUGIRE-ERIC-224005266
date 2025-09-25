nyabugogo_bus = ["bus1", "bus2", "bus3","bus4","bus5","bus6","bus7"]
print("the buses at nyabugogo :", nyabugogo_bus)
for _ in range(4):
    derparted = nyabugogo_bus.pop(0)
    print("departed : ",derparted)
print("the bus on the front :", nyabugogo_bus[0])

