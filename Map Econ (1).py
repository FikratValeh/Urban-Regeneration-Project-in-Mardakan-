#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipyleaflet import Map, basemaps, basemap_to_tiles, Circle, LayersControl, LegendControl, FullScreenControl, Rectangle, Polygon
import pandas as pd
import os
os.chdir('C:/Users/Fikrat Valehli/Downloads')

map_df = pd.read_excel('mardakan_map_main.xlsx')
map_social_index = pd.read_excel('mardakanin mapi.xlsx')
social_map_df = map_social_index['index_social']
cars_df = map_social_index['how_worried_you_are_because_of_cars_in_Mardakan']
narcos_df = map_social_index['how_worried_of_narcoaddicts']
pandemic_econ_df = map_social_index['pandemic_income_impact']
pandemic_social_df =map_social_index['pandemic_neighbor_relationship_impact']
police_df = map_social_index['religion_intensity']
education_df = map_social_index['education_level']
move_out_df = map_social_index['willing_to_move_out']
trust_df = map_social_index['neighbo_trust']
cordinates_df = [[(40.490966, 50.141218), (40.491434, 50.141133), (40.491464, 50.141617), (40.491213, 50.141776), (40.490966, 50.141742)],
[(40.491063, 50.139966), (40.491336, 50.139966), (40.491369, 50.140536), (40.491023, 50.140560)],
[(40.491362, 50.140734), (40.491781, 50.140633), (40.491805, 50.141263), (40.491464, 50.141617)],
[(40.491348, 50.139927), (40.491527, 50.139816), (40.491786, 50.140608), (40.491384, 50.140707)],
[(40.491365, 50.139202), (40.491563, 50.139755), (40.491336, 50.139953), (40.491055, 50.139975), (40.491082, 50.139577)],
[(40.490660, 50.139501), (40.491313, 50.139203), (40.491073, 50.139554), (40.491029, 50.140066), (40.490772, 50.140069)],
[(40.491551, 50.139757), (40.491943, 50.139595), (40.492088, 50.141106), (40.491814, 50.141268), (40.491805, 50.140626)],
[(40.490792, 50.140135), (40.491021, 50.140090), (40.490991, 50.140686), (40.490382, 50.140899), (40.490261, 50.140463), (40.490760, 50.140367)],
[(40.491785, 50.137973), (40.492655, 50.138027), (40.491841, 50.138775)],
[(40.492387, 50.138353), (40.492766, 50.139013), (40.492795, 50.139174), (40.492325, 50.139620)],
[(40.493119, 50.137988), (40.493189, 50.138407), (40.492763, 50.139148), (40.492746, 50.139009), (40.492372, 50.138322)],
[(40.492784, 50.139174), (40.492897, 50.139681), (40.492378, 50.139835), (40.492328, 50.139593)],
[(40.492880, 50.139712), (40.492979, 50.140218), (40.492404, 50.140502), (40.492398, 50.139800)],
[(40.492979, 50.140218), (40.493093, 50.140625), (40.492448, 50.140982), (40.492375, 50.140552)],
[(40.493469, 50.139996), (40.493528, 50.140886), (40.493186, 50.140921), (40.493137, 50.140614), (40.492976, 50.140192)],
[(40.493140, 50.138415), (40.493446, 50.139140), (40.492827, 50.139455), (40.492775, 50.139167)],
[(40.493697, 50.137931), (40.493811, 50.138583), (40.493823, 50.139029), (40.493472, 50.139151), (40.493186, 50.138395), (40.493087, 50.138015)],
[(40.493858, 50.139052), (40.493922, 50.140003), (40.493502, 50.139996), (40.493443, 50.139163)],
[(40.493925, 50.140007), (40.493896, 50.140852), (40.493537, 50.140917), (40.493507, 50.139992)],
[(40.494115, 50.139435), (40.494185, 50.140786), (40.493881, 50.140879), (40.493927, 50.140003), (40.493854, 50.139456)],
[(40.494066, 50.137922), (40.494131, 50.139419), (40.493846, 50.139467), (40.493825, 50.139022), (40.493854, 50.138630), (40.493711, 50.137943)],
[(40.491739, 50.141253), (40.491881, 50.142031), (40.491868, 50.142507), (40.491215, 50.142267), (40.491151, 50.141697)],
[(40.491198, 50.142267), (40.491364, 50.142324), (40.491510, 50.143289), (40.491060, 50.143596), (40.491232, 50.142934)],
[(40.491391, 50.142356), (40.491844, 50.142493), (40.491841, 50.142636), (40.492287, 50.142929), (40.491545, 50.143272)],
[(40.492381, 50.141918), (40.492659, 50.142941), (40.491881, 50.142643), (40.491905, 50.142207)],
[(40.492020, 50.141096), (40.492517, 50.141852), (40.491871, 50.142207), (40.491881, 50.142043), (40.491773, 50.141243)],
[(40.492533, 50.141867), (40.492942, 50.142271), (40.492649, 50.142946), (40.492377, 50.141950)],
[(40.492939, 50.142252), (40.493418, 50.142909), (40.492663, 50.142952)],
[(40.493113, 50.140627), (40.493408, 50.141897), (40.493178, 50.142092), (40.492424, 50.140948)],
[(40.493430, 50.141901), (40.493561, 50.142872), (40.493457, 50.142919), (40.492934, 50.142262)],
[(40.493186, 50.140906), (40.494182, 50.140788), (40.494351, 50.141539), (40.494392, 50.142715), (40.493564, 50.142869), (40.493427, 50.141784)],
[(40.490404, 50.140912), (40.490772, 50.141020), (40.490772, 50.141285), (40.490289, 50.141377), (40.490212, 50.141029)],
[(40.490157, 50.140957), (40.490264, 50.141374), (40.489922, 50.141547), (40.489738, 50.141100)],
[(40.489976, 50.142259), (40.490155, 50.142522), (40.489656, 50.142828), (40.489559, 50.142373)],
[(40.489246, 50.141270), (40.489747, 50.141049), (40.489917, 50.141562), (40.489405, 50.141881)],
[(40.489199, 50.140838), (40.489602, 50.140579), (40.489768, 50.141070), (40.489262, 50.141294)],
[(40.489582, 50.140570), (40.489720, 50.140483), (40.490085, 50.140492), (40.490171, 50.140975), (40.489734, 50.141088)],
[(40.490083, 50.140421), (40.490271, 50.140433), (40.490391, 50.140882), (40.490164, 50.140987)],
[(40.490069, 50.141920), (40.490241, 50.142322), (40.490114, 50.142432), (40.490024, 50.142206), (40.489552, 50.142447), (40.489500, 50.142188)],
[(40.490141, 50.142495), (40.490243, 50.142638), (40.489743, 50.143126), (40.489677, 50.142805)],
[(40.490048, 50.139676), (40.490638, 50.139540), (40.490810, 50.140065), (40.490051, 50.140221)],
[(40.489939, 50.139523), (40.490048, 50.139865), (40.490077, 50.140464), (40.489714, 50.140477), (40.489576, 50.140585), (40.489483, 50.139896)],
[(40.489051, 50.139128), (40.489579, 50.138751), (40.489681, 50.139045), (40.489985, 50.139531), (40.489457, 50.139909)],
[(40.489454, 50.139887), (40.489592, 50.140577), (40.489213, 50.140815), (40.488972, 50.140312)],
[(40.489074, 50.139124), (40.489444, 50.139900), (40.488966, 50.140254), (40.488575, 50.139474)],
[(40.488713, 50.138051), (40.489074, 50.139098), (40.488544, 50.139511), (40.488006, 50.138283)],
[(40.490538, 50.138104), (40.490035, 50.138466), (40.489902, 50.137864), (40.490320, 50.137677)],
[(40.489546, 50.138844), (40.491119, 50.137851), (40.491257, 50.138026), (40.489651, 50.139020)],
[(40.489902, 50.137864), (40.490020, 50.138466), (40.489535, 50.138758), (40.489421, 50.138228)],
[(40.490839, 50.136930), (40.491109, 50.137717), (40.490542, 50.138104), (40.490237, 50.137473)],
[(40.490930, 50.136274), (40.490006, 50.137059), (40.490237, 50.137473), (40.490839, 50.136930)],
[(40.490064, 50.137152), (40.490304, 50.137618), (40.489917, 50.137909), (40.489707, 50.137404)],
[(40.489421, 50.138228), (40.489185, 50.137860), (40.489722, 50.137517), (40.489902, 50.137864)],
[(40.489138, 50.137777), (40.488991, 50.136870), (40.489424, 50.136666), (40.489636, 50.137482)],
[(40.488983, 50.136817), (40.488845, 50.136216), (40.489187, 50.135996), (40.489975, 50.137133), (40.489697, 50.137337), (40.489428, 50.136656)],
[(40.489318, 50.135915), (40.489656, 50.135776), (40.490052, 50.136302), (40.490379, 50.136248), (40.490573, 50.136606), (40.490011, 50.137067),(40.489597, 50.136489)],
[(40.490692, 50.135482), (40.489608, 50.135801), (40.489980, 50.136367), (40.490365, 50.136257), (40.490635, 50.136679), (40.490930, 50.136274)],
[(40.488931, 50.136130), (40.487848, 50.136604), (40.487914, 50.136964), (40.488948, 50.136378)],
[(40.491156, 50.141775), (40.491240, 50.142771), (40.490751, 50.142654), (40.490837, 50.142234), (40.490710, 50.141683)],
[(40.491222, 50.142784), (40.491241, 50.142939), (40.490991, 50.143364), (40.490614, 50.143226), (40.490674, 50.142691)],
[(40.490805, 50.142228), (40.490710, 50.142685), (40.490650, 50.143059), (40.490368, 50.143114), (40.490252, 50.142676), (40.490553, 50.142374)],
[(40.490367, 50.143115), (40.490408, 50.143834), (40.489996, 50.144041), (40.489820, 50.143400)],
[(40.489880, 50.143713), (40.490361, 50.145321), (40.490037, 50.145470), (40.489550, 50.143916)],
[(40.491335, 50.145321), (40.491540, 50.145958), (40.491311, 50.146301), (40.491047, 50.146264), (40.490835, 50.145598)],
[(40.490835, 50.145598), (40.491047, 50.146261), (40.491027, 50.146594), (40.490652, 50.146627), (40.490538, 50.145761)],
[(40.491040, 50.146671), (40.490890, 50.148103), (40.490589, 50.148153), (40.490647, 50.146741)],
[(40.491680, 50.150489), (40.492248, 50.150272), (40.492395, 50.150999), (40.491747, 50.151011)],
[(40.492120, 50.148596), (40.491842, 50.148608), (40.492001, 50.150183), (40.492306, 50.150083)],
[(40.491680, 50.150457), (40.490830, 50.150416), (40.490946, 50.151059), (40.491692, 50.151015)]]

