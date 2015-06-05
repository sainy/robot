import unittest
class CI:
    def __init__(self):
        self.work_dir = "/Data/ci"
    
    def command(self, cmd):
        return " ".join(["echo", cmd])

    def main(self):
        return ["ci", self.command("cmd")]


class TestSuite(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_ci(self):
        ci = CI()
        self.assertEqual(ci.work_dir, "/Data/ci")
        self.assertEqual(ci.command("sh"), "echo sh")
        self.assertEqual(ci.command(["sh"]), "echo sh")
    
    def test_ci_main(self):
        ci = CI()
        self.assertEqual(ci.main(), ["ci", "echo cmd"])

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
    unittest.TextTestRunner(verbosity=5).run(suite)
