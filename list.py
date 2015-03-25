def my_uniq(list):
    new_list = []
    for i in range(0, len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    return new_list

def two_sum(list):
    pairs = []
    for i in range(0, len(list)):
        for j in range(i, len(list)):
            if list[i] + list[j] == 0:
                pairs.append([i, j])
    return pairs

def transpose(matrix):
    new_matrix = []
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if col >= len(new_matrix):
                new_matrix.append([matrix[row][col]])
            else:
                new_matrix[col].append(matrix[row][col])
    return new_matrix

def stock_picker(dates):
    buy_date = 0
    sell_date = 0
    profit = 0
    for buy in range(0, len(dates)):
        for sell in range(buy + 1, len(dates)):
            if dates[sell] - dates[buy] > profit:
                buy_date = buy
                sell_date = sell
                profit = dates[sell] - dates[buy]
    return [buy_date, sell_date]

print(stock_picker([100, 90, 105, 250, 200]))
