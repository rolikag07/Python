import random
import os

print("WELCOME TO THE PROGRAMMING LANGUAGE GUESS-GAME")

print("please ensure to keep your capslock off")
  
name = input("What is your name? ")
print("Hello! ", name,"let's start the game")
 
langs = ['java', 'c', 'c++', 'ruby',
         'python', 'scala','swift',
         'javascript', 'pascal', 'php']


c='yes'
while c == 'yes':
    
    lang = random.choice(langs)
    print("Guess the programming language ")
 
    guesses = ''
    turns=12
     
    while turns > 0:
        os.system('cls')
        
        failed = 0
        
        for char in lang:
             
          
            if char in guesses:
                print(char)
                 
            else:
                print("_")
                 
             
                failed += 1
                 
     
        if failed == 0:
           
              print("The language is: ", lang)
              ch=input("Enter the name of programmer who cretaed this language : ")
              
              if lang =='java':
                  if ch == 'james gosling':
                      print("You Guessed correctly you WIN!")
                      break
                 
    
              if lang =='c':
                  if ch == 'dennis ritchie':
                      print("you guessed correctly you WIN!")
                      break
                  else:
                      print('Worng Answer')
                      break
    
              if lang =='scala':
                  if ch == 'martin odersky':
                      print("you guessed correctly you WIN!")
                      break
                 
    
              if lang =='python':
                  
                  if ch == 'guido van rossum':
                      print("you guessed correctly you WIN!")
                      break
                  
              if lang =='ruby':
                  if ch == 'yukihiro matz matsumoto':
                      print("you guessed correctly you WIN!")
                      break
                  else:
                      print('Worng Answer')
                      break
    
              if lang =='c++':
                  if ch == 'bjarne stroustrup':
                      print("you guessed correctly you WIN!")
                      break
               
              if lang =='php':
                  if ch == 'rasmus lerdorf':
                      print("you guessed correctly you WIN!")
                      break
                  else:
                      print('Worng Answer')
                      break
                      
              if lang =='swift':
                  if ch == 'chris lattner':
                      print("you guessed correctly you WIN!")
                      break
                
              if lang =='pascal':
                  if ch == 'niklaus wirth':
                      print("you guessed correctly you WIN!")
                      break
                  
    
              if lang =='javascript':
                  if ch == 'brendan eich':
                      print("you guessed correctly you WIN!")
                      break
                       
        guess = input("guess a character:")
             
        guesses += guess
             
          
        if guess not in lang:
                 
                          turns = turns - 1
         
        
                          print("Wrong")
         
       
                          print("You have", + turns, 'more guesses')
         
             
        if turns == 0:
            print("You Loose")
            
    c=input("Do you want to keep playing yes/no: ")
