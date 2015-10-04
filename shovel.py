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

RAML_TEMPLATE = '_templates/api.md'
RAML_TEMPLATE = 'api.md'

CONFIG_FILE = "config.yml"


# ''' Reads all files in '_data' directory. '''
# def load_data():
#     stream = open(CONFIG_FILE, "r")
#     config = yaml.load(stream)
#     # print config['data_files']
#     data = {}
#     for f in config['data_files']:
#         (root, name) = os.path.split(f)
#         (name_no_ext, ext) = os.path.splitext(name)
#         data[name_no_ext] = []
#         load_functions[ext](f, data, name_no_ext)        
#     return data


# def load_data_as_json(path, data_store, name):
#     # print path
#     # json_data = open(path).read()
#     # print json_data
#     json_data = open(path)
#     data = json.load(json_data)
#     data_store[name] = data


# def load_data_as_csv(path, data_store, name):
#     with open(path, 'rb') as csvfile:
#         datareader = csv.DictReader(csvfile)
#         for row in datareader:
#             data_store[name].append(row)


# load_functions = {'.csv':load_data_as_csv,'.json':load_data_as_json}


# def parse_doc(template_path, data):
#     # api = ramlfications.parse(RAML_FILE)

#     env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
#     env.filters['jsonify'] = json.dumps
#     template = env.get_template(template_path)

#     f = open(os.path.join('docs', template_path), 'w')
#     f.write(template.render(data=data))
#     f.close()


# def convert_templates():
#     print 'Scanning files...'
#     data = load_data()

#     for root, subdirs, files in os.walk('templates'):
#         for f in files:
#             templates_sub_path = root.replace('templates/', '')
#             template = os.path.join(templates_sub_path, f)
#             if f == '.DS_Store':
#                 continue
#             parse_doc(template, data)


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

