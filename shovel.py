import csv
import json
import jinja2
import livereload
import os
import ramlfications
import time


from shovel import task

RAML_TEMPLATE = '_layouts/api.md'
RAML_TEMPLATE = 'api.md'


''' Reads all files in '_data' directory. '''
def load_data():
    data = {}
    for f in os.listdir('_data'):
        name = f.replace('.csv', '')
        data[name] = []
        path = os.path.join('_data', f)
        with open(path, 'rb') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                data[name].append(row)
    return data


def parse_doc(template_path, data):
    api = ramlfications.parse(RAML_FILE)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
    env.filters['jsonify'] = json.dumps
    template = env.get_template(template_path)

    f = open(os.path.join('docs', template_path), 'w')
    f.write(template.render(api=api, data=data))
    f.close()


def scan_files():
    print 'Scanning files...'
    data = load_data()

    for root, subdirs, files in os.walk('templates'):
        for f in files:
            templates_sub_path = root.replace('templates/', '')
            template = os.path.join(templates_sub_path, f)
            if f == '.DS_Store':
                continue
            parse_doc(template, data)


def parse_raml(raml_file, data):
    print 'Parsing ' + raml_file
    api = ramlfications.parse(raml_file)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./_layouts'))
    env.filters['jsonify'] = json.dumps
    template = env.get_template(RAML_TEMPLATE)

    f = open(os.path.join('docs', raml_file.replace('.raml', '.md')), 'w')
    f.write(template.render(api=api, data=data))
    f.close()


def build_api_docs():
    print 'Building API docs...'
    data = load_data()

    for root, subdirs, files in os.walk('apis'):
        for f in files:
            if f == '.DS_Store':
                continue
            file_sub_path = root.replace('apis/', '')
            file_path = os.path.join(file_sub_path, f)
            parse_raml(file_path, data)

@task
def raml():
    '''Converts RAML to Markdown'''
    build_api_docs()


@task
def watch():
    server = livereload.Server()
    server.watch('templates/**/*', scan_files)
    server.watch('apis/*', build_api_docs)
    server.watch('examples/*.json', scan_files)
    server.serve()



@task
def hello(name):
    '''Prints hello and the provided name'''
    print 'Hello, %s' % name

