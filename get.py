#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# trojan://pswd@clean.it:2053?security=tls&fp=chrome&type=ws&host=domain&path=%2Fpyip%3Dclean.it#name


import csv
import os

domain = 'qndb.pages.dev'

pswd = 'qndb'

# trojan://{pswd}@{col1}:{col2}?security=tls&fp=chrome&type=ws&host={domain}&path=%2Fpyip%3D{col1}:{col2}#{col6} - {cnt}

def csv_to_txt(input_csv='proxies.csv', output_txt='result.txt'):
    # 确保输入文件存在
    if not os.path.isfile(input_csv):
        raise FileNotFoundError(f"找不到文件：{input_csv}")

    seen_col1 = set()  # 用于追踪已处理过的第1列值

    with open(input_csv, newline='', encoding='utf-8') as csvfile, \
         open(output_txt, 'w', encoding='utf-8') as txtfile:

        reader = csv.reader(csvfile)
        # 跳过第一行（表头）
        next(reader, None)

        cnt = 1

        # enumerate 从 2 开始，行号即为 CSV 中的真实行号
        for line_num, row in enumerate(reader, start=2):
            # 确保这一行至少有 6 列
            if len(row) < 6:
                continue

            col1 = row[0].strip()
            col2 = row[1].strip()
            col6 = row[5].strip()

            # 对第1列内容去重：如果已见过则跳过
            if col1 in seen_col1:
                continue
            seen_col1.add(col1)

            # 按照要求的格式写入
            line = f'trojan://{pswd}@{col1}:{col2}?security=tls&fp=chrome&type=ws&host={domain}&path=%2Fpyip%3D{col1}:{col2}#{col6} - {cnt}'
            txtfile.write(line + '\n')
            cnt += 1

    print(f'已生成：{output_txt}（第1列内容已去重，共写入 {len(seen_col1)} 行）')

if __name__ == '__main__':
    csv_to_txt()
