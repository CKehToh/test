import requests
import matplotlib.pyplot as plt

headers = {"identity": "Y2",
           "token": "411e25a9-5fff-42b5-8a2d-272f94b4a26f"}


def getCustomerId(name):
    url = "https://techtrek-api-gateway.cfapps.io/customers/" + name
    r = requests.get(url, headers=headers)
    return r.json()['customerId']


def getDetails(name):
    url = "https://techtrek-api-gateway.cfapps.io/customers/"+getCustomerId(name)+"/details"
    r = requests.get(url, headers=headers)
    return r.json()


def getAccountId(name):
    url = "https://techtrek-api-gateway.cfapps.io/accounts/deposit/"+getCustomerId(name)
    r = requests.get(url, headers=headers)
    for i in range(0, len(r.json())):
        return r.json()[i]['accountId']

def getTransectionDetails(accountId, datefrom, dateto):
    url = "https://techtrek-api-gateway.cfapps.io/transactions/"+accountId+"?from="+datefrom+"&to="+dateto
    r = requests.get(url, headers=headers)
    return r.json()

def getTags(accountId, datefrom, dateto):
    url = "https://techtrek-api-gateway.cfapps.io/transactions/"+accountId+"?from="+datefrom+"&to="+dateto
    r = requests.get(url, headers=headers)
    list1 = []
    for i in range(0, len(r.json())):
        if r.json()[i]['tag'] not in list1:
            list1.append(r.json()[i]['tag'])
    return list1


def showByTags(accountId, tag, datefrom, dateto):
    url = "https://techtrek-api-gateway.cfapps.io/transactions/"+accountId+"?from="+datefrom+"&to="+dateto
    r = requests.get(url, headers=headers)
    list1 = []
    for i in range(0, len(r.json())):
        if r.json()[i]['tag'] == tag:
            list1.append(r.json()[i])
    return list1

def graph(accountId, datefrom, dateto):
    url = "https://techtrek-api-gateway.cfapps.io/transactions/" + accountId + "?from=" + datefrom + "&to=" + dateto
    r = requests.get(url, headers=headers)
    list1 = []
    for i in range(0, len(r.json())):
        list1.append([r.json()[i]['date'], r.json()[i]['amount']])
    list1 = sorted(list1)

    list2 = []
    for i in range(0, len(list1)):
        list2.append([list1[i][0][5:7], list1[i][1]])

    dictTotal = {}
    for x in list2:
        if x[0] not in dictTotal:
            dictTotal[x[0]] = round(float(x[1]),2)
        else:
            dictTotal[x[0]] += round(float(x[1]),2)

    bars = plt.bar(range(len(dictTotal)),list(dictTotal.values()))
    plt.ylabel('Amount Spent ($)')
    plt.xlabel('Month')
    plt.xticks(range(len(dictTotal)), dictTotal.keys())
    plt.title('Total Spending per Month')
    for bar in bars:
        yval = round(bar.get_height(),2)
        plt.text(bar.get_x(), yval + .1, yval)
    plt.savefig('TotalExpentiturebyMonth.png')

def graphExpenditure( accountId, dateFrom, dateto) :
    url = "https://techtrek-api-gateway.cfapps.io/transactions/" + accountId + "?from=" + dateFrom + "&to=" + dateto
    r = requests.get(url, headers=headers)
    list1 = []
    for i in range(0, len(r.json())):
        list1.append([r.json()[i]['tag'], r.json()[i]['amount']])
    list1 = sorted(list1)

    list2 = []
    for i in range(0, len(list1)):
        list2.append([list1[i][0][5:7], list1[i][1]])

    dictTotal = {}
    for x in list1:
        if x[0] not in dictTotal:
            dictTotal[x[0]] = round(float(x[1]),2)
        else:
            dictTotal[x[0]] += round(float(x[1]),2)

    bars = plt.bar(range(len(dictTotal)),list(dictTotal.values()))
    plt.xticks(range(len(dictTotal)),dictTotal)
    plt.ylabel('Amount Spent ($)')
    plt.xlabel('Spent type')
    plt.xticks(range(len(dictTotal)), dictTotal.keys())
    plt.title('What you have spent on')
    for bar in bars:
        yval = round(bar.get_height(),2)
        plt.text(bar.get_x(), yval + .1, yval)
    plt.savefig('TotalExpentiture.png')
    plt.show()


