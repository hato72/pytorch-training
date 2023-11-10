import numpy as np
from num_def.nump import *

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]])


if __name__ == '__main__':
    print("data shape:",data.shape)
    print("各クラスの科目別平均点:",class_mean(data))
    print("全クラスの番号3番の学生の中で2科目目の最高得点:",sec_max(data))
    print("各科目で一番点数が高い人と低い人の点差:",dif_point(data))
    print("各クラスで1科目目が80点以上の人数:",eighty_point(data))
    print("2科目の合計点が135点を超えている人数:",sum_point(data))
    print("全生徒の1科目目と2科目目の相関係数:",r_count(data))
