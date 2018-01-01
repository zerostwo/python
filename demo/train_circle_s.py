import numpy as np
import matplotlib.pyplot as plt
import theano
import theano.tensor as T
class Layer(object):
	def __init__(self,inputs,in_size,out_size,activation_function=None):
		self.w=theano.shared(np.random.normal(0,1,(in_size,out_size))
		self.b=theano.shared(np.zeros((out_size,))+0.1)
		self.wx_plus_b=T.dot(inputs,self.w+self.b)
		self.activation_function=activation_function
		if activation_function is None:
			self.outputs=self.wx_plus_b
		else:
			self.outputs=self.activation_function(self.wx_plus_b)


x_data=np.linspace(-1,1,300)[:,np.newaxis]
#noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5#+noise

x=T.dmatrix('x')
y=T.dmatrix('y')

#add layers
l1=Layer(x,1,10,T.nnet.relu)
l2=Layer(l1.outputs,10,1,None)

#compute the cost
cost=T.mean(T.square(l2.outputs-y))

#compute the gradients
gW1,gb1,gW2,gb2=T.grad(cost,[l1.W,l1.b,l2.W,l2.b])

#apply gradient descent
learning_rate=0.05
train=theano.function(inputs=[x,y],outputs=cost,updates=[(l1.W,l1.W-learning_rate*gW1),(l1.b,l1.b-learning_rate*gb1),(l2.W,l2.W-learning_rate*gW2),(l2.b,l2.b-learning_rate*gb2)]) 

#prediction
predict=theano.function(inputs=[x],outputs=l2.outputs)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()


for i in range(100000):
    # training
    err = train(x_data, y_data)
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = predict(x_data)
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=2)
plt.show()
