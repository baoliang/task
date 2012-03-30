import csv
import os
file = open("/root/his_excel.txt")
from lib.store import insert
from lib.utils import print_err
def create_node():
    for line in file.readlines():
        try:
            os.mknod("/root/excel/"+line+".csv")
        except OSError:
            print "over"


for line in open("/root/his.txt").readlines():
    try:
        line  = line.split("	")
        if not len(line) > 3:
            line = line.split("	") 
        insert("loupanxinxi",{
            'name': line[0],
            'phone1': line[1],
            'phone2': line[2],
            'area': line[3],
            'area_name': line[4],
            'loc': line[5]
        })
            
    except:
        print '---------------king___________________'
        print line
        print_err()
def insert_file():        
    for line in file.readlines():
        try:
            list  = find("loupanxinxi", query={'area': line})
            writer = csv.writer(file("/root/excel/"+line+".csv",'wb'))
            writer.writerow(['名称', '电话', '电话', '面积', '小区', '地址'])
            for item in list:
                writer.writerow(
                    [
                        item.get('name'),
                        item.get('phone1'), 
                        item.get('phone2'),
                        item.get('area'),
                        item.get('area_name'),
                        item.get('loc')
                    ]
                )
        except:
            print_err()