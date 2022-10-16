import os
 
readCmd = os.popen('netsh wlan show profile').readlines()
wifiList = []
passwordList = []
 
for output in readCmd:
    if "All User Profile" in output:
        wifiList.append(output[output.rfind(':')+2:].strip())
        
for network in wifiList:
    PasswordOutput = (os.popen('netsh wlan show profile {0} key=clear'.format(network)).readlines())
    for line in PasswordOutput:
        if "Key Content" in line:
            password = line[line.rfind(':') + 2:]
            print("Network: " + network + ", Password: " + password)