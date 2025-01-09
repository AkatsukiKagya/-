import os
import json

def txt_to_json(src_dir, dest_dir):
    # 确保目标目录存在
    os.makedirs(dest_dir, exist_ok=True)

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file == "bitext.txt":  # 仅处理名为 bitext.txt 的文件
                txt_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, src_dir)
                json_dir = os.path.join(dest_dir, relative_path)

                # 确保JSON文件的目录存在
                os.makedirs(json_dir, exist_ok=True)

                # 读取并解析txt文件内容
                with open(txt_path, 'r', encoding='utf-8') as txt_file:
                    lines = txt_file.readlines()

                data = []
                current_entry = {}
                for line in lines:
                    line = line.strip()
                    if line.startswith("古文："):
                        if current_entry:
                            data.append(current_entry)
                            current_entry = {}
                        current_entry['古文'] = line[3:].strip()
                    elif line.startswith("现代文："):
                        current_entry['现代文'] = line[4:].strip()
                if current_entry:  # 添加最后一个条目
                    data.append(current_entry)

                # 准备JSON文件路径
                json_path = os.path.join(json_dir, f"{os.path.splitext(file)[0]}.json")

                # 将内容保存为JSON文件
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)

                print(f"Converted: {txt_path} -> {json_path}")

# 使用示例
src_directory = "E:\Files\projects\古诗文语料库\Classical-Modern-main\Classical-Modern-main\双语数据"  # 替换为你的源目录路径
dest_directory = "E:\Files\projects\古诗文语料库\Classical-Modern-main\Classical-Modern-main\双语json"  # 替换为你的目标目录路径
txt_to_json(src_directory, dest_directory)