def graphExpenditureByTag(accountId, dateFrom, dateto,tag):
    url = "https://techtrek-api-gateway.cfapps.io/transactions/" + accountId + "?from=" + dateFrom + "&to=" + dateto
    r = requests.get(url, headers=headers)
    list1 = []
    for i in range(0, len(r.json())):
        if r.json()[i]['tag'] == tag:
            list1.append([r.json()[i]['date'][5:7], r.json()[i]['amount']])
    list1 = sorted(list1)

    list2 = []
    for i in range(0, len(list1)):
        list2.append([list1[i][0][5:7], list1[i][1]])

    dictTotal = {}
    for x in list1:
        if x[0] not in dictTotal:
            dictTotal[x[0]] = round(float(x[1]),2)
        else:
            dictTotal[x[0]] += round(float(x[1]),2)

    bars = plt.bar(range(len(dictTotal)),list(dictTotal.values()))

    plt.ylabel('Amount Spent ($)')
    plt.xlabel('Month')
    plt.xticks(range(len(dictTotal)), dictTotal.keys())
    plt.title('Spendings per month on ' + tag.lower())
    for bar in bars:
        yval = round(bar.get_height(),2)
        plt.text(bar.get_x(), yval + .1, yval)
    plt.savefig('Expentiture on' + tag +'.png')


def getCreditAccount(customerId):
    url = "https://techtrek-api-gateway.cfapps.io/accounts/credit/"+customerId
    r = requests.get(url, headers=headers)
    return r.json()

def getCreditBalance(creditId):
    url = "https://techtrek-api-gateway.cfapps.io/accounts/credit/"+creditId+"/balance"
    r = requests.get(url, headers=headers)
    return r.json()

def getPm(customerId):
    url = "https://techtrek-api-gateway.cfapps.io/message/"+customerId
    r = requests.get(url, headers=headers)
    return r.json()

def getMarketingList():
    url = "https://techtrek-api-gateway.cfapps.io/marketing/"
    r = requests.get(url, headers=headers)
    return r.json()

def getMarketingDetails(messageId):
    url = "https://techtrek-api-gateway.cfapps.io/marketing/"+messageId
    r = requests.get(url, headers=headers)
    return r.json()


#print(getCustomerId("marytan"))
#print(getDetails("marytan"))
print(getAccountId("marytan"))
#print(getTransectionDetails("74","01-01-2018","02-01-2019"))
#print(getTags("74","01-01-2018","02-01-2019"))
#print(showByTags("74","TRANSPORT","01-01-2018","02-01-2019"))
#graph("74","01-01-2018","02-01-2019")
#print(getCreditAccount("2"))
#print(getCreditBalance("106"))
#print(getPm("02"))
#print(getMarketingList())
#print(getMarketingDetails("01"))
#print(getCustomerId("marytan"))
#print(getDetails("marytan"))
#print(getAccountId("marytan"))
#print(getTransectionDetails("74","01-01-2018","02-01-2019"))
#print(getTags("74","01-01-2018","02-01-2019"))
#print(showByTags("74","TRANSPORT","01-01-2018","02-01-2019"))
#graph("74","01-01-2018","02-01-2019")
#graphExpenditure("74","01-01-2018","02-01-2019")
#graphExpenditureByTag("74","01-01-2018","02-01-2019","TRANSPORT")
#graphExpenditureByTag("74","01-01-2018","02-01-2019","F&B")
#graphExpenditureByTag("74","01-01-2018","02-01-2019","ATM")
#graphExpenditureByTag("74","01-01-2018","02-01-2019","TRANSFER")
#graphExpenditure("74","01-01-2018","02-01-2019")