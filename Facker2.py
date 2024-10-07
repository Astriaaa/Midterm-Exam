import random
from faker import Faker

def generate_random_transaction_id(length=10):
    """Generate a random alphanumeric transaction ID."""
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_fake_transactions(num_transactions=10):
    faker = Faker()
    transactions = []

    for _ in range(num_transactions):
        transaction = {
            "transaction_id": generate_random_transaction_id(),
            "transaction_date": faker.date_between(start_date='-1y', end_date='today').isoformat(),
            "amount": round(random.uniform(100.00, 5000.00), 2)
        }
        transactions.append(transaction)

    return transactions

def print_transactions(transactions):
    for i, transaction in enumerate(transactions, start=1):
        print(f"Transaction {i}:")
        print(f"  Transaction ID: {transaction['transaction_id']}")
        print(f"  Transaction Date: {transaction['transaction_date']}")
        print(f"  Amount: ${transaction['amount']}")
        print()  # Print a newline for better readability

def main():
    transaction_records = generate_fake_transactions()
    print_transactions(transaction_records)

if __name__ == "__main__":
    main()
