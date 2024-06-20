def get_bins(data, n_bins):

    min_val = min(data)
    max_val = max(data)

    bins = [[] for _ in range(n_bins)]

    for num in data:
        if num == max_val:
            bin_index = n_bins - 1
        else:
            bin_index = int((num - min_val) / (max_val - min_val) * n_bins)
        bins[bin_index].append(num)

    return bins


def print_histogram(data, n_bins):
    bins = get_bins(data, n_bins)

    max_count = max(len(bin_) for bin_ in bins)

    for i in range(max_count, 0, -1):
        row = ""
        for bin_ in bins:
            if len(bin_) >= i:
                row += "#"
            else:
                row += " "
        print(row)

    labels = ["Bin " + str(i + 1) for i in range(n_bins)]
    print("".join(labels))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_bins = 4
print(get_bins(data, n_bins))
print('\n\n')
print_histogram(data, n_bins)
