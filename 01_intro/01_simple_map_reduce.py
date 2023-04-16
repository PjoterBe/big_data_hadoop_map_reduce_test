from mrjob.job import MRJob

class MRWordCountMRJob):

    def mapper(self, _, line):
        yield  'chars', len(line)