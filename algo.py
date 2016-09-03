from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('clean.csv','r'), delimiter=',', dtype='f8')[1:]    
    target = [x[1] for x in dataset]
    train = [x[2:] for x in dataset]
    test = genfromtxt(open('test.csv','r'), delimiter=',', dtype='f8')[1:]
    
    #create and train the random forest
    #multi-core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
    rf = RandomForestClassifier(n_estimators=100)
    rf.fit(train, target)

    savetxt('submission.csv', rf.predict(test), delimiter=',', fmt='%f')

if __name__=="__main__":
    main()