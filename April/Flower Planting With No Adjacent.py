from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        '''
        伪代码：
        标注：
            collections.defaultdict
        :param N:
        :param paths:
        :return:
        '''
        color = [1] * N # 有N个颜色
        graph = [[] for i in range(N)]  # 有N个花园  [1~N]
        # 对于每条双向的通道进行遍历
        for path in paths:
            if path[0] > path[1]:
                graph[path[0] - 1].append(path[1] - 1)
            else:
                graph[path[1] - 1].append(path[0] - 1)
        for i in range(1, N):
            flower = [1, 2, 3, 4]
            for node in graph[i]:
                if color[node] in flower:
                    flower.remove(color[node])
            color[i] = flower[0]
        return color



if __name__ == '__main__':
    # 测试collections.defaultdict方法
    from collections import defaultdict

    d = defaultdict(list)
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    for k, v in s:
        d[k].append(v)
    print(d)
