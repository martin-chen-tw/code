# -*- coding: big5 -*-

def filter_land_data(land_data, filter_criteria):
    # �L�o��ơG�ˬd�C����ƬO�_�ŦX�L�o����
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

# ���]���g�a��ƶ��G�C�Ӧr���ܤ@���a�y���
land_data = [
    {'id': 1, 'area': 120, 'zoning': '��v��', 'owner': 'A���q', 'value': 100},
    {'id': 2, 'area': 80, 'zoning': '�ӷ~��', 'owner': 'B���q', 'value': 150},
    {'id': 3, 'area': 150, 'zoning': '��v��', 'owner': 'C���q', 'value': 200},
    {'id': 4, 'area': 90, 'zoning': '��v��', 'owner': 'D���q', 'value': 50},
]

# �d�ҹL�o����G�L�o��v�ϥB���n�j�󵥩�100�B���Ȥp�󵥩�150�����
filter_criteria = {'zoning': '��v��', 'min_area': 100, 'max_value': 150}

# ��ܭ쥻����ƩM�L�o�᪺���G
print(f"�쥻����ƪ�\n{land_data}\n����ƦC��ŦX�L�o���󪺸�ƦC��\n{filter_land_data(land_data, filter_criteria)}")