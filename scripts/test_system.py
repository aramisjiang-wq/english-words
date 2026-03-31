import json
import time
import sys
from pathlib import Path

class VocabularySystemTest:
    def __init__(self):
        self.data_file = '../data/words_merged.json'
        self.test_results = []
        
    def load_data(self):
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def test_data_integrity(self):
        print('测试数据完整性...')
        data = self.load_data()
        
        tests = []
        
        tests.append(('单词总数检查', len(data) >= 5000, f'单词总数: {len(data)}'))
        tests.append(('数据结构检查', all('english' in word and 'chinese' in word for word in data), '所有单词包含必需字段'))
        tests.append(('音标检查', all('phonetic' in word for word in data), '所有单词包含音标'))
        tests.append(('例句检查', all('example' in word for word in data), '所有单词包含例句'))
        tests.append(('分类检查', all('category' in word for word in data), '所有单词包含分类'))
        tests.append(('词性检查', all('part_of_speech' in word for word in data), '所有单词包含词性'))
        tests.append(('主题检查', all('theme' in word for word in data), '所有单词包含主题'))
        
        for test_name, passed, detail in tests:
            status = '✅ 通过' if passed else '❌ 失败'
            print(f'  {test_name}: {status} - {detail}')
            self.test_results.append(('数据完整性', test_name, passed, detail))
        
        return all(t[1] for t in tests)
    
    def test_categories(self):
        print('\n测试分类功能...')
        data = self.load_data()
        
        categories = set(word['category'] for word in data)
        part_of_speeches = set(word['part_of_speech'] for word in data)
        themes = set(word['theme'] for word in data)
        
        tests = []
        
        tests.append(('分类数量检查', len(categories) > 0, f'分类数量: {len(categories)}'))
        tests.append(('词性数量检查', len(part_of_speeches) > 0, f'词性数量: {len(part_of_speeches)}'))
        tests.append(('主题数量检查', len(themes) > 0, f'主题数量: {len(themes)}'))
        
        for test_name, passed, detail in tests:
            status = '✅ 通过' if passed else '❌ 失败'
            print(f'  {test_name}: {status} - {detail}')
            self.test_results.append(('分类功能', test_name, passed, detail))
        
        print(f'\n  分类列表: {", ".join(sorted(list(categories))[:10])}...')
        print(f'  词性列表: {", ".join(sorted(list(part_of_speeches))[:10])}...')
        print(f'  主题列表: {", ".join(sorted(list(themes))[:10])}...')
        
        return all(t[1] for t in tests)
    
    def test_duplicates(self):
        print('\n测试重复数据...')
        data = self.load_data()
        
        english_words = [word['english'] for word in data]
        duplicates = len(english_words) - len(set(english_words))
        
        passed = duplicates == 0
        status = '✅ 通过' if passed else '❌ 失败'
        print(f'  重复单词检查: {status} - 重复数量: {duplicates}')
        self.test_results.append(('数据质量', '重复单词检查', passed, f'重复数量: {duplicates}'))
        
        return passed
    
    def test_performance(self):
        print('\n测试性能...')
        data = self.load_data()
        
        tests = []
        
        start_time = time.time()
        filtered = [word for word in data if word['part_of_speech'] == '名词']
        filter_time = time.time() - start_time
        tests.append(('词性过滤性能', filter_time < 0.1, f'过滤时间: {filter_time:.4f}秒'))
        
        start_time = time.time()
        filtered = [word for word in data if word['theme'] == '商业']
        filter_time = time.time() - start_time
        tests.append(('主题过滤性能', filter_time < 0.1, f'过滤时间: {filter_time:.4f}秒'))
        
        start_time = time.time()
        search_results = [word for word in data if 'test' in word['english'].lower()]
        search_time = time.time() - start_time
        tests.append(('搜索性能', search_time < 0.1, f'搜索时间: {search_time:.4f}秒'))
        
        for test_name, passed, detail in tests:
            status = '✅ 通过' if passed else '❌ 失败'
            print(f'  {test_name}: {status} - {detail}')
            self.test_results.append(('性能测试', test_name, passed, detail))
        
        return all(t[1] for t in tests)
    
    def test_filtering_logic(self):
        print('\n测试过滤逻辑...')
        data = self.load_data()
        
        tests = []
        
        nouns = [word for word in data if word['part_of_speech'] == '名词']
        tests.append(('名词过滤', len(nouns) > 0, f'名词数量: {len(nouns)}'))
        
        business = [word for word in data if word['theme'] == '商业']
        tests.append(('商业主题过滤', len(business) > 0, f'商业主题数量: {len(business)}'))
        
        combined = [word for word in data if word['part_of_speech'] == '名词' and word['theme'] == '商业']
        tests.append(('组合过滤', len(combined) >= 0, f'组合过滤结果: {len(combined)}'))
        
        for test_name, passed, detail in tests:
            status = '✅ 通过' if passed else '❌ 失败'
            print(f'  {test_name}: {status} - {detail}')
            self.test_results.append(('过滤逻辑', test_name, passed, detail))
        
        return all(t[1] for t in tests)
    
    def test_data_quality(self):
        print('\n测试数据质量...')
        data = self.load_data()
        
        tests = []
        
        empty_english = sum(1 for word in data if not word['english'].strip())
        tests.append(('英文单词非空检查', empty_english == 0, f'空英文单词: {empty_english}'))
        
        empty_chinese = sum(1 for word in data if not word['chinese'].strip())
        tests.append(('中文翻译非空检查', empty_chinese == 0, f'空中文翻译: {empty_chinese}'))
        
        invalid_phonetic = sum(1 for word in data if not word['phonetic'].strip())
        tests.append(('音标有效性检查', invalid_phonetic == 0, f'无效音标: {invalid_phonetic}'))
        
        for test_name, passed, detail in tests:
            status = '✅ 通过' if passed else '❌ 失败'
            print(f'  {test_name}: {status} - {detail}')
            self.test_results.append(('数据质量', test_name, passed, detail))
        
        return all(t[1] for t in tests)
    
    def generate_report(self):
        print('\n' + '='*60)
        print('测试报告')
        print('='*60)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for t in self.test_results if t[2])
        failed_tests = total_tests - passed_tests
        
        print(f'总测试数: {total_tests}')
        print(f'通过: {passed_tests}')
        print(f'失败: {failed_tests}')
        print(f'通过率: {passed_tests/total_tests*100:.1f}%')
        
        if failed_tests > 0:
            print('\n失败的测试:')
            for category, test_name, passed, detail in self.test_results:
                if not passed:
                    print(f'  [{category}] {test_name}: {detail}')
        
        print('='*60)
        
        return failed_tests == 0
    
    def run_all_tests(self):
        print('开始运行全面测试...')
        print('='*60)
        
        results = []
        results.append(self.test_data_integrity())
        results.append(self.test_categories())
        results.append(self.test_duplicates())
        results.append(self.test_performance())
        results.append(self.test_filtering_logic())
        results.append(self.test_data_quality())
        
        all_passed = self.generate_report()
        
        return all_passed

if __name__ == '__main__':
    tester = VocabularySystemTest()
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)
