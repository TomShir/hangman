from colorama import Fore 
import time 
import sys 
import random 
import os 
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTMAGENTA_EX,Fore.LIGHTRED_EX,Fore.BLACK,Fore.CYAN,Fore.RESET]
letters='abcdefghijklmnopqrstuvwxyz'
incorrect_inputs_list=[]
stick_man_parts=['''
                      .
                    .
                  .
                .
              .''','''
                      .
                    .   .
                  .       .
                .           .
              .               .''',''' 
                      .
                      .
                      .
                      .
                      .
                    .   .
                  .       .
                .           .
              .               .''',''' 
                      .
                    . .
                  .   .
                .     .
              .       .
                    .   .
                  .       .
                .           .
              .               .''',''' 
                      .
                    . . .
                  .   .   .
                .     .     . 
              .       .       .
                    .   .
                  .       .
                .           .
              .               .''',''' 
                      
                     ◯ 
                      .
                    . . .
                  .   .   .
                .     .     .
              .       .       .
                    .   .
                  .       .
                .           .
              .               .''']
letters_list=[]
for letter in letters:
    letters_list.append(letter)
else:
    pass
#Creating a function that takes in a subscriptable sequence and loops over it and prints it horizontially 
def loop_over(sequence,color,delay_time):
    for txt in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{txt}')
    else:
        print(f'{colors[-1]}')
        
program_title='hangman'.upper()
for text in program_title:
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f'\t\t\t{random.choice(colors)}{"  ".join(text)}')
else:
    print(f'{colors[-1]}')
    time.sleep(1)
    os.system("cls")
    time.sleep(1)
    loop_over(sequence='Note:given word must be in lowercase\n\n',color=colors[6],delay_time=0.1)
    time.sleep(1)
    word_input=input('Word:')
    while word_input!=word_input.lower():
      loop_over(sequence='You did not adhere to the note,please try again',color=colors[0],delay_time=0.1)
      word_input=input('Word:')
      if word_input.lower():
        break 
    word_list=[]
    underscore_list=[]
    for letter in word_input:
        word_list.append(letter)
    else:  
     for num in range(len(word_input)):
        underscore_list.append('_')
     else:
         def create_dash_line():
             for underscore in underscore_list:
                 print(f'{underscore}',end=' ')
             else:
                 pass
             
         create_dash_line()
         time.sleep(1)
     try:
        while word_list!=underscore_list:
          select_index=int(input(f'\n\n{Fore.CYAN}Select an index from 0 to {len(word_input)-1}:{colors[-1]}'))
          while select_index<0 or select_index>len(word_input)-1:
            loop_over(sequence=f'IndexError,inputted index is not between the range of {0} and {len(word_input)-1}',color=colors[0],delay_time=0.1)
            select_index=int(input(f'\n\n{Fore.CYAN}Select an index from 0 to {len(word_input)-1}:{colors[-1]}'))
            if select_index>=0 and select_index<=len(word_input)-1:
              break 
            else:
              pass
          def guess_letter(index):
              guess_letter_input=input('letter:')
              while len(guess_letter_input)>1 or guess_letter_input not in letters_list:
                  time.sleep(1)
                  loop_over(sequence=f'{guess_letter_input} was not a letter please try again',color=colors[0],delay_time=0.1) 
                  time.sleep(1)
                  guess_letter_input=input('letter:')
                  if len(guess_letter_input)==1:
                      break
                  else:
                      pass
              else:
                  if guess_letter_input==word_list[index]:
                    for letter in underscore_list:
                        if letter==underscore_list[index]:
                            underscore_list.remove(letter)
                            underscore_list.insert(index,guess_letter_input)
                        else:
                            pass 
                        
                    create_dash_line()
                  else:
                      incorrect_inputs_list.append('X')
                      if len(incorrect_inputs_list)==1:
                          print(f'{stick_man_parts[0]}')
                      elif len(incorrect_inputs_list)==2:
                          print(f'{stick_man_parts[1]}')
                      elif len(incorrect_inputs_list)==3:
                          print(f'{stick_man_parts[2]}')
                      elif len(incorrect_inputs_list)==4:
                          print(f'{stick_man_parts[3]}')
                      elif len(incorrect_inputs_list)==5:
                          print(f'{stick_man_parts[4]}')
                      elif len(stick_man_parts)==6:
                          print(f'{stick_man_parts[5]}')
                          time.sleep(1)
                          loop_over(sequence='You lost!',color=colors[0],delay_time=0.1)
                          sys.exit('')
          guess_letter(index=select_index)
        else:
            loop_over(sequence='\nYou won!',color=colors[1],delay_time=0.1)
            time.sleep(1)
            os.system('cls')
            time.sleep(1)
            loop_over(sequence='Exitting program...',color=colors[0],delay_time=0.1)
            time.sleep(1)
            sys.exit('')
     except ValueError:
          loop_over(sequence='Error,an inappropriate value was entered',color=colors[0],delay_time=0.1)