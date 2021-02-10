import polaris
import torch
def train():
  in = polaris.data.get_inputs()
  train_X = in[["region", "age"]]
  train_Y = in["known_price"]

  l2 = polaris.train.parameters.get("l2")

  model = torch.train(train_X, train_Y, l2 = l2) # this is heavily simplified.

  score for hyperopt - scoring for the NN model using inputs for this step
  not raw inputs to the model.

  test_X = polaris.pipeline.current_step.get_inputs()
  true_Y = polaris.pipeline.current_step.get_outputs()

  pred_Y = model.predict(test_X)
  r2 = torch.r2(true_Y, pred_Y)
  polaris.train.score(val=r2, "r2")
  
  # save off the artifact
  model_path = polaris.artifacts.path_for("neural_reg_model")
  torch.save(model, model_path)