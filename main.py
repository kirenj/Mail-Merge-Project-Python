#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# with open('Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as file:
#   content = file.read()
#   # print(content)



# with open('Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='w') as file1:
  
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Reading all the names in the file and inputing them as a list

def open_names():
  with open('Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as name:
    all_names = name.readlines()
    names = []
    for i in all_names:       
      new_names = i.strip('\n')
      names.append(new_names)
    return names


letter_number = 1
letter_name = f'letter {letter_number}'
save_path = f'Mail Merge Project Start/Output/ReadyToSend/{letter_name}.txt'

names = open_names()
for i in names:
  with open('Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as file:
    content_read = file.read()
    
    
      # print(i)
    with open(save_path, mode='w') as letter_name:      
      content = content_read.replace('[name]', i)
      letter_name.write(content)
      letter_number += 1
  