from db import DBConnection as mydb

class Datamahasiswa:

    def __init__(self):
        self.__id = None
        self.__nim = None
        self.__nama = None
        self.__kelas = None
        self.__matkul = None
        self.__tanggal_lahir = None

        self.conn = None
        self.affected = None
        self.result = None


    @property
    def id(self):
        return self.__id

    @property
    def nim(self):
        return self.__nim
        
    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def kelas(self):
        return self.__kelas
        
    @kelas.setter
    def kelas(self, value):
        self.__kelas = value

    @property
    def matkul(self):
        return self.__matkul
        
    @matkul.setter
    def matkul(self, value):
        self.__matkul = value

    @property
    def tanggal_lahir(self):
        return self.__tanggal_lahir
        
    @tanggal_lahir.setter
    def tanggal_lahir(self, value):
        self.__tanggal_lahir = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__kelas, self.__matkul, self.__tanggal_lahir)
        sql = "INSERT INTO Datamahasiswa (nim, nama, kelas, matkul, tanggal_lahir) VALUES " + str(val)

        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nim, self.__nama, self.__kelas, self.__matkul, self.__tanggal_lahir, id)
        sql = "UPDATE datamahasiswa SET nim = %s, nama = %s, kelas = %s, matkul = %s, tanggal_lahir = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nim):
        self.conn = mydb()
        val = (self.__nama, self.__kelas, self.__matkul, self.__tanggal_lahir, nim)
        sql = "UPDATE datamahasiswa SET nama = %s, kelas = %s, matkul = %s, tanggal_lahir = %s WHERE nim = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM datamahasiswa WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nim):
        self.conn = mydb()
        sql = "DELETE FROM datamahasiswa WHERE nim='" + str(nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM datamahasiswa WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)

        self.__id = self.result[0]
        self.__nim = self.result[1]
        self.__nama = self.result[2]
        self.__kelas = self.result[3]
        self.__matkul = self.result[4]
        self.__tanggal_lahir = self.result[5]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nim):
        a = str(nim)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM datamahasiswa WHERE nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if self.result != None:
           self.__id = self.result[0]
           self.__nim = self.result[1]
           self.__nama = self.result[2]
           self.__kelas = self.result[3]
           self.__matkul = self.result[4]
           self.__tanggal_lahir = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nim = ''
           self.__nama = ''
           self.__kelas = ''
           self.__matkul = ''
           self.__tanggal_lahir = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM datamahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql = "SELECT id, nama FROM datamahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result
