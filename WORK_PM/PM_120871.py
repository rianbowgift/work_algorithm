a = int(input())
three = 1
//
while a>=1:
    if three%3==0:
        three= three+1
        continue
    num =str(three).find('3')
    if num!=-1:
        three= three+1
        continue
    else:
        a= a-1
        three= three+1




print(three-1)