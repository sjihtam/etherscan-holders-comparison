import csv

def main():
    simAdress = []
    newname = ''
    bestanden = []
    i=1
    while newname != 'quit':
        newname = input("Bestandsnaam of quit: \n")
        if newname != 'quit':
            bestanden.append(newname)
            print(bestanden)
    simAdress = VergelijkBestanden(bestanden[0], bestanden[i])
    print(simAdress)
    print(len(simAdress))
    for i in range(2,len(bestanden)):
        temp = simAdress
        simAdress = VergelijkResultaten(temp,bestanden[i])
        print(simAdress)
        print(len(simAdress))

def VergelijkBestanden(file1,file2):
    temp = []
    with open(file1,'r') as eerste:
        for line in eerste:
            address = line.split(',')[0]
            with open(file2,'r') as tweede:
                for line in tweede:
                    address2 = line.split(',')[0]
                    if (address == address2):
                        temp.append(address)
    return temp

def VergelijkResultaten(oudeAdressen,nieuwBestand):
    newlist = []
    for address in oudeAdressen:
        with open(nieuwBestand,'r') as tweede:
                for line in tweede:
                    address2 = line.split(',')[0]
                    if (address == address2):
                        newlist.append(address)
    return newlist

main()
