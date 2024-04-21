# 124
def find_series(arr):
    series = []
    current_series = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_series.append(arr[i])
        else:
            series.append(current_series)
            current_series = [arr[i]]

    series.append(current_series)
    return series


def swap_series(arr, k):
    series = find_series(arr)

    if len(series) < k:
        return arr

    last_series = series[-1]
    k_series = series[k - 1]

    last_series_start = len(arr) - len(last_series)
    k_series_start = sum(len(series[i]) for i in range(k - 1))
    k_series_end = k_series_start + len(k_series)

    arr[last_series_start:last_series_start + len(last_series)], arr[k_series_start:k_series_end] = arr[
                                                                                                    k_series_start:k_series_end], arr[
                                                                                                                                  last_series_start:last_series_start + len(
                                                                                                                                      last_series)]

    return arr