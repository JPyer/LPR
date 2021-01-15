# Kangjier@2021:FocalAcoustics.CODE.The maintenance email is Jwjier@gmail.com .


from aip import AipOcr
import os

filename = 'file/key.txt'   # record the file location of the applied Key
if os.path.exists(filename):              
    with open(filename,"r") as file:     
        dictkey = eval(file.readlines()[0])  
        # The following three Key are created in the list of applications in the console of Baidu AI open platform.
        APP_ID = dictkey['APP_ID']     
        API_KEY = dictkey['API_KEY']     
        SECRET_KEY =  dictkey['SECRET_KEY']     
else:
    print("Please first create a key.txt, under the file directory and write the application key! the format is as follows:" 
"\ nThe SECRETKEY' of the APIID', 'API_KEY':' application of the APIID',' API_KEY':' application of the APIKEY', 'SECRET_KEY':' application of the\ n' APP_ID':' application.")
# Initialize the AipOcr object
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# read file
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# Return the license plate number according to the picture
def getcn():
  image = get_file_content('file/test.jpg')
  results =client.licensePlate(image)["words_result"]['number']
#   print(results)
  return results



