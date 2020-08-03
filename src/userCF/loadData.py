
import pandas as pd
def creat_data():
    movies = pd.read_csv("../../data/movies.csv")
    ratings = pd.read_csv("../../data/ratings.csv")  ##这里注意如果路径的中文件名开头是r，要转义。
    data = pd.merge(movies, ratings, on='movieId')  # 通过两数据框之间的movieId连接
    data[['userId', 'rating', 'movieId', 'title']].sort_values('userId').to_csv(
        '..\data\data.csv', index=False)
    print(data)

def load_data():
    # !/usr/bin/env python
    # encoding: utf-8
    """
    @Company：华中科技大学电气学院聚变与等离子研究所
    @version: V1.0
    @author: YEXIN
    @contact: 1650996069@qq.com or yexin@hust.edu.cn 2018--2020
    @software: PyCharm
    @file: movie_rating_user.py
    @time: 2018/8/19 17:50
    @Desc：采用python字典来表示每位用户评论的电影和评分
    """
    file = open("../../data/data.csv", 'r',
                encoding='UTF-8')  # 记得读取文件时加‘r’， encoding='UTF-8'
    ##读取data.csv中每行中除了名字的数据
    data = {}  ##存放每位用户评论的电影和评分
    for line in file.readlines()[1:-1]:
        # 注意这里不是readline()
        line = line.strip().split(',')
        # 如果字典中没有某位用户，则使用用户ID来创建这位用户
        if not line[0] in data.keys():
            data[line[0]] = {line[3]: line[1]}
        # 否则直接添加以该用户ID为key字典中
        else:
            data[line[0]][line[3]] = line[1]

    print(data)

if __name__ == "__main__":
    load_data()