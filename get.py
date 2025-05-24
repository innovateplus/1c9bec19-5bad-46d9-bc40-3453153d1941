#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

def csv_to_txt(input_csv='proxies.csv', output_txt='result.txt'):
    # 确保输入文件存在
    if not os.path.isfile(input_csv):
        raise FileNotFoundError(f"找不到文件：{input_csv}")

    with open(input_csv, newline='', encoding='utf-8') as csvfile, \
         open(output_txt, 'w', encoding='utf-8') as txtfile:

        reader = csv.reader(csvfile)
        # 跳过第一行（表头）
        next(reader, None)

        # enumerate 从 2 开始，行号即为 CSV 中的真实行号
        for line_num, row in enumerate(reader, start=2):
            # 确保这一行至少有 6 列
            if len(row) < 6:
                # 如果列数不足，可以选择跳过或报错，这里跳过
                continue

            col1 = row[0].strip()
            col2 = row[1].strip()
            col6 = row[5].strip()

            # 按照要求的格式写入
            line = f'{col1}:{col2}#{col6} - {line_num-1}'
            txtfile.write(line + '\n')

    print(f'已生成：{output_txt}')

if __name__ == '__main__':
    csv_to_txt()