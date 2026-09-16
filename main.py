from customer import Customer

def main():
    # Create a list of customers
    customers = [
        Customer("Alice", "New York", 12000),
        Customer("Bob", "Los Angeles", 7000),
        Customer("Charlie", "Chicago", 3000),
    ]

    # Print the summary of each customer
    for customer in customers:
        print(customer.summary())

main()