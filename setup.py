# coding: UTF-8
import tkinter


#ウィンドウの作成
setup_window = tkinter.Tk()
setup_window.title("Setup")
setup_window.geometry("960x540")

#データを開く
apitxt = open('data/api.txt','r', encoding='UTF-8')

#チェックボックスにチェックが入ってるかの確認
platform = tkinter.IntVar()

#ラジオボタンデフォルトの設定
platform.set(0)

#ラジオボタンの作成
radio1 = tkinter.Radiobutton(text=u"PC", variable=platform, value=0)
radio2 = tkinter.Radiobutton(text=u"XboX", variable=platform, value=1)
radio3 = tkinter.Radiobutton(text=u"Playstation", variable=platform, value=2)
radio1.pack()
radio2.pack()
radio3.pack()

#ラジオボタンに応じてプラットフォームを選択
plt = ""

if platform.get() == 0:
    plt += "origin/"

elif platform.get() == 1:
    plt += "xbl/"

elif platform.get() == 2:
    plt += "psn/"

apiinfo = apitxt.read()

#ID入力欄の作成
tllabel = tkinter.Label(setup_window, text=u'IDを入力')
tllabel.pack()
PlyIDbox = tkinter.Entry()
PlyIDbox.pack()

#APIキーの入力
apilabel = tkinter.Label(text=u'APIを入力')
apilabel.pack()
apiky = tkinter.Entry()
apiky.insert(0, str(apiinfo))
apiky.pack()

def write():
    idtxt = open('data/id.txt', 'w', encoding='UTF-8')
    apitxto = open('data/api.txt','w', encoding='UTF-8')

    apid = apiky.get()
    PlayerID = PlyIDbox.get()
    #プラットフォームとIDを変数にぶち込む
    PlayerList = plt + PlayerID
    #変数PlayerListの値をtxtに書き込む
    idtxt.write(PlayerList)
    apitxto.write(apid)

    apitxt.close()
    apitxto.close()
    idtxt.close()

def end():
    setup_window.destroy()#画面を閉じる

# buttonwriteをクリックした時の処理
Buttonwrite = tkinter.Button(text=u'idとapiキーを更新', command = write)
Buttonwrite.pack(pady=10)

Buttonend = tkinter.Button(text=u'セットアップを終わる', command = end)
Buttonend.pack(pady=20)


setup_window.mainloop()