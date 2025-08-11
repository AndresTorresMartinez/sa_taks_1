from abc import ABC, abstractmethod

class Builder(ABC):
    
    @property
    @abstractmethod
    def reporte(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def añadir_portada(self):
        pass
    
    @abstractmethod
    def añadir_graficos(self):
        pass
    
    @abstractmethod
    def añadir_tabla_movimientos(self):
        pass
    
    @abstractmethod
    def añadir_analisis_tendencias(self):
        pass
    
    @abstractmethod
    def añadir_pie_de_pagina(self):
        pass


class BuilderPDF(Builder):
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self._reporte = Reporte()
                
    @property
    def reporte(self):
        reporte = self._reporte
        self.reset()
        return reporte
                
    def añadir_portada(self, cliente: str, logotipo: str):
        self._reporte.añadir(f"Portada de {cliente}, {logotipo}")
        
    def añadir_graficos(self):
        self._reporte.añadir("Gráficos de reporte")
        
    def añadir_tabla_movimientos(self):
        self._reporte.añadir("Tabla de Movimientos")
        
    def añadir_analisis_tendencias(self):
        self._reporte.añadir("Análisis de Tendencias")
        
    def añadir_pie_de_pagina(self, asesor: str):
        self._reporte.añadir(f"Pie de Página, Asesor: {asesor}")
        
    def get_reporte(self):
        reporte = '\n'.join(self._reporte.parts)
        print(f"Reporte: \n{reporte}", end="\n")
    
        
class Reporte():
    
    def __init__(self):
        self.parts = []
        
    def añadir(self, part: any):
        self.parts.append(part)

if __name__ == "__main__":
    
    builder = BuilderPDF()
    cliente =  "Cliente 1"
    builder.añadir_portada(cliente, logotipo="src://")
    builder.añadir_graficos()
    builder.añadir_pie_de_pagina("Asesor 1")
    builder.get_reporte()

