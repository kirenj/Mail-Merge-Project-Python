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



names = open_names()

for i in names:
  letter_name = f'letter_for_{i}'
  save_path = f'Mail Merge Project Start/Output/ReadyToSend/{letter_name}.txt'
  with open('Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as file:
    content_read = file.read()
    content = content_read.replace('[name]', i)
    
  with open(save_path, mode='w') as new_letter:    
    new_letter.write(content)
  
  