import re

def read_template(fileURL):
  try:
      with open(fileURL) as file:
        return file.read()
  except FileNotFoundError:
    print('file not found')

def parse_template(text):
  pattern=(r'{(.+?)}')
  wordWithBrackets=re.findall(pattern,text)
  return wordWithBrackets


def askUserQ(Q):
  listOfParse=[]
  for item in Q:
    ask=input(f'Please Enter {item} :')
    listOfParse+=[ask]
  return listOfParse

def merge(text,parse,list):
  for item in range(len(parse)):
    text=text.replace('{'+parse[item]+'}' ,list[item] )
  return text  

def madlibGame():
    fURL='./assets/madlibGameText.txt'
    textOt=read_template(fURL) 
    parseOt=parse_template(textOt)
    answer=askUserQ(parseOt)
    # print(merge(textOt,parseOt,answer))  