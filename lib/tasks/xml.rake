require 'active_support/all'
require 'json'

EXAMPLES_DIR = "./_includes/examples"

desc 'Create XML examples'
task :xml do
  puts "Creating XML examples"
  Dir.entries("./_includes/examples").each do |file|
    if file.end_with?('.json')
      content = File.open(File.join(EXAMPLES_DIR, file)).read
      content.gsub!(/\@/, '_')
      xml = JSON.parse(content).to_xml(:root => :root)
      filename = File.join(EXAMPLES_DIR, file.sub(/\.json/, '.xml'))
      out = File.open(filename, 'w')
      out.write(xml)
      out.close
    end
  end
end
