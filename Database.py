import sqlite3

def createTables():
    
    koneksi=sqlite3.connect('financial.db')

    koneksi.execute("CREATE TABLE PEMASUKAN(Jumlah_Pemasukkan INT NOT NULL)")
    koneksi.execute("CREATE TABLE PENGELUARAN(Jumlah_Pengeluaran INT NOT NULL)")
    koneksi.commit()

    koneksi.close()

createTables()