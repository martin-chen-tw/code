def calculate_land_conversion_fee(original_usage, new_usage, area, base_price):
    if original_usage not in ("residential", "commercial", "industrial", "agricultural") or \
   new_usage not in ("residential", "commercial", "industrial", "agricultural"):
        print("error")
        return
    match original_usage,new_usage:
        case "agricultural","residential":
            ratio = 1.5
        case "agricultural","commercial":
            ratio = 2.0
        case "agricultural","industrial":
            ratio = 1.8
        case "residential","commercial":
            ratio = 1.2
        case "residential","industrial":
            ratio = 1.0
        case "commercial","industrial":
            ratio=0.8
        case "industrial","commercial":
            ratio = 1.5
        case "industrial", "residential":
            ratio = 0.7
        case "commercial", "residential":
            ratio = 0.7
        case _:
            if new_usage == "agricultural":
                ratio = 0.5
            else:
                return "Invalid conversion"
    return area * base_price * ratio

# ´ú¸Õ®×¨Ò
test_cases = [
    {
        "original_usage": "agricultural",
        "new_usage": "commercial",
        "area": 500,
        "base_price": 5000
    },
    {
        "original_usage": "residential",
        "new_usage": "industrial",
        "area": 800,
        "base_price": 6000
    },
    {
        "original_usage": "commercial",
        "new_usage": "residential",
        "area": 300,
        "base_price": 7000
    },
    {
        "original_usage": "industrial",
        "new_usage": "agricultural",
        "area": 1000,
        "base_price": 4000
    }
]
test_case_iter = iter(test_cases)
i = 0
for item in test_case_iter:
    tax = calculate_land_conversion_fee(item['original_usage'], item['new_usage'], item['area'], item['base_price'])   
    test_cases[i] = {**test_cases[i],'tax':tax}
    i+=1
print(test_cases)