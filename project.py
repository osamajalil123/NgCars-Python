# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Nt7OLX7WB5p6-3fbjijbIgqnvIgTWot
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeRegressor
import seaborn as sns
from sklearn.svm import SVR
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import sys
# pd.set_option('display.max_rows', 40000)
# %matplotlib inline
#from sklearn.tree import DecisionTreeClassifier

#from sklearn.ensemble import RandomForestClassifier

"""# User Input Getting Data From Nodejs"""
get = requests.get('http://localhost:3000/python/getdata')  # GET request
data = get.json()

user_company = data['userCompany']
user_transmission = data['userTransmission']
user_assembly = data['userAssembly']
user_color = data['userColor']
user_ecapacity = data['userEcapacity']
user_etype = data['userEtype']
user_mname = data['userMname']
user_myear = data['userMyear']
user_mileage = data['userMileage']
user_regcity = data['userRegcity']
user_cruisecontrol = data['userCruisecontrol']
user_airbags = data['userAirbags']
user_airconditioning = data['userAirConditiong']
user_alloyrims = data['userAlloyrims']
user_powerlocks = data['userPowerlocks']
user_powersteering = data['userPowerSteering']
user_powerwindows = data['userPowerWindows']
user_sunroof = data['userSunroof']
user_powermirrors = data['userPowerMirrors']
user_immobilizerkey = data['userImmobilizerkey']
user_abs = data['userAbs']

"""# Loading Data"""


path = 'features updated .csv'

df = pd.read_csv(path)

df2 = df[['Price', 'Model Year', 'Mileage', 'Registered City', 'Engine Type', 'Engine Capacity', 'Transmission', 'Color',
          'Assembly', 'Company', 'Model Name', 'Features']]
heat = df[['Price', 'Model Year', 'Mileage']]

idata = df2.dropna()

idata[['CruiseControl', 'AirBags', 'AirConditioning', 'AlloyRims', 'PowerLocks',
       'PowerSteering', 'PowerWindows', 'SunRoof', 'PowerMirrors', 'ImmobilizerKey', 'ABS']] = df[['CruiseControl', 'AirBags', 'AirConditioning', 'AlloyRims', 'PowerLocks',
                                                                                                   'PowerSteering', 'PowerWindows', 'SunRoof', 'PowerMirrors', 'ImmobilizerKey', 'ABS']]

data = idata.fillna(0)

# changed=data[['Company','Transmission','Assembly','Color','Engine Capacity','Engine Type','Model Name','Model Year','Mileage','Registered City','CruiseControl','AirBags',
#               'AirConditioning','AlloyRims','PowerLocks','PowerSteering','PowerWindows','SunRoof','PowerMirrors','ImmobilizerKey','ABS']]
# writer = pd.ExcelWriter('/content/drive/My Drive/Colab Notebooks/data2.xlsx')
# changed.to_excel(writer)
# writer.save()
# print('DataFrame is written successfully to Excel File.')

"""# Incorrect Data"""

# Incorrect data

# data[data['Mileage']==1]

data.drop(data[data['Mileage'] == 1].index, inplace=True)

# data['Price']<=150000) &(data['Model Year']>2005)

data.drop(data[(data['Price'] <= 150000) & (
    data['Model Year'] > 2005)].index, inplace=True)

# data['Mileage']<500

data.drop(data[data['Mileage'] < 500].index, inplace=True)

data['Model Name'] = data['Model Name'].str.rstrip()

# Companies that have appeared single time..
# data.drop(data[data['Company']=='Adam'].index,inplace=True)
# data.drop(data[data['Company']=='Classic'].index,inplace=True)
# data.drop(data[data['Company']=='Datsun'].index,inplace=True)
# data.drop(data[data['Company']=='Dongfeng'].index,inplace=True)
# data.drop(data[data['Company']=='Geely'].index,inplace=True)
# data.drop(data[data['Company']=='Golden'].index,inplace=True)
# data.drop(data[data['Company']=='JAC'].index,inplace=True)
# data.drop(data[data['Company']=='JW'].index,inplace=True)
# data.drop(data[data['Company']=='MG'].index,inplace=True)
# data.drop(data[data['Company']=='Skoda'].index,inplace=True)
# data.drop(data[data['Company']=='Smart'].index,inplace=True)
# data.drop(data[data['Company']=='Sogo'].index,inplace=True)

# counted=data.groupby(['Model Name','Company']).count()
# counted[counted['Price']>=10]

# # counted=data.groupby('Company').count()

# # counted[counted['Price']==1]
# data.groupby('Company').count()

