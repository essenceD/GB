import json
res = []
with open('samples\\inputs\\text_7.txt', 'r', encoding='utf-8') as file_r:
    accounting = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in file_r}
    for i in accounting.keys():
        if int(accounting[i]) > 0:
            res.append(int(accounting[i]))
    avg = {'Average_profit': sum(res) / len(res)}
    res = [accounting, avg]
print(res)
with open('samples\\outputs\\account.json', 'w', encoding='utf-8') as file_w:
    json.dump(res, file_w, ensure_ascii=False)
