def qg (qz,AwnserList,Awnser):

    print(qz)

    a = AwnserList[0]
    b = AwnserList[1]
    c = AwnserList[2]
    d = AwnserList[3]
    OptionList=[f'a) {a}',f'b) {b}',f'c) {c}',f'd) {d}']
    for i in OptionList:
        print(i)

    AwnserInput = str(input('use option (bettwen a,b,c,d):'))
    for i in AwnserList:
        if AwnserInput == Awnser :
            print('that is right :)')
            break
        else:
            print('that is False :(')
            break

qg("2+2=?",[5,9,3,4],str('d'))
qg("wath's wheather now?",['sunny','rainy','icy','each one'],str('d'))
qg("85-92+23",['16','23','13','each one'],str('a'))
qg("What's season  are we in now?",['fall','spring','summer','each one'],str('c'))