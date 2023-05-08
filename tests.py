import unittest
from main import findPathBetween

stopIntersections = {'place-alfcl': ['Red'],
                     'place-davis': ['Red'],
                     'place-portr': ['Red'],
                     'place-harsq': ['Red'],
                     'place-cntsq': ['Red'],
                     'place-knncl': ['Red'],
                     'place-chmnl': ['Red'],
                     'place-pktrm': ['Red', 'Green-B', 'Green-C', 'Green-D', 'Green-E'],
                     'place-dwnxg': ['Red', 'Orange'],
                     'place-sstat': ['Red'],
                     'place-brdwy': ['Red'],
                     'place-andrw': ['Red'],
                     'place-jfk': ['Red'],
                     'place-shmnl': ['Red'], 'place-fldcr': ['Red'], 'place-smmnl': ['Red'],
                     'place-asmnl': ['Red', 'Mattapan'], 'place-nqncy': ['Red'], 'place-wlsta': ['Red'],
                     'place-qnctr': ['Red'], 'place-qamnl': ['Red'], 'place-brntn': ['Red'],
                     'place-cedgr': ['Mattapan'], 'place-butlr': ['Mattapan'], 'place-miltt': ['Mattapan'],
                     'place-cenav': ['Mattapan'], 'place-valrd': ['Mattapan'], 'place-capst': ['Mattapan'],
                     'place-matt': ['Mattapan'], 'place-forhl': ['Orange'], 'place-grnst': ['Orange'],
                     'place-sbmnl': ['Orange'], 'place-jaksn': ['Orange'], 'place-rcmnl': ['Orange'],
                     'place-rugg': ['Orange'], 'place-masta': ['Orange'], 'place-bbsta': ['Orange'],
                     'place-tumnl': ['Orange'], 'place-chncl': ['Orange'], 'place-state': ['Orange', 'Blue'],
                     'place-haecl': ['Orange', 'Green-D', 'Green-E'], 'place-north': ['Orange', 'Green-D', 'Green-E'],
                     'place-ccmnl': ['Orange'], 'place-sull': ['Orange'], 'place-astao': ['Orange'],
                     'place-welln': ['Orange'], 'place-mlmnl': ['Orange'], 'place-ogmnl': ['Orange'],
                     'place-gover': ['Green-B', 'Green-C', 'Green-D', 'Green-E', 'Blue'],
                     'place-boyls': ['Green-B', 'Green-C', 'Green-D', 'Green-E'],
                     'place-armnl': ['Green-B', 'Green-C', 'Green-D', 'Green-E'],
                     'place-coecl': ['Green-B', 'Green-C', 'Green-D', 'Green-E'],
                     'place-hymnl': ['Green-B', 'Green-C', 'Green-D'], 'place-kencl': ['Green-B', 'Green-C', 'Green-D'],
                     'place-bland': ['Green-B'], 'place-buest': ['Green-B'], 'place-bucen': ['Green-B'],
                     'place-amory': ['Green-B'], 'place-babck': ['Green-B'], 'place-brico': ['Green-B'],
                     'place-harvd': ['Green-B'], 'place-grigg': ['Green-B'], 'place-alsgr': ['Green-B'],
                     'place-wrnst': ['Green-B'], 'place-wascm': ['Green-B'], 'place-sthld': ['Green-B'],
                     'place-chswk': ['Green-B'], 'place-chill': ['Green-B'], 'place-sougr': ['Green-B'],
                     'place-lake': ['Green-B'], 'place-clmnl': ['Green-C'], 'place-engav': ['Green-C'],
                     'place-denrd': ['Green-C'], 'place-tapst': ['Green-C'], 'place-bcnwa': ['Green-C'],
                     'place-fbkst': ['Green-C'], 'place-bndhl': ['Green-C'], 'place-sumav': ['Green-C'],
                     'place-cool': ['Green-C'], 'place-stpul': ['Green-C'], 'place-kntst': ['Green-C'],
                     'place-hwsst': ['Green-C'], 'place-smary': ['Green-C'], 'place-river': ['Green-D'],
                     'place-woodl': ['Green-D'], 'place-waban': ['Green-D'], 'place-eliot': ['Green-D'],
                     'place-newtn': ['Green-D'], 'place-newto': ['Green-D'], 'place-chhil': ['Green-D'],
                     'place-rsmnl': ['Green-D'], 'place-bcnfd': ['Green-D'], 'place-brkhl': ['Green-D'],
                     'place-bvmnl': ['Green-D'], 'place-longw': ['Green-D'], 'place-fenwy': ['Green-D'],
                     'place-spmnl': ['Green-D', 'Green-E'], 'place-lech': ['Green-D', 'Green-E'],
                     'place-unsqu': ['Green-D'], 'place-hsmnl': ['Green-E'], 'place-bckhl': ['Green-E'],
                     'place-rvrwy': ['Green-E'], 'place-mispk': ['Green-E'], 'place-fenwd': ['Green-E'],
                     'place-brmnl': ['Green-E'], 'place-lngmd': ['Green-E'], 'place-mfa': ['Green-E'],
                     'place-nuniv': ['Green-E'], 'place-symcl': ['Green-E'], 'place-prmnl': ['Green-E'],
                     'place-esomr': ['Green-E'], 'place-gilmn': ['Green-E'], 'place-mgngl': ['Green-E'],
                     'place-balsq': ['Green-E'], 'place-mdftf': ['Green-E'], 'place-bomnl': ['Blue'],
                     'place-aqucl': ['Blue'], 'place-mvbcl': ['Blue'], 'place-aport': ['Blue'], 'place-wimnl': ['Blue'],
                     'place-orhte': ['Blue'], 'place-sdmnl': ['Blue'], 'place-bmmnl': ['Blue'], 'place-rbmnl': ['Blue'],
                     'place-wondl': ['Blue']}


class MyTestCase(unittest.TestCase):

    def testFindPathOneLine(self):
        path1 = findPathBetween('place-dwnxg', 'place-rugg', stopIntersections)
        self.assertEqual(['place-dwnxg', 'Orange', 'place-rugg'], path1)

    def testFindPathLineSwitch(self):
        path1 = findPathBetween('place-dwnxg', 'place-lech', stopIntersections)
        self.assertEqual(['place-dwnxg', 'Red', 'place-pktrm', 'Green-E', 'place-lech'], path1)

        path2 = findPathBetween('place-rugg', 'place-wondl', stopIntersections)
        self.assertEqual(['place-rugg', 'Orange', 'place-state', 'Blue', 'place-wondl'], path2)

    def testFindPathSameDestinationAsOrigin(self):
        path1 = findPathBetween('place-rugg', 'place-rugg', stopIntersections)
        self.assertEqual(['place-rugg'], path1)


    def testFindPathInvalidDestination(self):
        path1 = findPathBetween('place-rugg', 'place-atlantis', stopIntersections)
        self.assertEqual(None, path1)

    def testFindPathInvalidOrigin(self):
        path1 = findPathBetween('place-atlantis', 'place-rugg', stopIntersections)
        self.assertEqual(None, path1)


if __name__ == '__main__':
    unittest.main()