# Writed The Data To The Data2 excel file....
# changed=data[['Registered City','Numeric RegCity','Engine Type','Numeric EType','Engine Capacity','Numeric ECapacity','Transmission','Numeric Transmission','Color','Numeric Color','Company','Numeric Company','Model Name','Numeric MName',
#               'Model Year','Numeric MYear','Mileage','Numeric Mileage']]
# writer = pd.ExcelWriter('/content/drive/My Drive/Colab Notebooks/data2.xlsx')
# data.to_excel(writer)
# writer.save()
# print('DataFrame is written successfully to Excel File.')

"""# Factorization"""

# Factorizing the String Values...
data['Numeric RegCity'] = pd.factorize(data['Registered City'])[0]
data['Numeric MName'] = pd.factorize(data['Model Name'])[0]
data['Numeric EType'] = pd.factorize(data['Engine Type'])[0]
data['Numeric ECapacity'] = pd.factorize(data['Engine Capacity'])[0]
data['Numeric Transmission'] = pd.factorize(data['Transmission'])[0]
data['Numeric Color'] = pd.factorize(data['Color'])[0]
data['Numeric Assembly'] = pd.factorize(data['Assembly'])[0]
data['Numeric Company'] = pd.factorize(data['Company'])[0]

# Replacing the availabe features with 1.
data.loc[data['ABS'] == 'ABS', 'ABS'] = 1
data.loc[data['ImmobilizerKey'] == 'ImmobilizerKey', 'ImmobilizerKey'] = 1

data.loc[data['CruiseControl'] == 'CruiseControl', 'CruiseControl'] = 1

data.loc[data['SunRoof'] == 'SunRoof', 'SunRoof'] = 1

data.loc[data['AirBags'] == 'AirBags', 'AirBags'] = 1

data.loc[data['AirConditioning'] == 'AirConditioning', 'AirConditioning'] = 1

data.loc[data['AlloyRims'] == 'AlloyRims', 'AlloyRims'] = 1

data.loc[data['PowerLocks'] == 'PowerLocks', 'PowerLocks'] = 1

data.loc[data['PowerMirrors'] == 'PowerMirrors', 'PowerMirrors'] = 1

data.loc[data['PowerSteering'] == 'PowerSteering', 'PowerSteering'] = 1

data.loc[data['PowerWindows'] == 'PowerWindows', 'PowerWindows'] = 1


"""# NORMALIZATION"""

# Scalling The Numeric Value between (0-1)
scalling = MinMaxScaler()
norm = scalling.fit_transform(data[['Numeric Company', 'Numeric Assembly', 'Numeric Color', 'Numeric Transmission', 'Numeric ECapacity', 'Numeric EType',
                                    'Numeric MName', 'Numeric RegCity', 'Model Year', 'Mileage']])
data[['Numeric Company', 'Numeric Assembly', 'Numeric Color', 'Numeric Transmission', 'Numeric ECapacity', 'Numeric EType',
      'Numeric MName', 'Numeric RegCity', 'Numeric MYear', 'Numeric Mileage']] = norm

# Graphs Commented Out....
# plt.figure(figsize=(14, 8))
# sns.heatmap(heat.corr(), annot=True)

# plt.figure(figsize=(14, 8))
# sns.lmplot(x='Model Year', y='Price', data=data)

# plt.figure(figsize=(14, 8))
# sns.lmplot(x='Mileage', y='Price', data=data)

"""# Objects To Float"""

# Converting from objects to floats...
data['CruiseControl'] = data.CruiseControl.astype(float)
data['AirBags'] = data.AirBags.astype(float)
data['AirConditioning'] = data.AirConditioning.astype(float)
data['AlloyRims'] = data.AlloyRims.astype(float)
data['PowerLocks'] = data.PowerLocks.astype(float)
data['PowerSteering'] = data.PowerSteering.astype(float)
data['PowerWindows'] = data.PowerWindows.astype(float)
data['SunRoof'] = data.SunRoof.astype(float)
data['PowerMirrors'] = data.PowerMirrors.astype(float)
data['ImmobilizerKey'] = data.ImmobilizerKey.astype(float)
data['ABS'] = data.ABS.astype(float)

# data.drop(['Registered City','Engine Type','Transmission','Assembly','Engine Capacity','Company','Model Name','Features','Color'],axis='columns',inplace=True)
# data.info()
# Seperating the dependent and independent variables.....
X = data[['Numeric Company', 'Numeric Transmission', 'Numeric Assembly', 'Numeric Color', 'Numeric ECapacity', 'Numeric EType', 'Numeric MName', 'Numeric MYear', 'Numeric Mileage',
          'Numeric RegCity', 'CruiseControl', 'AirBags', 'AirConditioning', 'AlloyRims', 'PowerLocks',
          'PowerSteering', 'PowerWindows', 'SunRoof', 'PowerMirrors', 'ImmobilizerKey', 'ABS']]
