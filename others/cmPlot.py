from sklearn.metrics import confusion_matrix
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

'''
**remember**:
    import sys
    import os
    sys.path.insert(0, os.path.join(os.getcwd()))
'''

def cmPlot(y_pred,y_test,labels):
    ax = plt.subplot()
    matrix = confusion_matrix(y_test, y_pred, labels=labels)
    matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]
    
    # Plot the matrix
    sns.heatmap(matrix,annot=True)
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels'); 
    ax.set_title('Confusion Matrix'); 
    ax.xaxis.set_ticklabels(labels)
    ax.yaxis.set_ticklabels(labels)