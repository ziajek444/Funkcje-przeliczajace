from enum import Enum 

# start class ------------------
class Sint:
    class data_representation(Enum):
        Binary = 1;
        Octal = 2;
        Decimal = 3; # only decimal is supported right now
        Hexadecimal = 4;
    def hex_to_dec(self,hexi:str):
        hexi = ord(hexi)
        if (hexi >= ord('a') and hexi <= ord('f')):
            tmp = hexi - ord('a') + 10
        elif (hexi >= ord('A') and hexi <= ord('F')):
            tmp = hexi - ord('A') + 10
        else:
            tmp = int(chr(hexi))
        return tmp
    def dec_to_hex(self,dec):
        # dec have to be in range -7 to 15
        if (dec > 0):
            if (dec <= 9):
                return chr(dec+48)
            else:
                return chr(ord('a')+(dec-10))
        else:
            return "0";
    __value = "0";
    __size = 1;
    __representation = data_representation.Decimal;
    __UnSaveFastMode = False;
    
    def __init__(self, number = "0", repres = None):
        if repres is None:
            self.__representation = self.data_representation.Decimal;
            #print(type(self.__representation))
            #print(self.__representation)
        else:
            #print(type(repres))
            #print(repres)
            self.__representation = repres;
            #print(type(self.__representation))
            #print(self.__representation)
            
        self.value = str(number);
        self.size = len(self.value);
    def __str__(self):
        return self.value;
    def __radd__(self, other):
        self.ADD(other);
        return self;
    def __add__(self, other):
        self.ADD(other);
        return self;
    def __rmul__(self, other):
        self.MUL(other);
        return self;
    def __mul__(self, other):
        self.MUL(other);
        return self;
    def __rsub__(self, other):
        self.MUL(other);
        return self;
    def __sub__(self, other):
        self.MUL(other);
        return self;
    def __str__(self):
        return "{0}".format(self.value)
    def __len__(self):
        return len(self.value);
    
    def ADD(self,input_value):
        input_value = str(input_value);
        if self.__UnSaveFastMode == False:
            if (self.__representation.name == 'Decimal'):
                for el in input_value:
                    if not (el in ['0','1','2','3','4','5','6','7','8','9']):
                        raise Exception("It is not Dec type");
            elif (self.__representation.name == 'Binary'):
                for el in input_value:
                    if not (el in ['0','1']):
                        raise Exception("It is not Bin type");
            elif (self.__representation.name == 'Octal'):
                for el in input_value:
                    if not (el in ['0','1','2','3','4','5','6','7']):
                        raise Exception("It is not Octal type");
            elif (self.__representation.name == 'Hexadecimal'):
                for el in input_value:
                    if not (el in ['0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','f','F']):
                        raise Exception("It is not Hexa type");
            else:
                print(self.__representation.name)
                raise Exception("Wrong representation type #1");
        # END if
        if (self.__representation.name == 'Decimal'):
            print("deci add")
            gora = self.value[::-1];
            dol  = str(input_value)[::-1];
            wyn = ""
            lg = len(gora)
            ld = len(dol)
            if lg > ld:
                dol = dol + (lg - ld) * '0'
                ld = len(dol)
            else:
                gora = gora + (ld - lg) * '0'
                lg = len(gora)
            mem = 0
            
            for it in range(0,lg):
              dig = int(gora[it]) + int(dol[it]) + mem;
              if dig >= 10 and dig <= 19:
                mem = 1
                dig = dig - 10
                wyn += chr(dig + 48)
              else:
                mem = 0;
                wyn += chr(dig + 48)
            if mem > 0:
                wyn += chr(mem+48)
            self.value = wyn[::-1];
        elif (self.__representation.name == 'Octal'):
            pass
        elif (self.__representation.name == 'Binary'):
            pass
        elif (self.__representation.name == 'Hexadecimal'):
           pass
        else: raise Exception("Wrong representation type #2");
        # END if
    def SUB(self,input_value,Right = True):
        if (self.__representation.name == 'Decimal'):
            print("deci sub")
            if Right:
                # self.value - input_value
                
            else:
                # input_value - self.value
        pass;
    def MUL(self,input_value):
        if (self.__representation.name == 'Decimal'):
            print("deci mul")
            pass
        elif (self.__representation.name == 'Octal'):
            pass
        elif (self.__representation.name == 'Binary'):
            pass
        elif (self.__representation.name == 'Hexadecimal'):
           pass
        else: raise Exception("Wrong representation type #2");
        pass;
    def DIV(self,input_value):
        pass;
    def FDIV(self,input_value): #floor div
        pass;
    def MOD(self,input_value):
        pass;
    def POW(self,input_value):
        pass;
    def LESS(self,input_value):
        pass;
    def LESSEQUAL(self,input_value):
        pass;
    def GREATER(self,input_value):
        pass;
    def GREATEREQUAL(self,input_value):
        pass;
    def EQUAL(self,input_value):
        pass;
    def NEQUAL(self,input_value):
        pass;
    def SUB(self,input_value):
        pass;
    def BLS(self,input_value): # Bitwise Left Shift <<
        pass;
    def BRS(self,input_value): # Bitwise Right Shift >>
        pass;
    def AND(self,input_value): 
        pass;
    def OR(self,input_value): 
        pass;
    def XOR(self,input_value): 
        pass;
    def NOT(self,input_value): 
        pass;

# end class --------------------

if __name__ == "__main__":
    
    twoja1 = Sint("65535",Sint.data_representation.Decimal);
    twoja2 = Sint("986881",Sint.data_representation.Decimal);
    twoja2 = twoja2 + twoja1;
    print("go: ",twoja2," ? 1052416")
    twoja1 = Sint("12432345")
    twoja2 = "12432345" + twoja1;
    print("go: ",twoja2," ? 24864690")
    twoja1 = Sint("0000111122223333")
    twoja2 = twoja1 + "9999999999"
    print("go: ",twoja2," ? 0000121122223332")









    
