# 功能 1：新增地段資料
def add_land_record(code, owner, area, city, district, zoning, tax_value):
    land_registry[code] = {
        "owner": owner,
        "area": area,
        "location": {
            "city": city,
            "district": district
        },
        "zoning": zoning,
        "tax_value": tax_value
    }

# 功能 2：查詢功能（根據城市、用途、擁有者等條件）
def query_lands(keyword, value):
    results = {}
    for code, info in land_registry.items():
        if keyword == "owner" and info["owner"] == value:
            results[code] = info
        elif keyword == "city" and info["location"]["city"] == value:
            results[code] = info
        elif keyword == "district" and info["location"]["district"] == value:
            results[code] = info
        elif keyword == "zoning" and info["zoning"] == value:
            results[code] = info
    return results

# 功能 3：統計功能（總面積、平均公告現值、不同用途數量）
def registry_statistics():
    total_area = 0
    total_value = 0
    count = 0
    zoning_count = {}

    for info in land_registry.values():
        total_area += info["area"]
        total_value += info["tax_value"]
        count += 1

        zoning = info["zoning"]
        if zoning not in zoning_count:
            zoning_count[zoning] = 0
        zoning_count[zoning] += 1

    avg_tax_value = total_value / count if count > 0 else 0

    return {
        "total_area": round(total_area, 2),
        "average_tax_value": round(avg_tax_value, 2),
        "zoning_distribution": zoning_count
    }


land_registry = {
    "A12345": {
        "owner": "張小明",
        "area": 250.75,
        "location": {
            "city": "臺北市",
            "district": "信義區"
        },
        "zoning": "住宅用地",
        "tax_value": 8500000
    },
    "B56789": {
        "owner": "李小華",
        "area": 180.3,
        "location": {
            "city": "新北市",
            "district": "板橋區"
        },
        "zoning": "商業用地",
        "tax_value": 6500000
    },
    "C24680": {
        "owner": "陳大仁",
        "area": 320.0,
        "location": {
            "city": "臺中市",
            "district": "北區"
        },
        "zoning": "工業用地",
        "tax_value": 9200000
    }
}
# 新增地段
add_land_record("D11111", "黃婷婷", 275.5, "新竹縣", "竹北市", "教育用地", 7800000)

# 查詢特定用途
print("【查詢用途為工業用地】")
industrial_lands = query_lands("zoning", "工業用地")
for k, v in industrial_lands.items():
    print(k, v)

# 統計資訊
print("\n【統計資訊】")
stats = registry_statistics()
for key, val in stats.items():
    print(f"{key}: {val}")