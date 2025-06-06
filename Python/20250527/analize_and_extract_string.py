def analize_and_extract_string(descriptions):
    descriptions_tmp = {
        "地段編號": [],
        "城市": [],
        "總面積": [],
        "土地用途": []
    }

    for desc in descriptions:
        tmp_string = desc.split("，")
        descriptions_tmp["地段編號"].append(tmp_string[0].replace("地段編號", ""))
        descriptions_tmp["城市"].append(tmp_string[1].replace("位於", ""))
        descriptions_tmp["總面積"].append(tmp_string[2].replace("總面積", ""))
        descriptions_tmp["土地用途"].append(tmp_string[3])

    return descriptions_tmp

# 測試資料
descriptions = [
    "地段編號A12345，位於臺北市信義區，總面積250.75平方公尺，住宅用地",
    "地段編號Z78910，位於新北市板橋區，總面積180.30平方公尺，商業用地",
    "地段編號G64026，位於台北市文山區，總面積235.70平方公尺，工業用地",
    "地段編號I19980，位於新竹縣竹東鎮，總面積630.35平方公尺，能源用地",
    "地段編號U80130，位於彰化縣埔心鄉，總面積990.50平方公尺，教育用地",
]

# 呼叫並印出結果
descriptions_extracted = analize_and_extract_string(descriptions)
for i in range(len(descriptions)):
    print(f"地段編號: {descriptions_extracted['地段編號'][i]}")
    print(f"城市: {descriptions_extracted['城市'][i]}")
    print(f"總面積: {descriptions_extracted['總面積'][i]}")
    print(f"土地用途: {descriptions_extracted['土地用途'][i]}")
    print("------")
