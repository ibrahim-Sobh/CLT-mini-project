from CLT import CLT

if __name__ == '__main__':
    # Initializing an instance of Central Limit Theorem
    model = CLT()

    # Binomial Distribution
    model.simulate_Coin_tosses()
    model.simulate_samples()
    model.displaySample()
    model.showInAction()

    # Poisson Distribution
    model.simulate_Poisson()
    model.simulate_samples()
    model.displaySample()
    model.showInAction()

    # Discrete Uniform distribution
    model.simulate_Dice_tosses()
    model.simulate_samples()
    model.displaySample()
    model.showInAction()

    # Exponential Distribution
    model.simulate_Exponential()
    model.simulate_samples()
    model.displaySample()
    model.showInAction()

# Conclusion:
#------------
# At the end we can see that the central Limit Theorem works with any kind of distribution, and it is a way for us to
# normalize our data and transform it into something useful that we can use in our machine learning algorithms. the
# more Samples we take the more similar our distribution comes to a normal distribution.
