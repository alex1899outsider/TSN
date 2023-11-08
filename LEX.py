A = '\n A.coming back for everything'
B = 'B.without him'
C = 'C.find a lawyer'

print('\n(Please keep Caps Lock on ALL THE TIME.)'
      '\n\nMark SET YOU UP , and you have to make choice.'
      ,'\n',A,'\n',B,'\n',C)

ANSWER = 'ABC'
while True:
    choose = input('\n''you will:')
    if choose == ANSWER:
        print('\n''Ah , Brilliant.''\n')
        
        import random
        LUCKLYegg = ['Do you know WHO I am?', "I m not a bad buy,Eduardo\n"
                     "I'm just someone who wants to help you."]
        print('\n',random.choice(LUCKLYegg))
        
        LEX = random.choice(LUCKLYegg)
        
        
        if LEX == LUCKLYegg[0]:
           e = input("Do you wanna know WHO I am? A : 'YES' or 'NO'\n INTER:")
           if e == 'YES' :
            print('\nI m glad to knew you Eduardo,Welcome to LexCorp.\n')
            break
           elif e == 'NO' :
            print('\nAs you wish.BUT I will have time.\n\nTime,time.\n'
                  'That will all blow away,like sand in the desert.\n')
            break
           else:
            print('\nNo,no,no,you re too bad,dudu.please,Do as I said.\n')
            
            
    elif choose in 'DEFGHIJKLMNOPQRSTUVWXYZ' : 
         print('Follow the rules! Darling')
        
    else:
        print("\noh. What a shame.Do you truly think that's all? 'EVERYTHING' ?")
        import random
        egg = ['You felw too close to the sun.','Mr.Saverin,take it easy.',
               'I m not a bad buy,Eduardo',"Wow,It'cherry.\nUnfortunately,it will be rotten.\n"
                "\n'Cause time is the most cruel thing."]
        print('\n',random.choice(egg))
    