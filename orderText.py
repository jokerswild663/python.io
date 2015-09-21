def test():
  print('hello')
  return

def removeDuplicates(dataList):
  unique=set(dataList)
  newList=list(unique)
  return newList

def readText(filePath):
  dataFromFile=[]
  with open(filePath,'r') as fileObject:
    fileLines=fileObject.readlines()
    
    for line in fileLines:
      print(line)
      word=str(line).strip().split(",")
      dataFromFile+=word
    
    return dataFromFile
