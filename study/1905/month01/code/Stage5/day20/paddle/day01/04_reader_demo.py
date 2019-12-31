# 04_reader_demo.py     实现文件的顺序读取、随机读取、批量读取
import paddle
# 读取文件的生成器函数
def reader_creator(file_path):
    def reader():
        with open(file_path) as f:
            lines = f.readlines()
            for line in lines:
                yield line  # 生成一行数据
    return reader

reader = reader_creator("test.txt")
shuffle_reader = paddle.reader.shuffle(reader,10)   # 随机读取
batch_reader = paddle.batch(shuffle_reader,3)       # 批量读取，每个批次3笔
# for data in reader():
# for data in shuffle_reader():
for data in batch_reader():
    print(data,end="")
