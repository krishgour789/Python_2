a = "KRiSh IS VeRy GoOd"
print(a.capitalize())     #Krish is very good
print(a.title())          #Krish Is Very Good
print(a.upper())          #KRISH IS VERY GOOD
print(a.lower())          #krish is very good
print(a.index("Sh"))      #3
print(a.find("hS"))       #-1 it wwill use to handle the error if the indexing of element is not found
print(a.startswith("K"))  #True
print(a.startswith("R"))  #False
print(a.count("i"))       #1

a = "Krish 123"  
print(a.isalnum())        #False   bcz there is space in string
a ="123"
print(a.isdigit())        #True
a = "  "  
print(a.isspace())        #True
a = "Krish Is Very Good"
print(a.istitle())        #True
a ="KRISH IS VERY GOOD"
print(a.isupper())        #True
a = "krish is very good"
print(a.islower())        #True
a = "Krish Is Very Good"
print(a.swapcase())       #kRISH iS vERY gOOD   
a = "Krish Is Very Good"
print(a.replace("Krish","Gour"))  #Gour Is Very Good
print(a.split(" "))      #['Krish', 'Is', 'Very', 'Good']
print(a.split("V"))      #['Krish Is ', 'ery Good']
print(a.splitlines())    #['Krish Is Very Good']    it will split the string into list of lines
print(a.partition("Is"))  #('Krish ', 'Is', ' Very Good')  it will split the string into 3 parts before, after and the separator
print(a.partition("V"))
print(a.rpartition("K"))  #('Krish Is ', 'V', 'ery Good')  it will split the string into 3 parts before, after and the separator from right side
print(a.zfill(30))  #000000000000000Krish Is Very Good  it will fill the string with zeros from left side to make the length of string 30
print(a.center(30,"*"))  #********Krish Is Very Good********  it will center the string and fill the remaining space with *
print(a.ljust(30,"*"))  #Krish Is Very Good**********  it will left justify the string and fill the remaining space with *
print(a.rjust(30,"*"))  #**********Krish Is Very Good
a = "   Krish Is Very Good   "
print(a.strip())  #Krish Is Very Good  it will remove the leading and trailing spaces from the string