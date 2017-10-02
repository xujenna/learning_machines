import numpy as np

andInSet = np.array([
[1,1],
[1,-1],
[-1,1],
[-1,-1]
])

andOutSet = np.array([
[1],
[-1],
[-1],
[-1]
])

orInSet = np.array([
[1,1],
[1,-1],
[-1,1],
[-1,-1]
])

orOutSet = np.array([
[1],
[1],
[1],
[-1]
])

XorInSet = np.array([
[1,1],
[1,-1],
[-1,1],
[-1,-1],
])

XorOutSet = np.array([
[-1],
[1],
[1],
[-1]
])


weight0 = np.random.random_sample()
weight1 = np.random.random_sample()
bias = np.random.random_sample()

# The Perceptron Algorithm

# 1. For every input, multiply that input by its weight. 
# 2. Sum all of the weighted inputs.
# 3. Compute the output based on that sum passed through an activation function.
# output = sign(sum)

def perceptron(dataset, knownOutputs, weight0, weight1, bias):
	predictedOutputs = [[] for i in range(len(dataset))]

	while predictedOutputs != list(knownOutputs):

		for i in range(len(dataset)): 
			input0 = dataset[i][0]
			input1 = dataset[i][1]

			sum = (input0 * weight0) + (input1 * weight1) + bias
			predictedOutputs[i] = np.sign(sum)


			print ("Predicted Outputs: ", predictedOutputs)
			print("Known Outputs: ", knownOutputs)


# Supervised Training Procedure

# 1. Provide the Perceptron with inputs for which there are known outputs.
# 2. Ask the Perceptron to guess the outputs.
# 3. Compute the error. (Error = OutputExpected − OutputGuessed)
# 4. Adjust all weights according to error (ΔWeight=Error∗Input)
# 5. Calculate new weight (WeightNew=WeightOld+ΔWeight∗LearningConstant)
# 5. Return to Step 1 and repeat.

			error = knownOutputs[i] - predictedOutputs[i]
			weight0change = error * dataset[i][0]
			weight1change = error * dataset[i][1]

			weight0 += weight0change
			weight1 += weight1change
			bias += error

			print("New Weights", weight0, weight1, bias)

	return weight0, weight1, bias, predictedOutputs

and_weight0, and_weight1, and_bias, and_prediction = perceptron(andInSet, andOutSet, weight0, weight1, bias)
print ("")
print("AND Results:")
print ("Weight0: ", and_weight0, "\nWeight1: ", and_weight1, "\nBias: ", and_bias, "\nPrediction: ", and_prediction, "\nKnown Outputs\n", andOutSet)

or_weight0, or_weight1, or_bias, or_prediction = perceptron(orInSet, orOutSet, weight0, weight1, bias)
print ("")
print("OR Results:")
print ("Weight0: ", or_weight0, "\nWeight1: ", or_weight1, "\nBias: ", or_bias, "\nPrediction: ", or_prediction, "\nKnown Outputs\n", orOutSet)

perceptron(XorInSet, XorOutSet, weight0, weight1, bias)
