# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

from pymongo import MongoClient
'''
常用mongodb api 
client.list_database_names()  查所以表名
client.admin 选择db
collection = client.admin.g4d301 选择集合
collection .insert_one/insert_many 插入
collection find/find_one 查找
'''


class Slag(object):

    def __init__(self):
        self.client = None
        self.db = None
        self.client_list = None

    def link_client(self, dburl='localhost', port=27017):
        # 连接db
        try:
            self.client = MongoClient(dburl, port, serverSelectionTimeoutMS=10)
            self.client.admin.command('ping')
            self.client_list = self.client.list_database_names()
            print('client links success')
        except Exception as e:
            self.client = None
            print('client links fail', e)

    def db_is_exist(self, db):
        # db是否存在
        if db in self.client_list:
            print("db exists")
            return True
        else:
            print("err")
            return False

    def link_db(self, db='admin'):
        if not self.db_is_exist(db):
            print('db links error,please relink')
            self.db = None
            return
        # 获取数据库
        self.db = self.client.get_database(db)

    def link_coll(self, collection='G4D301'):
        if self.db is None:
            print('collection links error,please retry')
            return None
        # 连接集合
        return self.db.get_collection(collection)

    @staticmethod
    def cal_slag_thickness1(coeff, var):
        if len(coeff) != 4:
            print("coefficient error")
            return False
        return (coeff[0]+coeff[2] * var)/(1+coeff[1] * var+ coeff[3] * var ** 2)

    @staticmethod
    def cal_slag_thickness2(coeff, var):
        if len(coeff) != 4:
            print("coefficient error")
            return False
        return (coeff[0]+coeff[2] * math.log(var))/(1+coeff[1] * math.log(var) + coeff[3] * math.log(var) ** 2)

    def b0_model(self):
        b0LayerCoeff = [-102.1569223, -0.0307082, 0.5377985, -9.393E-05]  # B0外层系数a b c d

        result = self.cal_slag_thickness1(b0LayerCoeff, xo[6])
        print(result)
        return result

    def b1b2_model(self):
        b1LowerLayerCoeff = [-105.2629217, -0.0228199, 0.325837, 7.695E-06]  # B1下层系数a b c d
        b1UpperLayerCoeff = [-93.79482751, -0.0229174, 0.3242479, 8.408E-06]  # B1上层系数a b c d
        b2LowerLayerCoeff = [-96.98242679, -0.0228389, 0.3235343, 7.401E-06]  # B2下层系数a b c d
        b2UpperLayerCoeff = [-84.43153341, -0.0228309, 0.3216437, 7.976E-06]  # B2上层系数a b c d

        result = self.cal_slag_thickness1(b1UpperLayerCoeff, 240)
        print(result)

    def s1s2s3_model(self):
        s1LowerLayerCoeff = [-82.75101831, -0.0228458, 0.3216399, 6.946E-06]  # S1下层系数a b c d
        s1UpperLayerCoeff = [-71.87864339, -0.0227861, 0.3191679, 7.551E-06]  # S1上层系数a b c d
        s2LowerLayerCoeff = [-71.43415199, -0.0227477, 0.3184581, 6.546E-06]  # S2下层系数a b c d
        s2UpperLayerCoeff = [-60.98525935, -0.0227598, 0.315542, 6.991E-06]  # S2上层系数a b c d
        s3LowerLayerCoeff = [-59.85052196, -0.0227241, 0.314578, 6.208E-06]  # S3下层系数a b c d
        s3UpperLayerCoeff = [-51.12396191, -0.0227079, 0.3130791, 6.663E-06]  # S3下层系数a b c d

        result = self.cal_slag_thickness1(s2LowerLayerCoeff, 200)
        print(result)

    def s4s5_model(self):
        s4LowerLayerCoeff = [-151.3863073, -0.0305225, 0.6515521, -6.423E-05]  # S4下层系数a b c d
        s4UpperLayerCoeff = [29.56025181, -0.6432605, -5.861591, 0.1038437]  # S4上层系数a b c d
        s5LowerLayerCoeff = [-122.3696102, -0.0293118, 0.6770175, -9.459E-05]  # S5下层系数a b c d
        s5UpperLayerCoeff = [5.853390403, -0.5476014, -1.1968025, 0.0758181]  # S5上层系数a b c d

        result = self.cal_slag_thickness2(s5UpperLayerCoeff, 132.3)
        print(result)

    def r1r2r3_model(self):
        r1LowerLayerCoeff = [-70.09545619, -0.0316336, 0.6061685, 2.624E-06]  # R1下层系数a b c d
        r1UpperLayerCoeff = [-47.76479636, -0.0314862, 0.6048967, 1.373E-06]  # R1上层系数a b c d
        r2LowerLayerCoeff = [-60.05258136, -0.031446, 0.6220929, -4.458E-07]  # R2下层系数a b c d
        r2UpperLayerCoeff = [-41.762378, -0.0313101, 0.6125091, -4.419E-06]  # R2上层系数a b c d
        r3LowerLayerCoeff = [-54.06005764, -0.0313791, 0.6161497, -3.345E-06]  # R3下层系数a b c d
        r3UpperLayerCoeff = [-39.41791166, -0.0312714, 0.6173207, -4.169E-06]  # R3下层系数a b c d

        result = self.cal_slag_thickness1(r3LowerLayerCoeff, 43.3)
        print(result)



if __name__ == '__main__':
    myslag = Slag()
    myslag.r1r2r3_model()
