import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout,Flatten,Conv2D, MaxPooling2D 
import h5py
from tensorflow.keras.callbacks import ModelCheckpoint, CSVLogger
import pickle

import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
from PIL import Image, ImageFilter, ImageEnhance


def main() :
    st.title('뇌종양 판정 예측')

    # 사이드바 메뉴
    menu = ['HOME','EDA','ML'] 
    choice =  st.sidebar.selectbox('메뉴', menu)

    if choice == 'HOME' :
        st.write('뇌종양 판정 어플리케이션 입니다.')
        st.write('고객의 MRI 사진을 입력하여 뇌종양이 있는지 없는지, 그리고 그 종류를 알 수 있습니다. ')
        st.write('왼쪽의 메뉴에서 선택하여 진행하십시오.')

    # if choice == 'EDA' :
    #     st.write( 지금 화면에서는 이 앱의 오차가 얼마나 되는지 즉, 얼마나 정확한 앱인지 알 수 있는 그래프를 보여줍니다)

    # if choice == 'ML' :
    #     st.write('정확도를 확인 하셨으면 고객의 MRI 사진을 넣어 판별된 결과를 확인하십시오. ')




if __name__ == '__main__' :
    main()