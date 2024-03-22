class number:
    def __init__(self,num):
        self.num=num
        if(num > 0):
            print("positive number")
        else:
            print("negative number")
n=number(5)
print(n.num)