#!/usr/bin/env python
# coding: utf-8


#menghubungkan python dengan mysql
import mysql.connector 
from mysql.connector import Error
def create_server_connection(host_name, user_name, user_password):
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: {err}")
    return connection

host = "localhost"
user = 'root'
pw = "hwxq6762"

# koneksi ke server
connection = create_server_connection(host, user, pw)




#Membuat database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database berhasil dibuat")
    except Error as err:
        print(f"Error: {err}")

# Membuat database mysql_python
create_database_query = """CREATE DATABASE IF NOT EXISTS lms"""
create_database(connection, create_database_query)




#fungsi koneksi dengan data base
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db)
        print("MySQL database connection successfull")
    except Error as err:
        print(f"Error: {err}")
    return connection

# definisi parameter
user = "root"
host = 'localhost'
pw = "hwxq6762"
db = "lms"

# koneksi ke database 'lms'
connection = create_db_connection(host, user, pw, db)




# membuat cursor
mydb = connection
mycursor = mydb.cursor(buffered=True)
c = mycursor




# membuat table user
sql = """CREATE TABLE IF NOT EXISTS table_user (
  user_id int NOT NULL AUTO_INCREMENT,
  nama_user varchar(50) NOT NULL,
  umur int,
  pekerjaan varchar(50),
  alamat varchar(500),
  tanggal_bergabung date,
  PRIMARY KEY (user_id)
  )"""
c.execute(sql)





# membuat table buku
sql = """CREATE TABLE IF NOT EXISTS buku (
    id_buku int NOT NULL,
    nama_buku varchar(50), 
    kategori varchar(50), 
    PRIMARY KEY (id_buku)
    )"""
c.execute(sql)





# membuat table peminjam
sql = """ CREATE TABLE IF NOT EXISTS peminjam (
  id_peminjam int NOT NULL AUTO_INCREMENT,
  user_id int NOT NULL,
  nama_user varchar(50),
  id_buku int NOT NULL,
  nama_buku varchar(50),
  jumlah_buku int NOT NULL,
  peminjaman_date date,
  pengembalian_date date,
  PRIMARY KEY (id_peminjam),
  KEY user_id (user_id),
  KEY id_buku (id_buku),
  FOREIGN KEY (user_id) REFERENCES table_user (user_id),
  FOREIGN KEY (id_buku) REFERENCES buku (id_buku)
  )"""
c.execute(sql)





# membuat table stock
sql ="""CREATE TABLE IF NOT EXISTS stock (
  id_buku int,
  stockin int,
  stockout int,
  KEY id_buku (id_buku),
  CONSTRAINT stock FOREIGN KEY (id_buku) REFERENCES buku (id_buku)
  )"""
c.execute(sql)





# membuat fungsi pendfataran user baru
def adduser():
    usernama = input("MASUKAN NAMA ANDA : ")
    userumur = input("MASUKAN UMUR ANDA : ")
    userpekerjaan = input("MASUKAN PEKERJAAN ANDA : ")
    useralamat = input("MASUKAN ALAMAT ANDA : ")
    data = (usernama,userumur,userpekerjaan,useralamat)
    sql = ("INSERT INTO table_user(nama_user,umur,pekerjaan,alamat,tanggal_bergabung) VALUES (%s,%s,%s,%s,curdate());")
    c.execute(sql,data)
    mydb.commit()
    print("...................")
    print("DATA BERHASIL DITAMBAHKAN!")
    main()




# membuat fungsi pendaftaran buku
def addbuku():
    bukukode = input("MASUKAN KODE BUKU : ")
    bukujudul = input("MASUKAN JUDUL BUKU :")
    bukukategori = input("MASUKAN KATEGORI BUKU : ")
    bukujumlah = int(input("MASUKAN JUMLAH BUKU : "))
    data1 = (bukukode,bukujudul,bukukategori)
    data2 = (bukukode,bukujumlah)
    sql1 = ("INSERT INTO buku(id_buku,nama_buku,kategori) VALUES (%s,%s,%s);")
    sql2 = ("INSERT INTO stock(id_buku,stockin) VALUES (%s,%s)")
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    mydb.commit()
    print("...................")
    print("BUKU BERHASIL DITAMBAHKAN!")
    main()




