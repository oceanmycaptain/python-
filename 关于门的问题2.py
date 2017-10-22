from random import randint
count = 100000
def four_door():
    counts,changenum,no_changenum,no_change_get_num,change_get_num,change_wrongnum,no_changewrongnum = 0,0,0,0,0,0,0
    #计数 改变次数 没改变次数 没改变时猜对的 改变后的猜对的 没改变时猜对的
    while counts < count:#用于记下我们的循环次数
        list1 = ['sheep','sheep','car','sheep']
        list2 = ['change','no_change']
        firstchoice = randint(0,3)
        secondchoice = randint(0,1)
        peopleget = list1[firstchoice]
        ischange = list2[randint(0,1)]
        if ischange == 'change':
            changenum += 1
            list1.pop(firstchoice)#此时将我们第一次选择的排除掉
            list1.remove('sheep')#此时删除主持人已经帮我们排除的‘sheep'
            if list1[secondchoice] == 'car':#最后判断我们留下的是什么
                change_get_num += 1#此时改了后确认是'car'的数量上加一。
            else:
                change_wrongnum +=1
        else:
            no_changenum += 1#不改变的选择次数加上一次
            if peopleget =='car':
                no_change_get_num +=1#如果第一次选择就正确的话，就在我们的次数加一
            else:
                no_changewrongnum +=1
        counts += 1#循环次数加上一次在再次循环
    a = change_get_num/changenum*100#改变后选择为‘car’的概率
    c = change_wrongnum/changenum*100#改变后失败的概率
    b = no_change_get_num/no_changenum*100#没有改变后的选择为‘car’的概率
    d = no_changewrongnum/no_changenum*100#没有改变失败的概率为
    print('一共测试了 %d 次\n'%count)
    print('改变了：%d 次\n'%changenum)
    print('猜对的概率为 %f %%\n'%a)
    print('猜错的概率为 %f %%\n'%c)
    print('没改变: %d 次\n'%no_changenum)
    print('猜对的概率为 %f %%\n'%b)
    print('猜错的概率为 %f %%\n'%d)
four_door()