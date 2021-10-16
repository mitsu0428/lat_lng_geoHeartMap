import folium
import pandas as pd

df_prefecture = pd.read_csv("mapping_example.csv")

def visualize_locations(df,  zoom=4):
    f = folium.Figure(width=1000, height=500)

    # 初期表示の中心の座標を指定して地図を作成する。
    center_lat=34.686567
    center_lon=135.52000
    m = folium.Map([center_lat,center_lon], zoom_start=zoom).add_to(f)
        
    for i in range(0,len(df)):
        #※※dfのラベルは要変更
        folium.Marker(location=[df["35.6413399"][i],df["139.6997705"][i]]).add_to(m)
        
    return m
    
visualize_locations(df_prefecture).save("buildingMapping.html")