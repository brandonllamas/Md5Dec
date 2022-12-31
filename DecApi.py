import sys,requests

if len(sys.argv) != 7:
    print("Use => %s <filename> <email> <typeHash> <code> <premium? 0 | 1 >  <out>" % sys.argv[0])
    print("Reference => https://md5decrypt.net/en/Api/")
    # print(len(sys.argv))
    sys.exit();
    
emailMdDec = sys.argv[2]
typeHash = sys.argv[3]
codeMd5 =  sys.argv[4]
premium =  sys.argv[5]
out =  sys.argv[6]

accountsTest = []
accountsDect = []


def readFile():
    filename = open(sys.argv[1]) 
    lines = filename.readlines()
    
    for item in lines:
        textLine = item.split(":")
        accountsTest.append({
            'account':textLine[0],
            'passw':textLine[1]
        })
def writeFile(item,passw):
     file1 = open(out,'w+')
     file1.write("{0}:{1}".format(item['account'],passw))
     file1.close()
     
def decrypt():
    # print(accountsTest)
    for item in accountsTest:
        # print(item["passw"])
        params = {
            'hash' :item['passw'].replace('\n', ''),
            'hash_type' :typeHash,
            'email' :emailMdDec,
            'code' :codeMd5,
            'premium' :premium,
        }
        resp = requests.get('https://md5decrypt.net/en/Api/api.php',params=params)
        respuesta = str(resp.content).split(":")
        # print(respuesta)
        # print(params)
        if(respuesta[0] == "b'ERROR CODE "):
            print("{0}:{1} => not pwned".format(item['account'],item['passw']))
        else:
            passw = str(resp.content).replace('b\'', '').replace('\'', '')
            print("{0}:{1} => pwned => {2}:{3}".format(item['account'],item['passw'],item['account'],passw))
            writeFile(item,passw)
        # print(resp.content)



readFile()
decrypt()
# print(accountsTest)