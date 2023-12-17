# from https://ognjen.io/generate-pdf-of-jekyll-page/

Jekyll::Hooks.register :site, :post_write do |page|
  `wkhtmltopdf http://localhost:4000/work _site/work/resume.pdf`
end
