def update_dictionary(d, key, value):
    # put your python code here
    if key in d.keys():
        d[key].append(value)
    elif 2*key in d.keys():
        d[2*key].append(value)
    else:
        d.update({2*key : [value]})


def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif 2*key in d.keys():
        d[2*key].append(value)
    else:
        d[2*key]=[value]


# def update_dictionary(di: dict, key: int, value: int) -> None:

