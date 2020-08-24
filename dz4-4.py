# dz4-4

if __name__ == '__main__':
    data = [1, 2, 1, 2, 1, 2, 3]
    result = [itm for itm in data if data.count(itm) == 1]
    print(result)