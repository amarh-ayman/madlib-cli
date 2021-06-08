import re

def read_template():
  try:
      with open('./asset/madlibGameText.txt') as file:
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
    textOt=read_template() 
    parseOt=parse_template(textOt)
    answer=askUserQ(parseOt)
    # print(merge(textOt,parseOt,answer))  