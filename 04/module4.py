# Test and validate all functions
if __name__ == "__main__":
    # Create an instance of the MultilayerPerceptron class
    mlp = MultilayerPerceptron()
    
    # Test step function with single values
    print("Step Function Tests")
    # Result should be 1
    print("Step function output for 2: ", mlp.step_function(2))
    # Result should be 0
    print("Step function output for -200: ", mlp.step_function(-200))
    
    # Test step function with an array of inputs
    inputs = np.array([1, 200, -2, 0, 500])
    # We expect 1, 1, 0, 0, 1
    print("Step function output for array", inputs, ":", mlp.step_function(inputs))
    
    # Plotting step function for a range of values
    print("Plotting Step Function...")
    mlp.plot_step_function()
    
    # Test sigmoid function with single values
    print("Sigmoid Function Tests")
    print("Sigmoid function output for 2: ", mlp.sigmoid(2))
    print("Sigmoid function output for -2: ", mlp.sigmoid(-2))
    
    # Test sigmoid function with an array of inputs
    print("Sigmoid function output for array", inputs, ":", mlp.sigmoid(inputs))
    
    # Plotting sigmoid function for a range of values
    print("Plotting Sigmoid Function...")
    mlp.plot_sigmoid_function()