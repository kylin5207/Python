"""
均匀分布随机数比较
numpy的random.rand()生成的随机浮点数遵循[0, 1)区间上的均匀分布（uniform distribution）
random.random()这个函数。这个函数是Python标准库中random模块提供的，其功能与numpy.random.random()类似


"""
import numpy as np
import random


class MiniPCG64:
    def __init__(self, seed=1):
        self.state = seed
        self.inc = 0xDA3E39CB94B95BDB # 增量
        self.multiplier = 0x5851F42D4C957F2D # 常数
        self.modulus = 2**64

    def next(self):
        # 记录更新前的状态
        old_state = self.state

        # 线性同余
        self.state = (old_state * self.multiplier + self.inc) % self.modulus

        # 置换步骤：XORSHIFT和右旋转
        # 首先，对old_state进行位移和异或操作
        # 1. 右移动18位，
        # 2. 之后和old_state异或，这一步增加了数值的随机性，因为它结合了原始数字的高位和低位信息。
        xorshifted = ((old_state >> 18) ^ old_state) >> 27
        # 最终结果需要旋转的位数
        # 实际上，提取 old_state 最高的几位（目前是5位，因为64-59=5）来决定最终结果需要旋转的位数。
        # old_state的高位变化可以用来影响随机数生成的细节，使得每个生成的随机数都有略微不同的行为
        rot = old_state >> 59

        # 将xorshifted变量右旋转rot位来生成最终的随机数。这里使用了位运算来实现旋转
        # 转操作不同于简单的位移，因为它将位移出的位重新引入到数值的另一端
        # 1. 首先，向右旋转rot位，高位被移出的同时，相同数量的位（从最低位开始）被设置为0。
        # 2. 将xorshifted向左旋转，并确保旋转的位数在0到31之间（因为我们只旋转32位整数的位），这个操作把原本要被移出的低位移动到了数值的高位。
        # 3. 两个操作的结果通过位或操作（|）结合起来，实现了将xorshifted的位以rot为单位进行旋转。这种旋转操作使得即使是连续的随机数也具有很高的不相关性，从而增强了生成器的随机性和输出的不可预测性。
        return (xorshifted >> rot) | (xorshifted << ((-rot) & 31))

    def random(self):
        # 线性同余后归一化
        return self.next() / self.modulus

def main():
    random_rand = random.random()
    np_rand = np.random.rand()

    print(f"numpy random number: {np_rand}")
    print(f"random number: {random_rand}")

    # 手动实现简易版PCG64
    pcg = MiniPCG64(seed=42)

    print("======PCG64 simulation======")
    for i in range(50):
        print(f"No.{i} = {pcg.random()}")

if __name__ == "__main__":
    main()