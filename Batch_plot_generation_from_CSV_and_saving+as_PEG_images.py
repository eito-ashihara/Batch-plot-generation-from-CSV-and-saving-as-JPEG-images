import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from pathlib import Path
import atexit

def cleanup(): #プログラム終了時の動作を定義
    print('PLEASE TYPE SOME KEY TO CLOSE')
    input() #exe化した際に一瞬で閉じないように
    
atexit.register(cleanup) #プログラム終了の際に強制的に↑で定義したclaenup関数を呼び出す。これで自動で画面が閉じない

#パスの取得
path = Path.cwd()
print("YOUR PATH IS", path, '\n')

#初期DF作成
df=pd.DataFrame()

#データ処理するファイルパスを表示
print('CSV FILE IN YOUR DIRECTORY IS BELOW')
for i in glob.glob('%s/*.csv'% path):
    filepath = os.path.split(i)[1] #split関数を使用してファイル名のみを表示
    print(filepath)

#ヘッダーを取得する関数
def header_func(DataFrame):
    for i in range(len(DataFrame.columns)): 
        header.append(DataFrame.columns[i])
        print('header%s is:'%[i], header[i])
        
#データクレンジング
def Datacleansing(DataFrame):
     for i in range(len(DataFrame.columns)): 
         DataFrame[header[i]]= pd.to_numeric(DataFrame[header[i]], errors = 'coerce')
    
#グラフ表示する関数
def ScatterPlot_withABS(DataFrame, DataFrame_abs, size = 1):
    fig, ax = plt.subplots(1,2, squeeze = False)
    
    #各列からLinerグラフを作成
    for i in range(1, len(DataFrame.columns)): #縦軸の２列目以降をy軸に指定。
        ax[0,0].scatter(x = DataFrame[header[0]], y = DataFrame[header[i]], label = DataFrame.columns[i], s = size)
    ax[0,0].set_xlabel('x axis')
    ax[0,0].set_ylabel('y axis')
    ax[0,0].legend()
    
    #各列からLog用のグラフを作成　データをLogに変換する処理自体は別で処理
    for i in range(1, len(DataFrame_abs.columns)): 
        ax[0,1].scatter(x = DataFrame[header[0]], y = DataFrame_abs[header[i]], label = DataFrame_abs.columns[i], s = size)#横軸x_axisはABSしないのでDataFrameの方を指定
    ax[0,1].set_xlabel('x axis')
    ax[0,1].set_ylabel('y axis log')
    ax[0,1].legend()
    
    #タイトルや画像サイズの指定
    fig.suptitle(filepath, fontname = 'MS Gothic')
    fig.set_size_inches(12,5)
    plt.yscale('log')
    
    #グラフを画像として保存
    save_file_name = os.path.splitext(filepath)[0] #ファイル保存用に拡張子部分（.csv）をsplit関数で選択しないように
    plt.savefig(str(save_file_name) + '.jpeg') #↑で.csvの部分を削除。そしてファイル名のあとに.jpegを追加。
    
    plt.close() 
    
#メイン処理
for i in glob.glob('%s/*.csv'% path):
    filepath = os.path.split(i)[1]
    df = pd.read_csv(i, header= 0)
    
    print(filepath, '\n')
    print('DF SHOW IN BELOW','\n',  df, '\n')

    #ヘッターを取得
    header = [] #ヘッダーを毎回初期化することでファイルごとにヘッダーがわかっても対応できるように
    print('GETTING HEADER')
    header_func(df)
    
    #データクレンジング実行　数値以外をNANに変更
    print('\n''DATA CLEANSING')
    Datacleansing(df)
    print('DATA CLEANSING OVER')
    
     #絶対値計算してdf_absに格納
    df_abs = df.abs()
    print('\n' 'DF_ABS SHOW IN BELOW ','\n', df_abs, '\n')
    
    #グラフを作成
    print("GENERATING PLOT", '\n')
    ScatterPlot_withABS(df, df_abs, size = 10)
    print('PLOT FINISH''\n''\n')
    
print('\n''COMPLETE!!!')
