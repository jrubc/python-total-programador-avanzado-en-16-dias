import pickle

with open("pkls/customers.pkl", "wb") as f:
    pickle.dump([], f)

with open("pkls/customer_account_numbers.pkl", "wb") as f:
    pickle.dump(list(range(1, 101)), f)
