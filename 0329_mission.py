import re
def test():
    print("파이썬 피자에 오신것을 환영합니다!")
    value = {"S":15000,"M":20000,"L":30000}
    
    pizasize = input("원하는 피자 사이즈는 (S,M,L)").upper()
    p = re.compile("^[M|S|L]{1}")
    if(not p.match(pizasize)):
        print("다시 골라주세요")
        test()
        return
    sub = input("페퍼로니 추가는 2천원 추가 하시겠습니까? (Y/N) : ").upper()
    sub2 = input("치즈 추가는 3천원 추가 하시겠습니까? (Y/N) : ").upper()
    money = value[pizasize]
    if(sub == "Y"):
        money += 2000
    if(sub2 == "Y"):
        money += 3000
    print("총 지불하실 금액은? "+str(money))
test()

