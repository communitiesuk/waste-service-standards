
desc 'Create API Markdown docs'
task :api do
  sh "shovel raml"
end

desc 'Run Jekyll to build the site'
task :serve do
  sh "bundle exec jekyll serve --watch --baseurl ''"
end

task :default => :serve