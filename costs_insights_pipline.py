import sys
from PyQt4 import QtCore, QtGui, uic
from update_gui import Ui_MainWindow
from sklearn.neural_network import MLPClassifier
from pre_process import *


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.df=pd.DataFrame()
        self.pushButton.clicked.connect(self.getCSV)
        self.GetRatio.clicked.connect(self.getratio)


    def getCSV(self):

        self.df=pd.DataFrame()
        self.comboBox0.clear()
        self.comboBox1.clear()
        self.comboBox2.clear()
        self.comboBox3.clear()
        self.comboBox4.clear()

        filePath = QtGui.QFileDialog.getOpenFileName(self,
                                                    'Single File',
                                                    '/',
                                                    '*.csv')
        #print filePath

        self.df = csv_preprocess(pd.read_csv(str(filePath)))


        self.label0.setText(self.df.iloc[:,0].name)
        self.list0 = [str(x) for x in self.df.iloc[:,0].unique().tolist()]
        self.comboBox0.addItems(self.list0)

        self.label1.setText(self.df.iloc[:,1].name)
        self.list1 = [str(x) for x in self.df.iloc[:,1].unique().tolist()]
        self.comboBox1.addItems(self.list1)

        self.label2.setText(self.df.iloc[:, 2].name)
        self.list2 = [str(x) for x in self.df.iloc[:,2].unique().tolist()]
        self.comboBox2.addItems(self.list2)

        self.label3.setText(self.df.iloc[:, 3].name)
        self.list3 = [str(x) for x in self.df.iloc[:,3].unique().tolist()]
        self.comboBox3.addItems(self.list3)

        self.label4.setText(self.df.iloc[:, 4].name)
        self.list4 = [str(x) for x in self.df.iloc[:,4].unique().tolist()]
        self.comboBox4.addItems(self.list4)

        self.X = self.df.iloc[:,:-2]
        X_dummy = pd.get_dummies(self.X)

        y1=self.df.iloc[:,-1]
        self.y1_name=y1.name
        self.rfc1 = MLPClassifier(activation='relu',solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 3))
        self.rfc1.fit(X_dummy, y1)

        y2=self.df.iloc[:,-2]
        self.y2_name=y2.name
        self.rfc2 = MLPClassifier(activation='relu',solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6, 3),learning_rate='invscaling')
        self.rfc2.fit(X_dummy, y2)

    def getratio(self):
        ###model building

        text0 = self.comboBox0.currentText()
        text1 = self.comboBox1.currentText()
        text2 = self.comboBox2.currentText()
        text3 = self.comboBox3.currentText()
        text4 = self.comboBox4.currentText()

        s = pd.Series([str(text0),str(text1),str(text2),str(text3),str(text4)],index=self.df.columns[:-2])
        x_try_dummy=pd.get_dummies(self.X.append(s,ignore_index=True)).iloc[-1,:].values.reshape(1,-1)

        Predicted_Cate1 = self.rfc1.predict(x_try_dummy)[0]
        Predicted_prob1 = round(self.rfc1.predict_proba(x_try_dummy).max(), 2)

        Predicted_Cate2 = self.rfc2.predict(x_try_dummy)[0]
        Predicted_prob2 = round(self.rfc2.predict_proba(x_try_dummy).max(), 2)

        self.result.setText("%s:%s\nAccuracy of this prediction:%s\n\n%s:%s\nAccuracy of this prediction:%s"%(self.y1_name,Predicted_Cate1,Predicted_prob1,self.y2_name,Predicted_Cate2,Predicted_prob2))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
