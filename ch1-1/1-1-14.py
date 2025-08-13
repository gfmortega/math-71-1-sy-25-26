cookie_count = int(input())
cookies_per_box = int(input())
pesos_per_box = int(input())

boxes_sold = cookie_count // cookies_per_box

print(boxes_sold * pesos_per_box)