y = data['Price']

"""# User Input Matcher"""

# User Input Matcher..
# Read Data2......
path = 'data2.xlsx'

df = pd.read_excel(path)

data2 = df[['Company', 'Transmission', 'Assembly', 'Color', 'Engine Capacity', 'Engine Type', 'Model Name', 'Model Year', 'Mileage', 'Registered City', 'CruiseControl', 'AirBags',
            'AirConditioning', 'AlloyRims', 'PowerLocks', 'PowerSteering', 'PowerWindows', 'SunRoof', 'PowerMirrors', 'ImmobilizerKey', 'ABS']]
# creating new Row......
new_row = {'Company': user_company, 'Transmission': user_transmission, 'Assembly': user_assembly, 'Color': user_color, 'Engine Capacity': user_ecapacity, 'Engine Type': user_etype, 'Model Name': user_mname, 'Model Year': user_myear, 'Mileage': user_mileage, 'Registered City': user_regcity, 'CruiseControl': user_cruisecontrol,
           'AirBags': user_airbags, 'AirConditioning': user_airconditioning, 'AlloyRims': user_alloyrims, 'PowerLocks': user_powerlocks, 'PowerSteering': user_powersteering, 'PowerWindows': user_powerwindows, 'SunRoof': user_sunroof, 'PowerMirrors': user_powermirrors, 'ImmobilizerKey': user_immobilizerkey, 'ABS': user_abs}

# append row to dataframe...data2
data2 = data2.append(new_row, ignore_index=True)

# Factorizing the data2.......
data2['Numeric RegCity'] = pd.factorize(data2['Registered City'])[0]
data2['Numeric MName'] = pd.factorize(data2['Model Name'])[0]
data2['Numeric EType'] = pd.factorize(data2['Engine Type'])[0]
data2['Numeric ECapacity'] = pd.factorize(data2['Engine Capacity'])[0]
data2['Numeric Transmission'] = pd.factorize(data2['Transmission'])[0]
data2['Numeric Color'] = pd.factorize(data2['Color'])[0]
data2['Numeric Assembly'] = pd.factorize(data2['Assembly'])[0]
data2['Numeric Company'] = pd.factorize(data2['Company'])[0]

# Making the available features equal to 1...
data2.loc[data2['ABS'] == 'ABS', 'ABS'] = 1
data2.loc[data2['ImmobilizerKey'] == 'ImmobilizerKey', 'ImmobilizerKey'] = 1

data2.loc[data2['CruiseControl'] == 'CruiseControl', 'CruiseControl'] = 1

data2.loc[data2['SunRoof'] == 'SunRoof', 'SunRoof'] = 1

data2.loc[data2['AirBags'] == 'AirBags', 'AirBags'] = 1

data2.loc[data2['AirConditioning'] == 'AirConditioning', 'AirConditioning'] = 1

data2.loc[data2['AlloyRims'] == 'AlloyRims', 'AlloyRims'] = 1

data2.loc[data2['PowerLocks'] == 'PowerLocks', 'PowerLocks'] = 1

data2.loc[data2['PowerMirrors'] == 'PowerMirrors', 'PowerMirrors'] = 1

data2.loc[data2['PowerSteering'] == 'PowerSteering', 'PowerSteering'] = 1

data2.loc[data2['PowerWindows'] == 'PowerWindows', 'PowerWindows'] = 1

# Normalizing........
scalling = MinMaxScaler()
norm = scalling.fit_transform(data2[['Numeric Company', 'Numeric Assembly', 'Numeric Color', 'Numeric Transmission', 'Numeric ECapacity', 'Numeric EType',
                                     'Numeric MName', 'Numeric RegCity', 'Model Year', 'Mileage']])
data2[['Numeric Company', 'Numeric Assembly', 'Numeric Color', 'Numeric Transmission', 'Numeric ECapacity', 'Numeric EType',
       'Numeric MName', 'Numeric RegCity', 'Numeric MYear', 'Numeric Mileage']] = norm

# Matching the input with the corresponding numeric values......
company = data2[['Company', 'Numeric Company']]
user_company = company[company['Company'] ==
                       user_company]['Numeric Company'].iloc[0]

transmission = data2[['Transmission', 'Numeric Transmission']]
user_transmission = transmission[transmission['Transmission']
                                 == user_transmission]['Numeric Transmission'].iloc[0]

assembly = data2[['Assembly', 'Numeric Assembly']]
user_assembly = assembly[assembly['Assembly'] ==
                         user_assembly]['Numeric Assembly'].iloc[0]

