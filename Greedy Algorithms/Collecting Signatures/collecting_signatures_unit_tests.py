import unittest
from collecting_signatures import compute_optimal_points, Segment


class CollectingSignatures(unittest.TestCase):
    def test(self):
        for (segments, answer) in [
            ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], 2),
            ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1),
            ([Segment(5, 10), Segment(5, 9), Segment(6, 7), Segment(8, 9)], 2),
            ([Segment(5, 10)], 1)
        ]:
            self.assertEqual(len(compute_optimal_points(segments)), answer)


if __name__ == '__main__':
    unittest.main()
