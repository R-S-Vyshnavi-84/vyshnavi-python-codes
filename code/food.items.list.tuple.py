food_list=["panipuri","pizza","soup","biryani","dal","chawal","chaats"]
price_items=[50,300,150,250,150,200,100]
food_list=len(food_list)
for i in range(food_list):
    temp=int(input(f"enter the food items {i} index position: "))
    food_list.append(temp)