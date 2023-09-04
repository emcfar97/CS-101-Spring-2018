#################################################################################
##
## CS 101
## Makeup Program
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: 
##
## ALGORITHM: 
##      
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
#################################################################################

def integral(a,b,tol):
   midpnt = (a+b)/2
   if midpnt <= tol:
       return midpnt**2
   else:
       return midpnt**2 + integral(a,midpnt,tol)


while True:
    print(
        'This program will estimate the area under a curve.\n'
        'You can enter a formula in terms of x. 2*x or x**3 etc\n'
        )
    
    user_func = input('Enter the function ==> ')
    val_a = float(input('Enter the value for a ==> 1'))
    val_b = float(input('Enter the value for b ==>'))
    tol = float(input('Enter the value the tolerance ==> '))

    try:
        print(eval(user_func))
    except:
        print('There was an error')
        continue
    
    again = input('\nDo you want to calculate another? Y/N ').upper()
    while not (again in ('Y', 'YES', 'N', 'NO')):
        again = input('You must enter Y YES N or NO\n\nDo you want to try another word? Y/YES/N/NO ==> ').upper()
    if again in ('Y', 'YES'):
        continue
    else:
        print('Thanks for using The Estimator
              ')
        break
