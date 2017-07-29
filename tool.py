import json


def res_to_dic(r):
    j = json.loads(r.text)
    return j


def output_r(r):
    j = json.dumps(res_to_dic(r), indent=1, ensure_ascii=False)
    print(j)
    return
