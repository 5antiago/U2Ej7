from Hora import Hora

class FechaHora:
    __Dia = int
    __Mes = int
    __Anio = int
    __Hora = int
    __Min = int
    __Segs = int
    __meses31 =[1,3,5,7,8,10,12]

    def __init__(self, dia = 1, mes = 1, anio = 2020, hora = 0, mins = 0, seg = 0):
        self.__Anio=anio
        self.__Mes=mes
        self.__Dia=dia
        self.__Hora=hora
        self.__Min=mins
        self.__Segs=seg
    def Mostrar(self):
        return str("{}/{}/{}  {}:{}:{}".format(self.__Dia, self.__Mes, self.__Anio, self.__Hora, self.__Min, self.__Segs))
    def getdia(self):
        return int(self.__Dia)
    def getmes(self):
        return int(self.__Mes)
    def getanio(self):
        return int(self.__Anio)
    def gethora(self):
        return int(self.__Hora)
    def getmins(self):
        return int(self.__Min)
    def getsegs(self):
        return int(self.__Segs)
    def PonerEnHora(self, hora=0, mins=0, seg=0):
        if type(hora) ==int and type(mins) == int and type(seg)==int :
            self.__Hora=hora
            self.__Min=mins
            self.__Segs=seg
    def AdelantarHora(self, hora=0, mins=0, seg=0):
        if type(hora) ==int and type(mins) == int and type(seg)==int :
            self.__Hora+=hora
            self.__Min+=mins
            self.__Segs+=seg
            self.controla()
    def controla(self):
        if self.__Segs >= 60:
            self.__Min += 1
            self.__Segs -= 60
        if self.__Min >= 60:
            self.__Hora += 1
            self.__Min -= 60
        if self.__Hora >= 24:
            self.__Hora -= 24
            self.__Dia += 1
        if self.__Dia >= 29 and self.__Mes == 2:
            if  (self.__Anio % 4 == 0 and self.__Anio % 100 != 0 or self.__Anio % 400 == 0) and self.__Dia == 29:
                pass
            else:
                self.__Dia = 1
                self.__Mes += 1 
        if self.__Dia >= 31:
            if self.__Dia == 31  and self.__Mes in self.__meses31:
                pass
            else:
                self.__Mes += 1
                self.__Dia = 1
        if self.__Mes > 12:
            self.__Mes = 1
            self.__Anio += 1
    def __add__(self, Dias):
        if type(Dias)== int:
            aux = FechaHora(self.__Dia + Dias, self.__Mes, self.__Anio, self.__Hora, self.__Min, self.__Segs)
            aux.controla()
            return aux
        elif type(Dias) == Hora:
            aux = FechaHora(self.__Dia, self.__Mes, self.__Anio, self.__Hora + Dias.gethora(), self.__Min + Dias.getmins(), self.__Segs + Dias.getsegs())
            aux.controla()
            return aux
    def __radd__(self, Dias):
        if type(Dias)== int:
            aux = FechaHora(self.__Dia + Dias, self.__Mes, self.__Anio, self.__Hora, self.__Min, self.__Segs)
            aux.controla()
            return aux
        elif type(Dias) == Hora:
            aux = FechaHora(self.__Dia, self.__Mes, self.__Anio, self.__Hora + Dias.gethora(), self.__Min + Dias.getmins(), self.__Segs + Dias.getsegs())
            aux.controla()
            return aux
    def __sub__(self, Dias):
        if type(Dias)== int:
            return FechaHora(self.__Dia - Dias, self.__Mes, self.__Anio, self.__Hora , self.__Min, self.__Segs)
    def __rsub__(self, Dias):
        if type(Dias)== int:
            return FechaHora(self.__Dia - Dias, self.__Mes, self.__Anio, self.__Hora , self.__Min, self.__Segs)
    def __gt__(self, otro):
        if type(otro) == FechaHora:
            if self.__Hora > otro.gethora():
                return True
            else:
                return False
        elif type(otro) == int:
            if self.__Hora > otro.gethora():
                return True
            else:
                return False
