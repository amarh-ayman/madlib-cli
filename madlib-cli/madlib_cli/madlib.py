import re

def read_template(fileURL):
  '''
  function to read file text and strip it 
  also it will give an error if the file path not correct
 <FileNotFoundError>
  '''
  try:
      with open(fileURL) as file:
        return file.read().strip()
  except FileNotFoundError:
        raise 

def parse_template(text):
  '''
  parse_template function for find all the words inside brackets ,and replace them with an empty in the origin text 
  so the output from this function will be 
  parse_template[0]=text with empty brackets
  parse_template[1]=tuple with the word's inside brackets 
  '''
  pattern=(r'{(.+?)}')
  wordWithBrackets=re.findall(pattern,text)
  restTheText=text
  for item in wordWithBrackets:
    restTheText=restTheText.replace(item,'')
  return (restTheText,tuple(wordWithBrackets))


def askUserQ(Q):
  '''
  askUserQ function for asking the user some question and put the answer in list array , 
  the answer's will appear in the text in brackets place
  '''
  listOfParse=[]
  for item in Q:
    ask=input(f'Please Enter {item} :')
    listOfParse+=[ask]
  return listOfParse

def merge(text,parse):
  '''
  merge function for merge the text with the empty brackets with the answer's of the user
  '''
  return text.format(*parse)  

if __name__=="__main__":
    fURL='./assets/madlibGameText.txt'
    textOt=read_template(fURL) 
    parseOt=parse_template(textOt)[1]
    restext=parse_template(textOt)[0]
    print(restext)
    answer=askUserQ(parseOt)
    # print(merge(textOt,parseOt,answer))  

