print("Bienvenido/a a la calculadora de propinas")
food_bill = float(input("¿Cuánto costó la comida?\n $"))
people = input("¿Cuántas personas hay?\n ")
tip = int(input("¿Qué porcentaje de propina están dispuestos a dar? (Nota: No escribas el simbolo %. Sólo escribe el número) = ¿1, 5 or 10?\n"))
tip_percentage = tip / 100
total_tip = tip_percentage * food_bill
total_bill = total_tip + food_bill
bill_per_person = float(total_bill) / int(people)
solution = round(float(bill_per_person),2)
print(f"Cada persona debe pagar: ${solution}")