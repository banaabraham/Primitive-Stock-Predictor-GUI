# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:00:27 2017

@author: lenovo
"""
import pandas
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class stock_machine(object):
    def __init__(self):   
        self.data = pandas.read_csv('data_spek.csv')
        self.target = pandas.read_csv('target_spek.csv')
     
    def fitting_frt(self):   
        self.forest = RandomForestClassifier(n_estimators=5, random_state=2)  
        self.data=self.data.values
        self.target = self.target.values.reshape(len(self.target),)
        self.forest.fit(self.data,self.target)
        RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gint', max_depth=None, max_features='auto', max_leaf_nodes=None,min_samples_leaf=1,min_samples_split=2,min_weight_fraction_leaf=0.0, n_estimators=5,n_jobs=1,oob_score=False, random_state=2, verbose= 2, warm_start=False)
        y_pred_frt = self.forest.predict(self.data)
        return np.mean(y_pred_frt == self.target)
    
    def fitting_knn(self):
        self.knn =  KNeighborsClassifier(n_neighbors=1)  
        self.knn.fit(self.data,self.target)
        KNeighborsClassifier(algorithm='auto',leaf_size=30,metric='minkowski',metric_params=None,n_jobs=1,n_neighbors=1,p=2,weights='uniform')
        y_pred_knn = self.knn.predict(self.data)
        return (np.mean(y_pred_knn == self.target))
    
    def predict_frt(self,pps,book_prc,divy,pe):
        x_new = np.array([[pps,book_prc,divy,pe]])       
        prediction_frt = self.forest.predict(x_new)
        return prediction_frt
    
    def predict_knn(self,pps,book_prc,divy,pe):
        x_new = np.array([[pps,book_prc,divy,pe]])       
        prediction_knn = self.knn.predict(x_new)
        return prediction_knn
        
        

if __name__ == '__main__':
    s=stock_machine()
    print("%.2f %%"  %(s.fitting_frt()*100))
    print(s.predict_frt(1.2,1.1,1.1,12.0))
    

