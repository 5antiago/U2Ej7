
class Hora:
    __Hora = int
    __Mins = int
    __Segs = int

    def __init__(self, h, m, s):
        self.__Hora = h
        self.__Mins = m
        self.__Segs = s
    def gethora(self):
        return int(self.__Hora)
    def getmins(self):
        return int(self.__Mins)
    def getsegs(self):
        return int(self.__Segs)

    def Mostrar(self):
        return str("{}:{}:{}".format(self.__Hora, self.__Mins, self.__Segs))

    def controla(self): 
        if self.__Segs >= 60:
            self.__Mins += 1
            self.__Segs -= 60
        if self.__Mins >= 60:
            self.__Hora += 1
            self.__Mins -= 60
        if self.__Hora >= 24:
            self.__Hora -= 24 
        