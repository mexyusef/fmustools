(ns todo-app.handler
  (:require [compojure.core :refer :all]
            [ring.util.response :refer [response]]))

(defroutes app-routes
  (GET "/" [] "Hello, world!"))

(def app
  (-> app-routes
      (wrap-defaults (assoc-in site-defaults [:security :anti-forgery] false))))
