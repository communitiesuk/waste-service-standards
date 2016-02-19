import csv
import json
import jinja2
import livereload
import os
import ramlfications
import sys
import time
import yaml

from shovel import task

RAML_TEMPLATE = 'api.md'

CONFIG_FILE = "config.yml"


''' Turns a RAML file into a Markdown page. '''
def parse_raml(raml_file):
    print 'Parsing ' + raml_file
    api = ramlfications.parse(raml_file)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./_templates'))
    env.filters['jsonify'] = json.dumps
    template = env.get_template(RAML_TEMPLATE)

    # f = open(os.path.join('docs', raml_file.replace('.raml', '.md')), 'w')
    out = raml_file.replace('.raml', '.md')
    out = out.replace('_api', 'api')
    f = open(out, 'w')
    f.write(template.render(api=api))#, data=data))
    f.close()


def build_api_docs():
    print 'Building API docs...'
    # data = load_data()

    for root, subdirs, files in os.walk('_apis'):
        for f in files:
            if f == '.DS_Store':
                continue
            file_sub_path = root.replace('_apis/', '')
            file_path = os.path.join(file_sub_path, f)
            parse_raml(file_path)#, data)

@task
def raml():
    '''Converts RAML to Markdown'''
    build_api_docs()
    # convert_templates()


@task
def watch():
    raml()
    server = livereload.Server()
    server.watch('_data/**/*', convert_templates)
    server.watch('templates/**/*', convert_templates)
    server.watch('apis/*', build_api_docs)
    server.watch('examples/*.json', convert_templates)
    server.serve()

