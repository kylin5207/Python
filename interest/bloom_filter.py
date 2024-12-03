import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size  # 位数组大小
        self.num_hashes = num_hashes  # 哈希函数数量
        self.bit_array = [0] * size  # 初始化位数组，全为0

    def _hash(self, item, seed):
        """使用哈希函数对元素进行哈希，并返回一个哈希值"""
        # 使用了简单的 MD5 哈希算法，并根据不同的“种子”（seed）值生成多个不同的哈希值。
        hash_object = hashlib.md5((str(seed) + item).encode())  # 简单的 MD5 哈希
        return int(hash_object.hexdigest(), 16) % self.size

    def add(self, item):
        """将元素添加到布隆过滤器中"""
        for i in range(self.num_hashes):
            hash_value = self._hash(item, i)
            self.bit_array[hash_value] = 1  # 将对应的位设为1

    def contains(self, item):
        """检查元素是否可能在布隆过滤器中"""
        for i in range(self.num_hashes):
            hash_value = self._hash(item, i)
            # 通过多个哈希函数计算位置，检查位是否都为 1，如果任何一个位置为 0，则说明该元素不在集合中。
            if self.bit_array[hash_value] == 0:
                return False  # 如果某个位为0，肯定不在集合中
        return True  # 如果所有位都是1，则元素可能在集合中


# 使用示例
bloom_filter = BloomFilter(size=1000, num_hashes=3)

# 向布隆过滤器添加元素
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

# 检查元素是否存在
print(bloom_filter.contains("apple"))  # 输出: True
print(bloom_filter.contains("banana"))  # 输出: True
print(bloom_filter.contains("orange"))  # 输出: True
print(bloom_filter.contains("grape"))  # 输出: False（很可能不在集合中）

