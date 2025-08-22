import time
while True:
    in1=int(input("whats the first number:"))
    in2=int(input("whats the second number:"))
    in3=input("what action must happen +(plus) -(minus) x(multeply) /(devide):")
    def isrightinput():
        if in3 not in (('+','-','x','/')) :#Note if u use in use ',' becose or might give problems rather use or when ==
            return False
        else:
            return True
    while isrightinput() == False:
        print("wrong input")
        in3=input("what action must happen +(plus) -(minus) x(multeply) /(devide)")
    output=str(in1)+in3+str(in2)
    if in3 =='+':
      answ=in1 + in2
    elif in3 =='-':
       answ=in1 - in2
    elif in3 == 'x':
      answ=in1 * in2 
    elif in3 == '/':
        answ=in1 / in2
    print(output+" =") 
    print(answ)
    stop=input("press 1 to stop or 2 to restart ")
    if stop == '1':
        break
    elif stop =='2':
        continue
    else:
        print("invalid input stopping")
        time.sleep(3)
        break