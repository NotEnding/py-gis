#-*- coding:utf-8 _*- 
""" 
@file: test2.py 
@time: 2021/01/22
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""


try:
    import gdal
except:
    from osgeo import gdal


#打开已有的 GeoTIF文件
dataset = gdal.Open("./gdata/ai.tif")

#快速查看一下当前对象可用的操作
# print(dir(dataset))

'''

dataset.GetDescription() 获得栅格的描述信息
dataset.RasterCount 获得栅格数据集的波段数
dataset.RasterXSize 栅格数据的宽度(X方向上的像素个数)
dataset.RasterYSize 栅格数据的高度(Y方向上的像素个数)
dataset.GetGeoTransform() 栅格数据的六参数。
GetProjection() 栅格数据的投影
'''

print(dataset.GetDescription())
print(dataset.RasterCount)
print(dataset.RasterXSize)
print(dataset.RasterYSize)
print(dataset.GetGeoTransform())
print(dataset.GetProjection())

#可以访问数据的元数据信息，元数据信息对于每个数据都是不一样的
print(dataset.GetMetadata())
