import moxel
# Does it feel better to be "moxel.Image"
from moxel.space import Image

model = moxel.Model('strin/py-foo:latest', where='localhost')

# Ping the model to see if it works.
ok = model.ping()
print('ok', ok)
#
# Make a prediction.
results = model.predict(seed=123)

print(results['number'])
