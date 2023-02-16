class Calculator:

    def gumarel(self,tiv1,tiv2):
        return f'{tiv1 + tiv2}'
    def hanum(self,tiv1,tiv2):
        return f'{tiv1 - tiv2}'
    def bazmapatkum(self,tiv1,tiv2):
        return f'{tiv1 * tiv2}'
    def bajanum(self,tiv1,tiv2):
        return f'{tiv1 / tiv2}'
    def sqrt(self,tiv):
        return f'{tiv ** 0.5}'
        

Vahe = Calculator()
print(Vahe.gumarel(6,9))
print(Vahe.sqrt(81))
---------------------------
class Mard:
    def __init__(self,anun,azganun):
        self.anun = anun
        self.azganun = azganun
    def barev(self):
        return f'Barev es {self.anun} {self.azganun}n em: '
    def xpel(self,um):
        return f'Es {self.anun} n em ev xpum em {um} in'
Sargis = Mard('Sargis','Sargsyan')
print(Sargis.barev())
print(Sargis.xpel('Gor'))


-----------------xndir1-------------
class Century:
    def tari_to_dar(self,tari):
        if tari % 100 == 0:
            return tari / 100 
        else:
            return tari // 100 + 1
dar = Century()
print(dar.tari_to_dar(int(input('enter century: '))))

-----------------xndir2-------------
class Palindrome:
    def check(self,string):
        string.islower()
        if 1 <= len(string) <= 12:
            if string[0:len(string)//2] == string[len(string)//2 + 1 ::]:
                return True
            else:
                return False
        else:
            return 'string is too long!!!'
text = Palindrome()
print(text.check(input('enter the string: ')))

--------xndir3------- ''' vonc listy input anem,68 toxov '''
class Largest_product:
    def product(self,mylist):
        
        product = mylist[0] * mylist[1] 
        for i in range(1,len(mylist) - 1):
            if mylist[i] * mylist[i+1]  > product:
                product = mylist[i] * mylist[i+1]
                return product
            else:
                pass
mylist = Largest_product()
print(mylist.product([3,6,-2,-5,7,3]))
-----------------xndir4???????-------------
class Highest_word:
    def longest_str(self,mylist,newlist = []):
        length = len(mylist[0])
        for i in range(1,len(mylist)):
            if len(mylist[i]) > length:
                length = len(mylist[i])   
            else:
                pass
        for i in mylist:
            if len(i) == length:
                newlist.append(i)
            return newlist
mylist = Highest_word()
print(mylist.longest_str([["aba", "aa", "ad", "vcd", "aba"]]))
       #'''voncer senc''' # [for i in mylist newlist.append(i) if len(i) == length]

-----------------xndir5-------------
class Lucky:
    def check(self,n):
        mid = len(n)//2
        f_part = 0
        s_part = 0
        for i in n[:mid]:
            f_part += int(i)
        for j in n[mid:]:
            s_part += int(j)
        if f_part == s_part:
            return True
        else:
            return False

num = Lucky()
print(num.check(input('enter num: ')))

-----------------xndir6-------------''' ??? '''
class List_sort:
    def height(self,mylist):
        for i in mylist:
            if mylist[i] == -1:
                continue
            else:
                mylist.sorted()
            return mylist
listt = List_sort()
print(listt.height([-1, 150, 190, 170, -1, -1, 160, 180]))
        

-----------------xndir7-------------
class Weight:
    def teams(self,mylist,new = []):
        f_team = 0
        s_team = 0
        for i in range(0,len(mylist)+1,2):
            f_team += mylist[i]
        for j in range(1,len(mylist),2):
            s_team += mylist[j]
        new.append(f_team)
        new.append(s_team)
        return new
mylist = Weight()
print(mylist.teams([50, 60, 60, 45, 70]))

    