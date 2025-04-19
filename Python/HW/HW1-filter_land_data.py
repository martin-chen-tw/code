# -*- coding: big5 -*-

def filter_land_data(land_data, filter_criteria):
    # 過濾函數：檢查每條資料是否符合過濾條件
    filtered_data = filter(
        lambda data: (
            (filter_criteria.get('max_id') is None or data['id'] <= filter_criteria['max_id']) and
            (filter_criteria.get('spec_area') is None or data['area'] == filter_criteria['spec_area']) and
            (filter_criteria.get('zoning') is None or data['zoning'] == filter_criteria['zoning']) and
            (filter_criteria.get('min_area') is None or data['area'] >= filter_criteria['min_area']) and
            (filter_criteria.get('max_value') is None or data['value'] <= filter_criteria['max_value'])
        ),land_data
    )
    return list(filtered_data)

# 假設的土地資料集：每個字典表示一條地籍資料
land_data = [
    {'id': 1, 'area': 120, 'zoning': '住宅區', 'owner': 'A公司', 'value': 100},
    {'id': 2, 'area': 80, 'zoning': '商業區', 'owner': 'B公司', 'value': 150},
    {'id': 3, 'area': 150, 'zoning': '住宅區', 'owner': 'C公司', 'value': 200},
    {'id': 4, 'area': 90, 'zoning': '住宅區', 'owner': 'D公司', 'value': 50},
]

# 範例過濾條件：過濾住宅區且面積大於等於100且價值小於等於150的資料
filter_criteria = {'zoning': '住宅區', 'min_area': 100, 'max_value': 150}

# 顯示原本的資料和過濾後的結果
print(f"原本的資料表\n{land_data}\n的資料列表符合過濾條件的資料列表\n{filter_land_data(land_data, filter_criteria)}")