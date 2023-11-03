def ten_popular(text: str):
    import re
    delete = ".,!?;:-[]{}()="
    for i in delete:
        text = text.replace(i, "")
    words = re.split(" |'", text.lower())
    temp_list = []
    for el in words:
        if not (el in temp_list) and not el.isdigit():
            temp_list.append(el)
    temp_list2 = []
    for el in temp_list:
        a = el, words.count(el)
        temp_list2.append(a)

    return sorted(temp_list2, key=lambda sort_col: sort_col[1], reverse=True)[:10]


text = "Hello world. Hello Py it's thon. Hello again."
print(ten_popular(text))