color = data2[['Color', 'Numeric Color']]
user_color = color[color['Color'] == user_color]['Numeric Color'].iloc[0]

ecapacity = data2[['Engine Capacity', 'Numeric ECapacity']]
user_ecapacity = ecapacity[ecapacity['Engine Capacity']
                           == user_ecapacity]['Numeric ECapacity'].iloc[0]

etype = data2[['Engine Type', 'Numeric EType']]
user_etype = etype[etype['Engine Type'] == user_etype]['Numeric EType'].iloc[0]


mname = data2[['Model Name', 'Numeric MName']]
user_mname = mname[mname['Model Name'] == user_mname]['Numeric MName'].iloc[0]

myear = data2[['Model Year', 'Numeric MYear']]
user_myear = myear[myear['Model Year'] == user_myear]['Numeric MYear'].iloc[0]


mileage = data2[['Mileage', 'Numeric Mileage']]
user_mileage = mileage[mileage['Mileage'] ==
                       user_mileage]['Numeric Mileage'].iloc[0]

regcity = data2[['Registered City', 'Numeric RegCity']]
user_regcity = regcity[regcity['Registered City']
                       == user_regcity]['Numeric RegCity'].iloc[0]

# user_mileage


"""# Random Forest Regressor 96%"""

# regressor=RandomForestRegressor(n_estimators=10,random_state=0)
# data[data['Numeric Mileage']==1]

# regressor.fit(X_train,y_train)
# joblib.dump(regressor,'/content/drive/My Drive/Colab Notebooks/pricemodel.joblib')

# Loading the trained model...
model = joblib.load('pythonModel.joblib')
# model

# pred=model.predict([[0.000121,0.0,0.0,0.000000,0.4,0.8,0.00000,0.4,0.4,0.4,0.0,0.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,0.0]])
# pred=model.predict(X_test)
pred = model.predict([[user_company, user_transmission, user_assembly, user_color, user_ecapacity, user_etype, user_mname, user_myear, user_mileage, user_regcity,
                       user_cruisecontrol, user_airbags, user_airconditioning, user_alloyrims, user_powerlocks, user_powersteering, user_powerwindows, user_sunroof, user_powermirrors, user_immobilizerkey, user_abs]])

# r2_score(y_test,pred)*100
# print(f"The Predicted Value is {pred}")
price = pred[0]
# requests.post('http://localhost:3000/python/postdata',
#               json=result)  # the POST request
# print('Sended Successfully')
print(str(price))


# extra....
# counted=data.groupby('Company').count()
# counted

# counted[counted['Price']==1]

"""# Decision Tree Regressor 90%"""

# regressor = DecisionTreeRegressor(random_state=0)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# regressor.fit(X_train, y_train)

# # pred=regressor.predict(X_test)
# pred = regressor.predict([[user_company, user_transmission, user_assembly, user_color, user_ecapacity, user_etype, user_mname, user_myear, user_mileage, user_regcity,
#                            user_cruisecontrol, user_airbags, user_airconditioning, user_alloyrims, user_powerlocks, user_powersteering, user_powerwindows, user_sunroof, user_powermirrors, user_immobilizerkey, user_abs]])

# # r2_score(y_test,pred)*100
# pred


"""# Linear Regression 40%

> Indented block
"""

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# regressor = LinearRegression()

# regressor.fit(X_train, y_train)

# # pred=regressor.predict(X_test)
# pred = regressor.predict([[user_company, user_transmission, user_assembly, user_color, user_ecapacity, user_etype, user_mname, user_myear, user_mileage, user_regcity,
#                            user_cruisecontrol, user_airbags, user_airconditioning, user_alloyrims, user_powerlocks, user_powersteering, user_powerwindows, user_sunroof, user_powermirrors, user_immobilizerkey, user_abs]])

# # sns.residplot(pred,y_test-pred,lowess=True)
# # plt.title('Residual Plot')
# # plt.xlabel("Predicted Car Price")
# # plt.xticks(rotation=90)
# # plt.ylabel("Residuals")
# pred

# regressor.score(X_train, y_train)

# regressor.score(X_test, y_test)


"""# SVM (96%)"""

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# regressor = SVR(kernel='rbf')

# regressor.fit(X_train, y_train)

# # pred=model.predict(X_test)
# pred = regressor.predict([[user_company, user_transmission, user_assembly, user_color, user_ecapacity, user_etype, user_mname, user_myear, user_mileage, user_regcity,
#                            user_cruisecontrol, user_airbags, user_airconditioning, user_alloyrims, user_powerlocks, user_powersteering, user_powerwindows, user_sunroof, user_powermirrors, user_immobilizerkey, user_abs]])

# pred
# r2_score(y_test,pred)*100
