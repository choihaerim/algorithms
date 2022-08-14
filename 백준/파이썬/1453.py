def pc_room_alba(customer):
    customer = customer.split()
    return len(customer) - len(set(customer))

if __name__ == "__main__":
    N = input()
    customer = input()
    print(pc_room_alba(customer))