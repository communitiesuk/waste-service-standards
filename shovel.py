import csv
import json
import jinja2
import os
import ramlfications
import time

from livereload import Server, shell
from shovel import task

RAML_FILE = 'raml/waste_services.raml'

def parse_raml(template_path):
    api = ramlfications.parse(RAML_FILE)

    data = {}
    data['collection_event_types'] = []
    with open('taxonomies/collection_event_types.csv', 'rb') as csvfile:
        spamreader = csv.DictReader(csvfile)
        # header = spamreader.read()
        for row in spamreader:
            data['collection_event_types'].append(row)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
    env.filters['jsonify'] = json.dumps
    template = env.get_template(template_path)


    f = open(os.path.join('docs', template_path), 'w')
    f.write(template.render(api=api, data=data))
    f.close()

def scan_files():
    print 'Scanning files...'
    for root, subdirs, files in os.walk('templates'):
        for f in files:
            templates_sub_path = root.replace('templates/', '')
            template = os.path.join(templates_sub_path, f)
            if f == '.DS_Store':
                continue
            parse_raml(template)

@task
def raml():
    '''Converts RAML to Markdown'''
    scan_files()


@task
def raml_watch():
    '''Converts RAML to Markdown'''

    # TODO: move to var
    # template_file = open('api-templates/api.md')
    props = os.stat(RAML_FILE)
    this = last = props.st_mtime

    print 'Watching for changes...'
    while 1:
        if this > last:
            print 'Updating output.'
            last = this

            parse_raml()

        props = os.stat(RAML_FILE)
        this = props.st_mtime
        time.sleep(0.2)

@task
def watch():
    server = Server()

    server.watch('templates/**/*', scan_files)
    server.watch('raml/*', scan_files)
    server.watch('examples/*.json', scan_files)
    server.serve()



@task
def hello(name):
    '''Prints hello and the provided name'''
    print 'Hello, %s' % name

