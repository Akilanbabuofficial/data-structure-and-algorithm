class con:
    def getdata(self):
        self.string1=input("enter string 1:")
        self.string2=input("enter string 2:") 
    def printdata(self):
        print("string 1 is:",self.string1)
        print("string 2 is:",self.string2)
        print("con string is :",self.string1+self.string2)
    def lengetdata(self):
        self.str3=input("enter a string:")
    def lenprintdata(self):
        print("length of string:",len(self.str3))
    def revgetdata(self):
        self.str4=input("enter a string:")
    def revprintdata(self):
        print("reverse of string:",reversed(self.str4))
p=con()
p.getdata()
p.printdata()
p.lengetdata()
p.lenprintdata()
p.revgetdata()
p.revprintdata()