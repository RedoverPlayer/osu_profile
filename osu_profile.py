import urllib.request

def getdata(url):
    data = str(urllib.request.urlopen(url).read())
    return data

def getpseudo(data):
    tmp = data.split('<title>',1)[1]
    tmp = tmp.split(' ',1)[0]
    return tmp   

def getlevel(data):
    tmp = data.split('"level":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"current":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getlevelprogress(data):
    tmp = data.split('"level":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"progress":',1)[1]
    tmp = tmp.split('}',1)[0]
    return tmp

def getpp(data):
    pp1 = data.split('statistics":{"level":{"current":',1)[1]
    pp2 = pp1.split(',"pp_rank":',1)[0]
    ppfinal = pp2.split('"pp":')[1]
    return ppfinal

def getrank(data):
    tmp = data.split('"pp_rank":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getrankedscore(data):
    tmp = data.split('"ranked_score":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def gethitaccuracy(data):
    tmp = data.split('"hit_accuracy":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getplaycount(data):
    tmp = data.split('"play_count":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getplaytime(data):
    tmp = data.split('"play_time":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def gettotalscore(data):
    tmp = data.split('"total_score":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def gettotalhits(data):
    tmp = data.split('"total_hits":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getmaximumcombo(data):
    tmp = data.split('"maximum_combo":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getglobalrank(data):
    tmp = data.split('"rank":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"global":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getcountryrank(data):
    tmp = data.split('"rank":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"country":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getss(data):
    tmp = data.split('"grade_counts":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"ss":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getssh(data):
    tmp = data.split('"grade_counts":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"ssh":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def gets(data):
    tmp = data.split('"grade_counts":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"s":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def getsh(data):
    tmp = data.split('"grade_counts":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"sh":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

def geta(data):
    tmp = data.split('"grade_counts":{',1)[1]
    tmp = tmp.split('}',1)[0]
    tmp = tmp.split('"a":',1)[1]
    tmp = tmp.split(',',1)[0]
    return tmp

if __name__ == '__main__':
    data = getdata("https://osu.ppy.sh/users/11995261")
    # data = getdata("https://osu.ppy.sh/users/9997447")

    print(getpseudo(data))
    print("level : " + getlevel(data) + " (" + getlevelprogress(data) + "%)")
    print("pp : " + getpp(data))
    print("rank : " + getrank(data))
    print("ranked score : " + getrankedscore(data))
    print("play count : " + getplaycount(data))
    print("play time : " + getplaytime(data))
    print("total score : " + gettotalscore(data))
    print("total hits : " + gettotalhits(data))
    print("maximum combo : " + getmaximumcombo(data))
    print("global rank : " + getglobalrank(data))
    print("country rank : " + getcountryrank(data))
    print("\nss : " + getss(data))
    print("ssh : " + getssh(data))
    print("s : " + gets(data))
    print("sh : " + getsh(data))
    print("a : " + geta(data))