import sys,threading,hashlib

hash = []
password_found = False
threads = []

if len(sys.argv) != 4:
    print("Use => %s <filename_to_desc> <filename_pass> <out> " % sys.argv[0])
    print("Reference => https://md5decrypt.net/en/Api/")
    # print(len(sys.argv))
    sys.exit();



def readHash():
    filename = open(sys.argv[1]) 
    lines = filename.readlines()
    for item in lines:
        if  item:
            hash.append(item.replace('\n', ''))
    
        
def DescHash(passwrod):
    filename = open(sys.argv[2], 'rb') 
    lines = filename.readlines()
    
    for item in lines:
        item_desc =((str(item).replace('b\'', '')).replace('n\'', '')).replace('\\', '')
        # print(item_desc)
        if  item :
            passTest = item_desc.encode()
            m = hashlib.md5()
            m.update(passTest)
            if m.hexdigest() ==  passwrod:
                print("password to hash {} Found => {}".format(passwrod,passTest))
                return
     
 

readHash()
# DescHash("7ecbf38edffdec2542db73a8668ebd60")
# DescHash("e10adc3949ba59abbe56e057f20f883e")
for item in hash:
    t = threading.Thread(target=DescHash,args=(item,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    