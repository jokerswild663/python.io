def test():
  print('hello')
  return

def removeDuplicates(dataList):
  unique=set(dataList)
  newList=list(unique)
  return newList

def readText(filePath):
  fileObject=open(filePath,'r')
  print(fileObject.read())
  return
