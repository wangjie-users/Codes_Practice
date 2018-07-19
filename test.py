'''
本实验考察Python中列表和字典的性能对比。
实验思路：
	
	1、生成一个很大的文本文件

	2、分别用列表和字典来存储数据，然后读取并搜索数据

	3、考察列表和字典做为数据结构的时候，存储的时间，搜索和访问的时间

	4、计算两种方案的消耗时间

'''

import random
import time

'''
part1 生成100万行、每一行有95个随机字符的文件

'''
def get_random_chars():
	return [chr(n) for n in range(32,127)] # 生成95个随机字符


def create_random_nums(nums=None): 
	random.shuffle(nums) # 将字符串nums随机排序
	return nums

def create_file():
	chars = get_random_chars()
	for i in range(1000000):
		with open('data.txt', 'at') as f:
			data = create_random_nums(chars)
			f.writelines(data)
			f.write('\n')

'''
part2

用列表作为数据结构容器，从百万文件中来读取数据
考察列表的存储数据的时间，以及列表的搜索数据的时间

先从百万行随机字符串文件中，读取一定数量的数据(10000行数据);
存入10000行放入all_data列表;
接着从10000行all_data列表里面随机取1000行;
放到一个target_data列表;
最后搜索这个target_data列表;

'''
def read_list_data(file_name, total_num, search_num):
	all_data = []
	target_data = []
	with open(file_name, 'rt') as f:
		all_data = f.readlines()[:total_num]
	for i in range(search_num):
		rand_index = random.randint(0, total_num - 1)
		if all_data[rand_index] not in target_data:
			target_data.append(all_data[rand_index])
			if len(target_data) == search_num:
				break
	return all_data, target_data


'''
part3：

用字典作为数据结构容器
先从百万行字符串文件中，读取一定数量的字符(假如为10000行)
存到到字典里面,把每一行的内容做为key，value设为0
接着提取这个字典里面的key,把这个10000行的数据，转为列表
从10000行里面随机取1000行出来，放到target_data列表

'''
def read_dict_data(file_name, total_num, search_num):
	all_data = {}
	target_data = []
	with open (file_name, 'rt') as f:
		for index, line in enumerate(f):
			if index < total_num:
				all_data[line] = 0 # 将line值作为key，value为0写入字典中
			else:
				break
	# print(all_data)
	all_data_list = list(all_data)
	print(all_data)
	# print(all_data_list)
	for x in range(search_num):
		random_index = random.randint(0, total_num - 1)
		if all_data_list[random_index] not in target_data:
			target_data.append(all_data_list[random_index])
			if len(target_data) == search_num:
				break
	return all_data, target_data


def cost_time(all_data, target_data): # 运行100次求均值时间
	max_times = 100
	total_time = 0
	for i in range(max_times):
		n = 0
		start_time = time.time()
		for line in target_data:
			if line in all_data:
				n += 1
		cost_time = time.time() - start_time
		total_time += cost_time
		print("第{}次运行时间:{}".format(i, total_time))
	return total_time / max_times
	
if __name__ == '__main__':
	# create_file()
	# all_data1, target_data1 = read_list_data('data.txt', 1000000, 1000)
	all_data2, target_data2 = read_dict_data('data.txt', 1000000, 1000) 
	# cost1 = cost_time(all_data1, target_data1)
	cost2 = cost_time(all_data2, target_data2)
	# print("list_cost:", cost1)
	# print("dict_cost:", cost2)