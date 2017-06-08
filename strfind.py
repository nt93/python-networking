str1 = 'apni poori aish aish hai'
str2 = 'aish'

j = str1.find(str2,3)

print ('The string is matched at index:',end=" ")
print (str1.rfind(str2,3))
print ('The string find at index', j)