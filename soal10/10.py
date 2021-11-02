"""
NAMA: AHMAD FATHONI R
NPM: 1194002
KELAS: D4 TI 3A
"""


import shapefile

w=shapefile.Writer('./nomer10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")




w.poly([[[1,6], [5,6], [5,9], [1,9], [1,6]]])
w.poly([[[-5,5],[5,5], [5,-5],[-5,-5], [-5,5]]])
