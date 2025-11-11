#detector_apk/.py
#main.py 

from kivi.app import app
from kivy.lang import Builder
from kivy.uix.boxlayout import Boxlayout
import csv, os


KV = '''
BoxLayout:
    orientation: "vertical"
    padding: 12
    TextInput:
    id: path
    hint_text: "/sdcard/Download/registro_llamadas.csv"
    size_hint_y: None
    heigth: "40dp"
Button:
    text:Analizar CSV"
    size_hint_y: None
    height: "40dp"
    on_release:
app.analizar(path.text)
 ScrollView:
     Label:
         id: out
         text:""
         size_hint_y: None
         height: self.texture_size [1]'''

class MyRoot(BoxLayout):
    pass

class detector_App(App):
    def build(self):
        return Builder.load_string(KV)
    
    def analizar(self,ruta):
        out = self.root.ids.out
        if not ruta or not 
        os.path.exists(ruta):
            out.text = 'Archivo no encontrado.'
            
            return
        encontrados = []
        with open(ruta, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                numero = row.get('Numero','').replace('','').replace('_','')
                if numero in 
                {"+5222412237988", "+525512345678"}:
                    
                    encontrados.append(f"{row.get('Numero')}-{row.get('fecha')}")
                    out.text = '\\n'.join(encontrados) if encontrados
                    else 'No se encontraron números.'
                    
                    if__name == '__main__':
                        DetectorApp().run()       