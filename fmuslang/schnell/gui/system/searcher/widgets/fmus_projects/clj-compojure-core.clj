(ns todo-app.core
  (:require [todo-app.handler :as handler]
            [ring.adapter.jetty :as jetty]))

(defn -main []
  (let [port (Integer/parseInt (or (System/getenv "PORT") "3000"))]
    (jetty/run-jetty handler/app {:port port})))
