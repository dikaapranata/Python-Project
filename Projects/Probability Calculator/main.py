import prob_calculator

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
# print(hat.draw(4))
probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print("Probability:", probability)




