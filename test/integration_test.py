import os
import platform
import pprint
from unittest import TestCase

from grammar.models import Literal
from parser.models import Parser
from parser.utils import create_transition_diagram
from parser.utils import get_all_literals_from_non_terminals
from scanner.scanner import Scanner
from ui.manage import BASE_DIR


class Test(TestCase):
    test_cases = [file_name.split('.')[0] for file_name in os.listdir(os.path.join(BASE_DIR, 'resources/test/output'))]

    def test(self):
        with open(os.path.join(BASE_DIR, 'resources/src/predictable_grammar.txt')) as grammar_file:
            non_terminals = Literal.parse(grammar_file)
            all_literals = get_all_literals_from_non_terminals(non_terminals)
            start, states = create_transition_diagram(non_terminals)
            os.chdir(os.path.join(BASE_DIR, 'resources/test/executable'))

            for filename in Test.test_cases:

                with open(os.path.join('..', 'code', filename + '.nc')) as test_file:
                    parser = Parser(
                        states, start,
                        Scanner(
                            test_file.read(),
                            all_literals
                        )
                    )
                    errors = parser.parse()
                    if errors:
                        print(errors)
                        self.fail()
                    else:
                        with open(os.path.join(filename + '.nco'), mode='w') as output_file:
                            output_file.write(str(parser.program))
                        os.system('cp ' + filename + '.nco output.txt')
                        if platform.system() == 'Darwin':
                            os.system('./tester_Mac.out > tmptmp')
                        elif platform.system() == 'Linux':
                            os.system('./tester.out > tmptmp')
                        else:
                            assert 0, "I don't give a F*** to Windows"
                        if 0 != os.system('diff tmptmp ../output/' + filename + '.txt'):
                            print("Integration test {} failed.".format(filename))
                            pprint.pprint(parser.tree)
                            self.fail()
                        self.assertEqual(0, os.system('rm output.txt tmptmp'))
