
# a = [1,2,3,4,5]
# b = 5
# if b in a:
#     print("333")

exp = "2022-03-28 出金  客戶號：129998 USD33,333.00"

exp_list = exp.split()
c_num = exp_list[2].split("：")
print(c_num)

pk_accasoa= "1112223232345"
currtypeCode = pk_accasoa[-2:]
print(currtypeCode)