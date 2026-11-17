name=input('enter your name:')
def quest():
    score=0
    tup1=['1.full form of w: ',
            '2.full form of d:',
            '3.full form of o ']
    #print(tup1)
    tup2=[['a.world','b.devil','c.oganize'],
            ['a.world','b.devil','c.oganize'],
            ['a.world','b.devil','c.oganize']]
    #print(tup2)

    list1=['world','devil','oganize']

    for i in range(len(tup1)):
            print(tup1[i])
            for item in tup2[i]:
                print(f'{item}')
            answer=input('answer: ')
            if(answer==list1[i]):
                score=score+1
    print(f"congrajulations! {name}")
    print(f"your score is {score}")
quest()
    
