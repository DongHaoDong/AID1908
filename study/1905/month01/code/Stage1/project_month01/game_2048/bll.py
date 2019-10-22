"""
    游戏逻辑控制器，负责处理游戏核心算法
"""
from model import DirectionModel
from model import Location
import random
class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.__list_empty_location = []
    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾
        :return:
        """
        for index in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[index] == 0:
                del self.__list_merge[index]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
        """
        for index in range(len(self.__list_merge) - 1):
            self.__zero_to_end()
            if self.__list_merge[index] == self.__list_merge[index + 1]:
                # 后一个累加前一个之上
                self.__list_merge[index] += self.__list_merge[index + 1]
                del self.__list_merge[index + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
            向左移动
        :return:
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        """
            向右移动
        :return:
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            # 从右向左 接收合并后的数据
            line[::-1] = self.__list_merge

    def __move_up(self):
        """
            向上移动
        :return:
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        """
            向下移动
        :return:
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
        方阵转置
        :param sqr_matrix:二维列表类型的方阵
        :return:
        """
        for col in range(1, len(self.__map)):
            for row in range(col, len(self.__map)):
                self.__map[row][col - 1], self.__map[col - 1][row] = self.__map[col - 1][row], self.__map[row][col - 1]

    def move(self,dir):
        """
            移动
        :param dir: 方向，DirectionModel类型
        :return:
        """
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()

    # def generate_new_number(self):
    #     # 思路：选出所有空白位置，再随机挑选一个
    #     list_empty_location = []
    #     for row in range(len(self.__map)):
    #         for col in range(len(self.__map[row])):
    #             if self.__map[row][col] == 0:
    #                 # 记录row col --> 元组
    #                 list_empty_location.append((row,col))
    #     # 确定哪个空白位置
    #     location = random.choice(list_empty_location)
    #     # 产生随机数
    #     if random.randint(1,10) == 1:
    #         self.__map[location[0]][location[1]] = 4
    #     else:
    #         self.__map[location[0]][location[1]] = 2
    def generate_new_number(self):
            """
                生成新数字
            :return:
            """
            # 获取所有空白位置
            self.__get_empty_location()
            if len(self.__list_empty_location) == 0:
                return
            # 产生一个随机数
            location = random.choice(self.__list_empty_location)
            # if random.randint(1,10) == 1:
            #     self.__map[location.row_index][location.col_index] = 4
            # else:
            #     self.__map[location.row_index][location.col_index] = 2
            self.__map[location.row_index][location.col_index] = self.__select_random_number()
            # 因为在该位置生成了新数字，所以该位置就不是空位置了
            self.__list_empty_location.remove(location)
    def __select_random_number(self):
        return 4 if random.randint(1,10) == 1 else 2

    def __get_empty_location(self):
        # 每次统计空位置，都先清空之前的数据，避免影响本次的数据
        self.__list_empty_location.clear()
        # 获取所有空白位置
        for row in range(len(self.__map)):
            for col in range(len(self.__map[row])):
                if self.__map[row][col] == 0:
                    self.__list_empty_location.append(Location(row,col))

    def is_game_over(self):
        """
            游戏是否结束
        :return:False表示游戏没有结束True表示结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False
        # # 判断横向有没有相同的元素
        # for row in range(len(self.__map)):
        #     for col in range(len(self.__map[row])-1):
        #         if self.__map[row][col] == self.__map[row][col + 1]:
        #             return False
        # # 判断竖向有没有相同的元素
        # for col in range(4):
        #     for row in range(3):
        #         if self.__map[row][col] == self.__map[row + 1][col]:
        #             return False

        # 判断横向有没有相同的元素
        for row in range(len(self.__map)):
            for col in range(len(self.__map[row])-1):
                if self.__map[row][col] == self.__map[row][col + 1] or self.__map[col][row] == self.__map[col+1][row]:
                    return False

        return True

# ---------------测试代码-----------------------------
if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move_left()
    # print(controller.map)
    # controller.move_down()
    # print(controller.map)

    # controller.move(DirectionModel.LEFT)
    # print(controller.map)
    # controller.move(DirectionModel.RIGHT)
    # print(controller.map)

    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.is_game_over()
    print(controller.map)
