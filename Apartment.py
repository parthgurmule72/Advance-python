class Resident:
    def __init__(self, name, flat, fee, status):
        self.name = name
        self.flat = flat
        self.fee = fee
        self.status = status

    def display(self):
        print("Name:", self.name)
        print("Flat:", self.flat)
        print("Fee:", self.fee)
        print("Status:", self.status)


class Society:
    def __init__(self):
        self.residents = []

    def add(self, r):
        self.residents.append(r)

    def display_all(self):
        for r in self.residents:
            r.display()
            print()


s = Society()

r1 = Resident("Rahul", 101, 2000, "Paid")
r2 = Resident("Amit", 102, 2000, "Pending")

s.add(r1)
s.add(r2)

s.display_all()