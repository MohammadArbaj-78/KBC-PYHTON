#exercise KBC

print('WelCome To'.center(50))
print('Kon Banega Karodpati\n'.center(50))

a= input('\nAre you Ready for playing KBC.....')

if ('ready'==a):
    print('Ok,ready to first Question')
else:
    print('Exit')
    
def answer(x):
    match x:
        case 0:
             print('A. 23\t  B. 36\nC. 29\t  D. 20')
        case 1:
             print('A. 600 karod\t  B. 500 karod\nC. 800 karod\t  D. 850 karod')
        case 2:
             print('A. 150 karod\t  B. 100 karod\nC. 50 karod\t  D. 200 karod')
        case 3:
             print('A. 600 karod\t  B. 200 karod\nC. 300 karod\t  D. 850 karod')
        case 4:  
            print('A. 15 karod\t  B. 10 karod\nC. 50 karod\t  D. 20 karod')
            
def ans(x,y):
  if (y==0):
    match x:
     #   case 'a':
     #       print('Your answer is wrong..')
     #   case 'b':
    #        print('Your answer is wrong..')
        case 'c':
            print('Your answer is wright..')         
            print('Aapne jite hai 1000 $')
            return int(1000)
     #   case 'd':
     #       print('Your answer is wrong..')
        case _:
            print('your answer is wrong..')
            print('wright Answer....C')
            return int(0)
  elif (y==1):
     match x:
     #   case 'a':
     #       print('Your answer is wrong..')
     #   case 'b':
     #       print('Your answer is wrong..')
    #    case 'c':
   #         print('Your answer is wrong..')
        case 'd':
            print('Your answer is wright..')
            print('Aapne jite hai 10,000 $')
            return int(10000)
        case _:
            print('your answer is wrong..')
            print('wright Answer....D')
            return int(0)
  elif (y==2):         
       match x:
        case 'a':
            print('Your answer is wright..')
            print('Aapne jite hai 1,00000 $')
            return int(100000)
     #   case 'b':
    #        print('Your answer is wrong..')
    #    case 'c':
    #        print('Your answer is wrong..')
     #   case 'd':
    #        print('Your answer is wrong..')
        case _:
            print('your answer is wrong..')
            print('wright Answer....A')
            return int(0)
  elif (y==3):     
      match x:
    #    case 'a':
     #       print('Your answer is wrong..')
        case 'b':
            print('Your answer is wright..')
            print('Aapne jite hai 10,00000 $')
            return int(1000000)
     #   case 'c':
        #    print('Your answer is wrong..')
     #   case 'd':
      #      print('Your answer is wrong..')
        case _:
            print('your answer is wrong..')
            print('wright Answer....B')
            return int(0)
  elif (y==4):     
      match x:
        case 'a':
            print('Your answer is wright..')
            print('Aapne jite hai 1,0000000 $')
            return int(10000000)
     #   case 'b':
       #     print('Your answer is wrong..')
     #   case 'c':
       #     print('Your answer is wrong..')
     #   case 'd':
     #       print('Your answer is wrong..')
        case _:
            print('your answer is wrong..')
            print('wright Answer....A')
            return int(0)
    
    
    
Qlist=['1. India me kitne state hai','2. world me total population kitni hai','3. India ki population kitni hai','4. world me total muslim population kitni hai','5. India me muslim population kitni hai']
sum=0
for Q in range(5):
    print('\n',Qlist[Q])
    answer(Q)
    an=input('Enter your answer...')
    Total=ans(an,Q)
    sum=sum+Total
   
print('Aapne aaj KBC me jite hai',sum,'$')
    