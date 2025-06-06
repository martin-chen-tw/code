# �\�� 1�G�s�W�a�q���
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

# �\�� 2�G�d�ߥ\��]�ھګ����B�γ~�B�֦��̵�����^
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

# �\�� 3�G�έp�\��]�`���n�B�������i�{�ȡB���P�γ~�ƶq�^
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
        "owner": "�i�p��",
        "area": 250.75,
        "location": {
            "city": "�O�_��",
            "district": "�H�q��"
        },
        "zoning": "��v�Φa",
        "tax_value": 8500000
    },
    "B56789": {
        "owner": "���p��",
        "area": 180.3,
        "location": {
            "city": "�s�_��",
            "district": "�O����"
        },
        "zoning": "�ӷ~�Φa",
        "tax_value": 6500000
    },
    "C24680": {
        "owner": "���j��",
        "area": 320.0,
        "location": {
            "city": "�O����",
            "district": "�_��"
        },
        "zoning": "�u�~�Φa",
        "tax_value": 9200000
    }
}
# �s�W�a�q
add_land_record("D11111", "���@�@", 275.5, "�s�˿�", "�˥_��", "�Ш|�Φa", 7800000)

# �d�߯S�w�γ~
print("�i�d�ߥγ~���u�~�Φa�j")
industrial_lands = query_lands("zoning", "�u�~�Φa")
for k, v in industrial_lands.items():
    print(k, v)

# �έp��T
print("\n�i�έp��T�j")
stats = registry_statistics()
for key, val in stats.items():
    print(f"{key}: {val}")