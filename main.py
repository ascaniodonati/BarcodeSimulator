import pyautogui as pa
import keyboard as k
import json as js

import gui as gui
import types

from types import BarcodeElement

BARCODES_PATH  = "barcodes.json"

def SimulateBarcodeFromHotkey(barcodeToSimulate):
    pa.write(barcodeToSimulate + "\n")
    print("Simulato l'inserimento del barcode: ", barcodeToSimulate)

#region GESTIONE HOTKEY
def RefreshHotKeys():
    k.clear_all_hotkeys

    for element in barcodeList:
        k.add_hotkey(element.hotkey, SimulateBarcodeFromHotkey, args=[element.barcode])
        print("Aggiunta combinazione " + element.hotkey + " per richiamare " + element.barcode)
    
    print("Hotkeys aggiunte: " + str(k._hotkeys))
#endregion

#region METODI GUI
def SimulateBarcode(e, v):
    if (v['BARCODE_LIST'] == []):
        return

    barcodeToSimulateElement = v['BARCODE_LIST'][0]
    barcodeToSimulate = barcodeToSimulateElement.barcode

    pa.write(barcodeToSimulate + "\n")
    print("Simulato l'inserimento del barcode: ", barcodeToSimulate)

def SaveBarcodes():
    with open(BARCODES_PATH, "w") as barcodes_file:
        js.dump(barcodeList, barcodes_file, indent=4, cls=BarcodeElementEncoder)

def LoadBarcodes():
    with open(BARCODES_PATH, 'r') as barcodes_file:
        barcodeList = js.load(barcodes_file)
        print("Barcodes aggiunti: " + str(barcodeList))

    RefreshWindow()

#endregion



LoadBarcodes()
print("LoadedBarcodes: " + str(barcodeList))
RefreshHotKeys()


