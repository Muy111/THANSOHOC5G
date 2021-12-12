n=int(input(">Nhập ngày sinh của bạn: "))
t=int(input(">>Nhập tháng sinh của bạn: "))
a=int(input(">>>Nhập năm sinh của bạn: "))
ntn=[]
tong=[]
def tongtach(x):
    tongso=0
    while (x>0):
        tongso=tongso + (x%10)
        x=int(x/10)
    if tongso <10:
     ntn.append(tongso)
    else:
        tongtach(tongso)
    return tongso
def tinhlai(s):
    tongsau= 0
    while (s >= 11):
        tongsau= tongsau + (s%10)
        s= int (s/10)
        tongsau= tongsau + s
    tong.append(tongsau)
    return tongsau
tongtach(n)
tongtach(a)
tongtach(t)
kq= 0
for i in range (len(ntn)):
    kq= ntn[i]+kq
    tong.append(kq)
if 1 < kq <= 11:
  print ("Con số chủ đạo của bạn là:", kq)
else:
  kq= tinhlai(kq)
  print ("Con số chủ đạo của bạn là:", kq )
import time
print ("Hãy đợi 1 chút trong khi chúng tớ tính toán nhé :>")
time.sleep(3)
if kq== 2:
    print ("Người mang con số 2 là người:")
    print ("Tư duy tốt, thích lập kế hoạch; Giỏi đánh giá; Đầu óc nhanh nhạy; Có khiếu hài hước; Vô cùng lý trí")
elif kq==3:
    print ("Người mang con số 3 là người: ")
    print ("Đầu óc nhanh nhạy; Có tính hài hước và tư duy linh hoạt; Sống kém tích cực; Thích chỉ đạo")
elif kq==4:
    print ("Người mang con số 4 là người: ")
    print ("Quan tâm các khía cạnh vật chất; Có thiên hướng về “thực tế” hoặc “ thực hành”; Thuộc nhóm những người nguyên tắc và đáng tin cậy nhất")
elif kq==5:
    print ("Người mang con số 5 là người: ")
    print ("Yêu tự do; Nhạy cảm và có nhu cầu bày tỏ cảm xúc; Có trực giác rất tốt, với cảm xúc sâu sắc và tư duy nghệ thuật mạnh mẽ.")
elif kq==6:
    print ("Người mang con số 6 là người: ")
    print  ("Ưu tú trong rất nhiều lĩnh vực sáng tạo; Thích cống hiến; Tận tâm sâu sắc; Có trách nhiệm; Đầy yêu thương, dễ bao dung")  
elif kq== 7:
    print ("Người mang con số 7 là người: ")
    print ("Học hỏi theo cách riêng của mình; Khát khao được học bằng cách tự trải nghiệm; Thích chia sẻ kinh nghiệm của bản thân")
elif kq== 8:
    print ("Người mang con số 8 là người: ")
    print ("Độc lập, tự chủ; Suy nghĩ phức tạp, đa chiều; Cá tính mạnh; Tự tin; Tư duy kinh doanh tốt")
elif kq== 9:
    print ("Người mang con số 9 là người: ")
    print ("Ước vọng, hoài bão lớn; Trách nhiệm, lý tưởng sống cao; Nghiêm túc trong cuộc sống; Thích các công việc cộng đồng")
elif kq== 10:
    print ("Người mang con số 10 là người: ")
    print ("Dễ thích nghi; Có lòng can đảm; Thẳng thắn, bộc trực, quyết đoán; Sống rất lạc quan; ")
elif kq== 11:
    print ("Năng lượng tâm linh mạnh; Tiềm năng nhận thức phi thường; Hướng đến cái đẹp; Nhạy cảm và tinh tế; ")

    
