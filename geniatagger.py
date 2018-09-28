#!/usr/bin/env python

from __future__ import print_function
from builtins import object
import argparse
import subprocess
import os.path

class GeniaTagger(object):
    """
    """
    
    def __init__(self, path_to_tagger):
        """
        
        Arguments:
        - `path_to_tagger`:
        """
        self._path_to_tagger = path_to_tagger
        self._dir_to_tagger = os.path.dirname(path_to_tagger)
        self._tagger = subprocess.Popen('./'+os.path.basename(path_to_tagger),
                                        cwd=self._dir_to_tagger,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def parse(self, text):
        """
        
        Arguments:
        - `self`:
        - `text`:
        """

        results = list()
        
        for oneline in text.split('\n'):
            try:
                self._tagger.stdin.write(oneline+'\n')
                while True:
                    r = self._tagger.stdout.readline()[:-1]
                    if not r:
                        break
                    results.append(tuple(r.split('\t')))
            except:
                continue
        return results

def callgenia(text):
    tagger = GeniaTagger("./genia/geniatagger")
    return (tagger.parse(text))

def _main():
    parser = argparse.ArgumentParser(description="GeniaTagger python binding")
    parser.add_argument('input_text')
    parser.add_argument('--tagger', help='Path to geniatagger', default='./genia/geniatagger')
    options = parser.parse_args()
    print(options.tagger)
    print(options.input_text)
    tagger = GeniaTagger(options.tagger)
    print(tagger.parse(options.input_text))
    
    pass
    
    
if __name__ == '__main__':
        _main()
        
