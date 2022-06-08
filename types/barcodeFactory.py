from json import JSONEncoder
import string

barcodeList = []

class BarcodeElement:
    def __init__(self, barcode, hotkey):
        self.barcode = barcode
        self.hotkey = hotkey

    def __repr__(self) -> string:
        return "Barcode: " + self.barcode + " - Shortcut: " + self.hotkey

    def __eq__(self, o) -> bool:
        return self.barcode == o.barcode

class BarcodeElementEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

#--------------------------------------------------------------------
#region DATA ACCESS LAYER

def AddBarcode(barcode, shortcut):
    barcodeList.append(BarcodeElement(barcode, shortcut))

def DeleteBarcode(barcodeToDelete):
    global barcodeList
    barcodeList = [barcode for barcode in barcodeList if barcode.barcode != barcodeToDelete ]
#endregion