#-*- coding:utf-8 _*- 
""" 
@file: test1.py 
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
    import gdal  #早期导入方式
except:
    from osgeo import gdal  #现在推荐导入方式
    from osgeo.gdalconst import *


#查看系统支持的数据格式
drv_count = gdal.GetDriverCount()
for idx in range(drv_count):
    driver = gdal.GetDriver(idx)
    print("%10s: %s" % (driver.ShortName, driver.LongName))


#驱动注册
driver = gdal.GetDriverByName('GRASSASCIIGrid')
driver.Register()
if driver:
    print('register success')