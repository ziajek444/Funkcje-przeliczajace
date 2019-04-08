from enum import Enum 

# start class ------------------
class Sint:
    class data_representation(Enum):
        Binary = 1;
        Octal = 2;
        Decimal = 3; # only decimal is supported right now
        Hexadecimal = 4;
    
    __value = "0";
    __size = 1;
    __representation = data_representation.Decimal;
    __UnSaveFastMode = False;
    
    def __init__(self,number = "0"):
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
                        raise
            elif (self.__representation.name == 'Binary'):
                for el in input_value:
                    if not (el in ['0','1']):
                        raise
            elif (self.__representation.name == 'Octal'):
                for el in input_value:
                    if not (el in ['0','1','2','3','4','5','6','7']):
                        raise
            elif (self.__representation.name == 'Hexadecimal'):
                for el in input_value:
                    if not (el in ['0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','f','F']):
                        raise
            else: raise
        # END if
        if (self.__representation.name == 'Decimal'):
            gora = self.value;
            dol  = str(input_value);
            wyn = ""
            dluzszy =  max(len(gora),len(dol))
            lg= len(gora)
            ld=len(dol)
            if lg > ld:
                dol = (lg - ld) * '0' + dol
            else:
                gora = (ld-lg) * '0' + gora
            mem = 0
            for it in range(dluzszy,0,-1):
              dig = int(gora[it-1])+int(dol[it-1])
              if dig>9 : 
                dig = dig -10
                wyn += chr(dig+mem+48)
                mem = 1
              else:
                wyn += chr(dig+mem+48)
                mem =0
            if mem > 0:
                wyn += chr(mem+48)
            self.value = wyn[::-1];
        else: raise
        # END if
    def SUB(self,input_value):
        
        pass;
    def MUL(self,input_value):
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
    moja = Sint();
    print("go: ",moja)
    moja = "3" + moja;
    print("go: ",moja)
    elo = Sint("400") + moja;
    print("go: ",elo)
    elo = Sint("400") + "2340";
    print("go: ",elo)
    elo = Sint("400") + "2340";
    print("go: ",elo)


