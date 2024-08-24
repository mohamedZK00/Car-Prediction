import streamlit as st
import pandas as pd
import pickle

# upload data

model = pickle.load(open(r"E:\Data set from Kaggle\Model Saving\Cars_Prediction.sav" ,'rb'))

#streamlit page

st.title('Car Price Prediction')

st.sidebar.header('Feature Selecting')
st.sidebar.info('Easy Appliction For Predicting Cars Price')

st.image("E:\Data set from Kaggle\Pro_Stremlit بالعربي\lamborghini forest.png")
#---------------------------------------------------------------------------------------

m1 = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
       'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
       'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
       'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
       'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
       'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
       'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
       'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
       'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
       'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
       'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']
m2 = [16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 23, 20,  0, 44, 19, 39,  7, 25,  4,
       33, 47, 15,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]

manu_maping = dict(zip(m1,m2))
manu1 = st.selectbox("Manufacturer",m1)
manu2 = manu_maping[manu1]
#----------------------------------------------------------------------------------

mm1 = ['RX 450', 'Equinox', 'FIT', 'E 230 124', 'RX 450 F SPORT',
       'Prius C aqua']
mm2 = [1242,  658,  684, 582, 1243, 1169]

Model_maping = dict(zip(mm1,mm2))
Model1 = st.selectbox("Model",mm1)
Model = Model_maping[Model1]
#-------------------------------------------------------------------------------------

c1 = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup']
c2 = [ 4,  3,  9,  6,  2, 10,  1,  7,  0,  5,  8]

catg_maping = dict(zip(c1,c2))
catgu1 = st.selectbox("Category",c1)
category = catg_maping[catgu1]
#-----------------------------------------------------------------------------------
l1 = ['Yes', 'No']
l2 = [1, 0]

leather_maping = dict(zip(l1,l2))
leather1 = st.selectbox("Leather interior",l1)
leather = leather_maping[leather1]
#--------------------------------------------------------------------------------------
f1 = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG',
       'Hydrogen']
f2 = [2, 5, 1, 0, 6, 4, 3]

fuel_maping = dict(zip(f1,f2))
fuel1 = st.selectbox("Fuel type",f1)
fuel = fuel_maping[fuel1]
#----------------------------------------------------------------------------------
#mi1 = ['186005 km', '192000 km', '200000 km', '140607 km','307325 km', '186923 km']
#mi2 =[2838, 2960, 3140, 1541, 4454, 2857]

#mileg_maping = dict(zip(mi1,mi2))
#mileg1 = st.selectbox("Mileage",mi1)
#mileage = mileg_maping[mileg1]
mileage = st.number_input("Mileage")
#--------------------------------------------------------------------------------------
gb1 = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
gb2 = [0, 2, 3, 1]

gearbox_maping = dict(zip(gb1,gb2))
gbear1 = st.selectbox("Gear box type",gb1)
gbearbox = gearbox_maping[gbear1]
#-----------------------------------------------------------------------------------
d1 = ['4x4', 'Front', 'Rear']
d2 = [0, 1, 2]

drive_maping =  dict(zip(d1,d2))
drive1 = st.selectbox("Drive wheels",d1)
drivewheels = drive_maping[drive1]
#----------------------------------------------------------------------------------
w1 = ['Left wheel', 'Right-hand drive']
w2 = [0, 1]

wheel_maping = dict(zip(w1,w2))
wheel1 = st.selectbox("Wheel",w1)
wheel = wheel_maping[wheel1]
#----------------------------------------------------------------------------------
co1 = ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
co2 = [12,  1, 14,  7,  2,  6, 11, 13,  8, 15,  3,  5,  0,  4, 10,  9]

coloe_maping = dict(zip(co1,co2))
color1= st.selectbox("Color",co1)
color = coloe_maping[color1]
#-----------------------------------------------------------------------------------

Levy = st.number_input("Levy")

#--------------------------------------------------------------

E2 = [ 3.5,  3. ,  1.3,  2.5,  2. ,  1.8,  2.4,  4. ,  1.6,  3.3,  2.2,
        4.7,  1.5,  4.4,  1.4,  3.6,  2.3,  5.5,  2.8,  3.2,  3.8,  4.6,
        1.2,  5. ,  1.7,  2.9,  0.5,  1.9,  2.7,  4.8,  5.3,  0.4,  1.1,
        2.1,  0.7,  5.4,  3.7,  1. ,  2.6,  0.8,  0.2,  5.7,  6.7,  6.2,
        3.4,  6.3,  4.3,  4.2,  0. , 20. ,  0.3,  5.9,  5.6,  6. ,  0.6,
        6.8,  4.5,  7.3,  0.1,  3.1,  6.4,  3.9,  0.9,  5.2,  5.8]

#engine_mapping = dict(zip(E1,E2))
engine1 = st.selectbox("Engine Volume",E2)
#engine = engine_mapping[engine1]
#---------------------------------------------------------------------------------

Cy1  =[ 6.,  4.,  8.,  1., 12.,  3.,  2., 16.,  5.,  7.,  9., 10., 14.]
cylinders1 =st.selectbox("Cylinders",Cy1)
#--------------------------------------------------------------------------------
ar1 = [12,  8,  2,  0,  4,  6, 10,  3,  1, 16,  5,  7,  9, 11, 14, 15, 13]
airbag1 = st.selectbox("Airbags",ar1) 
#--------------------------------------------------------------------------------
#a1 = [14, 13, 18, 10,  8, 11, 17, 25, 27,  6, 16, 12,  7, 23, 29, 15, 24,
 #       5,  9, 20, 26, 34, 19, 21, 39, 28, 22, 31, 32, 36, 47, 35, 30,  4,
 #      40, 38, 33, 41, 71, 60, 50, 37, 81, 46, 59, 48, 67, 44, 85, 56, 77,
 #      42, 43, 51]
#age1 = st.selectbox("Age Of Car",a1)
Age = st.number_input("Age")
#------------------------------------------------------------------------------------



df = pd.DataFrame( {'Manufacturer':manu2 ,'Model':Model ,'Category':category ,'Leather interior':leather,
              'Fuel type':fuel ,'Mileage':mileage ,'Gear box type':gbearbox,
              'Drive wheels':drivewheels,'Wheel':wheel ,'Color':color,'Levy':Levy,'Engine Volume':engine1,
              'Cylinders':cylinders1 ,'Airbags':airbag1 ,'Age':Age},index=[0])



pr = st.sidebar.button("Predict Price")

if pr:
    pred = model.predict(df)
    st.sidebar.write("Price is Car : ",pred)