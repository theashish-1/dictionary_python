class ComplexNumber:
    def __init__(self,real , img):
        self.real = real
        self.img = img
    def conjugate(self):
        img = self.img * -1
        print(f"({self.real} + {img}i)")
        #or
        return ComplexNumber(self.real , -1*self.img)

    def __str__(self):
        # s = f"{self.real} + {self.img}"
        # return s
        if self.real == 0:
            return f"({self.img}i)"
        elif self.img<0:
            return f"({self.real}  {self.img}i)"
        else :
            return f"({self.real}+{self.img}i)"

    def __add__(self,other):
        realSum =self.real + other.real
        imgSum = self.img + other.img

        #create a new complex number and add realSum and imgSum
        # ans = ComplexNumber(realSum,imgSum)
        # return  f"{ans.real} + {ans.img}"

        #or
        return f"({realSum} + {imgSum}i)"
cn = ComplexNumber(6,4)
cn2 = ComplexNumber(3,8)
print(cn)
print(cn+cn2)
print(cn.conjugate())
# cn.conjugate()