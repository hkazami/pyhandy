import cProfile
import io
import pstats


class Profiler(object):
    def __init__(self, filepath):
        self.cprofiler = cProfile.Profile()
        self.filepath = filepath
    
    def start(self):
        self.cprofiler.enable()
    
    def stop(self):
        self.cprofiler.disable()
        self.cprofiler.dump_stats(self.filepath)
        
        s = io.StringIO()
        stats = pstats.Stats(self.cprofiler, stream=s).sort_stats('cumtime')
        stats.print_stats()
        with open(filepath.split('.')[0] + '.prof', 'w+') as f:
            f.write(s.getvalue())

