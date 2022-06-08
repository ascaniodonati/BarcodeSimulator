import PySimpleGUI as psg

#region GUI FRONTEND
psg.theme("DarkAmber")

gui_layout = [
    [ psg.Text("Inserisci il barcode: "), psg.In(key='BARCODE', expand_x=True) ],
    [ psg.Text("Shortcut: "), psg.In(key='SHORTCUT', expand_x=True) ],
    [ psg.Button("Aggiungi Barcode", key='BTN_ADD_BARCODE')],
    [ psg.Listbox(values=barcodeList, key="BARCODE_LIST", expand_x=True, expand_y=True)],
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

def RefreshWindow():
    window['BARCODE_LIST'].update(values = )
    window.refresh()

#region BACKEND
while True:

    #EVENTI GUI --------------------------
    e, v = window.read()

    #Premuto il pulsante "Invia barcode"
    if e == 'BTN_ADD_BARCODE':
        # AddBarcode(e, v)
        break

    elif e == 'BTN_SIMULATE_BARCODE':
        # SimulateBarcode(e, v)
        break
    
    if e == psg.WIN_CLOSED:
        # SaveBarcodes()
        break
    #--------------------------------------

window.close()
#endregion