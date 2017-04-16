import sys
import random
import math

def cmp(x ,y):
    if random.random() < 0.5:
        return int(x[0] > y[0]) if x[0] != y[0] else int(y[1] > x[1])
    return int(x[0] > y[0]) if x[0] != y[0] else int(x[1] > y[1])   

def calc_auc(y_true, y_pred, rev = True):
    NEG, POS = 0, 0
    for lab in y_true:
        if lab == 0:
            NEG += 1
        elif lab == 1:
            POS += 1
    # len(ypt) >= 2
    ypt = sorted(zip(y_pred, y_true), key = lambda x:x[0], reverse = rev)
#    ypt = sorted(zip(y_pred, y_true), cmp = cmp, reverse = rev)
    neg_num, pos_num = 0, 0
    fpr, tpr = [], []
    
    pos_num += ypt[0][1]
    neg_num += (1 - ypt[0][1])
    # calc fpr, tpr
    ind = 1 
    while ind < len(ypt):
        lab, sc = ypt[ind]
        if ypt[ind][0] != ypt[ind - 1][0]:
            fpr.append(neg_num * 1.0 / NEG)
            tpr.append(pos_num * 1.0 / POS)
        pos_num += ypt[ind][1]
        neg_num += (1 - ypt[ind][1])
        ind += 1
    # append last
    fpr.append(neg_num * 1.0 / NEG)
    tpr.append(pos_num * 1.0 / POS)
    if fpr[0] > 0.0:
        fpr.insert(0, 0.0)
        tpr.insert(0, 0.0)

    # print 'fpr:', fpr
    # print 'tpr:', tpr
    auc = 0.0 
    prev_fp, prev_tp = fpr[0], tpr[0]
    for fp, tp in zip(fpr, tpr)[1:]:
        if fp != prev_fp: # trapezoid
            auc += ((fp - prev_fp) * (tp + prev_tp) / 2.0)
        prev_fp = fp
        prev_tp = tp
    # if rev and auc <= 0.5:
    #     print auc, y_pred, y_true
    return auc 



fin = open(sys.argv[1])
time = int(sys.argv[2])
label = []
value = []

while True:
    line = fin.readline()
    if not line:
        break

    info = line.split(' ')
    a = int(info[0])
    b = float(info[1])
    label.append(a)
    value.append(b)

print calc_auc(label, value)
'''
auc = []
for i in range(time):    
   auc.append(calc_auc(label, value))
sum1 = 0.0
sum2 = 0.0
N = len(auc)
for i in range(N):
    sum1+=auc[i]
    sum2+=auc[i]**2
mean=sum1/N
var=math.sqrt(sum2/N-mean**2)
print "Mean = ",mean," Var = ",var
'''
