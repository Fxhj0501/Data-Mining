import joblib
import linecache
#id对应坐标
id_loc = joblib.load('/Users/fengzijian/PycharmProjects/DataMiningHW/DataMining/data/patient_idx_lat_lon.pkl')
del id_loc['52']
#data_num = {data:[id1,id2]}
data_num = {}
file = open("/Users/fengzijian/PycharmProjects/DataMiningHW/DataMining/data/date_num.txt")
filepath = r"/Users/fengzijian/PycharmProjects/DataMiningHW/DataMining/data/date_num.txt"
linenum = len(file.readlines())
num_data = {}
for i in range(1,linenum):
    lineinfo = linecache.getline(filepath,i)
    idx = lineinfo.index('日')
    data = lineinfo[2:idx+1]
    size = len(lineinfo)
    lineinfo = lineinfo[idx+5:size-3]
    lineinfo = lineinfo.split(',')
    data_num[data] = []
    for id in lineinfo:
        if id == lineinfo[0]:
            data_num[data].append(id)
            num_data[id] = data
        else:
            data_num[data].append(id[1:len(id)+1])
            num_data[id[1:len(id)+1]] = data