# mebuat fungsi peminjaman buku
def peminjaman():
    userid = input("MASUKAN ID USER : ")
    usernama = input("MASUKAN NAMA ANDA : ")
    bukukode = input("MASUKAN KODE BUKU YANG AKAN DIPINJAM : ")
    bukunama = input("MASUKAN JUDUL BUKU : ")
    bukujumlah = input("MASUKAN JUMLAH BUKU YANG AKAN DIPINJAM : ")
    tgl_pengembalian = input("MASUKAN TANGGAL PENGEMBALIAN (YYYY-MM-DD) : ")
    data1 = (userid,usernama,bukukode,bukunama,bukujumlah,tgl_pengembalian)
    data2 = (bukukode,bukujumlah)
    sql1 = ("INSERT INTO peminjam(user_id,nama_user,id_buku,nama_buku,jumlah_buku,peminjaman_date,pengembalian_date) VALUES (%s,%s,%s,%s,%s,curdate(),%s)")
    sql2 = ("INSERT INTO stock(id_buku,stockout) VALUES (%s,%s)")
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    mydb.commit()
    print("...................")
    print("BUKU BERHASIL DIPINJAM!")
    main()





# membuat fungsi menampilkan daftar buku
def daftarbuku():
    sql = """SELECT id_buku,nama_buku,kategori,SUM(stockin) - SUM(IFNULL(stockout, 0)) AS stock FROM buku JOIN stock USING (id_buku) GROUP BY id_buku;"""
    c.execute(sql)
    df = c.fetchall()
    for i in df:
        print("KODE BUKU :",i[0])
        print("JUDUL BUKU : ",i[1])
        print("KATEGORI : ",i[2])
        print("STOK : ", int(i[3]))
        print(" ")
    main()





# membuat fungsi menampilkan daftar user
def daftaruser():
    sql = "SELECT * FROM table_user"
    c.execute(sql)
    df = c.fetchall()
    for i in df:
        print("ID USER :",i[0])
        print("NAMA : ",i[1])
        print("UMUR : ",i[2])
        print("PEKERJAAN : ",i[3])
        print("ALAMAT : ",i[4])
        print("TANGGAL BERGABUNG : ",i[5])
        print(" ")
    main()





# membuat fungsi menampilkan daftar peminjaman
def daftarpeminjaman():
    sql = "SELECT * FROM peminjam"
    c.execute(sql)
    df = c.fetchall()
    for i in df:
        print("ID PEMINJAMAN : ",i[0])
        print("ID USER : ",i[1])
        print("NAMA : ",i[2])
        print("KODE BUKU : ",i[3])
        print("NAMA BUKU : ",i[4])
        print("JUMLAH PEMINJAMAN : ",i[5])
        print("TGL PEMINJAMAN : ",i[6])
        print("TGL PENGEMBALIAN : ",i[7])
    main()





# membuat fungsi pengembalian buku
def pengembalian():
    idpeminjaman = input("MASUKAN ID PEMINJAMAN : ")
    userid = input("MASUKAN ID USER : ")
    bukukode = input("MASUKAN KODE BUKU : ")
    bukujumlah = input("MASUKAN JUMLAH BUKU YANG AKAN DIKEMBALIKAN : ")
    data1 = (idpeminjaman,userid)
    data2 = (bukukode,bukujumlah)
    sql1 = ("DELETE FROM peminjam WHERE id_peminjam = %s and user_id = %s")
    sql2 = ("INSERT INTO stock(id_buku,stockin) VALUES (%s,%s)")
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    mydb.commit()
    print("...................")
    print("BUKU BERHASIL DIKEMBALIKAN!")
    main()





# membuat fungsi cari buku
def caribuku():
    bukukode = input("MASUKAN KODE BUKU : ")
    bukunama = input("MASUKAN JUDUL BUKU : ")
    data = (bukukode,)
    sql = ("SELECT id_buku, SUM(stockin) - SUM(IFNULL(stockout, 0)) AS stock FROM stock WHERE id_buku = %s GROUP BY id_buku;")
    c.execute(sql,data)
    df = c.fetchall()
    for i in df:
        print("KODE BUKU :",i[0])
        print("STOK : ",i[1])
        print(" ")
    main()




# fungsi main menu
def main():
    print("""
          ..........LIBRARY MANAGEMENT SYSTEM..........
          1. PENDAFTARAN USER BARU
          2. PENDAFTARAN BUKU BARU
          3. PEMINJAMAN
          4. DAFTAR BUKU
          5. DAFTAR USER
          6. DAFTAR PEMINJAMAN
          7. CARI BUKU
          8. PENGEMBALIAN
          9. EXIT
          """)
    choice = int(input("MASUKAN NO. PERINTAH : "))
    print("...............................")
    if choice == 1:
        adduser()
    elif choice == 2:
        addbuku()
    elif choice == 3:
        peminjaman()
    elif choice == 4:
        daftarbuku()
    elif choice == 5:
        daftaruser()
    elif choice == 6:
        daftarpeminjaman()
    elif choice == 7:
        caribuku()
    elif choice == 8:
        pengembalian()
    elif choice == 9:
        print("TERIMA KASIH :)")





main()

