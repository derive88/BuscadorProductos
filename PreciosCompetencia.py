# -*- coding: utf-8 -*-
from Tkinter import *
from bs4 import BeautifulSoup
import requests
import urllib3
import chardet
from re import sub

class Precios:
    def __init__(self):
        self.root = Tk()
        self.root.title("Buscar SAWERS")
        #self.root.geometry("1200x500+100+100")
        #cargando la cantidad de datos quitue tendra la ventana
        self.cantidad0 = 0 #cantidad de productos de tienda sawers
        self.cantidad1 = 0 #cantidad de productos de tecbolivia
        self.cantidad2 = 0 #cantidad de productos de i2cbolivia
        self.cantidad3 = 0 #cantidad de productos de importadora nova
        self.cantidad4 = 0 #cantidad de productos de black pig team
        self.refresh()

    def refresh(self):
        self.frame = Frame(self.root)
        self.frame.config(bg="white")
        self.frame.pack()
        self.instructionMessage = StringVar()
        Label(self.frame, textvariable = self.instructionMessage,bg="white").grid(row = 0)
        self.instructionMessage.set("Ingrese el nombre del producto a buscar")

        Label(self.frame, text = "PRODUCTO:",bg="white").grid(row = 1,column = 0)

        self.entry_product = Entry(self.frame,fg = "black",bg = "salmon")
        self.entry_product.grid(row = 2,column = 0)
        self.entry_product.insert(ANCHOR,"")

        b = Button(self.frame, text = "BUSCAR", command = self.ok,fg = "black",bg = "red")
        b.grid(row = 3,column = 0)
        Label(self.frame, text = "PRECIOS EN TIENDAS",bg = "white").grid(row = 4,column = 0)

        #SAWERS
        bandera = 5 #para ordenar todo lo que se mostrara inicia en sawers
        Label(self.frame, text = "Tienda Sawers",fg = "white",bg = "orange red").grid(row = bandera,column = 0,sticky = W+E+N+S)
        Label(self.frame, text = "Precio",fg = "white",bg = "orange red").grid(row = bandera,column = 1,sticky = W+E+N+S)
        Label(self.frame, text = "Stock",fg = "white",bg = "orange red").grid(row = bandera,column = 2,sticky = W+E+N+S)
        if self.cantidad0 == 0:
            bandera = bandera + 1
            Label(self.frame, text = "Sin producto",fg = "red",bg = "gold").grid(row = bandera,column = 0, sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "gold").grid(row = bandera,column = 1,sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "gold").grid(row = bandera,column = 2,sticky = W+E+N+S)
        else:
            for r in range(self.cantidad0):
                bandera = bandera + 1
                Label(self.frame, text = self.productosawers[r],fg = "black",bg = "gold").grid(row = bandera,column = 0, sticky = W+E+N+S)
                Label(self.frame, text = self.preciosawers[r],fg = "black",bg = "gold").grid(row = bandera,column = 1, sticky = W+E+N+S)
                Label(self.frame, text = self.stocksawers[r],fg = "black",bg = "gold").grid(row = bandera,column = 2, sticky = W+E+N+S)
        #TECBOLIVIA
        bandera = bandera + 1
        Label(self.frame, text = "TecBolivia",fg = "white",bg = "dark green").grid(row = bandera,column = 0,sticky = W+E+N+S)
        Label(self.frame, text = "Precio",fg = "white",bg = "dark green").grid(row = bandera,column = 1,sticky = W+E+N+S)
        Label(self.frame, text = "Stock",fg = "white",bg = "dark green").grid(row = bandera,column = 2,sticky = W+E+N+S)
        if self.cantidad1 == 0:
            bandera = bandera + 1
            Label(self.frame, text = "Sin producto",fg = "red",bg = "lime").grid(row = bandera,column = 0, sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "lime").grid(row = bandera,column = 1,sticky = W+E+N+S)
            Label(self.frame, text = "N/A",fg = "red",bg = "lime").grid(row = bandera,column = 2,sticky = W+E+N+S)
        else:
            for r in range(self.cantidad1):
                bandera = bandera + 1
                Label(self.frame, text = self.productoTecbolivia[r],fg = "black",bg = "lime").grid(row = bandera,column = 0, sticky = W+E+N+S)
                Label(self.frame, text = self.precioTecbolivia[r],fg = "black",bg = "lime").grid(row = bandera,column = 1, sticky = W+E+N+S)
                Label(self.frame, text = 'N/A',fg = "black",bg = "lime").grid(row = bandera,column = 2, sticky = W+E+N+S)
        #I2CBOLIVIA
        bandera = bandera + 1
        Label(self.frame, text = "I2cBolivia",fg = "white",bg="steel blue").grid(row = bandera,column = 0,sticky = W+E+N+S)
        Label(self.frame, text = "Precio",fg = "white",bg = "steel blue").grid(row = bandera,column = 1,sticky = W+E+N+S)
        Label(self.frame, text = "Stock",fg = "white",bg = "steel blue").grid(row = bandera,column = 2,sticky = W+E+N+S)
        if self.cantidad2 == 0:
            bandera = bandera + 1
            Label(self.frame, text = "Sin producto",fg = "red",bg = "turquoise").grid(row = bandera,column = 0, sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "turquoise").grid(row = bandera,column = 1,sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "turquoise").grid(row = bandera,column = 2,sticky = W+E+N+S)
        else:
            for r in range(self.cantidad2):
                bandera = bandera + 1
                Label(self.frame, text = self.productoi2c[r],fg = "black",bg = "turquoise").grid(row = bandera,column = 0, sticky = W+E+N+S)
                Label(self.frame, text = self.precioi2c[r],fg = "black",bg = "turquoise").grid(row = bandera,column = 1, sticky = W+E+N+S)
                Label(self.frame, text = self.stocki2c[r],fg = "black",bg = "turquoise").grid(row = bandera,column = 2, sticky = W+E+N+S)
        #IMPORTADORA NOVA
        bandera = bandera + 1
        Label(self.frame, text = "Importadora Nova",fg = "white",bg = "blue").grid(row = bandera,column = 0,sticky = W+E+N+S)
        Label(self.frame, text = "Precio",fg = "white",bg = "blue").grid(row = bandera,column = 1,sticky = W+E+N+S)
        Label(self.frame, text = "Stock",fg = "white",bg = "blue").grid(row = bandera,column = 2,sticky = W+E+N+S)
        if self.cantidad3 == 0:
            bandera = bandera + 1
            Label(self.frame, text = "Sin producto",fg = "red",bg = "royal blue").grid(row = bandera,column = 0, sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "royal blue").grid(row = bandera,column = 1,sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "royal blue").grid(row = bandera,column = 2,sticky = W+E+N+S)
        else:
            for r in range(self.cantidad3):
                bandera = bandera + 1
                Label(self.frame, text = self.productonova[r],fg = "black",bg = "royal blue").grid(row = bandera,column = 0, sticky = W+E+N+S)
                Label(self.frame, text = self.precionova[r],fg = "black",bg = "royal blue").grid(row = bandera,column = 1, sticky = W+E+N+S)
                Label(self.frame, text = self.stocknova[r],fg = "black",bg = "royal blue").grid(row = bandera,column = 2, sticky = W+E+N+S)
        #BLACK PIG TEAM
        bandera = bandera + 1
        Label(self.frame, text = "black pig team",fg = "white",bg = "black").grid(row = bandera,column = 0,sticky = W+E+N+S)
        Label(self.frame, text = "Precio",fg = "white",bg = "black").grid(row = bandera,column = 1,sticky = W+E+N+S)
        Label(self.frame, text = "Stock",fg = "white",bg = "black").grid(row = bandera,column = 2,sticky = W+E+N+S)
        if self.cantidad4 == 0:
            bandera = bandera + 1
            Label(self.frame, text = "Sin producto",fg = "red",bg = "gray").grid(row = bandera,column = 0, sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "gray").grid(row = bandera,column = 1,sticky = W+E+N+S)
            Label(self.frame, text = "0",fg = "red",bg = "gray").grid(row = bandera,column = 2,sticky = W+E+N+S)
        else:
            for r in range(self.cantidad4):
                bandera = bandera + 1
                Label(self.frame, text = self.productoblackpig[r],fg = "black",bg = "gray").grid(row = bandera,column = 0, sticky = W+E+N+S)
                Label(self.frame, text = self.precioblackpig[r],fg = "black",bg = "gray").grid(row = bandera,column = 1, sticky = W+E+N+S)
                Label(self.frame, text = self.stockblackpig[r],fg = "black",bg = "gray").grid(row = bandera,column = 2, sticky = W+E+N+S)

        self.root.protocol('WM_DELETE_WINDOW', self.no)

        self.root.mainloop()

    #LLAMADOR DE BUSQUEDAS(NECESARIO SEPARAR PARA EVITAR ERRORES)
    def ok(self):
        self.cantidad0 = 0
        self.cantidad1 = 0
        self.cantidad2 = 0
        self.cantidad3 = 0
        self.cantidad4 = 0
        #self.top = Toplevel()
        #self.top.title('BUSCANDO')
        self.sawers()
        #Message(self.top, text='BUSCANDO EN SAWERS', padx=20, pady=20).pack()
        self.tecbolivia()
        self.i2c()
        self.nova()
        self.blackpig()
        #self.top.destroy
        self.frame.destroy()
        self.refresh()

    def sawers(self):
        #primer buscador en tienda sawers
        nombre = self.entry_product.get()
        producto = nombre.replace(' ', '%20')
        URL='http://tienda.sawers.com.bo/index.php?route=product/search&search='+producto
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            self.productosawers = []
            self.preciosawers = []
            self.stocksawers = []
            #del self.productosawers[:]
            #del self.preciosawers[:]
            html = BeautifulSoup(req.text, "html.parser")
            entradas = html.find_all('div', {'class': 'caption'})
            for i, entrada in enumerate(entradas):
                producto = entrada.find('div', {'class': 'name-product'}).getText()
                precio = entrada.find('p', {'class': 'price'}).getText()
                precio1 = "".join(line.strip() for line in precio.split("\n"))
                self.cantidad0 = self.cantidad0 + 1
                self.productosawers.append(producto)
                self.preciosawers.append(precio1)
                enlace = entrada.find('a')['href']
                req2 = requests.get(enlace)
                html2 = BeautifulSoup(req2.text, "html.parser")
                stock = html2.find('ul', {'class': 'list-unstyled product-section'}).getText()
                cadena = sub("\D", "", stock)
                cadena1 = cadena.encode('utf-8')
                digitos = cadena1[0]+cadena1[1]+cadena1[2]+cadena1[3]+cadena1[4]
                final = cadena1.replace(digitos,'')
                self.stocksawers.append(final)
        else:
            print "Status Code %d" % status_code

    def tecbolivia(self):
        #segundo buscador en tecbolivia
        nombre = self.entry_product.get()
        producto = nombre.replace(' ', '+')
        URL='http://www.tecbolivia.com/index.php/venta-de-componentes-electronicos-11/search?keyword='+ producto +'&limitstart=0&option=com_virtuemart&view=category'
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            html = BeautifulSoup(req.text, "html.parser")
            self.productoTecbolivia = []
            self.precioTecbolivia = []
            #del self.productoTecbolivia[:]
            #del self.precioTecbolivia[:]
            entradas = html.find_all('div', {'class': 'width70 floatright'})
            for i, entrada in enumerate(entradas):
                producto = entrada.find('a').getText()
                precio = entrada.find('span', {'class': 'PricesalesPrice'}).getText()
                self.cantidad1 = self.cantidad1 + 1
                self.productoTecbolivia.append(producto)
                self.precioTecbolivia.append(precio)
        else:
            print "Status Code %d" % status_code

    def i2c(self):
        #tercer buscador en i2c
        nombre = self.entry_product.get()
        producto = nombre.replace(' ', '+')
        URL='http://i2celectronica.com/search?controller=search&orderby=position&orderway=desc&search_query='+ producto
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            self.productoi2c = []
            self.precioi2c = []
            self.stocki2c = []
            #del self.productoi2c[:]
            #del self.precioi2c[:]
            html = BeautifulSoup(req.text, "html.parser")
            entradas = html.find_all('div', {'class': 'right-block'})
            for i, entrada in enumerate(entradas):
                #producto = entrada.find('a').getText()
                producto = entrada.find('a')['title']
                precio = entrada.find('span', {'class': 'price product-price'}).getText()
                producto1 = "".join(line.strip() for line in producto.split("\n"))
                precio1 = "".join(line.strip() for line in precio.split("\n"))
                self.cantidad2 = self.cantidad2 + 1
                self.productoi2c.append(producto1)
                self.precioi2c.append(precio1)
                #stock de cada producto
                enlace=entrada.find('a')['href']
                req2 = requests.get(enlace)
                html2 = BeautifulSoup(req2.text, "html.parser")
                #cantidades = html2.find_all('div', {'class': 'pb-center-column col-xs-12 col-sm-4'})
                stock = html2.find('span', {'id': 'quantityAvailable'}).getText()
                self.stocki2c.append(stock)
                #for i, cantidad in enumerate(cantidades):
                    #stock = cantidad.find('span', {'id': 'quantityAvailable'}).getText()
                    #self.stocki2c.append(stock)
        else:
            print "Status Code %d" % status_code

    def nova(self):
        #cuarto buscador en importadora nova
        nombre = self.entry_product.get()
        producto = nombre.replace(' ', '+')
        URL='http://www.importadoranova.com/search?controller=search&orderby=position&orderway=desc&search_query='+producto+'&submit_search=Buscar'
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            self.productonova = []
            self.precionova = []
            self.stocknova = []
            html = BeautifulSoup(req.text, "html.parser")
            entradas = html.find_all('div', {'class': 'right_block'})
            for i, entrada in enumerate(entradas):
                producto = entrada.find('a')['title']#.getText()
                precio = entrada.find('span', {'class': 'price'}).getText()
                self.cantidad3 = self.cantidad3 + 1
                self.productonova.append(producto)
                self.precionova.append(precio)
                #stock
                stock=entrada.find('span', {'class': 'availability'}).getText()
                if stock == 'Disponibles':
                    stock1 = 'SI'
                else:
                    stock1 = 'NO'
                self.stocknova.append(stock1)
        else:
            print "Status Code %d" % status_code

    def blackpig(self):
        #quinto buscador en importadora black pig
        nombre = self.entry_product.get()
        producto = nombre.replace(' ', '+')
        URL='http://blackpigteam.com/index.php?controller=search&orderby=position&orderway=desc&search_query='+ producto +'&submit_search='
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        req = requests.get(URL, headers = headers)
        status_code = req.status_code
        if status_code == 200:
            self.productoblackpig = []
            self.precioblackpig = []
            self.stockblackpig = []
            #del self.productoblackpig[:]
            #del self.precioblackpig[:]
            html = BeautifulSoup(req.text, "html.parser")
            entradas = html.find_all('div', {'class': 'right-block'})
            for i, entrada in enumerate(entradas):
                producto = entrada.find('a')['title']
                precio = entrada.find('span', {'class': 'price product-price'}).getText()
                precio1 = "".join(line.strip() for line in precio.split("\n"))
                self.cantidad4 = self.cantidad4 + 1
                self.productoblackpig.append(producto)
                self.precioblackpig.append(precio1)
                #stock de cada producto
                enlace=entrada.find('a')['href']
                req2 = requests.get(enlace, headers = headers)
                status_code1 = req2.status_code
                html2 = BeautifulSoup(req2.text, "html.parser")
                stock = html2.find('span', {'id': 'quantityAvailable'}).getText()
                self.stockblackpig.append(stock)
        else:
            print "Status Code %d" % status_code

    def no(self):
        self.root.destroy()


if __name__ == "__main__":

    PreciosCompetencia = Precios()