from builders import BuilderPDF
from director import Director


if __name__ == "__main__":
    
    # Construcción directamente con el builder
    print("--------------- Reporte con builder directo ------------------------")
    builder = BuilderPDF()
    builder.añadir_portada("Cliente 1", logotipo="src://")
    builder.añadir_graficos()
    builder.añadir_pie_de_pagina("Asesor 1")
    builder.get_reporte()
    
    # Construcción con director para tendencias condicionadas
    print("---------------- Reporte con director y tendencias -----------------")
    director = Director()
    builder_director = BuilderPDF()
    director.builder = builder_director
    director.reporte_analisis_condicionado("Cliente director", "src_director", "Asesor director", [1, 1, 1, 1, 1, 1])
    builder_director.get_reporte()
    
    print("---------------- Reporte con director sin tendencias ---------------")
    director = Director()
    builder_director = BuilderPDF()
    director.builder = builder_director
    director.reporte_analisis_condicionado("Cliente director 2", "src_director 2", "Asesor director 2", [1, 1, 1, 1])
    builder_director.get_reporte()
