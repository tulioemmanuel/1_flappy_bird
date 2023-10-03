import json

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Configuration(metaclass=SingletonMeta):

    configuration_json = None
    SCREEN_SIZE = None

    def __init__(self):
        self.configuration_json = json.load(open('config.json'))
        self.SCREEN_SIZE = ((self.configuration_json['screen_width'],self.configuration_json['screen_height']))
        self.FPS = self.configuration_json['FPS']
        self.gravity = self.configuration_json['gravity']
        self.jump_force = self.configuration_json['jump_force']
        self.pipe_width = self.configuration_json['pipe_width']
        self.max_pipe_height = self.configuration_json['max_pipe_height']