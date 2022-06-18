import json, time, os
from symtable import Symbol
import requests
from decimal import Decimal
  
def loop_get():
    btc_key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    eth_key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    lrc_key = "https://api.binance.com/api/v3/ticker/price?symbol=LRCUSDT"
    imx_key = "https://api.binance.com/api/v3/ticker/price?symbol=IMXUSDT"
    doge_key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"
    xrp_key = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
    ada_key = "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT"
    bnb_key = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    dai_key = "https://api.binance.com/api/v3/ticker/price?symbol=DAIUSDT"
    sol_key = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"

    #BTC
    btc_data = requests.get(btc_key)  
    btc_data = btc_data.json()
    btc_data['price'] = Decimal(btc_data['price']).normalize()
    #ETH
    eth_data = requests.get(eth_key)  
    eth_data = eth_data.json()
    eth_data['price'] = Decimal(eth_data['price']).normalize()
    #LRC
    lrc_data = requests.get(lrc_key)  
    lrc_data = lrc_data.json()
    lrc_data['price'] = Decimal(lrc_data['price']).normalize()
    #IMX
    imx_data = requests.get(imx_key)  
    imx_data = imx_data.json()
    imx_data['price'] = Decimal(imx_data['price']).normalize()
    #doge
    doge_data = requests.get(doge_key)  
    doge_data = doge_data.json()
    doge_data['price'] = Decimal(doge_data['price']).normalize()
    #xrp
    xrp_data = requests.get(xrp_key)  
    xrp_data = xrp_data.json()
    xrp_data['price'] = Decimal(xrp_data['price']).normalize()
    #ada
    ada_data = requests.get(ada_key)  
    ada_data = ada_data.json()
    ada_data['price'] = Decimal(ada_data['price']).normalize()
    #bnb
    bnb_data = requests.get(bnb_key)  
    bnb_data = bnb_data.json()
    bnb_data['price'] = Decimal(bnb_data['price']).normalize()
    #dai
    dai_data = requests.get(dai_key)  
    dai_data = dai_data.json()
    dai_data['price'] = Decimal(dai_data['price']).normalize()
    #sol
    sol_data = requests.get(sol_key)  
    sol_data = sol_data.json()
    sol_data['price'] = Decimal(sol_data['price']).normalize()

    btc_data['price'] = str(btc_data['price'])
    eth_data['price'] = str(eth_data['price'])
    lrc_data['price'] = str(lrc_data['price'])
    imx_data['price'] = str(imx_data['price'])
    doge_data['price'] = str(doge_data['price'])
    xrp_data['price'] = str(xrp_data['price'])
    ada_data['price'] = str(ada_data['price'])
    bnb_data['price'] = str(bnb_data['price'])
    dai_data['price'] = str(dai_data['price'])
    sol_data['price'] = str(sol_data['price'])

    btc_cryp_data = open("coins/BTC.price","w+")
    eth_cryp_data = open("coins/ETH.price","w+")
    lrc_cryp_data = open("coins/LRC.price","w+")
    imx_cryp_data = open("coins/IMX.price","w+")
    doge_cryp_data = open("coins/DOGE.price","w+")
    xrp_cryp_data = open("coins/XRP.price","w+")
    ada_cryp_data = open("coins/ADA.price","w+")
    bnb_cryp_data = open("coins/BNB.price","w+")
    dai_cryp_data = open("coins/DAI.price","w+")
    sol_cryp_data = open("coins/SOL.price","w+")

    btc_cryp_data.write(btc_data['price'])
    eth_cryp_data.write(eth_data['price'])
    lrc_cryp_data.write(lrc_data['price'])
    imx_cryp_data.write(imx_data['price'])
    doge_cryp_data.write(doge_data['price'])
    xrp_cryp_data.write(xrp_data['price'])
    ada_cryp_data.write(ada_data['price'])
    bnb_cryp_data.write(bnb_data['price'])
    dai_cryp_data.write(dai_data['price'])
    sol_cryp_data.write(sol_data['price'])

    btc_cryp_data.close()
    eth_cryp_data.close()
    lrc_cryp_data.close()
    imx_cryp_data.close()
    doge_cryp_data.close()
    xrp_cryp_data.close()
    ada_cryp_data.close()
    bnb_cryp_data.close()
    dai_cryp_data.close()
    sol_cryp_data.close()

    os.system('cls')

    print(f"[BTC] {btc_data['price']} USD")
    print(f"[ETH] {eth_data['price']} USD")
    print(f"[LRC] {lrc_data['price']} USD")
    print(f"[IMX] {imx_data['price']} USD")
    print(f"[DOGE] {doge_data['price']} USD")
    print(f"[XRP] {xrp_data['price']} USD")
    print(f"[ADA] {ada_data['price']} USD")
    print(f"[BNB] {bnb_data['price']} USD")
    print(f"[DAI] {dai_data['price']} USD")
    print(f"[SOL] {sol_data['price']} USD")

    loop_get()


print("[BTC] Loading...")
print("[ETH] Loading...")
print("[LRC] Loading...")
print("[IMX] Loading...")
print("[DOGE] Loading...")
print("[XRP] Loading...")
print("[ADA] Loading...")
print("[BNB] Loading...")
print("[DAI] Loading...")
print("[SOL] Loading...")

loop_get()