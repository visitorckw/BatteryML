# Licensed under the MIT License.
# Copyright (c) Microsoft Corporation.

from sklearn.linear_model import ElasticNetCV

from src.builders import MODELS
from src.models.sklearn_model import SklearnModel


@MODELS.register()
class ElasticNetRULPredictor(SklearnModel):
    def __init__(self, *args, workspace: str = None, **kwargs):
        SklearnModel.__init__(self, workspace)
        self.model = ElasticNetCV(**kwargs)
