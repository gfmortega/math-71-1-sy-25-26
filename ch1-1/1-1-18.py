donut_count = int(input())

boxes = donut_count // 12
individual = donut_count % 12
total_cost = boxes*8 + individual

print(f'boxes: {boxes}')
print(f'individual donuts: {individual}')
print(f'total cost: ${total_cost}')