df = pd.merge


m = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=15)
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)



map_df_status = map_df.economic_status
empty = [0] 
for i in cordinates_df:
    empty.append(1)
    index = len(empty) - 2
    if map_df_status[index] == 'Qazancım yoxdur':
        loc611 = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#d1fcff",
        fill_opacity = 1)
        m.add_layer(loc611) 
    elif map_df_status[index] == 'İmkansız':
        loc611 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#93eaef",
        fill_opacity = 1)
        m.add_layer(loc611)
    elif map_df_status[index] == 'Orta-aşağı imkanlı':
        loc611 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#35bfc8",
        fill_opacity = 1)
        m.add_layer(loc611)
    elif map_df_status[index] == 'Orta imkanlı':
        loc611 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#1b8389",
        fill_opacity = 1)
        m.add_layer(loc611)
    else:
        loc611 = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#004145",
        fill_opacity = 1)
        m.add_layer(loc611)
          
legend = LegendControl({"Qazancsız":"#d1fcff", "İmkansız":"#93eaef", 'Orta-aşağı imkanlı': "#35bfc8",
                       'Orta imkanlı' : "#1b8389", 'Orta Yuxarı və Yuxarı İmkanlı' : "#004145"}, 
                       name="Gəlir Səviyyəsinin Spatial Bölgüsü", position="topright")          
