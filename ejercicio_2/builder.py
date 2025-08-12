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
    def añadir_portada(self, cliente: str, logotipo: str):
        pass
    
    @abstractmethod
    def añadir_graficos(self):
        pass
    
    @abstractmethod
    def añadir_tabla_movimientos(self):
        pass
    
    @abstractmethod
    def añadir_analisis_tendencias(self, tendencias: list[int]):
        pass
    
    @abstractmethod
    def añadir_pie_de_pagina(self, asesor: str):
        pass

