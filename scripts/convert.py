#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import json

def parse_markdown_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    words = []
    current_category = "其他"
    
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('## '):
            current_category = line[3:].strip()
            continue
            
        if line.startswith('| ') and not line.startswith('|---'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5 and parts[0] != '单词' and parts[1] != '单词':
                english = parts[1]
                phonetic = parts[2]
                chinese = parts[3]
                example = parts[4]
                
                if english:  # 只添加有英文单词的条目
                    words.append({
                        'english': english,
                        'phonetic': phonetic,
                        'chinese': chinese,
                        'example': example,
                        'category': current_category
                    })
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f"成功转换 {len(words)} 个单词到 {output_file}")

if __name__ == '__main__':
    input_file = '../docs/英文单词分类大全.md'
    output_file = '../data/words.json'
    parse_markdown_to_json(input_file, output_file)