m.add_control(FullScreenControl())
m.add_control(legend)  
           
m





# In[ ]:





# In[3]:


l = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

l.add_layer(rectangle)  


empty_1 = [0] 
for i in cordinates_df:
    empty_1.append(1)
    index_1 = len(empty_1) - 2
    if social_map_df[index_1] == 1:
        loc61 = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#fcf4dd",
        fill_opacity = 1)
        l.add_layer(loc61) 
    elif social_map_df[index_1] == 2:
        loc61 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ffe295",
        fill_opacity = 1)
        l.add_layer(loc61)
    elif social_map_df[index_1] == 3:
        loc61 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ffc937",
        fill_opacity = 1)
        l.add_layer(loc61)
    elif social_map_df[index_1] == 4:
        loc61 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#dea202",
        fill_opacity = 1)
        l.add_layer(loc61)
    else:
        loc61 = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#997104",
        fill_opacity = 1)
        l.add_layer(loc61)
legend = LegendControl({"çox az sosial":"#fcf4dd", "az sosial":"#ffe295", 'orta sosial': "#ffc937",
                       'sosial' : "#dea202", 'çox sosial' : "#997104"}, 
                       name="Sosiallıq Şkalası", position="topright")          
l.add_control(FullScreenControl())
l.add_control(legend)  
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#CC6600', fill_opacity = 0)

