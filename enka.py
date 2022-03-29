from sys import stdin

def traziEps(lista):           
    izlazLista = lista
    for stanje in izlazLista:
        temp = []
        if prijelazDict.get(stanje):
            for prijelaz in prijelazDict.get(stanje):
                if prijelaz[0] == "$": temp.extend(prijelaz[1])
        if temp:
            [izlazLista.append(x) for x in temp if x not in izlazLista]
    return izlazLista

prijelazDict = dict(); pocStanja = []; izlazPoc = ""; prijTemp = []
ulaz        = input().split("\n")[0].split("|")
ulaz        = [x.split(",") for x in ulaz]
stanja      = input().split("\n")[0].split(",")
abeceda     = input().split("\n")[0].split(",")
prihSt      = input().split("\n")[0].split(",")
q0          = input().split("\n")[0]
for line in stdin: prijTemp.append(line.split("\n")[:-1][0])
for x in prijTemp:
    temp2 = x[x.find(",")+1:].split("->")
    temp2[1] = temp2[1].split(",")
    prijelazDict[x[:x.find(",")]] = [temp2] if(x[:x.find(",")] not in prijelazDict) else [*prijelazDict[x[:x.find(",")]], temp2]

pocStanja.append(q0)
pocStanja = sorted(traziEps(pocStanja))
for stanje in pocStanja: izlazPoc += stanje + ","

for trenNiz in ulaz:
    trenStanja = pocStanja; izlaz = ""
    for slovo in trenNiz:
        izlazLista = []; izlaz += "|"
        for stanje in trenStanja:
            if stanje in prijelazDict.keys():
                tempStanja = [x for x in prijelazDict.get(stanje) if slovo in x]
                if tempStanja: izlazLista.extend(tempStanja[0][1])
        trenStanja = sorted(traziEps(list(set(izlazLista))))
        if('#' in trenStanja): trenStanja.remove("#")
        izlaz = izlaz + (",").join(trenStanja) if trenStanja else izlaz + "#"
    print(izlazPoc[:-1] + izlaz)
