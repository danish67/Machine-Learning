import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0

    # Take iterations according to you
    iterations = 10000

    n = len(x)

    # Take learning rate according to you
    learning_rate = 0.08

    for i in range(iterations):

        # Formula for y_predicted -> y=mx+b where m_curr is slope and b_curr is intercept
        y_predicted = m_curr * x + b_curr

        # Formula for cost -> (1/n) * summation of (y - y_predicted)^2
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)]) 

        # Formula for m derivative -> -(2/n) * summation of (x * (y - y_predicted))
        md = -(2/n)*sum(x*(y-y_predicted))
        
        # Formula for b derivative -> -(2/n) * summation of (y - y_predicted)
        bd = -(2/n)*sum(y-y_predicted)

        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)