import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import argparse

def gen(n=1500, seed=None):
    if seed is not None:
        np.random.seed(seed)
    s = np.random.randint(30,100,size=n)
    a = np.random.randint(50,100,size=n)
    h = np.random.randint(0,10,size=n)
    calc = s*0.5 + a*0.2 + h*3 + np.random.randint(-10,10,size=n)
    r = (calc>65).astype(int)
    return pd.DataFrame({'score':s,'att':a,'hrs':h,'res':r})

def fit(df):
    X = df[['score','att','hrs']]
    y = df['res']
    Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=0.2,random_state=42)
    m = LogisticRegression(solver='liblinear')
    m.fit(Xtr,ytr)
    pred = m.predict(Xte)
    print(f'accuracy: {accuracy_score(yte,pred):.4f}')
    return m

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--no-input',action='store_true')
    args = p.parse_args()
    print('Student Predictor')
    df = gen()
    print(df.head())
    m = fit(df)
    joblib.dump(m,'model.joblib')
    print('saved model.joblib')
    if args.no_input:
        return
    while True:
        q = input('score (or q to quit): ').strip()
        if q.lower() in ('q','exit'):
            break
        try:
            s = float(q)
            a = float(input('att: '))
            h = float(input('hrs: '))
            o = m.predict([[s,a,h]])[0]
            print('PASS' if o==1 else 'FAIL')
        except Exception:
            print('invalid')

if __name__=='__main__':
    main()
