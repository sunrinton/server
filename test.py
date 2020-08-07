import pymongo
from pymongo import MongoClient
import csv

conn=MongoClient('localhost',27017)
db=conn['sunrinton']
table=db['data']
with open('./data.csv','r',encoding='utf-8') as fp:
    data=fp
    table.delete_many({})
    n=0
    for i in data:
        print(i)
        n+=1
        line=i.split(',')
        table.insert_one({'index':n,'word':line[0],'mean':line[1],'sentence':line[2][0:-1]})    
        
    fp.close()

