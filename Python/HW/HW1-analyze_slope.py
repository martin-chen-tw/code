# -*- coding: big5 -*-
def analyze_slope(elevation_data, threshold):
    #��l�ƿ�X�C��
    overthreshold_data = []
    for i in range(len(elevation_data)-1):
        #�p��ײv(X�t�ȻPY�t��)
        delta_x = elevation_data[i+1][0]-elevation_data[i][0]
        delta_y = elevation_data[i+1][1]-elevation_data[i][1]
        #�����ײv�O�_�W�L�֭ȡA�W�L��JTRUE�A�_�h��JFALSE
        if (delta_y/delta_x >= threshold):
            overthreshold_data.append("TURE")
        else:
            overthreshold_data.append("FALSE")
    return overthreshold_data

#��l�ƿ�J��
elevation_data = [[1,2],[2,4],[3,8],[4,16],[5,32],[6,64],[8,128]]
threshold = 16
print(f"��J�Ȭ�:{elevation_data}\n�W�L�֭Ȫ��ϰ즳:{analyze_slope(elevation_data, threshold)}")