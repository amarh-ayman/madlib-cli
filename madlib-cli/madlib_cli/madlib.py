import re

def read_template(fileURL):
  '''
  function to read file text
  '''
  try:
      with open(fileURL) as file:
        return file.read().strip()
  except FileNotFoundError:
        return 'FileNotFoundError'

def parse_template(text):
  pattern=(r'{(.+?)}')
  wordWithBrackets=re.findall(pattern,text)
  restTheText=text
  for item in wordWithBrackets:
    restTheText=restTheText.replace(item,'')
  return (restTheText,tuple(wordWithBrackets))


def askUserQ(Q):
  listOfParse=[]
  for item in Q:
    ask=input(f'Please Enter {item} :')
    listOfParse+=[ask]
  return listOfParse

def merge(text,parse):
  return text.format(*parse)  

if __name__=="__main__":
    fURL='./assets/madlibGameText.txt'
    textOt=read_template(fURL) 
    parseOt=parse_template(textOt)[1]
    restext=parse_template(textOt)[0]
    print(restext)
    answer=askUserQ(parseOt)
    # print(merge(textOt,parseOt,answer))  

