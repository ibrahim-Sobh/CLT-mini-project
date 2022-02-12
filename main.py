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
