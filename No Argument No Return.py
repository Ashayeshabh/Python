class IIBM:
    def input(self):
        self.p=float(input("enter principal value"))
        self.r=float(input("enter rate value"))
        self.t=float(input("enter time value"))
    def process(self):
        self.si=(self.p*self.r*self.t)/100
    def result(self):
        print(self.si)
k=IIBM()
k.input()
k.process()
k.result()

