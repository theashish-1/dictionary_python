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
    def __mul__(self, other):
        realResult = 0
        imgResult = 0
        par1 = self.real * other.real
        par2 = self.img * other.img
        par3 = self.real * other.img
        par4 = other.real * self.img

        realResult = par1 - par2
        imgResult = par3 + par4

        ans = ComplexNumber(realResult , imgResult)
        return ans
        # return f"{par1-par2} + ({par3+par4})j"

    def __truediv__(self, other):
        denominator = other.real**2 + other.img**2
        ans = self*ComplexNumber(other.real/denominator,-1*other.img/denominator)
        return ans
    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

cn = ComplexNumber(6,4)
cn2 = ComplexNumber(3,8)
cn3 = ComplexNumber(3,4)
cn4 = ComplexNumber(4,5)
print("division of complex number is ",cn3/cn4)
print(cn)
print(cn+cn2)
print(cn.conjugate())
print(cn3 * cn4)
print("comparison operator is ",cn == cn2)

# cn.conjugate()