from com.missArthas.bs4.PairFinder import PairFinder

pairFinder = PairFinder('/home/kevin/github/ParallelCorpus')
# print(pairFinder.basepath)

# pairFinder.slashPathSearch('/home/kevin/github/ParallelCorpus/websites/www.edb.gov.hk',
#                            '/home/kevin/github/ParallelCorpus/texts/www.edb.gov.hk',
#                            'en', 'sc', 0)
# pairFinder.languageSearchAll('/home/kevin/github/ParallelCorpus/websites/', '/home/kevin/github/ParallelCorpus/texts/')

pairFinder.slashSearchAll('/home/kevin/github/ParallelCorpus/websites/', '/home/kevin/github/ParallelCorpus/texts/')
# pairFinder.slashPathSearch('/Users/nali/github/ParallelCorpus/websites/www.lcsd.gov.hk/',
#                            '/Users/nali/github/ParallelCorpus/texts/www.lcsd.gov.hk/','en', 'sc', 0)