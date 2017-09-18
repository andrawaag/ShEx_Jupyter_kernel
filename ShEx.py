import shlex
import json
import subprocess
import pprint


class validate:
    def __init__(self, shex, data):
        self.data = data
        self.shex = shex
        self.output = "{}"
        args = shlex.split(
            "/Users/andra/projects/shex.js/bin/validate -x {} -d {}".format(self.shex, self.data))
        try:
            p = subprocess.check_output(args)
        except subprocess.CalledProcessError as grepexc:
            #pprint.pprint(grepexc)
            #pprint.pprint(grepexc.output.decode("utf-8"))
            #pprint.pprint(grepexc.output)

            self.output = json.loads(grepexc.output)

def main():
    input_url = "https://www.wikidata.org/wiki/Special:EntityData/Q42"
    input_shex = "https://github.com/shexSpec/schemas/raw/master/Wikidata/pathways/Wikipathways/wikipathways.shex"
    shex_start = "wd:Q42"
    validation = validate(input_shex, input_url)
    pprint.pprint(validation.output["errors"])

if  __name__ =='__main__':
    main()