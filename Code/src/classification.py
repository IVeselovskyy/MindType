import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import scipy.io


class Data:
    """Preprocessing and data collection."""

    def __init__(self, all_data):

        self.training_data = all_data
        self.epochs = 15
        self.flashes_per_epoch = 12
        self.flashes_per_character = self.epochs * self.flashes_per_epoch
        self.datapoints_per_flash = 96
        self.points_btw_flashes = 42
        self.channels = [8, 10, 12, 48, 50, 52, 60, 62]
        self.characters = []
        self.characters_number_training = 85
        self.character_signals = self.get_all_character_signals()
        self.character_labels = self.get_all_character_labels()

    def get_one_character_signals(self, index):
        one_character_signals = []
        for flash in range(180):
            one_flash = []
            for channel in self.channels:
                channel_signals = []
                for signal in range(96):
                    channel_signals.append(float(self.training_data['Signal'][index][flash*42][channel]))
                one_flash.append(max(channel_signals))
            one_character_signals.append(one_flash)
        np_one_character_signals = np.array(one_character_signals)
        return np_one_character_signals

    def get_one_character_labels(self, index):
        one_character_labels = []
        for flash in range(180):
            one_character_labels.append(self.training_data['StimulusType'][index][flash*42])
        np_character_labels = np.array(one_character_labels)
        return np_character_labels

    def get_all_character_signals(self):
        all_character_signals = []
        for character in range(85):
            all_character_signals.append(self.get_one_character_signals(character))
        return all_character_signals
    
    def get_all_character_labels(self):
        all_character_labels = []
        for character in range(85):
            all_character_labels.append(self.get_one_character_labels(character))
        return all_character_labels

class CharacterClassification:
    def __init__(self, channels_data, expected_result):
        # initializing class var
        self.training_data = channels_data
        self.training_results = expected_result
        self.lda = LinearDiscriminantAnalysis()

        self.lda.fit_transform(channels_data, expected_result)

    def is_required_character(self, channels_data):
        prediction = self.lda.predict(channels_data)
        print(prediction)
        if 0 == prediction:
            return False
        return True

