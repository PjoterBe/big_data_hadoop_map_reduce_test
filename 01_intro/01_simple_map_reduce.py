from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        yield  'chars', len(line) #liczy liczbe znaków w pliku

    def reducer(self, key, values):
        yield key, sum(values) #;iczy wszystkie znaki pliku

if __name__ == '__main__':
    MRWordCount.run()