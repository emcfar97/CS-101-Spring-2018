import unittest
import Synonym as a6

class TestAssignment(unittest.TestCase):

    def test_NormReturnsANormalizedVectorSOS(self):
        """ Tests the proper return of a normalized sum of squares. """
        
        result = a6.norm({"a":5, "b":8, "c":9})
        self.assertAlmostEqual(13.03840481, result, 3)

    def test_cosine_similarity(self):
        result = a6.cosine_similarity({"a":2, "d":8}, {"a":5, "b":8, "c":9})
        self.assertAlmostEqual(0.0930081664755, result, 3)

class TestSentenceLists(unittest.TestCase):

    def test_sentence(self):

        test_sentence = "a quick test"
        results = a6.get_sentence_lists(test_sentence)
        self.assertEqual([["a", "quick", "test"]], results)

    def test_sentence_1(self):

        test_sentence = "Hello, Jack. How is it going? Not bad; pretty good, actually... Very very good, in fact."
        results = a6.get_sentence_lists(test_sentence)
    
        answer = [['hello', 'jack'], ['how', 'is', 'it', 'going'], ['not', 'bad', 'pretty', 'good', 'actually'], ['very', 'very', 'good', 'in', 'fact']]
        self.assertEqual(answer, results)

    def test_sentence_double_spaces(self):

        test_sentence = "Hello there?   this    is    a     test."
        results = a6.get_sentence_lists(test_sentence)
        answer = [['hello', 'there'], ['this', 'is', 'a', 'test']]
        self.assertEqual(answer, results)

    def test_sentence_has_line_feeds(self):
        test_sentence = "Hello there\nthis is a test."
        results = a6.get_sentence_lists(test_sentence)
        answer = [['hello', 'there', 'this', 'is', 'a', 'test']]
        self.assertEqual(answer, results)

    def test_sentence_removes_all_punctuations(self):
        test_sentence = "Hello( there, this{ }is_ a; test.  Hope; it: works% for* you."
        results = a6.get_sentence_lists(test_sentence)
        answer = [['hello', 'there', 'this', 'is', 'a', 'test'], ["hope", "it", "works", "for", "you"]]
        self.assertEqual(answer, results)

    def test_sentence_removes_all_punctuations(self):
        test_sentence = "Hello( there, this{ }is_ a; test.  Hope; it: works% for* you."
        results = a6.get_sentence_lists(test_sentence)
        answer = [['hello', 'there', 'this', 'is', 'a', 'test'], ["hope", "it", "works", "for", "you"]]
        self.assertEqual(answer, results)

class TestSentenceFromFiles(unittest.TestCase):

    def test_sentence_from_file(self):
        results = a6.get_sentence_lists_from_files(["sample_file.txt"])
        answer = [['this', 'is', 'a', 'test'],
                    ['i', 'm', 'going', 'to', 'say', 'it', 'is'],
                    ['i', 'hope', 'it', 'works'],
                    ['if', 'not', 'then', 'you', 'still', 'have', 'work', 'to', 'do'],
                    ['e', 'm', 'c', '2']]
        self.assertEqual(answer, results)

