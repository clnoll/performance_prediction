__author__ = 'andy'

from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np

# create data to be fitted
xdata = np.linspace(-15, 0, 301)


def fcn2min(params, x):
    """ model decaying sine wave, subtract data"""
    amp = params['amp'].value
    shift = params['shift'].value
    omega = params['omega'].value
    decay = params['decay'].value

    model = amp * np.sin(x * omega + shift) * np.exp(-x * x * decay)
    return model

params = Parameters()
params.add('amp', value=5.05301627)
params.add('decay', value=0.02566187)
params.add('shift', value=-0.11151013)
params.add('omega', value=2.00150210)

ydata = [fcn2min(params, x) for x in xdata]

try:
    import pylab
    pylab.plot(xdata, ydata, 'g')
    pylab.show()
except:
    pass
