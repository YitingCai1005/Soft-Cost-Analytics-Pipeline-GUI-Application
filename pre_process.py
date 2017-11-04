import pandas as pd


def ratio_bin(nume,deno):
    ratio=nume/deno*100
    r1,bins=pd.qcut(ratio,6,retbins=True,precision=2,labels=False)

    bins=bins.round(2)
    label=['%s%%~%s%%' % (a, b) for a, b in zip(bins[:-1], bins[1:-1])]
    label.append('>%s%%'%bins[-2])

    label_dic={h: v for h, v in zip(range(0,6), label)}
    target=r1.map(label_dic)
    return target

def csv_preprocess(t):
    t.dropna(inplace=True)
    t=t.loc[t['CONS ACTUAL']!=0,:]
    t.loc[:,'IFA/CONS Category']=ratio_bin(t['IFA ACTUAL'],t['CONS ACTUAL'])
    t.loc[:,'SOFT/CONS Category']=ratio_bin(t['SOFT ACTUAL'],t['CONS ACTUAL'])
    T=t.iloc[:,range(0,5)+[8,9]]
    return T