class TestSemanticDescriptors(unittest.TestCase):

    def test_sentence_simple(self):
        test_sentence_list = [['two', 'words',]]
        results = a6.build_semantic_descriptors(test_sentence_list)
        answer = {'two': {'words': 1}, 'words': {'two': 1}}
        self.assertEqual(answer, results)
       

    def test_sentence_from_assignment(self):
        test_sentence_list = [['i', 'am', 'a', 'sick', 'man'], ['i', 'am', 'a', 'spiteful', 'man'], ['i', 'am', 'an', 'unattractive', 'man'], ['i', 'believe', 'my', 'liver', 'is', 'diseased'], ['however', 'i', 'know', 'nothing', 'at', 'all', 'about', 'my', 'disease', 'and', 'do', 'not', 'know', 'for', 'certain', 'what', 'ails', 'me']]
        results = a6.build_semantic_descriptors(test_sentence_list)
        answer = {'sick': {'man': 1, 'a': 1, 'am': 1, 'i': 1}, 'am': {'sick': 1, 'a': 2, 'an': 1, 'i': 3, 'man': 3, 'unattractive': 1, 'spiteful': 1}, 'know': {'what': 2, 'about': 2, 'disease': 2, 'my': 2, 'me': 2, 'certain': 2, 'and': 2, 'for': 2, 'do': 2, 'i': 2, 'at': 2, 'however': 2, 'all': 2, 'ails': 2, 'not': 2, 'nothing': 2}, 'disease': {'know': 2, 'ails': 1, 'about': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'not': 1, 'nothing': 1}, 'liver': {'believe': 1, 'is': 1, 'diseased': 1, 'i': 1, 'my': 1}, 'spiteful': {'man': 1, 'a': 1, 'am': 1, 'i': 1}, 'my': {'certain': 1, 'liver': 1, 'know': 2, 'ails': 1, 'and': 1, 'disease': 1, 'i': 2, 'not': 1, 'me': 1, 'believe': 1, 'nothing': 1, 'for': 1, 'do': 1, 'diseased': 1, 'at': 1, 'however': 1, 'all': 1, 'is': 1, 'about': 1, 'what': 1}, 'man': {'sick': 1, 'a': 2, 'am': 3, 'i': 3, 'unattractive': 1, 'an': 1, 'spiteful': 1}, 'and': {'know': 2, 'ails': 1, 'about': 1, 'my': 1, 'disease': 1, 'me': 1, 'certain': 1, 'nothing': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'not': 1}, 'an': {'man': 1, 'unattractive': 1, 'am': 1, 'i': 1}, 'do': {'know': 2, 'ails': 1, 'about': 1, 'my': 1, 'disease': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'not': 1, 'nothing': 1}, 'ails': {'know': 2, 'disease': 1, 'not': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'about': 1, 'nothing': 1}, 'however': {'know': 2, 'ails': 1, 'about': 1, 'disease': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'all': 1, 'what': 1, 'not': 1, 'nothing': 1}, 'all': {'know': 2, 'ails': 1, 'about': 1, 'my': 1, 'disease': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'nothing': 1, 'what': 1, 'not': 1}, 'is': {'believe': 1, 'diseased': 1, 'liver': 1, 'i': 1, 'my': 1}, 'not': {'know': 2, 'ails': 1, 'disease': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'about': 1, 'nothing': 1}, 'nothing': {'know': 2, 'ails': 1, 'about': 1, 'my': 1, 'disease': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'not': 1}, 'believe': {'diseased': 1, 'is': 1, 'liver': 1, 'i': 1, 'my': 1}, 'what': {'know': 2, 'disease': 1, 'not': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'ails': 1, 'about': 1, 'nothing': 1}, 'a': {'sick': 1, 'man': 2, 'am': 2, 'i': 2, 'spiteful': 1}, 'about': {'know': 2, 'ails': 1, 'disease': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'not': 1, 'nothing': 1}, 'me': {'know': 2, 'ails': 1, 'disease': 1, 'not': 1, 'my': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'about': 1, 'nothing': 1}, 'for': {'know': 2, 'ails': 1, 'disease': 1, 'not': 1, 'my': 1, 'me': 1, 'certain': 1, 'and': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'about': 1, 'nothing': 1}, 'diseased': {'believe': 1, 'is': 1, 'liver': 1, 'i': 1, 'my': 1}, 'at': {'know': 2, 'ails': 1, 'about': 1, 'my': 1, 'disease': 1, 'me': 1, 'certain': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'however': 1, 'all': 1, 'what': 1, 'not': 1, 'nothing': 1}, 'certain': {'know': 2, 'ails': 1, 'disease': 1, 'not': 1, 'my': 1, 'me': 1, 'and': 1, 'for': 1, 'do': 1, 'i': 1, 'at': 1, 'however': 1, 'all': 1, 'what': 1, 'about': 1, 'nothing': 1}, 'i': {'sick': 1, 'am': 3, 'know': 2, 'disease': 1, 'liver': 1, 'spiteful': 1, 'my': 2, 'believe': 1, 'and': 1, 'an': 1, 'do': 1, 'ails': 1, 'however': 1, 'all': 1, 'is': 1, 'not': 1, 'nothing': 1, 'man': 3, 'what': 1, 'a': 2, 'me': 1, 'for': 1, 'diseased': 1, 'at': 1, 'certain': 1, 'unattractive': 1, 'about': 1}, 'unattractive': {'man': 1, 'am': 1, 'i': 1, 'an': 1}}
        self.assertEqual(answer, results)

unittest.main()
