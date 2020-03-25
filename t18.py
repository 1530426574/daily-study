def precursion(r, *args):
    # recursion ternimator
    if r == None:
        return None

    # process logic  in current level
    print('rrr')

    # 进行递归
    precursion('r.left')
    precursion('r.right')
    # 返回当前层的状态
    return -1


def inorder(r, *args):
    if r == None:
        return None

    inorder('r.left')
    print('r')
    inorder('r.right')


def postorder(r, *args):
    if r == None:
        return None

    postorder('r.left')
    postorder('r.right')
    print('r')
