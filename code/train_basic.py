import polaris
def train():
  in = polaris.data.get_inputs()
  train_X = in[["region", "age"]]
  train_Y = in["known_price"]

  l2 = polaris.train.parameters.get("l2")
  model = sklearn.regression.fit(train_X, train_Y, l2 = l2)
  polaris.train.metrics.record("r2", model._scoring.r_2)

  # save off the artifact to the artifact storage dir
  model_path = polaris.artifacts.path_for("reg_model")
  model.save(model_path)