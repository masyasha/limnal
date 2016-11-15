require "./limnal/*"
require "kemal"

module Limnal
  get "/" do |env|
    send_file env, "public/index.html", "text/html"
  end
end

Kemal.run
