import tkinter as tk 
import requests
import time
from datetime import datetime
#requestを使えないときpy -m pip install requestsを実行する

while True:
    p2pquake_url = 'https://api.p2pquake.net/v2/history?codes=551&limit=1'
#https://api-v2-sandbox.p2pquake.net/v2/history?codes=551&limit=1
#https://api.p2pquake.net/v2/history?codes=551&limit=1
    p2pquake_json = requests.get(p2pquake_url).json()
#震央地名を取り出して、変数に代入する
    #Eq_name = p2pquake_json[0]["earthquake"]["hypocenter"]["name"]
    Eq_name = "2025/01/15 18:28:20"
    Eq_hukasa = p2pquake_json[0]["earthquake"]["hypocenter"]["depth"]
    Eq_maguni = p2pquake_json[0]["earthquake"]["hypocenter"]["magnitude"]
    Eq_sin = p2pquake_json[0]["earthquake"]["maxScale"]
    Eq_time = p2pquake_json[0]["earthquake"]["time"]
#if文で震度1から7までを変換
    if Eq_sin==10:
        Eq_sindo = "震度1"
    if Eq_sin==20:
        Eq_sindo = "震度2"
    if Eq_sin==30:
        Eq_sindo = "震度3"
    if Eq_sin==40:
        Eq_sindo = "震度4"
    if Eq_sin==50:
        Eq_sindo = "震度5弱"
    if Eq_sin==55:
        Eq_sindo = "震度5強"
    if Eq_sin==60:
        Eq_sindo = "震度6弱"
    if Eq_sin==65:
        Eq_sindo = "震度6強"
    if Eq_sin==70:
        Eq_sindo = "震度7"
    elif Eq_sin <10:
        Eq_sindo = "震度不明"

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    if formatted_time==Eq_name:
        print(Eq_sindo)
    