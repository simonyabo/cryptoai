import json
import ast
import os
import numpy as np


def read_in_data(filename=None):
    with open(filename, "r") as fp:
        bitcoin = json.load(fp)
    ast_bit = ast.literal_eval(bitcoin)
    print(len(ast_bit))
    return ast_bit


def extract_data(json_obj, filename):
    """
    Open, close, volume_traded, trades_count, price_high, price_low
    :param filename:
    :param json_obj:
    :return:
    """
    filename = filename.split(".")[0]
    extract_metrics = lambda line: [
        line['price_open'],
        line['price_close'],
        line['volume_traded'],
        line['trades_count'],
        line['price_high'],
        line['price_low']
    ]
    overall_coin_data = list(map(extract_metrics, json_obj))
    np.save("./np_coin_data/"+filename, np.array(overall_coin_data))


if __name__ in "__main__":
    direct = "./raw_coin_data/"
    for files in os.listdir(direct):
        bitcoin_data = read_in_data(os.path.join(direct, files))
        extract_data(bitcoin_data, files)
