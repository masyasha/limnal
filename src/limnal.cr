require "./limnal/*"
require "kemal"

module Limnal
  get "/" do |env|
    #send_file env, "public/index.html", "text/html"
    render "public/index.ecr", "public/1.ecr"
  end
end

Kemal.run
