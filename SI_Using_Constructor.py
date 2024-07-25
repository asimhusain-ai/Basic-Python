class SimpleInterest:
    def __init__(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t
    def result(self):
        si = self.p * self.r * self.t //100
        print(si)
p=int(input("Enter principal: "))
r=int(input("Enter rate: "))
t=int(input("Enter time: "))

SI = SimpleInterest(p,r,t)
SI.result()