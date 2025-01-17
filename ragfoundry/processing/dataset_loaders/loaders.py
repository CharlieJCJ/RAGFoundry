from datasets import load_dataset

from ..step import GlobalStep


class HFLoader(GlobalStep):
    """
    Class to load a dataset using the Hugging Face datasets library.
    Can use either a HuggingFace tag or a local file.
    """

    def __init__(self, dataset_config: dict, **kwargs):
        super().__init__(**kwargs)
        self.dataset_config = dataset_config

    def process(self, dataset_name, datasets, **kwargs):
        datasets[dataset_name] = load_dataset(**self.dataset_config)


class LocalLoader(GlobalStep):
    """
    Class to load a local dataset, in a JSON format.
    """

    def __init__(self, filename, **kwargs):
        super().__init__(**kwargs)
        self.filename = filename

    def process(self, dataset_name, datasets, **kwargs):
        datasets[dataset_name] = load_dataset(
            "json",
            data_files=self.filename,
            split="train",
        )
