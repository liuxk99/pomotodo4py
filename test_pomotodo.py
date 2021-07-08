from unittest import TestCase

import conf
import pomotodo


class Test(TestCase):
    def test_get_todos(self):
        token = conf.load_token()
        json_items = pomotodo.get_todos(token)
        todos = []
        for e in json_items:
            todos.append(Pomo.from_json(e))

        #self.fail()
        pass
