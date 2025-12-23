class IIBM:
    def input(self,p,r,t):
        self.x=p
        self.y=r
        self.z=t
    def process(self):
        self.si=(self.x*self.y*self.z)/100
    def result(self):
        print(self.si)
k=IIBM()
m=float(input("enter principal value"))
n=float(input("enter rate value"))
o=float(input("enter time value"))
k.input(m,n,o)
k.process()
k.result()