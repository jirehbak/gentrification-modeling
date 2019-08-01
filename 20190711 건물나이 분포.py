import geopandas as gpd
import seaborn as sns

bc = gpd.read_file("C:/01 data/GIS/GIS건물통합정보/서울대입구.shp", encoding = 'utf-8')
hd = gpd.read_file("C:/01 data/GIS/GIS건물통합정보/홍대.shp", encoding = 'utf-8')
gg = gpd.read_file("C:/01 data/GIS/GIS건물통합정보/가로수길.shp", encoding = 'utf-8')
sl = gpd.read_file("C:/01 data/GIS/GIS건물통합정보/AL_11_D010_20190706.shp")

len(bc) # 694
len(hd) # 397
len(gg) # 498
len(sl) # 691,539

bc = bc[bc.A13.notnull()]
hd = hd[hd.A13.notnull()]
gg = gg[gg.A13.notnull()]
sl = sl[sl.A13.notnull()]

len(bc) # 590
len(hd) # 353
len(gg) # 485
len(sl) # 552,918

bc['age'] = 2019 - bc.A13.str[:4].astype(int)
hd['age'] = 2019 - hd.A13.str[:4].astype(int)
gg['age'] = 2019 - gg.A13.str[:4].astype(int)

bc.to_csv("C:/01 data/GIS/GIS건물통합정보/서울대입구.csv", encoding = 'cp949')
hd.to_csv("C:/01 data/GIS/GIS건물통합정보/홍대.csv", encoding = 'cp949')
gg.to_csv("C:/01 data/GIS/GIS건물통합정보/가로수길.csv", encoding = 'cp949')


sl['con_yr'] = sl.A13.str.split('-', expand = True)[0]
sl['con_yr'] = sl['con_yr'].str[:4]
sl['age'] = 2019 - sl['con_yr'].astype(float)
sl = sl[sl.age >= 0]
sl = sl[sl.age <= 40]

bc = bc[bc.age <= 40]
hd = hd[hd.age <= 40]
gg = gg[gg.age <= 40]

bc['age'].describe()
hd['age'].describe()
gg['age'].describe()
sl['age'].describe()

sns.distplot(bc['age'])
sns.distplot(hd['age'])
sns.distplot(gg['age'])
sns.distplot(sl['age'])

bc.age.hist(bins = 8)
hd.age.hist(bins = 8)
gg.age.hist(bins = 8)
sl.age.hist(bins = 8)

bc['con_year'] = bc['A13'].str[:4].astype(int)
bc_yr = bc.groupby('con_year')['A0'].count().reset_index()
len(bc)
bc_yr['con_rate'] = bc_yr['A0'] / len(bc) * 100

hd['con_year'] = hd['A13'].str[:4].astype(int)
hd_yr = hd.groupby('con_year')['A0'].count().reset_index()
len(hd)
hd_yr['con_rate'] = hd_yr['A0'] / len(hd) * 100
