#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

def process_proxies(csv_path='proxies.csv'):
    """
    读取当前目录下的 proxies.csv，
    从第2行开始，对第1列去重，
    按格式写入以第6列命名的 .txt 文件中。
    """
    # 用于去重第一列
    seen_col1 = set()
    # 存储每个第6列文件对应要写的行
    output_data = {}  # key: 文件名, value: list of lines
    cnt = 1
    # 读取 CSV
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # 跳过第一行（通常是表头）
        next(reader, None)

        for row_index, row in enumerate(reader, start=2):
            # 确保这一行至少有6列
            if len(row) < 6:
                continue

            col1 = row[0]
            col2 = row[1]
            col6 = row[5]

            # 如果第1列已处理过，则跳过
            if col1 in seen_col1:
                continue
            seen_col1.add(col1)

            # 构造输出行
            line = f'{col1}:{col2}#{col6}@{cnt}\n'

            cnt += 1
            # 文件名：第6列内容 + .txt
            filename = f'{col6}.txt'

            if filename not in output_data:
                output_data[filename] = []
            output_data[filename].append(line)

    # 将每个文件的数据写入磁盘（覆盖写入）
    for filename, lines in output_data.items():
        with open(filename, 'w', encoding='utf-8') as f_out:
            f_out.writelines(lines)

if __name__ == '__main__':
    # 调用主处理函数
    process_proxies()
