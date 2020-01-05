"""
题目描述
节点的从属关系如下，补全几个函数，使用可以完成 输入-> 输出 转换。
输入
relations = [('机器学习', '线性模型'), ('机器学习', '神经网络'), ('神经网络', '神经元模型'), ('机器学习', '强化学习'), ('线性回归', '最小二乘法'),
                 ('线性模型', '线性回归'), ('神经网络', '神经元模型'), ('神经元模型', '激活函数'), ('多层网络', '感知机'), ('多层网络', '连接权')]

输出
{
    "val": 4,
    "name": "机器学习",
    "childs": [
        {
            "val": 4,
            "name": "线性模型",
            "childs": []
        },
        {
            "val": 4,
            "name": "线性xx",
            "childs": []
        },
    ]
}


### 解题思路
1. 把嵌套的对象变成字典，嵌套对象可参考链表
2. 多重嵌套的对象，一层一层遍历，遍历每一层，把下一层的节点 拼成数组，接回去
3. build，把嵌套关系，变成字典，从 root，开始拼接
4. 递归一定要画图！！！用测试数据，每一层逻辑要写清楚！！！debug 都不行！！！递归太抽象了！

"""

a = {
    "val": 4,  # 下级有线性模型，神经网络，强化学习，神经元模型，共四个
    "childs": [
        {
            "val": 0,
            "childs": [],
            "name": "线性模型"
        },
        {
            "val": 1,  # 下级只有一个神经元模型
            "childs": [
                {
                    "val": 0,
                    "childs": [],
                    "name": "神经元模型"
                }
            ],
            "name": "神经网络"
        },
        {
            "val": 0,
            "childs": [],
            "name": "强化学习"
        }
    ],
    "name": "机器学习"
}


import json


class Node:
    def __init__(self, _name):
        self.name = _name
        self.val = 0
        self.childs = list()

    """
    题目：从当前节点开始，输出从当前节点开始的树结构转换成json格式后返回
    """
    def node2json(self):
        # 这一道题，要做得事情有

        # 0. 我们要处理的就是 fathers，是个数组
        # 1. 把 fathers 的 childs 转成字典，再拼回去，所有的 childs 拼成一个数组，这就是新的 fathers 了，只要 fathers 为空，就是要处理的为空
        # 2. 第一个 父节点们，就是 [root.__doct__]

        root = self.__dict__
        # fathers 是一个这样的东西
        # a = [{val: xx,
        #       name: xx,
        #       childs: [node, node, node]
        #       },
        #      {},
        #      {},
        #      ]

        fathers = [root]

        while len(fathers) != 0:
            next_fathers = []
            for n in fathers:

                # 把 childs 转字典，再拼回去
                n["val"] = len(n.get("childs"))
                childs = [x.__dict__ for x in n.get("childs")]
                n["childs"] = childs
                next_fathers += childs
            fathers = next_fathers

        return root



    """
    题目：更新当前node与下级node的val，val的值等于该node下一共有多少个子节点
    """
    def count_val(self):
        # 这个上一步就做完了
        pass


class Solve:
    def __init__(self, root_name):
        # 初始化根节点
        self.root_node = Node(root_name)
        # 边
        self.relations = list()
        # 节点list
        self.node_list = list()
        self.node_list.append(self.root_node)

    """
    题目：通过输入的各条边关系，创建出树结构，并返回根节点
    如：机器学习,线性模型。则线性模型node是机器学习node的child
    """
    def build(self):
        # 1. 把所有节点，搞个字典 {父节点: [子节点1, 子节点2, 子节点3]}
        # 2. 把这些节点拼成一个嵌套的对象
        # 3.
        node_dict = {self.root_node.name: []}
        for x in self.relations:
            name = x[0]
            if name in node_dict:
                node_dict[name].append(x[1])
            else:
                node_dict[name] = [x[1]]

        # fathers 是一个 node 的数组，是现在要处理的，要把 childs 给他们装上
        fathers = [self.root_node]
        while len(fathers) != 0:
            tmp = []
            for node in fathers:
                # 这里是拿 node 的子节点，拼接下一层
                if node_dict.get(node.name):
                    for child_name in node_dict.get(node.name):
                        # if not node_dict.get(child_name) is None:
                        n = Node(child_name)
                        node.childs.append(n)

                        # 这个是准备处理下一层 fathers
                        tmp.append(n)
            fathers = tmp

    def run(self, relations):
        self.relations = relations
        self.build()
        # self.root_node.count_val()
        print(json.dumps(self.root_node.node2json(), ensure_ascii=False, indent=4))


if __name__ == '__main__':
    # 根节点名为机器学习
    ans = Solve("机器学习")
    relations = [('机器学习', '线性模型'), ('机器学习', '神经网络'), ('机器学习', '强化学习'), ('线性回归', '最小二乘法'),
                 ('线性模型', '线性回归'), ('神经网络', '神经元模型'), ('神经元模型', '激活函数'), ('多层网络', '感知机'), ('多层网络', '连接权'),
                 ('神经网络', '多层网络'), ('强化学习', '有模型学习'), ('强化学习', '免模型学习'), ('强化学习', '模仿学习'), ('有模型学习', '策略评估'),
                 ('有模型学习', '策略改进'), ('免模型学习', '蒙特卡洛方法'), ('免模型学习', '时序差分学习'), ('模仿学习', '直接模仿学习'), ('模仿学习', '逆强化学习')]

    # 完成题目内要求的代码
    ans.run(relations)

    # test_node = Node('xly')
    # test_node.val = 2
    #
    # test_node2 = Node('111')
    # test_node2.val = 2
    #
    # test_node3 = Node('222')
    # test_node3.val = 2
    #
    # test_node4 = Node('333')
    # test_node4.val = 2
    #
    # test_node5 = Node('lzs')
    # test_node5.val = 2
    #
    # test_node6 = Node('qqq')
    # test_node6.val = 2
    #
    # test_node7 = Node('www')
    # test_node7.val = 2
    #
    # test_node.childs = [test_node5, test_node6]
    # test_node6.childs = [test_node7]
    # test_node5.childs = [test_node2]
    # test_node2.childs = [test_node3]
    # test_node3.childs = [test_node4]
    #
    # print(test_node.count_val())