l.add_layer(rectangle)          
l


# In[4]:


t = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

t.add_layer(rectangle)  

empty_2 = [0] 
for i in cordinates_df:
    empty_2.append(1)
    index_2 = len(empty_2) - 2
    if cars_df[index_2] == 1:
        loc6 = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#f6edfd",
        fill_opacity = 1)
        t.add_layer(loc6) 
    elif cars_df[index_2] == 2:
        loc6 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#e2cef6",
        fill_opacity = 1)
        t.add_layer(loc6)
    elif cars_df[index_2] == 3:
        loc6 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#d09ae3",
        fill_opacity = 1)
        t.add_layer(loc6)
    elif cars_df[index_2] == 4:
        loc6 = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#9860ab",
        fill_opacity = 1)
        t.add_layer(loc6)
    else:
        loc6 = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#562766",
        fill_opacity = 1)
        t.add_layer(loc6)
legend = LegendControl({"heç narahat olmuram":"#f6edfd", "çox az narahat olmuram":"#e2cef6", 'az narahat oluram': "#d09ae3",
                       'narahat oluram' : "#9860ab", 'çox narahat oluram' : "#562766"}, 
                       name="Maşınların Yaratdığı Narahatçılıq", position="topright")          
t.add_control(FullScreenControl())
t.add_control(legend)  
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#3D1452', fill_opacity = 0)

t.add_layer(rectangle)         
t


# In[5]:


e = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

e.add_layer(rectangle)  

empty_3 = [0] 
for i in cordinates_df:
    empty_3.append(1)
    index_3 = len(empty_3) - 2
    if narcos_df[index_3] == 1:
        loc = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#ffe6da",
        fill_opacity = 1)
        e.add_layer(loc) 
    elif narcos_df[index_3] == 2:
        loc = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ffb694",
        fill_opacity = 1)
        e.add_layer(loc)
    elif narcos_df[index_3] == 3:
        loc = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ff7838",
        fill_opacity = 1)
        e.add_layer(loc)
    elif narcos_df[index_3] == 4:
        loc = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ff5100",
        fill_opacity = 1)
        e.add_layer(loc)
    else:
        loc = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#b7430c",
        fill_opacity = 1)
        e.add_layer(loc)

legend = LegendControl({"heç narahat olmuram":"#ffe6da", "çox az narahat olmuram":"#ffb694", 'az narahat oluram': "#ff7838",
                       'narahat oluram' : "#ff5100", 'çox narahat oluram' : "#b7430c"}, 
                       name="Qəsəbədəki Narkotik Aludəçilərindən Narahatlıq", position="topright")          
e.add_control(FullScreenControl())
e.add_control(legend)  
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#990000', fill_opacity = 0)

e.add_layer(rectangle)
e


# In[5]:


p = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

p.add_layer(rectangle)  


empty_4 = [0] 
for i in cordinates_df:
    empty_4.append(1)
    index_4 = len(empty_4) - 2
    if pandemic_econ_df[index_4] == 1:
        lo = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#d1fcff",
        fill_opacity = 1)
        p.add_layer(lo) 
    elif pandemic_econ_df[index_4] == 2:
        lo = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#93eaef",
        fill_opacity = 1)
        p.add_layer(lo)
    elif pandemic_econ_df[index_4] == 3:
        lo = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#35bfc8",
        fill_opacity = 1)
        p.add_layer(lo)
    elif pandemic_econ_df[index_4] == 4:
        lo = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#1b8389",
        fill_opacity = 1)
        p.add_layer(lo)
    else:
        lo = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#004145",
        fill_opacity = 1)
        p.add_layer(lo)

