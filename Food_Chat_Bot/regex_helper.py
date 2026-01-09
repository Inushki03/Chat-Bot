import re

def get_seesion(session:str):
    match=re.search(r"/sessions/(.*?)/contexts/",session)

    if match:
        extract_Session = match.group(1)
        return extract_Session
    
    return ""

def get_str_from_food_dict(food_dict:dict):
    
    result = []
    
    for food, value in food_dict.items():
        
        if isinstance(value, dict):
            qty = value.get("Quantity")
            size = value.get("Size")
            result.append(f"{qty} {size} {food}")
       
        else:
            result.append(f"{value} {food}")

    return ", ".join(result)


def convert_str(food:dict):
    answer =[]

    for value in food.items():
        
        answer.append(f"{value}")

    return " ".join(answer)




























































