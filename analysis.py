def calculate_total(values):
    return sum(values)


def calculate_average(values):
    if len(values) == 0:
        raise ValueError("Boş liste için ortalama hesaplanamaz.")

    return sum(values) / len(values)


