import PySimpleGUI as psg
import pyautogui as pa
import keyboard as k

#region CLASSI E OGGETTI
class BarcodeElement:
    def __init__(self, barcode, hotkey):
        self.barcode = barcode
        self.hotkey = hotkey

    def __repr__(self):
        return "Barcode: " + self.barcode + " - Shortcut: " + self.hotkey

#endregion

barcodeList = [
    BarcodeElement("01ASAAA15", "6"),
    BarcodeElement("00COAAA0401", "7"),
    BarcodeElement("02CABB3025", "8"),
]

#region METODI GUI
def AddBarcode(e, v):
    scannedBarcode = v['BARCODE']
    barcodeList.append(scannedBarcode)

    window['BARCODE_LIST'].update(values = barcodeList)
    window.refresh()

def SimulateBarcode(e, v):
    if (v['BARCODE_LIST'] == []):
        return

    barcodeToSimulateElement = v['BARCODE_LIST'][0]
    barcodeToSimulate = barcodeToSimulateElement.barcode

    pa.write(barcodeToSimulate + "\n")
    print("Simulato l'inserimento del barcode: ", barcodeToSimulate)

def SimulateBarcodeFromHotkey(barcodeToSimulate):
    pa.write(barcodeToSimulate + "\n")
    print("Simulato l'inserimento del barcode: ", barcodeToSimulate)

#endregion

#region GESTIONE HOTKEY
for element in barcodeList:
    bkHotkey = 'f' + element.hotkey
    k.add_hotkey(bkHotkey, SimulateBarcodeFromHotkey,args=[element.barcode])

    print("Aggiunta combinazione " + bkHotkey + " per richiamare " + element.barcode)
#endregion

#region GUI FRONTEND
psg.theme("DarkAmber")

gui_layout = [
    [ psg.Text("Inserisci il barcode: "), psg.In(key='BARCODE', expand_x=True) ],
    [ psg.Text("Shortcut: "), psg.In(key='SHORTCUT', expand_x=True) ],
    [ psg.Button("Aggiungi Barcode", key='BTN_ADD_BARCODE')],
    [ psg.Listbox(values= barcodeList, key="BARCODE_LIST", expand_x=True, expand_y=True)],
    [ psg.Button("Simula barcode", key="BTN_SIMULATE_BARCODE", expand_x=True)]
]

window = psg.Window(
    title = "Barcode simulator",
    layout = gui_layout,
    size = (400, 400),
    margins= (10, 10),
    finalize=True
)
#endregion

#region BACKEND
while True:

    #EVENTI GUI --------------------------
    e, v = window.read()

    #Premuto il pulsante "Invia barcode"
    if e == 'BTN_ADD_BARCODE':
        AddBarcode(e, v)

    elif e == 'BTN_SIMULATE_BARCODE':
        SimulateBarcode(e, v)

    if e == psg.WIN_CLOSED:
        break
    #--------------------------------------

window.close()
#endregion
