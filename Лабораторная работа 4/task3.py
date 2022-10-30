def delete(list_, index=None):
    if index is not None:
        q_ = list_[0:index]
        w_ = list_[index+1:len(list_)]
        return (q_ + w_)
    index = None
    return list_[0:len(list_)-1]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
