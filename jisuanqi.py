print("欢迎使用hally的python简易计算器")

print("1、加法+")
print("2、减法-")
print("3、乘法*")
print("4、除法/")
k=1
while k==1:
    choice = input("请输入您要选择的运算方式(1/2/3/4):")
    if choice not in str(list(range(1,5))):
        print('选择错误')
        
    else:    
        num1 = input("请输入您要运算的第一个数：")
        if num1 =="":
            print("数字不可为空")
            num1=input("请重新输入第一个数:")
        else:
            print("您输入的第一个数是：",num1)

        num2 = input("请输入您要运算的第二个数：")
        if num2=="":
            print("数字不可为空")
            num2=input("请重新输入第二个数:")
        else:
            print("您输入的第二个数是：",num2)

        num1=float(num1)
        num2=float(num2)
        if choice == '1':
            print(num1,"+",num2,"=", num1+num2)

        elif choice == '2':
            print(num1,"-",num2,"=", num1-num2)

        elif choice == '3':
            print(num1,"x",num2,"=", num1*num2)

        elif choice == '4':
            print(num1,"/",num2,"=", num1/num2)
    
    chongxin=input('要重新开始吗？(y/n):')
    if chongxin.strip()=='n':
        print('计算结束')
        k+=1
                
                