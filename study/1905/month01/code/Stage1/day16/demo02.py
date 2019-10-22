"""
    迭代器
"""
class Skill:
    pass
class SkillIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        # 如果没有数据了则抛出异常
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        # 返回下一个数据
        temp = self.__target[self.__index]
        self.__index += 1
        return temp
class SkillManager:
    def __init__(self):
        self.__skills = []
    def add_skill(self,skill):
        self.__skills.append(skill)
    def __iter__(self):
        # 创建一个迭代器对象,并传递需要迭代的对象
        return SkillIterator(self.__skills)
manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())
for item in manager:
    print(item)
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

