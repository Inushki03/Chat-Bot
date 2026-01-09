from database import get_db_connection

cnx=get_db_connection()




def get_orderID(orderID:int):
    cursor = cnx.cursor(buffered=True)
    query =("select Status_of_Order from Order_Tracking where Order_ID=%s")

    cursor.execute(query,(orderID,))

    #fetch the Result
    result = cursor.fetchone()

    cursor.close()
    

    if result is not None:
        return result[0]
    else:
        return None


def get_max_order_ID():
    cursor = cnx.cursor(buffered=True)

    query = ("select max(Oredr_ID) from chatbot.food_order;")

    cursor.execute(query)

    max_order_ID =cursor.fetchone()[0]

    cursor.close()
    

    if max_order_ID is None:
        return 1
    else:
        return max_order_ID+1
    


def insert_order(order_id,food,qty,size):
    cursor =cnx.cursor(buffered=True)
    try:
        if size is not None:
            query = ("select Food_ID,Price_per_serving from chatbot.food_items where Food_Name=%s and Pizza_size=%s ;")
            cursor.execute(query,(food,size,))
        else:
            query = ("select Food_ID,Price_per_serving from chatbot.food_items where Food_Name=%s;")
            cursor.execute(query,(food,))
            
            

        result=cursor.fetchone()
        cursor.fetchall()

        print("Insert Order Result : ",result)

        if not result:
            raise ValueError("Food item not found")
        
        food_id,price_per_serving =result

        Total_Amount=price_per_serving*qty

        insert_query =("Insert into chatbot.Food_Order (Oredr_ID,Food_ID,quantity,Total_Amount) values(%s,%s,%s,%s)")
        print("Before INSERT")
        cursor.execute(insert_query,(order_id,food_id,qty,Total_Amount,))
        print("After INSERT, rowcount:", cursor.rowcount)


        cnx.commit()
        print("After COMMIT")

    except Exception as e:
        cnx.rollback()
        print("❌ DB ERROR:", e)
        raise
    finally:
        cursor.close()    


amount=[]
def get_total_amount(order_id:int):
    cursor = cnx.cursor(buffered=True)
    query=("select sum(Total_Amount) from chatbot.food_order where Oredr_ID = %s;")
    cursor.execute(query,(order_id,))
    result = cursor.fetchone()
    cursor.fetchall()

    if result is None:
        return -1
    else:
        return result[0]
    

def insert_order_tracking(order_id,status):
    cursor = cnx.cursor(buffered=True)

    query =("Insert into chatbot.Order_Tracking (Order_ID,Status_of_Order) values(%s,%s);")
    cursor.execute(query,(order_id,status,))

    cnx.commit()
    cursor.close()