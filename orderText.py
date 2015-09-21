def test():
  """this is a test function to see module is being called"""
  print('hello')
  return

def removeDuplicates(dataList):
  """This removes duplicate strings from a list of strings supplied
  input: list of strings
  output: list of strings"""
  unique=set(dataList)
  newList=list(unique)
  return newList

def readText(filePath):
  """This reads all text from a text file.  
  Removes whitespace and splits strings into list of strings based on delimeter ','
  input: relative path of text file
  output: list of strings"""
  dataFromFile=[]
  with open(filePath,'r') as fileObject:
    fileLines=fileObject.readlines()
    
    for line in fileLines:
      print(line)
      word=str(line).strip().split(",")
      dataFromFile+=word
    
    return dataFromFile
