import folium
import pandas as pd

# このCSVには、県庁所在地の緯度・経度がlatitudeカラムとlongitudeカラムに入っている。
df_prefecture = pd.read_csv("mapping_example.csv")

def visualize_locations(df,  zoom=4):
    # 図の大きさを指定する。
    f = folium.Figure(width=1000, height=500)

    # 初期表示の中心の座標を指定して地図を作成する。
    center_lat=34.686567
    center_lon=135.52000
    m = folium.Map([center_lat,center_lon], zoom_start=zoom).add_to(f)
        
    # データフレームの全ての行のマーカーを作成する。
    for i in range(0,len(df)):
        #※※dfのラベルは要変更
        folium.Marker(location=[df["35.65834150000001"][i],df["139.8017334"][i]]).add_to(m)
        
    return m
    
visualize_locations(df_prefecture).save("buildingMapping.html")