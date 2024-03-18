#testing utilities

import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError


class Test_read_yaml:
    yaml_files = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml"
    ]
    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):  #can also write BoxValueError which raises when empty file is passed
            read_yaml(Path(self.yaml_files[0]))

    def test_read_yaml_return_type(self):
        respone = read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(respone, ConfigBox)

    @pytest.mark.parametrize("path_to_yaml", yaml_files)  #for multiple inputs
    def test_read_yaml_bad_type(self, path_to_yaml: str):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)

