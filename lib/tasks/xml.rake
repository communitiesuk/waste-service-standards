require 'active_support/all'
require 'json'

EXAMPLES_DIR = "./_includes/examples"

desc 'Create XML examples'
task :xml do
  puts "Creating XML examples"
  Dir.entries("./_includes/examples").each do |file|
    next unless file.end_with?('.json')

    filename_no_ext = file.sub(/\.json/, '')
    content = File.open(File.join(EXAMPLES_DIR, file)).read
    content.gsub!(/\@type/, 'type')
    content.gsub!(/\@id/, 'href')
    xml = JSON.parse(content).to_xml(:root => filename_no_ext)
    filename = File.join(EXAMPLES_DIR, "#{filename_no_ext}.xml")
    out = File.open(filename, 'w')
    out.write(xml)
    out.close
  end
end
