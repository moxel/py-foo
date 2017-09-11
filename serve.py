import random

from moxel.space import String

def predict(ins):
    seed = ins['seed'].to_str()
    random.seed(int(seed))
    result = str(random.random())
    return {
		'number': String()(result)
	}