legend = LegendControl({"heç təsir etmədi":"#d1fcff", "çox az təsir etdi":"#93eaef", 'zəif təsir etdi': "#35bfc8",
                       'pis təsir etdi' : "#1b8389", 'çox pis təsir etdi' : "#004145"}, 
                       name="Pandemiyanın Gəlirə Təsiri", position="topright")          
p.add_control(FullScreenControl())
p.add_control(legend)  
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#5C0A0A', fill_opacity = 0)

p.add_layer(rectangle)

p


# In[6]:


k = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

k.add_layer(rectangle)  

empty_5 = [0] 
for i in cordinates_df:
    empty_5.append(1)
    index_5 = len(empty_5) - 2
    if pandemic_social_df[index_5] == 'Əlaqələrimizi gücləndirdi':
        lott = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#ffddce",
        fill_opacity = 1)
        k.add_layer(lott) 
    elif pandemic_social_df[index_5] == 'Əlaqələrimizi zəiflətdi':
        lott = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#873d25",
        fill_opacity = 1)
        k.add_layer(lott)
    
    else:
        lott = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ffddce",
        fill_opacity = 1)
        k.add_layer(lott)

        
legend = LegendControl({"pandemiya qonşularla əlaqəmizi zəiflətdi":"#873d25", "pandemiya qonşularla əlaqəmizə təsir etmədi":"#ffddce"}, 
                       name="Pandemiyanın Münasibətlərə Təsiri", position="topright")

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#AAFF00', fill_opacity = 0)

k.add_layer(rectangle)
k.add_control(legend)  
k.add_control(FullScreenControl())

k


# In[18]:


polis = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_opacity = 1)
polis.add_layer(rectangle)
empty_6 = [0] 
for i in cordinates_df:
    empty_6.append(1)
    index_6 = len(empty_6) - 2
    if police_df[index_6] == 1:
        safe = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#d0f2ff",
        fill_opacity = 1)
        polis.add_layer(safe) 
    elif police_df[index_6] == 2:
        safe = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#95d2e8",
        fill_opacity = 1)
        polis.add_layer(safe)
    elif police_df[index_6] == 3:
        safe = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#5795ac",
        fill_opacity = 1)
        polis.add_layer(safe)
    elif police_df[index_6] == 4:
        safe = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#215d83",
        fill_opacity = 1)
        polis.add_layer(safe)
    else:
        safe = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#2b405a",
        fill_opacity = 1)
        polis.add_layer(safe)
legend = LegendControl({"dindar deyiləm":"#d0f2ff", "inancım zəifdir":"#95d2e8", 'neytral mövqedəyəm':'#5795ac', 
                       'dini inancım yüksəkdir':'#215d83', 'dini inancım çox güclüdür':'#2b405a'}, 
                       name="Əhalinin Dindarlıq Dərəcəsi", position="topright")




polis.add_control(legend)  
polis.add_control(FullScreenControl())

display(polis)


# In[22]:


educat = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

educat.add_layer(rectangle)  

empty_6 = [0] 
for i in cordinates_df:
    empty_6.append(1)
    index_6 = len(empty_6) - 2
    if education_df[index_6] == 'Məktəb':
        edu = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#f6edfd",
        fill_opacity = 1)
        educat.add_layer(edu) 
    elif education_df[index_6] == 'Peşə Məktəbi':
        edu = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#e2cef6",
        fill_opacity = 1)
        educat.add_layer(edu)
    elif education_df[index_6] == 'Texnikum & Kollec':
        edu = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#d09ae3",
        fill_opacity = 1)
        educat.add_layer(edu)
    elif education_df[index_6] == 'Bakalavr':
        edu = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#9860ab",
        fill_opacity = 1)
        educat.add_layer(edu)
    else:
        edu = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#562766",
        fill_opacity = 1)
        educat.add_layer(edu)
          
