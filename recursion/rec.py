def open_giftbox(n):
    if (n>1):
        print(f'box {n} is opened')
        open_giftbox(n-1)
    else:
        print(f'gift found in box{n}')
open_giftbox(5)


 
