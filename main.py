from doctest import BLANKLINE_MARKER
import json
import tkinter as tk
import requests
from pprint import pprint

#ウィンドウの作成
score_window = tk.Tk()
score_window.title("Game & Exercise")
score_window.geometry("960x540")

#データを開く
idtxt = open('data/id.txt', 'r', encoding='UTF-8')
apitxt = open('data/api.txt', 'r', encoding='UTF-8')
idinfo = idtxt.readlines()
apiinfo = apitxt.readlines()
id = idinfo[0]
api = apiinfo[0]

#試合データを取ってくる
url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + str(id)
res = requests.get(url, "TRN-Api-Key=" + str(api))
apex = json.loads(res.text)
brs = apex["data"]["segments"][0]["stats"]["rankScore"]["value"]
bkd = apex["data"]["segments"][0]["stats"]["kills"]["value"]
bdm = apex["data"]["segments"][0]["stats"]["damage"]["value"]

#メインフレームの作成と設置
frame_leftup = tk.Frame(score_window, bd=2, relief=tk.RAISED)
frame_leftdown = tk.Frame(score_window, bd=2, relief=tk.RAISED)
frame_rightup = tk.Frame(score_window, bd=2, relief=tk.RAISED)
frame_rightdown = tk.Frame(score_window, bd=2, relief=tk.RAISED)

score_window.rowconfigure((0,1), weight=1)
score_window.columnconfigure((0,1), weight=1)

frame_leftup.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
frame_leftdown.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
frame_rightup.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
frame_rightdown.grid(column=1, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))

#ウィジェット配置
beforeranktxt = tk.Label(frame_leftup, text=u'開始時')
beforerankpoint = tk.Label(frame_leftup, text=u'ランクポイント' + str(brs))
beforekd = tk.Label(frame_leftup, text=u'累計キル' + str(bkd))
beforedamage = tk.Label(frame_leftup, text=u'累計ダメージ' + str(bdm))
beforeranktxt.pack()
beforerankpoint.pack()
beforekd.pack()
beforedamage.pack()

afterranktxt = tk.Label(frame_leftdown, text=u'今日の成績')
afterrankpoint = tk.Label(frame_leftdown, text=u'ランクポイント' + str(brs))
afterkd = tk.Label(frame_leftdown, text=u'キル' + str(brs))
afterdamage = tk.Label(frame_leftdown, text=u'ダメージ' + str(brs))
afterranktxt.pack()
afterrankpoint.pack()
afterkd.pack()
afterdamage.pack()

default = 0
menutxt = tk.Label(frame_rightup, text=u'今日の運動メニュー')
walking = tk.Label(frame_rightup, text=u'ランニングorウォーキング:' + str(default) + 'km')
pushups = tk.Label(frame_rightup, text=u'腕立て:' + str(default) + '回')
squat = tk.Label(frame_rightup, text=u'スクワット:' + str(default) + '回')
bunny = tk.Label(frame_rightup, text=u'バニージャンプ:' + str(default) + '回')
plank = tk.Label(frame_rightup, text=u'プランク:' + str(default) + '分')
menutxt.pack()
walking.pack()
pushups.pack()
squat.pack()
bunny.pack()
plank.pack()

refresh = tk.Label(frame_rightdown, text=u'')
refresh.pack()

#ボタンの実行内容記載
def ifjson():
    global brs
    global bkd
    global bdm

    idtxt = open('data/id.txt', 'r', encoding='UTF-8')
    apitxt = open('data/api.txt', 'r', encoding='UTF-8')
    idinfo = idtxt.readlines()
    apiinfo = apitxt.readlines()
    id = idinfo[0]
    api = apiinfo[0]

    url = "https://public-api.tracker.gg/v2/apex/standard/profile/" + str(id)
    res = requests.get(url, "TRN-Api-Key=" + str(api))
    aapex = json.loads(res.text)
    ars = aapex["data"]["segments"][0]["stats"]["rankScore"]["value"]
    akd = aapex["data"]["segments"][0]["stats"]["kills"]["value"]
    adm = aapex["data"]["segments"][0]["stats"]["damage"]["value"]

    #データの計算と記載
    if (brs != ars) or (bkd != akd) or (bdm != adm):
        rankscore = brs - ars
        kills = bkd - akd
        damage = adm - bdm

        walk = (rankscore * 0.05) + (kills * 0.05) - (damage * 0.001)
        psb = (rankscore * 0.1) + (kills) - (damage * 0.001)
        plan = (rankscore * 0.01) + (kills * 0.1) - (damage * 0.001)

        afterrankpoint['text'] ='ランクポイント' + str(rankscore)
        afterkd['text'] ='キル' + str(kills)
        afterdamage['text'] ='ダメージ' + str(damage)

        walking["text"] = 'ランニングorウォーキング:' + str(walk)
        pushups["text"] = '腕立て:' + str(psb)
        squat["text"] = 'スクワット:' + str(psb)
        bunny["text"] = 'バニージャンプ:' + str(psb)
        plank["text"] = 'プランク:' + str(plan)

        refresh['text'] = '更新しました'
        idtxt.close()
        apitxt.close()
        brs = ars
    else:
        refresh['text'] = 'マッチの処理がまだできていません。少し待ってから更新してください'


rebutton = tk.Button(frame_rightdown, text=u'更新', command=ifjson)
rebutton.pack()

idtxt.close()
apitxt.close()

score_window.mainloop()