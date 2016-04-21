import csv
import csv
from NetModule import *
from exhaustingTools import *
Domain = 'Domain'
ns = 'Name Servers'
ws = 'Web Servers'
dns = 'DNS Servers'
headers=[Domain,ns, ws, dns]

def urlGenerator():
    with open('C:\\Users\\Omer\\Desktop\\top.csv', 'r') as f:
        reader = csv.reader(f)
        for numberOfLine,URL in reader:
            yield URL
    yield True
#
#
def startExhust(exhustServerInfo):
    nsString=[]
    #TODO OR PLEASE MAKE SURE THE Http tool return any value you want. this value will be written to the "file3.csv
    # at the folder of the running python files. best of luck
    #Omer Ornan- English Teacher and sexual Instructor.
    print(str(exhustServerInfo['ipv4']))
    webInfo = test_HTTP_connection_tolerance(exhustServerInfo["DOM"], str(exhustServerInfo['ipv4']))
    wbSt='wsInfo: %d' % (webInfo,)
    print(wbSt)
    print("hh")
    resolverString = []
    resolver = exhustServerInfo['RESOLVER']
    for rs in resolver:
        rsInfo = dnsExhaust(rs)
        print(rsInfo)
        print(rs[0])
        rsSt= 'dns info %s: %s' % (rs[0],rsInfo)
        resolverString.append(rsInfo)

    ns = exhustServerInfo['NS']
    print("dfg")
    for nsInfo in ns:
        print("dfgjj")
        dnsInfo = dnsExhaust(nsInfo)
        stDns='nsInfo %s: %s'%(nsInfo[0], dnsInfo)
        nsString.append(stDns)
    return {'nsInfo' : nsString, 'webInfo' : wbSt, 'resInfo' : resolverString}



def main():
    # http_request("128.139.199.8")  # GOOGLE

    #bucket = queue.Queue()
    #thread_obj = HTTP_Tester.Threaded_Test(bucket, 'www.ynet.co.il', "128.139.199.8")
    #thread_obj.start()

    #num_of_connections = test_HTTP_connection_tolerance("www.ynet.co.il" ,"128.139.199.8")  # OR: This is to test the http tolerance
    getURL=urlGenerator()
    url = next(getURL);
    writeToFile=csv.DictWriter(open('file3.csv','w'), delimiter=',',lineterminator='\n', fieldnames=headers)
    writeToFile.writerow({Domain:Domain,ns:ns,ws:ws,dns : dns})
    while url!=True:
        exhustServerInfo=create_domain_dict(url)
        infoToWrite=startExhust(exhustServerInfo)
        writeToFile.writerow({Domain : url, ns : infoToWrite['nsInfo'], ws : infoToWrite['webInfo'] , dns:infoToWrite['resInfo']})
        url = next(getURL);
        return# TODO MOVE THIS SHIT
main()
