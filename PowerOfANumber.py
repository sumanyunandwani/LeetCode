from audioop import mul


class Power(object):
    def __init__(self, number, power) -> None:
        self.number = number
        self.power = power
    def __get_binary_number(self, num):
        if num == 1:
            return str(1)
        return (self.__get_binary_number(num//2) + str(num%2))
    def get_power(self):
        binary = self.__get_binary_number(self.power)
        print(binary)
        multiply = self.number
        for index, i in enumerate(map(int, binary)):
            print(i)
            if index == 0:
                continue
            if i == 1:
                multiply = multiply*multiply*self.number
            else:
                multiply = multiply*multiply
        return multiply

obj = Power(2,10)
print(obj.get_power())


         
    
