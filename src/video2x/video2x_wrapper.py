from context import Context
import configparser
import os

class Video2x_Wrapper:
    def __init__(self, config_file: str):
        self.context = Context(config_file=None)

        config = configparser.ConfigParser()
        config.read(config_file)

        self.context.block_size = config.get('dandere2x', 'block_size')
        self.context.step_size = config.get('dandere2x', 'step_size')
        self.context.bleed = config.get('dandere2x', 'bleed')
        self.context.quality_low = config.get('dandere2x', 'quality_low')


        # setup directories
        self.context.input_frames_dir = self.workspace + "inputs" + os.path.sep
        self.context.differences_dir = self.workspace + "differences" + os.path.sep
        self.context.upscaled_dir = self.workspace + "upscaled" + os.path.sep
        self.context.correction_data_dir = self.workspace + "correction_data" + os.path.sep
        self.context.merged_dir = self.workspace + "merged" + os.path.sep
        self.context.inversion_data_dir = self.workspace + "inversion_data" + os.path.sep
        self.context.pframe_data_dir = self.workspace + "pframe_data" + os.path.sep
        self.context.debug_dir = self.workspace + "debug" + os.path.sep
        self.context.log_dir = self.workspace + "logs" + os.path.sep
        self.context.compressed_dir = self.workspace + "compressed" + os.path.sep