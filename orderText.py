def test():
  print('hello')
  return

def removeDuplicates(dataList):
  unique=set(dataList)
  newList=list(unique)
  return newList

def readText(filePath):
  dataFromFile=[]
  fileObject=open(filePath,'r')
  fileLines=fileObject.readlines()

  for line in fileLines:
    print(line)
    word=str(line).strip().split(",")
    dataFromFile+=word

  print(dataFromFile)
  return

