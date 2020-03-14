class Grame(object):
    top_score = 0
    def __init__(self, player_name):
        self.name = player_name

    @staticmethod
    def show_hllep():
        print("这里是优秀帮助！")

    @classmethod
    def show_top_score(cls):
        print("历史最高分 %d " % cls.top_score)

    def statr_game(self):
        print("您好　%s ,游戏开始" % self.name)
        Grame.top_score += 1
        # print('你的最高分是：')
        Grame.show_top_score()


gamer1 = Grame("小明")


gamer1.statr_game()
Grame.show_top_score()
gamer1.statr_game()
Grame.show_top_score()
gamer1.statr_game()
Grame.show_top_score()


# 注意哈，实例方法中，可以访问类属性！类方法内部只能搞类的，