legend = LegendControl({"məktəb":"#f6edfd", "peşə məktəbi":"#e2cef6", 'texnikum & kollec':'#d09ae3', 
                       'bakalavr':'#9860ab', 'magistr':'#562766'}, 
                       name="Qəsəbənin Təhsil Səviyyəsi", position="topright")

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#FF7733', fill_opacity = 0)

educat.add_layer(rectangle)
educat.add_control(legend)  
educat.add_control(FullScreenControl())
educat


# In[7]:


w = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

w.add_layer(rectangle)  

empty_7 = [0] 
for i in cordinates_df:
    empty_7.append(1)
    index_7 = len(empty_7) - 2
    if move_out_df[index_7] == 'Bəli':
        tt = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#f0af00",
        fill_opacity = 1)
        w.add_layer(tt) 
    elif move_out_df[index_7] == 'Xeyr':
        tt = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ffe59f",
        fill_opacity = 1)
        w.add_layer(tt)
    
    else:
        tt = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#ffcd45",
        fill_opacity = 1)
        w.add_layer(tt)

        
legend = LegendControl({"Köçməyi Planlamıyanlar":"#ffe59f", 'Qərarsızlar':'#ffcd45', "Köçməyi Planlıyanlar":"#f0af00"}, 
                       name="Qəsəbədən Köçənlər", position="topright")

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'red', fill_opacity = 0)

w.add_layer(rectangle)
w.add_control(legend)  
w.add_control(FullScreenControl())

w


# In[8]:


trust = Map(basemap=basemaps.Esri.WorldTopoMap, center=(40.491244, 50.143200), zoom=14.85)
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = 'white', fill_color = 'white',
                      fill_opacity = 1)

trust.add_layer(rectangle)  


empty_8 = [0] 
for i in cordinates_df:
    empty_8.append(1)
    index_8 = len(empty_8) - 2
    if trust_df[index_8] == 1:
        tr = Polygon( 
        locations= i,
        color= 'white',
        weight = 2, 
        fill_color="#d1fcff",
        fill_opacity = 1)
        trust.add_layer(tr) 
    elif trust_df[index_8] == 2:
        tr = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#d1fcff",
        fill_opacity = 1)
        trust.add_layer(tr)
    elif trust_df[index_8] == 3:
        tr = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#35bfc8",
        fill_opacity = 1)
        trust.add_layer(tr)
    elif trust_df[index_8] == 4:
        tr = Polygon(
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#004145",
        fill_opacity = 1)
        trust.add_layer(tr)
    else:
        tr = Polygon( 
        locations= i,
        color= 'white',
        weight = 2,
        fill_color="#004145",
        fill_opacity = 1)
        trust.add_layer(tr)
          
legend = LegendControl({"güvənmirəm":"#d1fcff", 'neytral':'#35bfc8', 
                       'güvənirəm':'#004145'}, 
                       name="Sakinlərin Qonşularına Güvəni", position="topright")

rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#FF7733', fill_opacity = 0)

trust.add_layer(rectangle)
trust.add_control(legend)  
trust.add_control(FullScreenControl())
trust
from ipyleaflet import Map, basemaps, basemap_to_tiles, Circle, LayersControl, LegendControl, FullScreenControl, Rectangle
import pandas as pd
import os
import folium
os.chdir('C:/Users/Fikrat Valehli/Downloads')

mapvalues = pd.read_excel('mardakan_map.xlsx')
cordinates = mapvalues['cordinates']
cordinates


for i in range(0,69):
    circle = Circle()
    circle.location = (float(cordinates[i][1:10]), float(cordinates[i][12:21]))
    circle.radius = int((int(float(mapvalues['close_neighbor_number'][i])) + 8)**1.2)
    circle.color = "#ff5100"
    circle.weight = 1
    circle.fill_color =  '#ff5100'
    circle.fill_opacity = 0.3
    trust.add_layer(circle)
legend = LegendControl( {},
                       name="Qəsəbə Sakinlərinin Yaxın Olduqları Qonşu Sayı", position="bottomright")   
m.add_control(FullScreenControl())
  
rectangle = Rectangle(bounds=((40.495094, 50.152601), (40.486919, 50.134009)), weight = 2, color = '#5500FF', fill_opacity = 0)
trust.add_control(legend)
trust.add_layer(rectangle)         
trust


# In[ ]:




