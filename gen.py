from youtube_search import YoutubeSearch
import requests
from bs4 import BeautifulSoup

def insertSticFile(nameFiles):
    name_l = nameFiles.split(',')
    J = len(name_l)
    J = J - 1
    i = 0
    try:
        while i != J:
            file = open('stics/' + name_l[i] + '.txt', 'r')
            text = file.read()
            i = i + 1
            return text
    except:
        while i != J:
            file = open('stics/' + name_l[i] + '.txt', 'w')
            file.write('')
            i = i + 1

def UpDataStics(nameFiles):
    name_l = nameFiles.split(',')
    J = len(name_l)
    J = J - 1
    i = 0
    while i != J:
        file = open('stics/' + name_l[i] + '.txt', 'w')
        file.write('<h1 id="start-line"></h1>')
        i = i + 1

def creat(name):
    name_l = name.split(',')

    J = len(name_l)
    j = 0
    for i in name_l:
        print(i)
        file = open(i + '.html', 'w')
        file.write('')
        j = j + 1

class Parser:

    def Blyat():
        URL = 'http://fm4m.ru/bonus/sila/man/index.php?id=grud'
        HEDERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            }

        response = requests.get(URL, HEDERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = 'html5-video-player ytp-exp-bottom-control-flexbox ytp-title-enable-channel-logo ytp-embed ytp-embed-playlist ytp-fit-cover-video ytp-iv-drawer-enabled paused-mode unstarted-mode ytp-expand-pause-overlay')
        comps = []
        v_l = []

        for item in items:
            comps.append({'link': item.find('video', class_ = 'video-stream html5-main-video').get('src')})
        for comp in comps:
            v_l.append(comp['link'])


        
        print(v_l)


def ytPars(m=3):
    vidioList = []
    i = 0

    results = YoutubeSearch("Ярослав брин", max_results=m).to_dict()
    pull = str(results).split(',')
    print(pull[0])
    print(pull[1])
    print(pull[2])
    for o in pull:
        d = str(o)
        d_l = d.split(':')
        J = len(d_l)
        J = J - 1
        dd = str(d_l[J])
        dd_l = list(dd)
        Q = len(dd_l)
        Q = Q - 1
        del dd_l[Q]
        del dd_l[Q - 1]
        del dd_l[Q - 2] 
        fin = ''.join(dd_l)
        i = i + 1
        print(i)
        vidioList.append('https://www.youtube.com' + fin)
    return vidioList

class htm():

    def addVidio(url):
        text = '<div class="block-video"> <video src="'+ str(url) +'"></video> </div>'
        return text 

    def tp(name, home, homeUrl, nameUrl):
        text = '<h3><a class="tp" href="' + homeUrl + '">' + home + '</a>' + '<b class="tp">/</b>' + '<a class="tp" href="' + nameUrl + '">' + name + '</a></h3>'
        return text

def bild(name, stic):
    name_l = name.split(',')
    file = open(stic, 'r')
    s = file.read()
    stic_l = s.split('<|>')
    for i in name_l:
        print(i)
        file = open(i + '.html', 'w')
        print(s)
        file.write(stic_l[0] + htm.tp(i, 'Home', 'index.html', i+'.html') + str(insertSticFile(name))+ stic_l[1])     
UpDataStics("biceps,bicepsbedra,delta,diltaspina,golen,golenspina,grud,jivotkos,kvadriceps,predpl,press,spina,trapecspina,triceps,yagodic")
bild("biceps,bicepsbedra,delta,diltaspina,golen,golenspina,grud,jivotkos,kvadriceps,predpl,press,spina,trapecspina,triceps,yagodic", 'D:/Desktop/проект силачь/stic.txt')
#ytPars()
#Parser.Blyat()
