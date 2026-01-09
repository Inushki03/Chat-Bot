from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from model import get_orderID
import regex_helper
import model

app =FastAPI()
inprogress_order={}


Pizza_type =['Cheesy Pizza','Tandoori Chicken Pizza','Mushroom Pizza','Paneer Pizza','Veg Pizza']
@app.post('/')
async def hadnle_request(request:Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameter = payload['queryResult']['parameters']
    output_context=payload['queryResult']['outputContexts']
    session_id = regex_helper.get_seesion(output_context[0]['name'])
    
    
    if intent=='Track.order-context:Ongoing-tracking':
        return tracking_order(parameter)
    if intent=='order.add':
        return order_add(parameter,session_id)
    if intent=='Order.Complete':
        return oredr_complete(session_id)
    if intent =='Remove-Order':
        return remove_oreder(session_id,parameter)
    
def order_add(parameter:dict,session_id:str):
    order ={}
    food_items=parameter["food-items"]
    quantity=parameter["number"]
    pizza_size=parameter["Pizza-Size"]
    
    pizza_index=0
    
    if len(food_items) != len(quantity):
        text = f"!!!! Please clearly mention How many {food_items} do you want !!!!"
    for food,qty in zip(food_items,quantity):
        if food in Pizza_type:
            size=pizza_size[pizza_index] if pizza_index<len(pizza_size) else None
            if size is None:
                return JSONResponse(content={
                    "fulfillmentText":"Please clearly mention which size of pizza do you need"
                 })
            pizza_index=pizza_index+1

            order[food]={
                "Quantity":int(qty),
                "Size" : size}
            
        else:
            order[food]=int(qty)
   
        if session_id in inprogress_order:
            current_food_dict = inprogress_order[session_id]
            current_food_dict.update(order)
            inprogress_order[session_id]=current_food_dict

        else:
            inprogress_order[session_id]=order 
            

        order_str = regex_helper.get_str_from_food_dict(inprogress_order[session_id])
        text = f"Your Order is {order_str}. Do you want anything else?"

    return JSONResponse(content={
           "fulfillmentText":text
           
     })




def oredr_complete(session_id):
    if session_id not in inprogress_order:
        fullfilmentText = "I'm having trouble. I cant find the order.Please start new order"
    else:
        new_order =  inprogress_order[session_id]
    
        order_id = save_order(new_order)

        Total_Amount=model.get_total_amount(order_id)
      
        
        if order_id:
            fullfilmentText=f"Awsome we have placed your order. This your order id {order_id}. Your total amount is {Total_Amount}. Have a nice Day"
            
        else:
            fullfilmentText="Sorry I cant process your order.Start a new order"

        inprogress_order.pop(session_id, None)
    
    return JSONResponse(content={
        "fulfillmentText":fullfilmentText,
        "outputContexts": [] 
    })
    

def save_order(new_order:dict):

    new_order_ID = model.get_max_order_ID()

    for food,value in new_order.items():
        if isinstance(value,dict):
            qty=value.get("Quantity")
            size=(value.get("Size"))

        else:
            qty=value
            size=None
            print("Food : ",food)
            print("Qyanriry : ",qty)
            print("Size : ",size)
        
        model.insert_order(new_order_ID,food,qty,size)


    model.insert_order_tracking(new_order_ID,"in Progress")
    return new_order_ID


def remove_oreder(session_Id,parameter):
    if session_Id not in inprogress_order:
        fullfilmentText = "I'm having trouble. I cant find the order.Please start new order"
    else:
        
        current_order = inprogress_order[session_Id]  #1 pepsi 2Lava cake
        needed_removed_food_item = parameter["food-items"]  #Lava Cake
        needed_removed_food_qty =parameter["number"]  #1
        size = parameter['Pizza-Size']
        removed_food =[]
        food={}
        
        for item in needed_removed_food_item:
            if needed_removed_food_qty:
                current_order_qty = current_order[item]
               

                if isinstance(current_order_qty,dict):
                    current_order_qty=current_order_qty["Quantity"]
                    

                rest_food_qty =current_order_qty-needed_removed_food_qty[0]
                needed_removed_food_item_str =",".join(needed_removed_food_item)
                needed_removed_food_qty_int =int(needed_removed_food_qty[0])
                
                food = {
                    "food-items":needed_removed_food_item[0],
                    "number" : int(rest_food_qty),
                    "size":size
                }
                

                del current_order[item]

                if size :
                    current_order[needed_removed_food_item[0]] = {"Quantity":int(rest_food_qty),"Size":size}
                    
                    
                else:
                    current_order[needed_removed_food_item[0]] = int(rest_food_qty) #add new details into current_order
                    current_order_str = ",".join(current_order)
                    
                rest_items = regex_helper.get_str_from_food_dict(current_order)
                
                fullfilmentText = f"Remove {needed_removed_food_qty_int} {needed_removed_food_item_str}. Your order is {rest_items}.Do you nedd anything else? "

            else:
                if item not in current_order:
                    fullfilmentText= f"Sorry, there is no {item} in your order"

                else:
                    removed_food.append(item)
                    removed =",".join(removed_food)

                    del current_order[item]
                    not_removed_items = regex_helper.get_str_from_food_dict(current_order)
                    
                    fullfilmentText =  f"Succsesfully removed {removed}. Your order is  {not_removed_items}.Do you nedd anything else?"

                    if current_order == 0:
                        fullfilmentText =f"Remove all the food items Succsesfully"
           


    return JSONResponse(content={
        "fulfillmentText":fullfilmentText,
        
    })


def tracking_order(parameter:dict):
    order_id = int(parameter['number'])
    status = get_orderID(order_id)

    if status :
        text= f"The Order ID {order_id} is {status}"
    else:
        text =f"The order ID {order_id} is not found"

    return JSONResponse(content={
            "fulfillmentText":text
        })