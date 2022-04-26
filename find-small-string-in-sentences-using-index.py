

count = -1
str = "psrbobjrbobfhjbobkejdbob"
for char in str:
    count +=1
    print(char,count)
    if char == 'b' :    
       print('here is b at',count)
       if str[count + 1] == 'o' and str[count+2] == 'b':
          print('here is bob',count)     
       else:
         continue
     
#another method
str1 = "psrbobjrbobfhjbobkejdbob"
str2 = "bob"
str1.count('bob')
print(str1.count(str2))     