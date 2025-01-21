--% index/fmus
gingonic,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/.gitignore)
	.prettierrc,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/.prettierrc)
	go.mod,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/go.mod)
	go.sum,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/go.sum)
	LICENSE,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/LICENSE)
	main.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/main.go)
	Makefile,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/Makefile)
	modd.conf,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/modd.conf)
	README.md,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/README.md)
	renovate.json,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/renovate.json)
	.circleci,d(/mk)
		config.yml,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/.circleci/config.yml)
	app,d(/mk)
		config,d(/mk)
			dev.yml,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/app/config/dev.yml)
			dev.yml.default,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/app/config/dev.yml.default)
	blog,d(/mk)
		article.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/article.go)
		article_api.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/article_api.go)
		article_api_test.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/article_api_test.go)
		article_filter.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/article_filter.go)
		comment.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/comment.go)
		comment_api.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/comment_api.go)
		init.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/blog/init.go)
	cmd,d(/mk)
		api,d(/mk)
			api.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/cmd/api/api.go)
		migrate_db,d(/mk)
			1_init.up.sql,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/cmd/migrate_db/1_init.up.sql)
			migrate_db.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/cmd/migrate_db/migrate_db.go)
	httputil,d(/mk)
		middleware.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/httputil/middleware.go)
	org,d(/mk)
		auth.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/org/auth.go)
		init.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/org/init.go)
		token.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/org/token.go)
		user.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/org/user.go)
		user_api.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/org/user_api.go)
		user_api_test.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/org/user_api_test.go)
	rwe,d(/mk)
		app.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/rwe/app.go)
		postgres.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/rwe/postgres.go)
		redis.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/rwe/redis.go)
		router.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/rwe/router.go)
		uptrace.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/rwe/uptrace.go)
	scripts,d(/mk)
		Conduit.postman_collection.json,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/scripts/Conduit.postman_collection.json)
		README.md,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/scripts/README.md)
		run-api-tests.sh,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/scripts/run-api-tests.sh)
		swagger.json,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/scripts/swagger.json)
	testbed,d(/mk)
		http.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/testbed/http.go)
		util.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/testbed/util.go)
	xconfig,d(/mk)
		config.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/xconfig/config.go)
		postgres.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/xconfig/postgres.go)
		redis.go,f(e=utama=/tmp/hapus/jakartaee/go-realworld-example-app/xconfig/redis.go)
--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/.gitignore
dev.yml

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/.prettierrc
semi: false
singleQuote: true
proseWrap: always
printWidth: 100

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/go.mod
module github.com/uptrace/go-realworld-example-app

go 1.15

require (
	github.com/benbjohnson/clock v1.0.3
	github.com/dgrijalva/jwt-go v3.2.0+incompatible
	github.com/gin-gonic/gin v1.6.3
	github.com/go-pg/migrations/v8 v8.0.1
	github.com/go-pg/pg/v10 v10.6.2
	github.com/go-pg/pgext v0.2.0
	github.com/go-pg/urlstruct v1.0.0
	github.com/go-playground/validator/v10 v10.4.1 // indirect
	github.com/go-redis/cache/v8 v8.2.1
	github.com/go-redis/redis/v8 v8.3.3
	github.com/go-redis/redis_rate/v9 v9.0.2
	github.com/go-redis/redisext v0.3.1
	github.com/google/uuid v1.1.2 // indirect
	github.com/gosimple/slug v1.9.0
	github.com/json-iterator/go v1.1.10 // indirect
	github.com/klauspost/compress v1.11.2 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.1 // indirect
	github.com/onsi/ginkgo v1.14.2
	github.com/onsi/gomega v1.10.3
	github.com/segmentio/encoding v0.2.2 // indirect
	github.com/sirupsen/logrus v1.7.0
	github.com/ugorji/go v1.1.13 // indirect
	github.com/uptrace/uptrace-go v0.4.2
	github.com/vmihailenco/msgpack/v5 v5.0.0-rc.2 // indirect
	go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin v0.13.0
	go.opentelemetry.io/otel v0.13.0
	go.opentelemetry.io/otel/sdk v0.13.0
	golang.org/x/crypto v0.0.0-20201016220609-9e8e0b390897
	golang.org/x/exp v0.0.0-20201008143054-e3b2a7f2fdc7
	golang.org/x/net v0.0.0-20201031054903-ff519b6c9102 // indirect
	golang.org/x/sys v0.0.0-20201107080550-4d91cf3a1aaf // indirect
	golang.org/x/text v0.3.4 // indirect
	golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1 // indirect
	gopkg.in/yaml.v2 v2.3.0
)

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/go.sum
cloud.google.com/go v0.26.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
dmitri.shuralyov.com/gpu/mtl v0.0.0-20190408044501-666a987793e9/go.mod h1:H6x//7gZCb22OMCxBHrMx7a5I7Hp++hsVxbQ4BYO7hU=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/BurntSushi/xgb v0.0.0-20160522181843-27f122750802/go.mod h1:IVnqGOEym/WlBOVXweHU+Q+/VP0lqqI8lqeDx9IjBqo=
github.com/DataDog/sketches-go v0.0.0-20190923095040-43f19ad77ff7/go.mod h1:Q5DbzQ+3AkgGwymQO7aZFNP7ns2lZKGtvRBzRXfdi60=
github.com/DataDog/sketches-go v0.0.1 h1:RtG+76WKgZuz6FIaGsjoPePmadDBkuD/KC6+ZWu78b8=
github.com/DataDog/sketches-go v0.0.1/go.mod h1:Q5DbzQ+3AkgGwymQO7aZFNP7ns2lZKGtvRBzRXfdi60=
github.com/benbjohnson/clock v1.0.3 h1:vkLuvpK4fmtSCuo60+yC63p7y0BmQ8gm5ZXGuBCJyXg=
github.com/benbjohnson/clock v1.0.3/go.mod h1:bGMdMPoPVvcYyt1gHDf4J2KE153Yf9BuiUKYMaxlTDM=
github.com/census-instrumentation/opencensus-proto v0.2.1/go.mod h1:f6KPmirojxKA12rnyqOA5BBL4O983OfeGPqjHWSTneU=
github.com/cespare/xxhash/v2 v2.1.1 h1:6MnRN8NT7+YBpUIWxHtefFZOKTAPgGjpQSxqLNn0+qY=
github.com/cespare/xxhash/v2 v2.1.1/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/client9/misspell v0.3.4/go.mod h1:qj6jICC3Q7zFZvVWo7KLAzC3yx5G7kyvSDkc90ppPyw=
github.com/cncf/udpa/go v0.0.0-20191209042840-269d4d468f6f/go.mod h1:M8M6+tZqaGXZJjfX53e64911xZQV5JYwmTeXPW+k8Sc=
github.com/codemodus/kace v0.5.1 h1:4OCsBlE2c/rSJo375ggfnucv9eRzge/U5LrrOZd47HA=
github.com/codemodus/kace v0.5.1/go.mod h1:coddaHoX1ku1YFSe4Ip0mL9kQjJvKkzb9CfIdG1YR04=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/dgrijalva/jwt-go v3.2.0+incompatible h1:7qlOGliEKZXTDg6OTjfoBKDXWrumCAMpl/TFQ4/5kLM=
github.com/dgrijalva/jwt-go v3.2.0+incompatible/go.mod h1:E3ru+11k8xSBh+hMPgOLZmtrrCbhqsmaPHjLKYnJCaQ=
github.com/dgryski/go-rendezvous v0.0.0-20200823014737-9f7001d12a5f h1:lO4WD4F/rVNCu3HqELle0jiPLLBs70cWOduZpkS1E78=
github.com/dgryski/go-rendezvous v0.0.0-20200823014737-9f7001d12a5f/go.mod h1:cuUVRXasLTGF7a8hSLbxyZXjz+1KgoB3wDUb6vlszIc=
github.com/envoyproxy/go-control-plane v0.9.0/go.mod h1:YTl/9mNaCwkRvm6d1a2C3ymFceY/DCBVvsKhRF0iEA4=
github.com/envoyproxy/go-control-plane v0.9.1-0.20191026205805-5f8ba28d4473/go.mod h1:YTl/9mNaCwkRvm6d1a2C3ymFceY/DCBVvsKhRF0iEA4=
github.com/envoyproxy/go-control-plane v0.9.4/go.mod h1:6rpuAdCZL397s3pYoYcLgu1mIlRU8Am5FuJP05cCM98=
github.com/envoyproxy/protoc-gen-validate v0.1.0/go.mod h1:iSmxcyjqTsJpI2R4NaDN7+kN2VEUnK/pcBlmesArF7c=
github.com/fsnotify/fsnotify v1.4.7/go.mod h1:jwhsz4b93w/PPRr/qN1Yymfu8t87LnFCMoQvtojpjFo=
github.com/fsnotify/fsnotify v1.4.9 h1:hsms1Qyu0jgnwNXIxa+/V/PDsU6CfLf6CNO8H7IWoS4=
github.com/fsnotify/fsnotify v1.4.9/go.mod h1:znqG4EE+3YCdAaPaxE2ZRY/06pZUdp0tY4IgpuI1SZQ=
github.com/gin-contrib/sse v0.1.0 h1:Y/yl/+YNO8GZSjAhjMsSuLt29uWRFHdHYUb5lYOV9qE=
github.com/gin-contrib/sse v0.1.0/go.mod h1:RHrZQHXnP2xjPF+u1gW/2HnVO7nvIa9PG3Gm+fLHvGI=
github.com/gin-gonic/gin v1.6.3 h1:ahKqKTFpO5KTPHxWZjEdPScmYaGtLo8Y4DMHoEsnp14=
github.com/gin-gonic/gin v1.6.3/go.mod h1:75u5sXoLsGZoRN5Sgbi1eraJ4GU3++wFwWzhwvtwp4M=
github.com/go-gl/glfw/v3.3/glfw v0.0.0-20200222043503-6f7a984d4dc4/go.mod h1:tQ2UAYgL5IevRw8kRxooKSPJfGvJ9fJQFa0TUsXzTg8=
github.com/go-pg/migrations/v8 v8.0.1 h1:I3BOQGuWcft6Vro6MFOWee9go1YApmSRD91eDWT19vQ=
github.com/go-pg/migrations/v8 v8.0.1/go.mod h1:P+p8sfswdIZgyjB7hCrGGhjE4exeWVxhs76LpIS5cHc=
github.com/go-pg/pg/v10 v10.0.0-beta.5/go.mod h1:H9p3C643gy3Qq2MOs3NHi+iDrjF71Rzq1hXhLGBpYGk=
github.com/go-pg/pg/v10 v10.0.0-beta.8.0.20200812111426-e426cc8d5bad/go.mod h1:zReM3b5d0Ffy9d/OsqK0SNzG1kTp4BghvUMmgFVCixw=
github.com/go-pg/pg/v10 v10.0.0-beta.11/go.mod h1:8mcMTXR1lDg1AhKVxDnTurPDZeBPDy3CaINv+Ox+TqQ=
github.com/go-pg/pg/v10 v10.3.2/go.mod h1:wY0cRYyO1JfUXBF2XjkbnNvhce3WyunFDhEvZXnHbP0=
github.com/go-pg/pg/v10 v10.6.2 h1:IRvnj5AHg9eRnr101HM/w6n9jWreEx6M7kJxybxRiYg=
github.com/go-pg/pg/v10 v10.6.2/go.mod h1:BfgPoQnD2wXNd986RYEHzikqv9iE875PrFaZ9vXvtNM=
github.com/go-pg/pg/v9 v9.0.0-beta.14/go.mod h1:T2Sr6bpTCOr2lUqOUMiXLMJqZHSUBKk1LdgSqjwhZfA=
github.com/go-pg/pg/v9 v9.0.3/go.mod h1:Tm/Q3Vt6gdQOH6TTN1H/xLlIXc+Qrka7TZ6uREtu/eA=
github.com/go-pg/pg/v9 v9.1.6/go.mod h1:QM13HBLkdml4zcKOfUfGLymM6hb72aKTJLrmaH8rsFg=
github.com/go-pg/pgext v0.2.0 h1:hN5ex/T86L2/zMXp/wTlVRqf39eGKprLeoqOM+bdbOo=
github.com/go-pg/pgext v0.2.0/go.mod h1:0iPPtB2BIFZ2/Jzfr51HHcDEltm3tUVkXh4/su5u8kU=
github.com/go-pg/urlstruct v0.1.0/go.mod h1:2Nag+BIny6G/KYCkdt++ZnqU/VinzimGapKfs4kwlN0=
github.com/go-pg/urlstruct v0.2.6/go.mod h1:dxENwVISWSOX+k87hDt0ueEJadD+gZWv3tHzwfmZPu8=
github.com/go-pg/urlstruct v0.3.0/go.mod h1:/XKyiUOUUS3onjF+LJxbfmSywYAdl6qMfVbX33Q8rgg=
github.com/go-pg/urlstruct v0.4.0/go.mod h1:/XKyiUOUUS3onjF+LJxbfmSywYAdl6qMfVbX33Q8rgg=
github.com/go-pg/urlstruct v0.5.1/go.mod h1:VbjqQPvrKLolA2KROt9eUEOeYuu2mylco3uknDx05v8=
github.com/go-pg/urlstruct v1.0.0 h1:i6yB2e6m1+DtqlG9tOF9jA8+41ATdS9LUBcCNJCXVfE=
github.com/go-pg/urlstruct v1.0.0/go.mod h1:+vNFqd9u0YX0RqGCTA11SC+wRHM28EpwJpa/EwyHR+o=
github.com/go-pg/zerochecker v0.1.1/go.mod h1:NJZ4wKL0NmTtz0GKCoJ8kym6Xn/EQzXRl2OnAe7MmDo=
github.com/go-pg/zerochecker v0.2.0 h1:pp7f72c3DobMWOb2ErtZsnrPaSvHd2W4o9//8HtF4mU=
github.com/go-pg/zerochecker v0.2.0/go.mod h1:NJZ4wKL0NmTtz0GKCoJ8kym6Xn/EQzXRl2OnAe7MmDo=
github.com/go-playground/assert/v2 v2.0.1 h1:MsBgLAaY856+nPRTKrp3/OZK38U/wa0CcBYNjji3q3A=
github.com/go-playground/assert/v2 v2.0.1/go.mod h1:VDjEfimB/XKnb+ZQfWdccd7VUvScMdVu0Titje2rxJ4=
github.com/go-playground/locales v0.13.0 h1:HyWk6mgj5qFqCT5fjGBuRArbVDfE4hi8+e8ceBS/t7Q=
github.com/go-playground/locales v0.13.0/go.mod h1:taPMhCMXrRLJO55olJkUXHZBHCxTMfnGwq/HNwmWNS8=
github.com/go-playground/universal-translator v0.17.0 h1:icxd5fm+REJzpZx7ZfpaD876Lmtgy7VtROAbHHXk8no=
github.com/go-playground/universal-translator v0.17.0/go.mod h1:UkSxE5sNxxRwHyU+Scu5vgOQjsIJAF8j9muTVoKLVtA=
github.com/go-playground/validator/v10 v10.2.0/go.mod h1:uOYAAleCW8F/7oMFd6aG0GOhaH6EGOAJShg8Id5JGkI=
github.com/go-playground/validator/v10 v10.4.1 h1:pH2c5ADXtd66mxoE0Zm9SUhxE20r7aM3F26W0hOn+GE=
github.com/go-playground/validator/v10 v10.4.1/go.mod h1:nlOn6nFhuKACm19sB/8EGNn9GlaMV7XkbRSipzJ0Ii4=
github.com/go-redis/cache/v8 v8.2.1 h1:G4CtEQDT3JsiERPob1nUL/KTkiC317rAJvHx6GdWjiM=
github.com/go-redis/cache/v8 v8.2.1/go.mod h1:8PFGBZrRqG2nToSHw76mSsozxgSKrn3vsZerq/NJtt8=
github.com/go-redis/redis/v8 v8.0.0/go.mod h1:isLoQT/NFSP7V67lyvM9GmdvLdyZ7pEhsXvvyQtnQTo=
github.com/go-redis/redis/v8 v8.3.0/go.mod h1:a2xkpBM7NJUN5V5kiF46X5Ltx4WeXJ9757X/ScKUBdE=
github.com/go-redis/redis/v8 v8.3.2/go.mod h1:jszGxBCez8QA1HWSmQxJO9Y82kNibbUmeYhKWrBejTU=
github.com/go-redis/redis/v8 v8.3.3 h1:e0CL9fsFDK92pkIJH2XAeS/NwO2VuIOAoJvI6yktZFk=
github.com/go-redis/redis/v8 v8.3.3/go.mod h1:jszGxBCez8QA1HWSmQxJO9Y82kNibbUmeYhKWrBejTU=
github.com/go-redis/redis_rate/v9 v9.0.2 h1:Uwj0zTwwODzmL5E3UeN78jnyFxN41itYgkkCfqNYc7w=
github.com/go-redis/redis_rate/v9 v9.0.2/go.mod h1:Vrl8qDpRb7bHcLyr7OXVtKKww4bD8dLL9gmUdA6XClg=
github.com/go-redis/redisext v0.3.1 h1:Qh6Z8xxjt7F8Aa8BILk9ssW73UcTcXDytvblouBHWCE=
github.com/go-redis/redisext v0.3.1/go.mod h1:RsxZvP0ikgPfqLUIJ9MfRTDODm5PCW1UHO9DI9IMumU=
github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b/go.mod h1:SBH7ygxi8pfUlaOkMMuAQtPIUF8ecWP5IEl/CR7VP2Q=
github.com/golang/mock v1.1.1/go.mod h1:oTYuIxOrZwtPieC+H1uAHpcLFnEyAGVDL/k47Jfbm0A=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.1/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.2/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.3/go.mod h1:vzj43D7+SQXF/4pzW/hwtAqwc6iTitCiVSaWz5lYuqw=
github.com/golang/protobuf v1.3.4/go.mod h1:vzj43D7+SQXF/4pzW/hwtAqwc6iTitCiVSaWz5lYuqw=
github.com/golang/protobuf v1.4.0-rc.1/go.mod h1:ceaxUfeHdC40wWswd/P6IGgMaK3YpKi5j83Wpe3EHw8=
github.com/golang/protobuf v1.4.0-rc.1.0.20200221234624-67d41d38c208/go.mod h1:xKAWHe0F5eneWXFV3EuXVDTCmh+JuBKY0li0aMyXATA=
github.com/golang/protobuf v1.4.0-rc.2/go.mod h1:LlEzMj4AhA7rCAGe4KMBDvJI+AwstrUpVNzEA03Pprs=
github.com/golang/protobuf v1.4.0-rc.4.0.20200313231945-b860323f09d0/go.mod h1:WU3c8KckQ9AFe+yFwt9sWVRKCVIyN9cPHBJSNnbL67w=
github.com/golang/protobuf v1.4.0/go.mod h1:jodUvKwWbYaEsadDk5Fwe5c77LiNKVO9IDvqG2KuDX0=
github.com/golang/protobuf v1.4.1/go.mod h1:U8fpvMrcmy5pZrNK1lt4xCsGvpyWQ/VVv6QDs8UjoX8=
github.com/golang/protobuf v1.4.2/go.mod h1:oDoupMAO8OvCJWAcko0GGGIgR6R6ocIYbsSw735rRwI=
github.com/golang/protobuf v1.4.3 h1:JjCZWpVbqXDqFVmTfYWEVTMIYrL/NPdPSCHPJ0T/raM=
github.com/golang/protobuf v1.4.3/go.mod h1:oDoupMAO8OvCJWAcko0GGGIgR6R6ocIYbsSw735rRwI=
github.com/google/go-cmp v0.2.0/go.mod h1:oXzfMopK8JAjlY9xF4vHSVASa0yLyX7SntLO5aqRK0M=
github.com/google/go-cmp v0.3.0/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.3.1/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.4.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.0/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.1/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.2 h1:X2ev0eStA3AbceY54o37/0PQ/UWqKEiiO2dKL5OPaFM=
github.com/google/go-cmp v0.5.2/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/gofuzz v1.1.0 h1:Hsa8mG0dQ46ij8Sl2AYJDUv1oA9/d6Vk+3LG99Oe02g=
github.com/google/gofuzz v1.1.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/google/uuid v1.1.2 h1:EVhdT+1Kseyi1/pUmXKaFxYsDNy9RQYkMWRH68J/W7Y=
github.com/google/uuid v1.1.2/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/gosimple/slug v1.9.0 h1:r5vDcYrFz9BmfIAMC829un9hq7hKM4cHUrsv36LbEqs=
github.com/gosimple/slug v1.9.0/go.mod h1:AMZ+sOVe65uByN3kgEyf9WEBKBCSS+dJjMX9x4vDJbg=
github.com/hpcloud/tail v1.0.0/go.mod h1:ab1qPbhIpdTxEkNHXyeSf5vhxWSCs/tWer42PpOxQnU=
github.com/jinzhu/inflection v1.0.0 h1:K317FqzuhWc8YvSVlFMCCUb36O/S9MCKRDI7QkRKD/E=
github.com/jinzhu/inflection v1.0.0/go.mod h1:h+uFLlag+Qp1Va5pdKtLDYj+kHp5pxUVkryuEj+Srlc=
github.com/json-iterator/go v1.1.9/go.mod h1:KdQUCv79m/52Kvf8AW2vK1V8akMuk1QjK/uOdHXbAo4=
github.com/json-iterator/go v1.1.10 h1:Kz6Cvnvv2wGdaG/V8yMvfkmNiXq9Ya2KUv4rouJJr68=
github.com/json-iterator/go v1.1.10/go.mod h1:KdQUCv79m/52Kvf8AW2vK1V8akMuk1QjK/uOdHXbAo4=
github.com/klauspost/compress v1.11.1/go.mod h1:aoV0uJVorq1K+umq18yTdKaF57EivdYsUV+/s2qKfXs=
github.com/klauspost/compress v1.11.2 h1:MiK62aErc3gIiVEtyzKfeOHgW7atJb5g/KNX5m3c2nQ=
github.com/klauspost/compress v1.11.2/go.mod h1:aoV0uJVorq1K+umq18yTdKaF57EivdYsUV+/s2qKfXs=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/leodido/go-urn v1.2.0 h1:hpXL4XnriNwQ/ABnpepYM/1vCLWNDfUNts8dX3xTG6Y=
github.com/leodido/go-urn v1.2.0/go.mod h1:+8+nEpDfqqsY+g338gtMEUOtuK+4dEMhiQEgxpxOKII=
github.com/mattn/go-isatty v0.0.12 h1:wuysRhFDzyxgEmMf5xjvJ2M9dZoWAXNNr5LSBS7uHXY=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd h1:TRLaZ9cD/w8PVh93nsPXa1VrQ6jlwL5oN8l14QlcNfg=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/modern-go/reflect2 v1.0.1 h1:9f412s+6RmYXLWZSEzVVgPGK7C2PphHj5RJrvfx9AWI=
github.com/modern-go/reflect2 v1.0.1/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/niemeyer/pretty v0.0.0-20200227124842-a10e7caefd8e h1:fD57ERR4JtEqsWbfPhv4DMiApHyliiK5xCTNVSPiaAs=
github.com/niemeyer/pretty v0.0.0-20200227124842-a10e7caefd8e/go.mod h1:zD1mROLANZcx1PVRCS0qkT7pwLkGfwJo4zjcN/Tysno=
github.com/nxadm/tail v1.4.4 h1:DQuhQpB1tVlglWS2hLQ5OV6B5r8aGxSrPc5Qo6uTN78=
github.com/nxadm/tail v1.4.4/go.mod h1:kenIhsEOeOJmVchQTgglprH7qJGnHDVpk1VPCcaMI8A=
github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/ginkgo v1.10.1/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/ginkgo v1.12.1/go.mod h1:zj2OWP4+oCPe1qIXoGWkgMRwljMUYCdkwsT2108oapk=
github.com/onsi/ginkgo v1.14.0/go.mod h1:iSB4RoI2tjJc9BBv4NKIKWKya62Rps+oPG/Lv9klQyY=
github.com/onsi/ginkgo v1.14.1/go.mod h1:iSB4RoI2tjJc9BBv4NKIKWKya62Rps+oPG/Lv9klQyY=
github.com/onsi/ginkgo v1.14.2 h1:8mVmC9kjFFmA8H4pKMUhcblgifdkOIXPvbhN1T36q1M=
github.com/onsi/ginkgo v1.14.2/go.mod h1:iSB4RoI2tjJc9BBv4NKIKWKya62Rps+oPG/Lv9klQyY=
github.com/onsi/gomega v1.7.0/go.mod h1:ex+gbHU/CVuBBDIJjb2X0qEXbFg53c61hWP/1CpauHY=
github.com/onsi/gomega v1.7.1/go.mod h1:XdKZgCCFLUoM/7CFJVPcG8C1xQ1AJ0vpAezJrB7JYyY=
github.com/onsi/gomega v1.10.1/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
github.com/onsi/gomega v1.10.2/go.mod h1:iN09h71vgCQne3DLsj+A5owkum+a2tYe+TOCB1ybHNo=
github.com/onsi/gomega v1.10.3 h1:gph6h/qe9GSUw1NhH1gp+qb+h8rXD8Cy60Z32Qw3ELA=
github.com/onsi/gomega v1.10.3/go.mod h1:V9xEwhxec5O8UDM77eCW8vLymOMltsqPVYWrpDsH8xc=
github.com/opentracing/opentracing-go v1.1.1-0.20190913142402-a7454ce5950e/go.mod h1:UkNAQd3GIcIGf0SeVgPpRdFStlNbqXla1AfSYxPUl2o=
github.com/opentracing/opentracing-go v1.2.0/go.mod h1:GxEUsuufX4nBwe+T+Wl9TAgYrxe9dPLANfrWvHYVTgc=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/prometheus/client_model v0.0.0-20190812154241-14fe0d1b01d4/go.mod h1:xMI15A0UPsDsEKsMN9yxemIoYk6Tm2C1GtYGdfGttqA=
github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be h1:ta7tUOvsPHVHGom5hKW5VXNc2xZIkfCKP8iaqOyYtUQ=
github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be/go.mod h1:MIDFMn7db1kT65GmV94GzpX9Qdi7N/pQlwb+AN8wh+Q=
github.com/segmentio/encoding v0.1.10/go.mod h1:RWhr02uzMB9gQC1x+MfYxedtmBibb9cZ6Vv9VxRSSbw=
github.com/segmentio/encoding v0.1.14/go.mod h1:RWhr02uzMB9gQC1x+MfYxedtmBibb9cZ6Vv9VxRSSbw=
github.com/segmentio/encoding v0.1.15/go.mod h1:RWhr02uzMB9gQC1x+MfYxedtmBibb9cZ6Vv9VxRSSbw=
github.com/segmentio/encoding v0.2.0/go.mod h1:MJjRE6bMDocliO2FyFC2Dusp+uYdBfHWh5Bw7QyExto=
github.com/segmentio/encoding v0.2.2 h1:l0O7kBxWTfZcYMuOtuwLOvmqo2Sab0PwbG9utSaAzsE=
github.com/segmentio/encoding v0.2.2/go.mod h1:MJjRE6bMDocliO2FyFC2Dusp+uYdBfHWh5Bw7QyExto=
github.com/sirupsen/logrus v1.7.0 h1:ShrD1U9pZB12TX0cVy0DtePoCH97K8EtX+mg7ZARUtM=
github.com/sirupsen/logrus v1.7.0/go.mod h1:yWOB1SBYBC5VeMP7gHvWumXLIWorT60ONWic61uBYv0=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/stretchr/testify v1.5.1/go.mod h1:5W2xD1RspED5o8YsWQXVCued0rvSQ+mT+I5cxcmMvtA=
github.com/stretchr/testify v1.6.1 h1:hDPOHmpOpP40lSULcqw7IrRb/u7w6RpDC9399XyoNd0=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/tmthrgd/go-hex v0.0.0-20190904060850-447a3041c3bc h1:9lRDQMhESg+zvGYmW5DyG0UqvY96Bu5QYsTLvCHdrgo=
github.com/tmthrgd/go-hex v0.0.0-20190904060850-447a3041c3bc/go.mod h1:bciPuU6GHm1iF1pBvUfxfsH0Wmnc2VbpgvbI9ZWuIRs=
github.com/ugorji/go v1.1.7/go.mod h1:kZn38zHttfInRq0xu/PH0az30d+z6vm202qpg1oXVMw=
github.com/ugorji/go v1.1.13 h1:nB3O5kBSQGjEQAcfe1aLUYuxmXdFKmYgBZhY32rQb6Q=
github.com/ugorji/go v1.1.13/go.mod h1:jxau1n+/wyTGLQoCkjok9r5zFa/FxT6eI5HiHKQszjc=
github.com/ugorji/go/codec v1.1.7/go.mod h1:Ax+UKWsSmolVDwsd+7N3ZtXu+yMGCf907BLYF3GoBXY=
github.com/ugorji/go/codec v1.1.13 h1:013LbFhocBoIqgHeIHKlV4JWYhqogATYWZhIcH0WHn4=
github.com/ugorji/go/codec v1.1.13/go.mod h1:oNVt3Dq+FO91WNQ/9JnHKQP2QJxTzoN7wCBFCq1OeuU=
github.com/uptrace/uptrace-go v0.4.2 h1:GtYmOcGXql1BIWqgi/U4+bW1VDH+uQjCci+qb8yqnEQ=
github.com/uptrace/uptrace-go v0.4.2/go.mod h1:BnBB3O6BMIAv5am66zvQOxJ+luIsFsU5PkYpwydhkiE=
github.com/vmihailenco/bufpool v0.1.5/go.mod h1:fL9i/PRTuS7AELqAHwSU1Zf1c70xhkhGe/cD5ud9pJk=
github.com/vmihailenco/bufpool v0.1.11 h1:gOq2WmBrq0i2yW5QJ16ykccQ4wH9UyEsgLm6czKAd94=
github.com/vmihailenco/bufpool v0.1.11/go.mod h1:AFf/MOy3l2CFTKbxwt0mp2MwnqjNEs5H/UxrkA5jxTQ=
github.com/vmihailenco/go-tinylfu v0.1.0 h1:wNwKigNq50gfiyQDPpseEuGK4TZtFyjduJSg0M6gBns=
github.com/vmihailenco/go-tinylfu v0.1.0/go.mod h1:qZbD6U3F10Sfuxyy4c5wMq5CM4/t5I3eJJS9yMQoXU0=
github.com/vmihailenco/msgpack/v4 v4.3.5/go.mod h1:DuaveEe48abshDmz5UBKyZ+yDugvaeFk5ayfrewUOaw=
github.com/vmihailenco/msgpack/v4 v4.3.7/go.mod h1:Ii+PksJlvFT5ZRcB/4YLAInMIp6a0WOCm0L3BU0aNG4=
github.com/vmihailenco/msgpack/v4 v4.3.11/go.mod h1:gborTTJjAo/GWTqqRjrLCn9pgNN+NXzzngzBKDPIqw4=
github.com/vmihailenco/msgpack/v5 v5.0.0-beta.1/go.mod h1:xlngVLeyQ/Qi05oQxhQ+oTuqa03RjMwMfk/7/TCs+QI=
github.com/vmihailenco/msgpack/v5 v5.0.0-beta.5/go.mod h1:MPECSZPg8yittBek5Gq2MhEDJpB9FrbSzQOSWmJm38A=
github.com/vmihailenco/msgpack/v5 v5.0.0-rc.2 h1:ognci8XPlosGhIHK1OLYSpSpnlhSFeBklfe18zIEwcU=
github.com/vmihailenco/msgpack/v5 v5.0.0-rc.2/go.mod h1:HVxBVPUK/+fZMonk4bi1islLa8V3cfnBug0+4dykPzo=
github.com/vmihailenco/tagparser v0.1.0/go.mod h1:OeAg3pn3UbLjkWt+rN9oFYB6u/cQgqMEUPoW2WPyhdI=
github.com/vmihailenco/tagparser v0.1.1/go.mod h1:OeAg3pn3UbLjkWt+rN9oFYB6u/cQgqMEUPoW2WPyhdI=
github.com/vmihailenco/tagparser v0.1.2 h1:gnjoVuB/kljJ5wICEEOpx98oXMWPLj22G67Vbd1qPqc=
github.com/vmihailenco/tagparser v0.1.2/go.mod h1:OeAg3pn3UbLjkWt+rN9oFYB6u/cQgqMEUPoW2WPyhdI=
go.opentelemetry.io/contrib v0.13.0 h1:q34CFu5REx9Dt2ksESHC/doIjFJkEg1oV3aSwlL5JR0=
go.opentelemetry.io/contrib v0.13.0/go.mod h1:HzCu6ebm0ywgNxGaEfs3izyJOMP4rZnzxycyTgpI5Sg=
go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin v0.13.0 h1:kuqJ1YxAzMooElHDX5KzqyW9NLB4zWAamDF+d1p5Z8w=
go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin v0.13.0/go.mod h1:lQTQqWUP6YaM5x6lRi2ocfLSyoJ+Dc105u4zjIU3oLs=
go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace v0.13.0 h1:T6W6DcsRSLxMCv2J96fAkHaKu+V3tW/8vXdPNe/1B1A=
go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace v0.13.0/go.mod h1:TwTkyRaTam1pOIb2wxcAiC2hkMVbokXkt6DEt5nDkD8=
go.opentelemetry.io/contrib/propagators v0.13.0 h1:kvhyo7uEkOHzKLBCp0w6b5ZMukRHFOxgRgGQ7lLWFoM=
go.opentelemetry.io/contrib/propagators v0.13.0/go.mod h1:UYroyL3i60+ruw9LER9RhHNvBRo495v/LNpRwU/CJyQ=
go.opentelemetry.io/otel v0.7.0/go.mod h1:aZMyHG5TqDOXEgH2tyLiXSUKly1jT3yqE9PmrzIeCdo=
go.opentelemetry.io/otel v0.10.0/go.mod h1:n3v1JGUBpn5DafiF1UeoDs5fr5XZMG+43kigDtFB8Vk=
go.opentelemetry.io/otel v0.11.0/go.mod h1:G8UCk+KooF2HLkgo8RHX9epABH/aRGYET7gQOqBVdB0=
go.opentelemetry.io/otel v0.12.0/go.mod h1:dlSNewoRYikTkotEnxdmuBHgzT+k/idJSfDv/FxEnOY=
go.opentelemetry.io/otel v0.13.0 h1:2isEnyzjjJZq6r2EKMsFj4TxiQiexsM04AVhwbR/oBA=
go.opentelemetry.io/otel v0.13.0/go.mod h1:dlSNewoRYikTkotEnxdmuBHgzT+k/idJSfDv/FxEnOY=
go.opentelemetry.io/otel/exporters/stdout v0.13.0 h1:A+XiGIPQbGoJoBOJfKAKnZyiUSjSWvL3XWETUvtom5k=
go.opentelemetry.io/otel/exporters/stdout v0.13.0/go.mod h1:JJt8RpNY6K+ft9ir3iKpceCvT/rhzJXEExGrWFCbv1o=
go.opentelemetry.io/otel/sdk v0.13.0 h1:4VCfpKamZ8GtnepXxMRurSpHpMKkcxhtO33z1S4rGDQ=
go.opentelemetry.io/otel/sdk v0.13.0/go.mod h1:dKvLH8Uu8LcEPlSAUsfW7kMGaJBhk/1NYvpPZ6wIMbU=
golang.org/x/crypto v0.0.0-20180910181607-0e37d006457b/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190923035154-9ee001bba392/go.mod h1:/lpIB1dKB+9EgE3H3cr1v9wB50oz8l4C4h62xy7jSTY=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20191029031824-8986dd9e96cf/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20191128160524-b544559bb6d1/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200221231518-2aa609cf4a9d/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200622213623-75b288015ac9/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200728195943-123391ffb6de/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200820211705-5c72a883971a/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20201002170205-7f63de1d35b0/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20201012173705-84dcc777aaee/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20201016220609-9e8e0b390897 h1:pLI5jrR7OSLijeIDcmRxNmw2api+jEfxLoykJVice/E=
golang.org/x/crypto v0.0.0-20201016220609-9e8e0b390897/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/exp v0.0.0-20190121172915-509febef88a4/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20190306152737-a1d7652674e8/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/exp v0.0.0-20200513190911-00229845015e/go.mod h1:4M0jN8W1tt0AVLNr8HDosyJCDCDuyL9N9+3m7wDWgKw=
golang.org/x/exp v0.0.0-20200821190819-94841d0725da/go.mod h1:3jZMyOhIsHpP37uCMkUooju7aAi5cS1Q23tOzKc+0MU=
golang.org/x/exp v0.0.0-20200901203048-c4f52b2c50aa/go.mod h1:3jZMyOhIsHpP37uCMkUooju7aAi5cS1Q23tOzKc+0MU=
golang.org/x/exp v0.0.0-20200908183739-ae8ad444f925/go.mod h1:1phAWC201xIgDyaFpmDeZkgf70Q4Pd/CNqfRtVPtxNw=
golang.org/x/exp v0.0.0-20201008143054-e3b2a7f2fdc7 h1:2/QncOxxpPAdiH+E00abYw/SaQG353gltz79Nl1zrYE=
golang.org/x/exp v0.0.0-20201008143054-e3b2a7f2fdc7/go.mod h1:1phAWC201xIgDyaFpmDeZkgf70Q4Pd/CNqfRtVPtxNw=
golang.org/x/image v0.0.0-20190227222117-0694c2d4d067/go.mod h1:kZ7UVZpmo3dzQBMxlp+ypCbDeSB+sBbTgSJuh5dn5js=
golang.org/x/image v0.0.0-20190802002840-cff245a6509b/go.mod h1:FeLwcggjj3mMvU+oOTbSwawSJRM1uh48EjtB4UJZlP0=
golang.org/x/lint v0.0.0-20181026193005-c67002cb31c3/go.mod h1:UVdnD1Gm6xHRNCYTkRU2/jEulfH38KcIWyp/GAMgvoE=
golang.org/x/lint v0.0.0-20190227174305-5b3e6a55c961/go.mod h1:wehouNa3lNwaWXcvxsM5YxQ5yQlVC4a0KAMCusXpPoU=
golang.org/x/lint v0.0.0-20190313153728-d0100b6bd8b3/go.mod h1:6SW0HCj/g11FgYtHlgUYUwCkIfeOF89ocIRzGO/8vkc=
golang.org/x/mobile v0.0.0-20190719004257-d2bd2a29d028/go.mod h1:E/iHnbuqvinMTCcRqshq8CkpyQDoeVncDDYHnLhea+o=
golang.org/x/mod v0.1.1-0.20191105210325-c90efee705ee/go.mod h1:QqPTAvyqsEbceGzBzNggFXnrqF1CaUcvgkdR5Ot7KZg=
golang.org/x/mod v0.1.1-0.20191107180719-034126e5016b/go.mod h1:QqPTAvyqsEbceGzBzNggFXnrqF1CaUcvgkdR5Ot7KZg=
golang.org/x/mod v0.3.1-0.20200828183125-ce943fd02449/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180826012351-8a410e7b638d/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180906233101-161cd47e91fd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190213061140-3a22650c66bd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190420063019-afa5a82059c6/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190603091049-60506f45cf65/go.mod h1:HSz+uSET+XFnRR8LxR5pz3Of3rY3CfYBVs4xY44aLks=
golang.org/x/net v0.0.0-20190613194153-d28f0bde5980/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190923162816-aa69164e4478/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20191209160850-c0dbc17a3553/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200202094626-16171245cfb2/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200222033325-078779b8f2d8/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200301022130-244492dfa37a/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200520004742-59133d7f0dd7/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/net v0.0.0-20200625001655-4c5254603344/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20200707034311-ab3426394381/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20200822124328-c89045814202/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20200925080053-05aa5d4ee321/go.mod h1:/O7V0waA8r7cgGh81Ro3o1hOxt32SMVPicZroKQ2sZA=
golang.org/x/net v0.0.0-20201006153459-a7d1128ccaa0/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201009032441-dbdefad45b89/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201010224723-4f7140c49acb/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201022231255-08b38378de70/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201024042810-be3efd7ff127/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/net v0.0.0-20201031054903-ff519b6c9102 h1:42cLlJJdEh+ySyeUUbEQ5bsTiq8voBeTuweGVkY6Puw=
golang.org/x/net v0.0.0-20201031054903-ff519b6c9102/go.mod h1:sp8m0HH+o8qH0wwXwYZr8TS3Oi6o0r6Gce1SSxlDquU=
golang.org/x/oauth2 v0.0.0-20180821212333-d2e6202438be/go.mod h1:N/0e6XlmueqKjAGxoOufVs8QHGRruUQn6yWY3a++T0U=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181108010431-42b317875d0f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9 h1:SQFwaSi55rU7vdNs9Yr0Z324VNlrF+0wMqRXT4St8ck=
golang.org/x/sync v0.0.0-20201020160332-67f06af15bc9/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180830151530-49385e6e1522/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20180909124046-d0be0721c37e/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190312061237-fead79001313/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190904154756-749cb33beabd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190922100055-0a153f010e69/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191001151750-bb3f8db39f24/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191005200804-aed5e4c7ecf9/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191010194322-b09406accb47/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191026070338-33540a1f6037/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191120155948-bd437916bb0e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200323222414-85ca7c5b95cd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200519105757-fe76b779f299/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200615200032-f1bc736245b1/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200625212154-ddb9806d33ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200810151505-1b9f1253b3ed/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200824131525-c12d262b63d8/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200831180312-196b9ba8737a/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200923182605-d9f96fdee20d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200930185726-fdedc70b468f/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201009025420-dfb3f7c4e634/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201015000850-e3ed0017c211/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201107080550-4d91cf3a1aaf h1:kt3wY1Lu5MJAnKTfoMR52Cu4gwvna4VTzNOiT8tY73s=
golang.org/x/sys v0.0.0-20201107080550-4d91cf3a1aaf/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.2/go.mod h1:bEr9sfX3Q8Zfm5fL9x+3itogRgK3+ptLWKqgva+5dAk=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.4 h1:0YWbFKbhXG/wIiuHDSKpS0Iy7FSA+u45VtBMfQcFTTc=
golang.org/x/text v0.3.4/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190114222345-bf090417da8b/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190226205152-f727befe758c/go.mod h1:9Yl7xja0Znq3iFh3HoIrodX9oNMXvdceNzlUR8zjMvY=
golang.org/x/tools v0.0.0-20190311212946-11955173bddd/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190524140312-2c0ae7006135/go.mod h1:RgjU9mgBXZiqYHBnxXauZ1Gv1EHHAz9KjViQ78xBX0Q=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20200207183749-b753a1ba74fa/go.mod h1:TB2adYChydJhpapKDTa4BR/hXlZSLoq2Wpct/0txZ28=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1 h1:go1bK/D/BFZV2I8cIQd1NKEZ+0owSTG1fDTci4IqFcE=
golang.org/x/xerrors v0.0.0-20200804184101-5ec99f83aff1/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/appengine v1.1.0/go.mod h1:EbEs0AVv82hx2wNQdGPgUI5lhzA/G0D9YwlJXL52JkM=
google.golang.org/appengine v1.4.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/appengine v1.6.5/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/appengine v1.6.6/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/appengine v1.6.7/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/genproto v0.0.0-20180817151627-c66870c02cf8/go.mod h1:JiN7NxoALGmiZfu7CAH4rXhgtRTLTxftemlI0sWmxmc=
google.golang.org/genproto v0.0.0-20190819201941-24fa4b261c55/go.mod h1:DMBHOl98Agz4BDEuKkezgsaosCRResVns1a3J2ZsMNc=
google.golang.org/genproto v0.0.0-20191009194640-548a555dbc03/go.mod h1:n3cpQtvxv34hfy77yVDNjmbRyujviMdxYliBSkLhpCc=
google.golang.org/genproto v0.0.0-20200526211855-cb27e3aa2013/go.mod h1:NbSheEEYHJ7i3ixzK3sjbqSGDJWnxyFXZblF3eUsNvo=
google.golang.org/grpc v1.19.0/go.mod h1:mqu4LbDTu4XGKhr4mRzUsmM4RtVoemTSY81AxZiDr8c=
google.golang.org/grpc v1.23.0/go.mod h1:Y5yQAOtifL1yxbo5wqy6BxZv8vAUGQwXBOALyacEbxg=
google.golang.org/grpc v1.25.1/go.mod h1:c3i+UQWmh7LiEpx4sFZnkU36qjEYZ0imhYfXVyQciAY=
google.golang.org/grpc v1.27.0/go.mod h1:qbnxyOmOxrQa7FizSgH+ReBfzJrCY1pSN7KXBS8abTk=
google.golang.org/grpc v1.30.0/go.mod h1:N36X2cJ7JwdamYAgDz+s+rVMFjt3numwzf/HckM8pak=
google.golang.org/grpc v1.31.0/go.mod h1:N36X2cJ7JwdamYAgDz+s+rVMFjt3numwzf/HckM8pak=
google.golang.org/protobuf v0.0.0-20200109180630-ec00e32a8dfd/go.mod h1:DFci5gLYBciE7Vtevhsrf46CRTquxDuWsQurQQe4oz8=
google.golang.org/protobuf v0.0.0-20200221191635-4d8936d0db64/go.mod h1:kwYJMbMJ01Woi6D6+Kah6886xMZcty6N08ah7+eCXa0=
google.golang.org/protobuf v0.0.0-20200228230310-ab0ca4ff8a60/go.mod h1:cfTl7dwQJ+fmap5saPgwCLgHXTUD7jkjRqWcaiX5VyM=
google.golang.org/protobuf v1.20.1-0.20200309200217-e05f789c0967/go.mod h1:A+miEFZTKqfCUM6K7xSMQL9OKL/b6hQv+e19PK+JZNE=
google.golang.org/protobuf v1.21.0/go.mod h1:47Nbq4nVaFHyn7ilMalzfO3qCViNmqZ2kzikPIcrTAo=
google.golang.org/protobuf v1.22.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.23.0/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.23.1-0.20200526195155-81db48ad09cc/go.mod h1:EGpADcykh3NcUnDUJcl1+ZksZNG86OlYog2l/sGQquU=
google.golang.org/protobuf v1.25.0 h1:Ejskq+SyPohKW+1uil0JJMtmHCgJPJ/qWTxr8qp+R4c=
google.golang.org/protobuf v1.25.0/go.mod h1:9JNX74DMeImyA3h4bdi1ymwjUzf21/xIlbajtzgsN7c=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20200227125254-8fa46927fb4f h1:BLraFXnmrev5lT+xlilqcH8XK9/i0At2xKjWk4p6zsU=
gopkg.in/check.v1 v1.0.0-20200227125254-8fa46927fb4f/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/fsnotify.v1 v1.4.7/go.mod h1:Tz8NjZHkW78fSQdbUxIjBTcgA1z1m8ZHf0WmKUhAMys=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7 h1:uRGJdciOHaEIrze2W8Q3AKkepLTh2hOroT7a+7czfdQ=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7/go.mod h1:dt/ZhP58zS4L8KSrWDmTeBkI65Dw0HsyUHuEVlX15mw=
gopkg.in/yaml.v2 v2.2.1/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.7/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.8/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.3.0 h1:clyUAQHOM3G0M3f5vQj7LuJrETvjVot3Z5el9nffUtU=
gopkg.in/yaml.v2 v2.3.0/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c h1:dUUwHk2QECo/6vqA44rthZ8ie2QXMNeKRTHCNY2nXvo=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
honnef.co/go/tools v0.0.0-20190102054323-c2f93a96b099/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190523083050-ea95bdfd59fc/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
mellium.im/sasl v0.2.1 h1:nspKSRg7/SyO0cRGY71OkfHab8tf9kCts6a6oTDut0w=
mellium.im/sasl v0.2.1/go.mod h1:ROaEDLQNuf9vjKqE1SrAfnsobm2YKXT1gnN1uDp1PjQ=

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/LICENSE
Copyright (c) 2020 uptrace/go-realworld-example-app Authors. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

   * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/main.go
package main

import "fmt"

func main() {
	fmt.Println("Hello")
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/Makefile
db_reset:
	redis-cli flushall

	sudo -u postgres psql -c "DROP DATABASE IF EXISTS real_world_dev"
	sudo -u postgres psql -c "CREATE DATABASE real_world_dev"

	make db_migrate

db_migrate:
	go run cmd/migrate_db/*.go init
	go run cmd/migrate_db/*.go

test:
	TZ= go test ./org
	TZ= go test ./blog

api_test:
	TZ= go run cmd/api/*.go -env=dev &
	APIURL=http://localhost:8000/api ./scripts/run-api-tests.sh

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/modd.conf
**/*.go {
    daemon +sigterm: go run cmd/api/*.go -env=dev
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/README.md
http://172.21.37.37:8000/api/users
{"user": {"username": "yusef","email": "sample-email@gmail.com","password": "rahasia"}}

{
  "user": {
    "username": "yusef",
    "email": "sample-email@gmail.com",
    "bio": "",
    "image": "",
    "following": false,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDIzMjgwNzgsInN1YiI6IjMxIn0.-wgTAxzcExgDL_QMD-Gc3AlZmeMK_Z__4RHznWIimnQ"
  }
}

http://172.21.37.37:8000/api/users/login
{"user": {"email": "sample-email@gmail.com","password": "rahasia"}}
{
  "user": {
    "username": "yusef",
    "email": "sample-email@gmail.com",
    "bio": "",
    "image": "",
    "following": false,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDIzMjg5NzgsInN1YiI6IjMxIn0.IP-UhLbxgqowZ4z47J_SF-mf-kWgsy-pYjFNzrnqmHU"
  }
}

user id 31 = yusef
http://172.21.37.37:8000/api/user/31

=============== GET user dg header auth token
GET: http://172.21.37.37:8000/api/user
"Authorization", "Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDIzMjg5NzgsInN1YiI6IjMxIn0.IP-UhLbxgqowZ4z47J_SF-mf-kWgsy-pYjFNzrnqmHU"

{
  "user": {
    "username": "yusef",
    "email": "sample-email@gmail.com",
    "bio": "",
    "image": "",
    "following": false,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDIzMzAxNjMsInN1YiI6IjMxIn0.QWpQtbJe7gECJxrXevCoIuY05nuMrHZLP5W478-d-fw"
  }
}

func CreateUserToken(userID uint64, ttl time.Duration) (string, error) {
	claims := &jwt.StandardClaims{
		Subject:   strconv.FormatUint(userID, 10),
		ExpiresAt: time.Now().Add(ttl).Unix(),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	key := []byte(rwe.Config.SecretKey)
	return token.SignedString(key)
}

func setToken(req *http.Request, userID uint64) {
	if userID == 0 {
		return
	}

	token, err := org.CreateUserToken(userID, time.Hour)
	Expect(err).NotTo(HaveOccurred())

	req.Header.Set("Authorization", "Token "+token)
}

func GetWithToken(url string, userID uint64) *httptest.ResponseRecorder {
	req := httptest.NewRequest("GET", url, nil)
	req.Header.Set("Content-Type", "application/json")
	setToken(req, userID)
	return serve(req)
}

## update user 
				json := `{"user": {"username": "hello","email": "foo@bar.com", "image": "bar", "bio": "foo"}}`
				resp := PutWithToken("/api/user/", json, user.ID)
## follow user
				json := `{"user": {"username": "hello","email": "foo@bar.com","password": "pwd"}}`
				resp := Post("/api/users", json)
###
				data = ParseJSON(resp, http.StatusOK)

				username = data["user"].(map[string]interface{})["username"].(string)

				url := fmt.Sprintf("/api/profiles/%s/follow", username)
				resp = PostWithToken(url, "", user.ID)
				_ = ParseJSON(resp, 200)

				url = fmt.Sprintf("/api/profiles/%s", username)
				resp = GetWithToken(url, user.ID)
				data = ParseJSON(resp, 200)
## unfollow user

# Go Gin + go-pg realworld example application

[![CircleCI](https://circleci.com/gh/uptrace/go-realworld-example-app.svg?style=svg)](https://circleci.com/gh/uptrace/go-realworld-example-app)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/uptrace/go-realworld-example-app)](https://pkg.go.dev/github.com/uptrace/go-realworld-example-app)

> :heart: [**Uptrace.dev** - distributed traces, logs, and errors in one place](https://uptrace.dev)

- [Same app but with treemux instead of Gin](https://github.com/uptrace/go-treemux-realworld-example-app)

## Introduction

This project implements JSON API as specified in
[RealWorld](https://github.com/gothinkster/realworld) spec. It was created to demonstrate how to
use:

- [Gin Web framework](https://github.com/gin-gonic/gin)
- [go-pg PostgreSQL client and ORM](https://github.com/go-pg/pg).
- [Caching using Redis](https://github.com/go-redis/cache).
- [Rate limiting using Redis](https://github.com/go-redis/redis_rate).
- [go-pg/migrations](https://github.com/go-pg/migrations).
- [Tracing using uptrace-go](https://github.com/uptrace/uptrace-go).

## Project structure

Project consists of the following packages:

- [rwe](rwe) global package parses configs, establishes DB connections etc.
- [org](org) package manages users and tokens.
- [blog](blog) package manages articles and comments.
- [app](app) folder contains application resources such as config.
- [cmd/api](cmd/api) runs HTTP server with JSON API.
- [cmd/migrate_db](cmd/migrate_db) command that runs SQL migrations.

The most interesting part for go-pg users is probably [article filter](blog/article_filter.go).

## Project bootstrap

First of all you need to create a config file changing defaults as needed:

```
cp app/config/dev.yml.default app/config/dev.yml
```

Project comes with a `Makefile` that contains following recipes:

- `make db_reset` drops existing database and creates a new one.
- `make test` runs unit tests.
- `make api_test` runs API tests provided by
  [RealWorld](https://github.com/gothinkster/realworld/tree/master/api).

After checking that tests are passing you can start API HTTP server:

```shell
go run cmd/api/*.go -env=dev
```

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/renovate.json
{
  "extends": [
    "config:base"
  ]
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/.circleci/config.yml
version: 2
jobs:
  build:
    docker:
      - image: circleci/golang:1.15

      - image: circleci/postgres:12
        environment:
          POSTGRES_USER: postgres
          POSTGRES_DB: real_world_dev
          POSTGRES_HOST_AUTH_METHOD: trust

      - image: redis

    steps:
      - checkout

      - run: echo 0.0.0.0 dbhost | sudo tee -a /etc/hosts

      - run:
          name: wait for Postgres
          command: dockerize -wait tcp://dbhost:5432 -timeout 2m

      - run:
          name: wait for Redis
          command: dockerize -wait tcp://dbhost:6379 -timeout 2m

      - run:
          name: pre tests
          command: |
            sudo apt-get install npm
            npm install npx
            echo 0.0.0.0 dbhost | sudo tee -a /etc/hosts
            sudo apt-get install -y postgresql-client
            sudo apt-get install -y redis-server
            cp app/config/dev.yml.default app/config/dev.yml
            make db_migrate

      - run:
          name: tests
          command: |
            make api_test
            make test

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/app/config/dev.yml
secret_key: "JeFvgCrMuvkoAJjkHgyaMDxku"

redis_cache:
  addrs:
    server1: ":6379"

pg_main:
  addr: ":5432"
  user: "usef"
  password: "rahasia"
  database: "real_world_dev"

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/app/config/dev.yml.default
secret_key: "JeFvgCrMuvkoAJjkHgyaMDxku"

redis_cache:
  addrs:
    server1: ":6379"

pg_main:
  addr: ":5432"
  user: "postgres"
  database: "real_world_dev"

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/article.go
package blog

import (
	"context"
	"time"

	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

type Article struct {
	tableName struct{} `pg:"articles,alias:a"`

	ID          uint64 `json:"-"`
	Slug        string `json:"slug"`
	Title       string `json:"title"`
	Description string `json:"description"`
	Body        string `json:"body"`

	Author   *org.Profile `json:"author" pg:"rel:has-one"`
	AuthorID uint64       `json:"-"`

	Tags    []ArticleTag `json:"-" pg:"rel:has-many"`
	TagList []string     `json:"tagList" pg:"-,array"`

	Favorited      bool `json:"favorited" pg:"-"`
	FavoritesCount int  `json:"favoritesCount" pg:"-"`

	CreatedAt time.Time `json:"createdAt"`
	UpdatedAt time.Time `json:"updatedAt"`
}

type ArticleTag struct {
	tableName struct{} `pg:"alias:t"`

	ArticleID uint64
	Tag       string
}

type FavoriteArticle struct {
	tableName struct{} `pg:"alias:fa"`

	UserID    uint64
	ArticleID uint64
}

func SelectArticle(c context.Context, slug string) (*Article, error) {
	article := new(Article)
	if err := rwe.PGMain().ModelContext(c, article).
		Where("slug = ?", slug).
		Select(); err != nil {
		return nil, err
	}
	return article, nil
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/article_api.go
package blog

import (
	"errors"
	"math/rand"
	"net/http"
	"strconv"

	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"

	"github.com/gin-gonic/gin"
	"github.com/go-pg/pg/v10"
	"github.com/gosimple/slug"
)

func makeSlug(title string) string {
	return slug.Make(title) + "-" + strconv.Itoa(rand.Int())
}

func listArticles(c *gin.Context) {
	ctx := c.Request.Context()

	f, err := decodeArticleFilter(c)
	if err != nil {
		c.Error(err)
		return
	}

	articles := make([]*Article, 0)
	if err := rwe.PGMain().ModelContext(ctx, &articles).
		ColumnExpr("?TableColumns").
		Apply(f.query).
		Limit(f.Pager.GetLimit()).
		Offset(f.Pager.GetOffset()).
		Select(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{
		"articles":      articles,
		"articlesCount": len(articles),
	})
}

func showArticle(c *gin.Context) {
	slug := c.Param("slug")

	if slug == "feed" {
		listArticlesFeed(c)
		return
	}

	article, err := selectArticleByFilter(c)
	if err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{"article": article})
}

func selectArticleByFilter(c *gin.Context) (*Article, error) {
	ctx := c.Request.Context()

	f, err := decodeArticleFilter(c)
	if err != nil {
		return nil, err
	}

	article := new(Article)
	if err := rwe.PGMain().
		ModelContext(ctx, article).
		ColumnExpr("?TableColumns").
		Apply(f.query).
		Select(); err != nil {
		return nil, err
	}

	if article.TagList == nil {
		article.TagList = make([]string, 0)
	}

	return article, nil
}

func listArticlesFeed(c *gin.Context) {
	ctx := c.Request.Context()

	e, ok := c.Get("authErr")
	if ok {
		c.AbortWithError(http.StatusUnauthorized, e.(error))
		return
	}

	f, err := decodeArticleFilter(c)
	if err != nil {
		c.Error(err)
		return
	}

	articles := make([]*Article, 0)
	if err := rwe.PGMain().
		ModelContext(ctx, &articles).
		ColumnExpr("?TableColumns").
		Apply(f.query).
		Select(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{
		"articles":      articles,
		"articlesCount": len(articles),
	})
}

func createArticle(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	var in struct {
		Article *Article `json:"article"`
	}

	if err := c.BindJSON(&in); err != nil {
		return
	}

	if in.Article == nil {
		c.Error(errors.New(`JSON field "article" is required`))
		return
	}

	article := in.Article

	article.Slug = makeSlug(article.Title)
	article.AuthorID = user.ID
	article.CreatedAt = rwe.Clock.Now()
	article.UpdatedAt = rwe.Clock.Now()

	if _, err := rwe.PGMain().
		ModelContext(ctx, article).
		Insert(); err != nil {
		c.Error(err)
		return
	}

	if err := createTags(c, article); err != nil {
		c.Error(err)
		return
	}

	article.Author = org.NewProfile(user)
	c.JSON(200, gin.H{"article": article})
}

func updateArticle(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	var in struct {
		Article *Article `json:"article"`
	}

	if err := c.BindJSON(&in); err != nil {
		return
	}

	if in.Article == nil {
		c.Error(errors.New(`JSON field "article" is required`))
		return
	}

	article := in.Article

	if _, err := rwe.PGMain().
		ModelContext(ctx, article).
		Set("title = ?", article.Title).
		Set("description = ?", article.Description).
		Set("body = ?", article.Body).
		Set("updated_at = ?", rwe.Clock.Now()).
		Where("slug = ?", c.Param("slug")).
		Returning("*").
		Update(); err != nil {
		c.Error(err)
		return
	}

	if _, err := rwe.PGMain().ModelContext(ctx, (*ArticleTag)(nil)).
		Where("article_id = ?", article.ID).
		Delete(); err != nil {
		c.Error(err)
		return
	}

	if err := createTags(c, article); err != nil {
		c.Error(err)
		return
	}

	if article.TagList == nil {
		article.TagList = make([]string, 0)
	}

	article.Author = org.NewProfile(user)
	c.JSON(200, gin.H{"article": article})
}

func deleteArticle(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	if _, err := rwe.PGMain().
		ModelContext(ctx, (*Article)(nil)).
		Where("author_id = ?", user.ID).
		Where("slug = ?", c.Param("slug")).
		Delete(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, nil)
}

func createTags(c *gin.Context, article *Article) error {
	ctx := c.Request.Context()

	if len(article.TagList) == 0 {
		return nil
	}

	tags := make([]ArticleTag, 0, len(article.TagList))
	for _, t := range article.TagList {
		tags = append(tags, ArticleTag{
			ArticleID: article.ID,
			Tag:       t,
		})
	}

	if _, err := rwe.PGMain().
		ModelContext(ctx, &tags).
		Insert(); err != nil {
		return err
	}

	return nil
}

func favoriteArticle(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	article, err := selectArticleByFilter(c)
	if err != nil {
		c.Error(err)
		return
	}

	favoriteArticle := &FavoriteArticle{
		UserID:    user.ID,
		ArticleID: article.ID,
	}
	res, err := rwe.PGMain().
		ModelContext(ctx, favoriteArticle).
		Insert()
	if err != nil {
		c.Error(err)
		return
	}

	if res.RowsAffected() != 0 {
		article.Favorited = true
		article.FavoritesCount = article.FavoritesCount + 1
	}
	c.JSON(200, gin.H{"article": article})
}

func unfavoriteArticle(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	article, err := selectArticleByFilter(c)
	if err != nil {
		c.Error(err)
		return
	}

	res, err := rwe.PGMain().
		ModelContext(ctx, (*FavoriteArticle)(nil)).
		Where("user_id = ?", user.ID).
		Where("article_id = ?", article.ID).
		Delete()
	if err != nil {
		c.Error(err)
		return
	}

	if res.RowsAffected() != 0 {
		article.Favorited = false
		article.FavoritesCount = article.FavoritesCount - 1
	}
	c.JSON(200, gin.H{"article": article})
}

func listTags(c *gin.Context) {
	ctx := c.Request.Context()

	tags := make([]string, 0)
	if err := rwe.PGMain().ModelContext(ctx, (*ArticleTag)(nil)).
		ColumnExpr("tag").
		GroupExpr("tag").
		OrderExpr("count(tag) DESC").
		Select(&tags); err != nil && err != pg.ErrNoRows {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{"tags": tags})
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/article_api_test.go
package blog_test

import (
	"context"
	"fmt"
	"net/http"
	"testing"
	"time"

	"github.com/benbjohnson/clock"
	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
	. "github.com/uptrace/go-realworld-example-app/testbed"
	"github.com/uptrace/go-realworld-example-app/xconfig"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	. "github.com/onsi/gomega/gstruct"
)

func TestGinkgo(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "blog")
}

var ctx context.Context

func init() {
	mock := clock.NewMock()
	mock.Set(time.Date(2020, time.January, 1, 2, 3, 4, 5000, time.UTC))
	rwe.Clock = mock

	ctx = context.Background()

	cfg, err := xconfig.LoadConfig("test")
	if err != nil {
		panic(err)
	}

	ctx = rwe.Init(ctx, cfg)
}

var _ = Describe("createArticle", func() {
	var data map[string]interface{}
	var slug string
	var user *org.User

	var helloArticleKeys, fooArticleKeys, favoritedArticleKeys Keys

	createFollowedUser := func() *org.User {
		followedUser := &org.User{
			Username:     "FollowedUser",
			Email:        "foo@bar.com",
			PasswordHash: "h2",
		}
		_, err := rwe.PGMain().Model(followedUser).Insert()
		Expect(err).NotTo(HaveOccurred())

		url := fmt.Sprintf("/api/profiles/%s/follow", followedUser.Username)
		resp := PostWithToken(url, "", user.ID)
		_ = ParseJSON(resp, 200)

		return followedUser
	}

	BeforeEach(func() {
		ResetAll(ctx)

		helloArticleKeys = Keys{
			"title":          Equal("Hello world"),
			"slug":           HavePrefix("hello-world-"),
			"description":    Equal("Hello world article description!"),
			"body":           Equal("Hello world article body."),
			"author":         Equal(map[string]interface{}{"following": false, "username": "CurrentUser", "bio": "", "image": ""}),
			"tagList":        ConsistOf([]interface{}{"greeting", "welcome", "salut"}),
			"favoritesCount": Equal(float64(0)),
			"favorited":      Equal(false),
			"createdAt":      Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
			"updatedAt":      Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
		}

		favoritedArticleKeys = ExtendKeys(helloArticleKeys, Keys{
			"favorited":      Equal(true),
			"favoritesCount": Equal(float64(1)),
		})

		fooArticleKeys = Keys{
			"title":          Equal("Foo bar"),
			"slug":           HavePrefix("foo-bar-"),
			"description":    Equal("Foo bar article description!"),
			"body":           Equal("Foo bar article body."),
			"author":         Equal(map[string]interface{}{"following": false, "username": "CurrentUser", "bio": "", "image": ""}),
			"tagList":        ConsistOf([]interface{}{"foobar", "variable"}),
			"favoritesCount": Equal(float64(0)),
			"favorited":      Equal(false),
			"createdAt":      Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
			"updatedAt":      Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
		}

		user = &org.User{
			Username:     "CurrentUser",
			Email:        "hello@world.com",
			PasswordHash: "#1",
		}
		_, err := rwe.PGMain().Model(user).Insert()
		Expect(err).NotTo(HaveOccurred())
	})

	BeforeEach(func() {
		json := `{"article": {"title": "Hello world", "description": "Hello world article description!", "body": "Hello world article body.", "tagList": ["greeting", "welcome", "salut"]}}`
		resp := PostWithToken("/api/articles", json, user.ID)

		data = ParseJSON(resp, http.StatusOK)
		slug = data["article"].(map[string]interface{})["slug"].(string)
	})

	It("creates new article", func() {
		Expect(data["article"]).To(MatchAllKeys(helloArticleKeys))
	})

	Describe("showFeed", func() {
		BeforeEach(func() {
			followedUser := createFollowedUser()

			json := `{"article": {"title": "Foo bar", "description": "Foo bar article description!", "body": "Foo bar article body.", "tagList": ["foobar", "variable"]}}`
			resp := PostWithToken("/api/articles", json, followedUser.ID)

			_ = ParseJSON(resp, http.StatusOK)

			resp = GetWithToken("/api/articles/feed", user.ID)
			data = ParseJSON(resp, http.StatusOK)
		})

		It("returns article", func() {
			articles := data["articles"].([]interface{})

			Expect(articles).To(HaveLen(1))
			followedAuthorKeys := ExtendKeys(fooArticleKeys, Keys{
				"author": Equal(map[string]interface{}{"following": true, "username": "FollowedUser", "bio": "", "image": ""}),
			})
			Expect(articles[0].(map[string]interface{})).To(MatchAllKeys(followedAuthorKeys))
		})
	})

	Describe("showArticle", func() {
		BeforeEach(func() {
			url := fmt.Sprintf("/api/articles/%s", slug)
			resp := Get(url)

			data = ParseJSON(resp, http.StatusOK)
		})

		It("returns article", func() {
			Expect(data["article"]).To(MatchAllKeys(helloArticleKeys))
		})
	})

	Describe("listArticles", func() {
		BeforeEach(func() {
			url := fmt.Sprintf("/api/articles/%s?author=CurrentUser", slug)
			resp := Get(url)

			data = ParseJSON(resp, http.StatusOK)
		})

		It("returns articles by author", func() {
			Expect(data["article"]).To(MatchAllKeys(helloArticleKeys))
		})
	})

	Describe("favoriteArticle", func() {
		BeforeEach(func() {
			url := fmt.Sprintf("/api/articles/%s/favorite", slug)
			resp := PostWithToken(url, "", user.ID)
			_ = ParseJSON(resp, 200)

			url = fmt.Sprintf("/api/articles/%s", slug)
			resp = GetWithToken(url, user.ID)
			data = ParseJSON(resp, 200)
		})

		It("returns favorited article", func() {
			Expect(data["article"]).To(MatchAllKeys(favoritedArticleKeys))
		})

		Describe("unfavoriteArticle", func() {
			BeforeEach(func() {
				url := fmt.Sprintf("/api/articles/%s/favorite", slug)
				resp := DeleteWithToken(url, user.ID)
				_ = ParseJSON(resp, 200)

				url = fmt.Sprintf("/api/articles/%s", slug)
				resp = GetWithToken(url, user.ID)
				data = ParseJSON(resp, 200)
			})

			It("returns article", func() {
				Expect(data["article"]).To(MatchAllKeys(helloArticleKeys))
			})
		})
	})

	Describe("listArticles", func() {
		BeforeEach(func() {
			url := fmt.Sprintf("/api/articles/%s/favorite", slug)
			resp := PostWithToken(url, "", user.ID)
			_ = ParseJSON(resp, 200)

			resp = GetWithToken("/api/articles", user.ID)
			data = ParseJSON(resp, 200)
		})

		It("returns articles", func() {
			articles := data["articles"].([]interface{})

			Expect(articles).To(HaveLen(1))
			article := articles[0].(map[string]interface{})
			Expect(article).To(MatchAllKeys(favoritedArticleKeys))
		})
	})

	Describe("updateArticle", func() {
		BeforeEach(func() {
			json := `{"article": {"title": "Foo bar", "description": "Foo bar article description!", "body": "Foo bar article body.", "tagList": []}}`

			url := fmt.Sprintf("/api/articles/%s", slug)
			resp := PutWithToken(url, json, user.ID)
			data = ParseJSON(resp, 200)
		})

		It("returns article", func() {
			updatedArticleKeys := ExtendKeys(fooArticleKeys, Keys{
				"slug":      HavePrefix("hello-world-"),
				"tagList":   Equal([]interface{}{}),
				"updatedAt": Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
			})
			Expect(data["article"]).To(MatchAllKeys(updatedArticleKeys))
		})
	})

	Describe("deleteArticle", func() {
		BeforeEach(func() {
			url := fmt.Sprintf("/api/articles/%s", slug)
			resp := DeleteWithToken(url, user.ID)
			data = ParseJSON(resp, 200)
		})

		It("returns article", func() {
			Expect(data).To(BeNil())
		})
	})

	Describe("createComment", func() {
		var commentKeys Keys
		var commentID uint64
		var followedUser *org.User

		BeforeEach(func() {
			commentKeys = Keys{
				"id":        Not(BeZero()),
				"body":      Equal("First comment."),
				"author":    Equal(map[string]interface{}{"following": false, "username": "FollowedUser", "bio": "", "image": ""}),
				"createdAt": Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
				"updatedAt": Equal(rwe.Clock.Now().Format(time.RFC3339Nano)),
			}

			followedUser = createFollowedUser()

			json := `{"comment": {"body": "First comment."}}`
			url := fmt.Sprintf("/api/articles/%s/comments", slug)
			resp := PostWithToken(url, json, followedUser.ID)
			data = ParseJSON(resp, 200)

			commentID = uint64(data["comment"].(map[string]interface{})["id"].(float64))
		})

		It("returns created comment to article", func() {
			Expect(data["comment"]).To(MatchAllKeys(commentKeys))
		})

		Describe("showComment", func() {
			BeforeEach(func() {
				url := fmt.Sprintf("/api/articles/%s/comments/%d", slug, commentID)
				resp := Get(url)
				data = ParseJSON(resp, 200)
			})

			It("returns comment to article", func() {
				Expect(data["comment"]).To(MatchAllKeys(commentKeys))
			})
		})

		Describe("showComment with authentication", func() {
			BeforeEach(func() {
				url := fmt.Sprintf("/api/articles/%s/comments/%d", slug, commentID)
				resp := GetWithToken(url, user.ID)
				data = ParseJSON(resp, 200)
			})

			It("returns comment to article", func() {
				followedCommentKeys := ExtendKeys(commentKeys, Keys{
					"author": Equal(map[string]interface{}{"following": true, "username": "FollowedUser", "bio": "", "image": ""}),
				})
				Expect(data["comment"]).To(MatchAllKeys(followedCommentKeys))
			})
		})

		Describe("listArticleComments", func() {
			BeforeEach(func() {
				url := fmt.Sprintf("/api/articles/%s/comments", slug)
				resp := GetWithToken(url, user.ID)
				data = ParseJSON(resp, 200)
			})

			It("returns article comments", func() {
				followedCommentKeys := ExtendKeys(commentKeys, Keys{
					"author": Equal(map[string]interface{}{"following": true, "username": "FollowedUser", "bio": "", "image": ""}),
				})
				Expect(data["comments"].([]interface{})[0]).To(MatchAllKeys(followedCommentKeys))
			})
		})

		Describe("deleteComment", func() {
			BeforeEach(func() {
				url := fmt.Sprintf("/api/articles/%s/comments/%d", slug, commentID)
				resp := DeleteWithToken(url, followedUser.ID)
				data = ParseJSON(resp, 200)
			})

			It("deletes comment", func() {
				Expect(data).To(BeNil())
			})
		})
	})

	Describe("listTags", func() {
		BeforeEach(func() {
			resp := Get("/api/tags/")
			data = ParseJSON(resp, 200)
		})

		It("returns tags", func() {
			Expect(data["tags"]).To(ConsistOf([]string{
				"greeting",
				"salut",
				"welcome",
			}))
		})
	})
})

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/article_filter.go
package blog

import (
	"github.com/gin-gonic/gin"
	"github.com/go-pg/pg/v10"
	"github.com/go-pg/pg/v10/orm"
	"github.com/go-pg/urlstruct"
	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

type ArticleFilter struct {
	UserID    uint64
	Author    string
	Tag       string
	Favorited string
	Slug      string
	Feed      bool
	urlstruct.Pager
}

func decodeArticleFilter(c *gin.Context) (*ArticleFilter, error) {
	f := &ArticleFilter{
		Tag:       c.Query("tag"),
		Author:    c.Query("author"),
		Favorited: c.Query("favorited"),
		Slug:      c.Param("slug"),
		Feed:      c.Param("slug") == "feed",
	}

	user, ok := c.Get("user")
	if ok {
		f.UserID = user.(*org.User).ID
	}

	return f, nil
}

func (f *ArticleFilter) query(q *orm.Query) (*orm.Query, error) {
	q = q.Relation("Author")

	{
		subq := pg.Model((*ArticleTag)(nil)).
			ColumnExpr("array_agg(t.tag)::text[]").
			Where("t.article_id = a.id")

		q = q.ColumnExpr("(?) AS tag_list", subq)
	}

	if f.UserID == 0 {
		q = q.ColumnExpr("false AS favorited")
	} else {
		subq := pg.Model((*FavoriteArticle)(nil)).
			Where("fa.article_id = a.id").
			Where("fa.user_id = ?", f.UserID)

		q = q.ColumnExpr("EXISTS (?) AS favorited", subq)
	}

	q.Apply(authorFollowingColumn(f.UserID))

	{
		subq := pg.Model((*FavoriteArticle)(nil)).
			ColumnExpr("count(*)").
			Where("fa.article_id = a.id")

		q = q.ColumnExpr("(?) AS favorites_count", subq)
	}

	if f.Author != "" {
		q = q.Where("author.username = ?", f.Author)
	}

	if f.Tag != "" {
		subq := pg.Model((*ArticleTag)(nil)).
			Distinct().
			ColumnExpr("t.article_id").
			Where("t.tag = ?", f.Tag)

		q = q.Where("a.id IN (?)", subq)
	}

	if f.Feed {
		subq := pg.Model((*org.FollowUser)(nil)).
			ColumnExpr("fu.followed_user_id").
			Where("fu.user_id = ?", f.UserID)

		q = q.Where("a.author_id IN (?)", subq)
	} else if f.Slug != "" {
		q = q.Where("a.slug  = ?", f.Slug)
	}

	return q, nil
}

func authorFollowingColumn(userID uint64) func(*orm.Query) (*orm.Query, error) {
	return func(q *orm.Query) (*orm.Query, error) {
		if userID == 0 {
			q = q.ColumnExpr("false AS author__following")
		} else {
			subq := rwe.PGMain().Model((*org.FollowUser)(nil)).
				Where("fu.followed_user_id = author_id").
				Where("fu.user_id = ?", userID)

			q = q.ColumnExpr("EXISTS (?) AS author__following", subq)
		}

		return q, nil
	}
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/comment.go
package blog

import (
	"time"

	"github.com/uptrace/go-realworld-example-app/org"
)

type Comment struct {
	tableName struct{} `pg:"comments,alias:c"`

	ID   uint64 `json:"id"`
	Body string `json:"body"`

	Author   *org.Profile `json:"author" pg:"rel:has-one"`
	AuthorID uint64       `json:"-"`

	ArticleID uint64 `json:"-"`

	CreatedAt time.Time `json:"createdAt"`
	UpdatedAt time.Time `json:"updatedAt"`
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/comment_api.go
package blog

import (
	"errors"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

func listArticleComments(c *gin.Context) {
	ctx := c.Request.Context()

	article, err := SelectArticle(ctx, c.Param("slug"))
	if err != nil {
		c.Error(err)
		return
	}

	var userID uint64
	user, ok := c.Get("user")
	if ok {
		userID = user.(*org.User).ID
	}

	articles := make([]*Comment, 0)
	if err := rwe.PGMain().ModelContext(ctx, &articles).
		ColumnExpr("c.*").
		Relation("Author").
		Apply(authorFollowingColumn(userID)).
		Where("article_id = ?", article.ID).
		Select(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{"comments": articles})
}

func showComment(c *gin.Context) {
	ctx := c.Request.Context()

	article, err := SelectArticle(ctx, c.Param("slug"))
	if err != nil {
		c.Error(err)
		return
	}

	id, err := strconv.ParseUint(c.Param("id"), 10, 64)
	if err != nil {
		c.Error(err)
		return
	}

	var userID uint64
	user, ok := c.Get("user")
	if ok {
		userID = user.(*org.User).ID
	}

	comment := new(Comment)
	if err := rwe.PGMain().ModelContext(ctx, comment).
		ColumnExpr("c.*").
		Relation("Author").
		Apply(authorFollowingColumn(userID)).
		Where("c.id = ?", id).
		Where("article_id = ?", article.ID).
		Select(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{"comment": comment})
}

func createComment(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	article, err := SelectArticle(ctx, c.Param("slug"))
	if err != nil {
		c.Error(err)
		return
	}

	var in struct {
		Comment *Comment `json:"comment"`
	}

	if err := c.BindJSON(&in); err != nil {
		return
	}

	if in.Comment == nil {
		c.Error(errors.New(`JSON field "comment" is required`))
		return
	}

	comment := in.Comment

	comment.AuthorID = user.ID
	comment.ArticleID = article.ID
	comment.CreatedAt = rwe.Clock.Now()
	comment.UpdatedAt = rwe.Clock.Now()

	if _, err := rwe.PGMain().
		ModelContext(ctx, comment).
		Insert(); err != nil {
		c.Error(err)
		return
	}

	comment.Author = org.NewProfile(user)
	c.JSON(200, gin.H{"comment": comment})
}

func deleteComment(c *gin.Context) {
	ctx := c.Request.Context()

	user := c.MustGet("user").(*org.User)

	article, err := SelectArticle(ctx, c.Param("slug"))
	if err != nil {
		c.Error(err)
		return
	}

	if _, err := rwe.PGMain().
		ModelContext(ctx, (*Comment)(nil)).
		Where("author_id = ?", user.ID).
		Where("article_id = ?", article.ID).
		Delete(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, nil)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/blog/init.go
package blog

import (
	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

func init() {
	g := rwe.API.Group("")

	g.Use(org.UserMiddleware)

	g.GET("/tags/", listTags)
	g.GET("/articles", listArticles)
	g.GET("/articles/:slug", showArticle)
	g.GET("/articles/:slug/comments", listArticleComments)
	g.GET("/articles/:slug/comments/:id", showComment)

	g.Use(org.MustUserMiddleware)

	g.POST("/articles", createArticle)
	g.PUT("/articles/:slug", updateArticle)
	g.DELETE("/articles/:slug", deleteArticle)

	g.POST("/articles/:slug/favorite", favoriteArticle)
	g.DELETE("/articles/:slug/favorite", unfavoriteArticle)

	g.POST("/articles/:slug/comments", createComment)
	g.DELETE("/articles/:slug/comments/:id", deleteComment)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/cmd/api/api.go
package main

import (
	"context"
	"flag"
	"fmt"
	"net/http"
	"time"

	"github.com/sirupsen/logrus"

	_ "github.com/uptrace/go-realworld-example-app/blog"
	"github.com/uptrace/go-realworld-example-app/httputil"
	_ "github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
	"github.com/uptrace/go-realworld-example-app/xconfig"
)

var listenFlag = flag.String("listen", ":8000", "listen address")

func main() {
	flag.Parse()

	ctx := context.Background()

	cfg, err := xconfig.LoadConfig("api")
	if err != nil {
		logrus.WithContext(ctx).WithError(err).Fatal("LoadConfig failed")
	}

	ctx = rwe.Init(ctx, cfg)
	defer rwe.Exit(ctx)

	var handler http.Handler
	handler = rwe.Router
	handler = httputil.PanicHandler{Next: handler}

	logrus.WithContext(ctx).
		WithField("env", cfg.Env).
		WithField("addr", *listenFlag).
		Info("serving...")

	serveHTTP(ctx, handler)
}

func serveHTTP(ctx context.Context, handler http.Handler) {
	srv := &http.Server{
		Addr:         *listenFlag,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		IdleTimeout:  60 * time.Second,
		Handler:      handler,
	}
	go func() {
		if err := srv.ListenAndServe(); err != nil && !isServerClosed(err) {
			logrus.WithContext(ctx).WithError(err).Error("ListenAndServe failed")
		}
	}()

	fmt.Println(rwe.WaitExitSignal())

	if err := srv.Shutdown(ctx); err != nil {
		logrus.WithContext(ctx).WithError(err).Error("srv.Shutdown failed")
	}
}

//------------------------------------------------------------------------------

func isServerClosed(err error) bool {
	return err.Error() == "http: Server closed"
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/cmd/migrate_db/1_init.up.sql
CREATE TABLE users (
  id int8 PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  username varchar(500) NOT NULL,
  email varchar(500) NOT NULL,
  bio varchar(500),
  image varchar(500),
  password_hash varchar(500) NOT NULL
);

CREATE UNIQUE INDEX users_email_idx ON users (email);
CREATE UNIQUE INDEX users_username_idx ON users (username);

--gopg:split

CREATE TABLE articles (
  id int8 PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  slug varchar(500),
  title varchar(500) NOT NULL,
  description varchar(500) NOT NULL,
  body text NOT NULL,
  author_id int8 NOT NULL REFERENCES users (id) ON DELETE CASCADE,

  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

--gopg:split

CREATE TABLE article_tags (
  article_id int8 NOT NULL REFERENCES articles (id) ON DELETE CASCADE,
  tag varchar(500)
);

CREATE UNIQUE INDEX article_tags_article_id_tag_idx
ON article_tags (article_id, tag);

--gopg:split

CREATE TABLE favorite_articles (
  user_id int8 NOT NULL REFERENCES users (id) ON DELETE CASCADE,
  article_id int8 NOT NULL REFERENCES articles (id) ON DELETE CASCADE,

  PRIMARY KEY (user_id, article_id)
);

CREATE UNIQUE INDEX favorite_articles_user_id_article_id_idx
ON favorite_articles (user_id, article_id);

--gopg:split

CREATE TABLE follow_users (
  user_id  int8 NOT NULL REFERENCES users (id) ON DELETE CASCADE,
  followed_user_id int8 NOT NULL REFERENCES users (id) ON DELETE CASCADE,

  PRIMARY KEY (user_id, followed_user_id)
);

CREATE UNIQUE INDEX follow_users_user_id_followed_user_id_idx
ON follow_users (user_id, followed_user_id);

--gopg:split

CREATE TABLE comments (
  id int8 PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
  author_id int8 NOT NULL REFERENCES users (id) ON DELETE CASCADE,
  article_id int8 NOT NULL REFERENCES articles (id) ON DELETE CASCADE,

  body text NOT NULL,

  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/cmd/migrate_db/migrate_db.go
package main

import (
	"context"
	"flag"
	"fmt"
	"time"

	"github.com/go-pg/migrations/v8"
	"github.com/sirupsen/logrus"
	"github.com/uptrace/go-realworld-example-app/rwe"
	"github.com/uptrace/go-realworld-example-app/xconfig"
)

const stmtTimeout = 5 * time.Minute

func main() {
	flag.Parse()

	cfg, err := xconfig.LoadConfig("migrate_db")
	if err != nil {
		logrus.Fatal(err)
	}

	cfg.PGMain.ReadTimeout = stmtTimeout
	cfg.PGMain.PoolTimeout = stmtTimeout

	ctx := rwe.Init(context.Background(), cfg)
	defer rwe.Exit(ctx)

	args := flag.Args()
	oldVersion, newVersion, err := migrations.Run(rwe.PGMain(), args...)
	if err != nil {
		logrus.Fatalf("migration %d -> %d failed: %s",
			oldVersion, newVersion, err)
	}

	if newVersion != oldVersion {
		fmt.Printf("migrated from %d to %d\n", oldVersion, newVersion)
	} else {
		fmt.Printf("version is %d\n", oldVersion)
	}
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/httputil/middleware.go
package httputil

import (
	"fmt"
	"net/http"
	"os"
	"runtime"
)

type PanicHandler struct {
	Next http.Handler
}

func (h PanicHandler) ServeHTTP(w http.ResponseWriter, req *http.Request) {
	defer func() {
		if err := recover(); err != nil {
			buf := make([]byte, 1<<20)
			n := runtime.Stack(buf, true)
			fmt.Fprintf(os.Stderr, "panic: %v\n\n%s", err, buf[:n])
			os.Exit(1)
		}
	}()
	h.Next.ServeHTTP(w, req)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/org/auth.go
package org

import (
	"net/http"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func authToken(req *http.Request) string {
	const prefix = "Token "
	v := req.Header.Get("Authorization")
	v = strings.TrimPrefix(v, prefix)
	return v
}

func UserMiddleware(c *gin.Context) {
	ctx := c.Request.Context()

	token := authToken(c.Request)
	userID, err := decodeUserToken(token)
	if err != nil {
		c.Set("authErr", err)
		return
	}

	user, err := SelectUser(ctx, userID)
	if err != nil {
		c.Set("authErr", err)
		return
	}

	user.Token, err = CreateUserToken(user.ID, 24*time.Hour)
	if err != nil {
		c.Set("authErr", err)
		return
	}

	c.Set("user", user)
}

func MustUserMiddleware(c *gin.Context) {
	err, ok := c.Get("authErr")
	if ok {
		c.AbortWithError(http.StatusUnauthorized, err.(error))
		return
	}
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/org/init.go
package org

import (
	"github.com/uptrace/go-realworld-example-app/rwe"
)

func init() {
	g := rwe.API.Group("")

	g.Use(UserMiddleware)

	g.POST("/users", createUser)
	g.POST("/users/login", loginUser)
	g.GET("/profiles/:username", showProfile)

	g.Use(MustUserMiddleware)

	g.GET("/user/", currentUser)
	g.PUT("/user/", updateUser)

	g.POST("/profiles/:username/follow", followUser)
	g.DELETE("/profiles/:username/follow", unfollowUser)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/org/token.go
package org

import (
	"errors"
	"strconv"
	"time"

	"github.com/dgrijalva/jwt-go"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

func decodeUserToken(jwtToken string) (uint64, error) {
	if len(jwtToken) == 0 {
		return 0, errors.New("token is missing or empty")
	}

	token, err := jwt.ParseWithClaims(jwtToken, &jwt.StandardClaims{}, func(token *jwt.Token) (interface{}, error) {
		return []byte(rwe.Config.SecretKey), nil
	})
	if err != nil {
		return 0, err
	}

	if !token.Valid {
		return 0, errors.New("invalid token")
	}

	claims := token.Claims.(*jwt.StandardClaims)

	id, err := strconv.ParseUint(claims.Subject, 10, 64)
	if err != nil {
		return 0, err
	}

	return id, nil
}

func CreateUserToken(userID uint64, ttl time.Duration) (string, error) {
	claims := &jwt.StandardClaims{
		Subject:   strconv.FormatUint(userID, 10),
		ExpiresAt: time.Now().Add(ttl).Unix(),
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	key := []byte(rwe.Config.SecretKey)
	return token.SignedString(key)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/org/user.go
package org

import (
	"context"
	"fmt"
	"time"

	"github.com/go-redis/cache/v8"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

type User struct {
	tableName struct{} `pg:",alias:u"`

	ID           uint64 `json:"-"`
	Username     string `json:"username"`
	Email        string `json:"email"`
	Bio          string `json:"bio"`
	Image        string `json:"image"`
	Password     string `pg:"-" json:"password,omitempty"`
	PasswordHash string `json:"-"`
	Following    bool   `pg:"-" json:"following"`

	Token string `pg:"-" json:"token,omitempty"`
}

type FollowUser struct {
	tableName struct{} `pg:"alias:fu"`

	UserID         uint64
	FollowedUserID uint64
}

type Profile struct {
	tableName struct{} `pg:"users,alias:u"`

	ID        uint64 `json:"-"`
	Username  string `json:"username"`
	Bio       string `json:"bio"`
	Image     string `json:"image"`
	Following bool   `pg:"-" json:"following"`
}

func NewProfile(user *User) *Profile {
	return &Profile{
		Username:  user.Username,
		Bio:       user.Bio,
		Image:     user.Image,
		Following: user.Following,
	}
}

func SelectUser(ctx context.Context, userID uint64) (*User, error) {
	user := new(User)
	if err := rwe.RedisCache().Once(&cache.Item{
		Ctx:   ctx,
		Key:   fmt.Sprintf("user:%d", userID),
		Value: user,
		TTL:   15 * time.Minute,
		Do: func(item *cache.Item) (interface{}, error) {
			return selectUser(ctx, userID)
		},
	}); err != nil {
		return nil, err
	}
	return user, nil
}

func selectUser(ctx context.Context, id uint64) (*User, error) {
	user := new(User)
	if err := rwe.PGMain().
		ModelContext(ctx, user).
		Where("id = ?", id).
		Select(); err != nil {
		return nil, err
	}
	return user, nil
}

func SelectUserByUsername(ctx context.Context, username string) (*User, error) {
	user := new(User)
	if err := rwe.PGMain().
		ModelContext(ctx, user).
		Where("username = ?", username).
		Select(); err != nil {
		return nil, err
	}

	return user, nil
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/org/user_api.go
package org

import (
	"errors"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/go-pg/pg/v10"
	"github.com/go-pg/pg/v10/orm"
	"golang.org/x/crypto/bcrypt"

	"github.com/uptrace/go-realworld-example-app/rwe"
)

var errUserNotFound = errors.New("Not Registered email or invalid password")

func setUserToken(user *User) error {
	token, err := CreateUserToken(user.ID, 24*time.Hour)
	if err != nil {
		return err
	}

	user.Token = token
	return nil
}

func currentUser(c *gin.Context) {
	user := c.MustGet("user").(*User)
	c.JSON(200, gin.H{"user": user})
}

func createUser(c *gin.Context) {
	ctx := c.Request.Context()

	var in struct {
		User *User `json:"user"`
	}

	if err := c.BindJSON(&in); err != nil {
		return
	}

	if in.User == nil {
		c.Error(errors.New(`JSON field "user" is required`))
		return
	}

	user := in.User

	var err error
	user.PasswordHash, err = hashPassword(user.Password)
	if err != nil {
		c.Error(err)
		return
	}

	if _, err = rwe.PGMain().
		ModelContext(ctx, user).
		Insert(); err != nil {
		c.Error(err)
		return
	}

	if err = setUserToken(user); err != nil {
		c.Error(err)
		return
	}

	user.Password = ""
	c.JSON(200, gin.H{"user": user})
}

func hashPassword(pass string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(pass), bcrypt.DefaultCost)
	if err != nil {
		return "", err
	}
	return string(bytes), nil
}

func loginUser(c *gin.Context) {
	ctx := c.Request.Context()

	var in struct {
		User *struct {
			Email    string `json:"email"`
			Password string `json:"password"`
		} `json:"user"`
	}
	if err := c.BindJSON(&in); err != nil {
		return
	}

	if in.User == nil {
		c.Error(errors.New(`JSON field "user" is required`))
		return
	}

	user := new(User)
	if err := rwe.PGMain().
		ModelContext(ctx, user).
		Where("email = ?", in.User.Email).
		Select(); err != nil {
		if err == pg.ErrNoRows {
			err = errUserNotFound
		}

		c.Error(err)
		return
	}

	if err := comparePasswords(user.PasswordHash, in.User.Password); err != nil {
		c.Error(err)
		return
	}

	err := setUserToken(user)
	if err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{"user": user})
}

func comparePasswords(hash, pass string) error {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(pass))
	if err != nil {
		return errUserNotFound
	}
	return nil
}

func updateUser(c *gin.Context) {
	ctx := c.Request.Context()

	var in struct {
		User *User `json:"user"`
	}

	if err := c.BindJSON(&in); err != nil {
		return
	}

	if in.User == nil {
		c.Error(errors.New(`JSON field "user" is required`))
		return
	}

	user := in.User

	var err error
	user.PasswordHash, err = hashPassword(user.Password)
	if err != nil {
		c.Error(err)
		return
	}

	authUser := c.MustGet("user").(*User)
	if _, err = rwe.PGMain().
		ModelContext(ctx, authUser).
		Set("email = ?", user.Email).
		Set("username = ?", user.Username).
		Set("password_hash = ?", user.PasswordHash).
		Set("image = ?", user.Image).
		Set("bio = ?", user.Bio).
		Where("id = ?", authUser.ID).
		Returning("*").
		Update(); err != nil {
		c.Error(err)
		return
	}

	user.Password = ""
	c.JSON(200, gin.H{"user": authUser})
}

func showProfile(c *gin.Context) {
	ctx := c.Request.Context()

	followingColumn := func(q *orm.Query) (*orm.Query, error) {
		u, _ := c.Get("user")
		authUser, ok := u.(*User)

		if !ok {
			q = q.ColumnExpr("false AS following")
		} else {
			subq := rwe.PGMain().Model((*FollowUser)(nil)).
				Where("fu.followed_user_id = u.id").
				Where("fu.user_id = ?", authUser.ID)

			q = q.ColumnExpr("EXISTS (?) AS following", subq)
		}

		return q, nil
	}

	user := new(User)
	if err := rwe.PGMain().
		ModelContext(ctx, user).
		ColumnExpr("u.*").
		Apply(followingColumn).
		Where("username = ?", c.Param("username")).
		Select(); err != nil {
		c.Error(err)
		return
	}

	c.JSON(200, gin.H{"profile": NewProfile(user)})
}

func followUser(c *gin.Context) {
	ctx := c.Request.Context()

	authUser := c.MustGet("user").(*User)

	user, err := SelectUserByUsername(ctx, c.Param("username"))
	if err != nil {
		c.Error(err)
		return
	}

	followUser := &FollowUser{
		UserID:         authUser.ID,
		FollowedUserID: user.ID,
	}
	if _, err := rwe.PGMain().
		ModelContext(ctx, followUser).
		Insert(); err != nil {
		c.Error(err)
		return
	}

	user.Following = true
	c.JSON(200, gin.H{"profile": NewProfile(user)})
}

func unfollowUser(c *gin.Context) {
	ctx := c.Request.Context()

	authUser := c.MustGet("user").(*User)

	user, err := SelectUserByUsername(ctx, c.Param("username"))
	if err != nil {
		c.Error(err)
		return
	}

	if _, err := rwe.PGMain().
		ModelContext(ctx, (*FollowUser)(nil)).
		Where("user_id = ?", authUser.ID).
		Where("followed_user_id = ?", user.ID).
		Delete(); err != nil {
		c.Error(err)
		return
	}

	user.Following = false
	c.JSON(200, gin.H{"profile": NewProfile(user)})
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/org/user_api_test.go
package org_test

import (
	"context"
	"fmt"
	"net/http"
	"testing"

	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"
	. "github.com/uptrace/go-realworld-example-app/testbed"
	"github.com/uptrace/go-realworld-example-app/xconfig"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	. "github.com/onsi/gomega/gstruct"
)

func TestOrg(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "org")
}

var ctx context.Context

func init() {
	ctx = context.Background()

	cfg, err := xconfig.LoadConfig("test")
	if err != nil {
		panic(err)
	}

	ctx = rwe.Init(ctx, cfg)
}

var _ = Describe("createUser", func() {
	var data map[string]interface{}

	var userKeys Keys

	BeforeEach(func() {
		ResetAll(ctx)

		userKeys = Keys{
			"username":  Equal("wangzitian0"),
			"email":     Equal("wzt@gg.cn"),
			"bio":       Equal("bar"),
			"image":     Equal("img"),
			"token":     Not(BeEmpty()),
			"following": Equal(false),
		}

		json := `{"user": {"username": "wangzitian0","email": "wzt@gg.cn","password": "jakejxke", "image": "img", "bio": "bar"}}`
		resp := Post("/api/users", json)

		data = ParseJSON(resp, http.StatusOK)
	})

	It("creates new user", func() {
		Expect(data["user"]).To(MatchAllKeys(userKeys))
	})

	Describe("loginUser", func() {
		var user *org.User

		BeforeEach(func() {
			json := `{"user": {"email": "wzt@gg.cn","password": "jakejxke"}}`
			resp := Post("/api/users/login", json)

			data = ParseJSON(resp, http.StatusOK)

			username := data["user"].(map[string]interface{})["username"].(string)
			var err error
			user, err = org.SelectUserByUsername(context.Background(), username)
			Expect(err).NotTo(HaveOccurred())
		})

		It("returns user with JWT token", func() {
			Expect(data["user"]).To(MatchAllKeys(userKeys))
		})

		Describe("currentUser", func() {
			BeforeEach(func() {
				resp := GetWithToken("/api/user/", user.ID)
				data = ParseJSON(resp, http.StatusOK)
			})

			It("returns logged in user", func() {
				Expect(data["user"]).To(MatchAllKeys(userKeys))
			})
		})

		Describe("updateUser", func() {
			BeforeEach(func() {
				json := `{"user": {"username": "hello","email": "foo@bar.com", "image": "bar", "bio": "foo"}}`
				resp := PutWithToken("/api/user/", json, user.ID)
				data = ParseJSON(resp, http.StatusOK)
			})

			It("returns updated user", func() {
				user := data["user"].(map[string]interface{})
				Expect(user).To(MatchAllKeys(Keys{
					"username":  Equal("hello"),
					"email":     Equal("foo@bar.com"),
					"bio":       Equal("foo"),
					"image":     Equal("bar"),
					"token":     Not(BeEmpty()),
					"following": Equal(false),
				}))
			})
		})

		Describe("followUser", func() {
			var username string

			BeforeEach(func() {
				json := `{"user": {"username": "hello","email": "foo@bar.com","password": "pwd"}}`
				resp := Post("/api/users", json)

				data = ParseJSON(resp, http.StatusOK)

				username = data["user"].(map[string]interface{})["username"].(string)

				url := fmt.Sprintf("/api/profiles/%s/follow", username)
				resp = PostWithToken(url, "", user.ID)
				_ = ParseJSON(resp, 200)

				url = fmt.Sprintf("/api/profiles/%s", username)
				resp = GetWithToken(url, user.ID)
				data = ParseJSON(resp, 200)
			})

			It("returns followed profile", func() {
				profile := data["profile"].(map[string]interface{})
				Expect(profile).To(MatchAllKeys(Keys{
					"username":  Equal("hello"),
					"bio":       Equal(""),
					"image":     Equal(""),
					"following": Equal(true),
				}))
			})

			Describe("unfollowUser", func() {
				BeforeEach(func() {
					url := fmt.Sprintf("/api/profiles/%s/follow", username)
					resp := DeleteWithToken(url, user.ID)
					data = ParseJSON(resp, 200)
				})

				It("returns profile", func() {
					profile := data["profile"].(map[string]interface{})
					Expect(profile).To(MatchAllKeys(Keys{
						"username":  Equal("hello"),
						"bio":       Equal(""),
						"image":     Equal(""),
						"following": Equal(false),
					}))
				})
			})
		})
	})
})

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/rwe/app.go
package rwe

import (
	"context"
	mathRand "math/rand"
	"os"
	"os/signal"
	"sync"
	"sync/atomic"
	"syscall"
	"time"

	"github.com/benbjohnson/clock"
	"github.com/uptrace/go-realworld-example-app/xconfig"

	"github.com/sirupsen/logrus"
	"golang.org/x/exp/rand"
)

var Clock = clock.New()

var (
	WaitGroup sync.WaitGroup
	ExitCh    = make(chan struct{})
	exiting   uint32
)

func Exiting() bool {
	return atomic.LoadUint32(&exiting) == 1
}

func Running() bool {
	return !Exiting()
}

//------------------------------------------------------------------------------

var (
	Config *xconfig.Config
	Ctx    context.Context
)

func Init(ctx context.Context, cfg *xconfig.Config) context.Context {
	if Config != nil {
		panic("not reached")
	}

	rand.Seed(uint64(time.Now().UnixNano()))
	mathRand.Seed(time.Now().UnixNano())

	Config = cfg
	Ctx = ctx

	callOnInit(ctx)
	setupOtel(ctx)

	return ctx
}

//------------------------------------------------------------------------------

type hookFn func(context.Context)

var onInit []hookFn

func OnInit(fn hookFn) {
	if Ctx != nil {
		fn(Ctx)
		return
	}
	onInit = append(onInit, fn)
}

func callOnInit(ctx context.Context) {
	run(ctx, onInit)
	onInit = nil
}

//------------------------------------------------------------------------------

var (
	primarily []hookFn
	secondary []hookFn
)

func Exit(ctx context.Context) {
	if !atomic.CompareAndSwapUint32(&exiting, 0, 1) {
		return
	}

	close(ExitCh)
	if waitTimeout(&WaitGroup, 30*time.Second) {
		logrus.WithContext(ctx).Info("waitTimeout")
	}

	run(ctx, primarily)
	run(ctx, secondary)
}

func waitTimeout(wg *sync.WaitGroup, timeout time.Duration) bool {
	c := make(chan struct{})
	go func() {
		defer close(c)
		wg.Wait()
	}()
	select {
	case <-c:
		return false // completed normally
	case <-time.After(timeout):
		return true // timed out
	}
}

func run(ctx context.Context, hookFns []hookFn) {
	var wg sync.WaitGroup
	wg.Add(len(hookFns))
	for _, h := range hookFns {
		go func(h hookFn) {
			defer wg.Done()
			h(ctx)
		}(h)
	}
	wg.Wait()
}

func OnExit(h hookFn) {
	primarily = append(primarily, h)
}

func OnExitSecondary(h hookFn) {
	secondary = append(secondary, h)
}

//------------------------------------------------------------------------------

func WaitExitSignal() os.Signal {
	ch := make(chan os.Signal, 3)
	signal.Notify(
		ch,
		syscall.SIGINT,
		syscall.SIGQUIT,
		syscall.SIGTERM,
	)
	return <-ch
}

func IsDebug() bool {
	switch Config.Env {
	case "prod":
		return false
	}
	return true
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/rwe/postgres.go
package rwe

import (
	"context"
	"net"
	"sync"

	"github.com/go-pg/pg/v10"
	"github.com/go-pg/pgext"
	"github.com/sirupsen/logrus"
	"github.com/uptrace/go-realworld-example-app/xconfig"
)

var (
	pgMainOnce sync.Once
	pgMain     *pg.DB
)

func PGMain() *pg.DB {
	pgMainOnce.Do(func() {
		pgMain = NewPostgres(Config.PGMain, hasPgbouncer())
	})
	return pgMain
}

var (
	pgMainTxOnce sync.Once
	pgMainTx     *pg.DB
)

func PGMainTx() *pg.DB {
	pgMainTxOnce.Do(func() {
		pgMainTx = NewPostgres(Config.PGMain, false)
	})
	return pgMainTx
}

func hasPgbouncer() bool {
	switch Config.Env {
	case "test", "dev":
		return false
	default:
		return true
	}
}

func NewPostgres(cfg *xconfig.Postgres, usePool bool) *pg.DB {
	addr := cfg.Addr
	if usePool {
		addr = replacePort(addr, cfg.ConnectionPoolPort)
	}

	opt := cfg.Options()
	opt.Addr = addr

	db := pg.Connect(opt)
	OnExitSecondary(func(ctx context.Context) {
		if err := db.Close(); err != nil {
			logrus.WithError(err).Error("pg.Close failed")
		}
	})

	db.AddQueryHook(pgext.OpenTelemetryHook{})
	if IsDebug() {
		db.AddQueryHook(pgext.DebugHook{})
	}

	return db
}

func replacePort(s, newPort string) string {
	if newPort == "" {
		return s
	}
	host, _, err := net.SplitHostPort(s)
	if err != nil {
		host = s
	}
	return net.JoinHostPort(host, newPort)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/rwe/redis.go
package rwe

import (
	"context"
	"sync"
	"time"

	"github.com/go-redis/cache/v8"
	"github.com/go-redis/redis/v8"
	"github.com/go-redis/redis_rate/v9"
	"github.com/go-redis/redisext"
)

var (
	redisRingOnce sync.Once
	redisRing     *redis.Ring
)

func RedisRing() *redis.Ring {
	redisRingOnce.Do(func() {
		opt := Config.RedisCache.Options()
		redisRing = redis.NewRing(opt)

		_ = redisRing.ForEachShard(context.TODO(),
			func(ctx context.Context, shard *redis.Client) error {
				shard.AddHook(redisext.OpenTelemetryHook{})
				return nil
			})
	})
	return redisRing
}

//------------------------------------------------------------------------------

var (
	rateLimiterOnce sync.Once
	rateLimiter     *redis_rate.Limiter
)

func RateLimiter() *redis_rate.Limiter {
	rateLimiterOnce.Do(func() {
		rateLimiter = redis_rate.NewLimiter(RedisRing())
	})
	return rateLimiter
}

//------------------------------------------------------------------------------

var (
	redisCacheOnce sync.Once
	redisCache     *cache.Cache
)

func RedisCache() *cache.Cache {
	redisCacheOnce.Do(func() {
		redisCache = cache.New(&cache.Options{
			Redis:      RedisRing(),
			LocalCache: cache.NewTinyLFU(1000, time.Minute),
		})
	})
	return redisCache
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/rwe/router.go
package rwe

import (
	"errors"
	"net"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/go-redis/redis_rate/v9"
	"go.opentelemetry.io/contrib/instrumentation/github.com/gin-gonic/gin/otelgin"
)

var (
	Router *gin.Engine
	API    *gin.RouterGroup
)

func init() {
	Router = gin.Default()
	Router.Use(corsMiddleware)
	Router.Use(errorMiddleware)
	Router.Use(rateLimitMiddleware)
	Router.Use(otelgin.Middleware("rwe"))

	API = Router.Group("/api")
}

func errorMiddleware(c *gin.Context) {
	c.Next()

	ginErr := c.Errors.Last()
	if ginErr == nil {
		return
	}

	switch err := ginErr.Err.(type) {
	default:
		c.JSON(400, gin.H{
			"error": err.Error(),
		})
	}
}

func corsMiddleware(c *gin.Context) {
	origin := c.Request.Header.Get("Origin")
	if origin == "" {
		return
	}

	if c.Request.Method == http.MethodOptions {
		h := c.Writer.Header()
		h.Set("Access-Control-Allow-Origin", origin)
		h.Set("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,HEAD")
		h.Set("Access-Control-Allow-Headers", "authorization,content-type")
		h.Set("Access-Control-Max-Age", "86400")
		c.AbortWithStatus(http.StatusNoContent)
		return
	}

	h := c.Writer.Header()
	h.Set("Access-Control-Allow-Origin", origin)
}

func rateLimitMiddleware(c *gin.Context) {
	if c.Request.Method == http.MethodOptions {
		return
	}

	host, _, err := net.SplitHostPort(c.Request.RemoteAddr)
	if err != nil {
		c.Error(err)
		return
	}

	rateKey := "rl:" + host
	limit := redis_rate.PerMinute(100)

	res, err := RateLimiter().Allow(c.Request.Context(), rateKey, limit)
	if err != nil {
		c.Error(err)
		return
	}
	if res.Allowed == 0 {
		c.AbortWithError(http.StatusTooManyRequests, errors.New("rate limited"))
		return
	}
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/rwe/uptrace.go
package rwe

import (
	"context"
	"os"

	"github.com/sirupsen/logrus"
	"github.com/uptrace/uptrace-go/uptrace"
	"go.opentelemetry.io/otel/api/global"
	"go.opentelemetry.io/otel/label"
	"go.opentelemetry.io/otel/sdk/resource"
)

var (
	upclient *uptrace.Client
	Tracer   = global.Tracer("github.com/uptrace/go-realworld-example-app")
)

func setupOtel(ctx context.Context) {
	if err := setupUptrace(ctx); err != nil {
		logrus.WithContext(ctx).WithError(err).Error("setupUptrace")
	}
}

func setupUptrace(ctx context.Context) error {
	hostname, _ := os.Hostname()
	upclient = uptrace.NewClient(&uptrace.Config{
		DSN: Config.Uptrace.DSN,

		Resource: resource.New(
			label.String("service.name", Config.Service),
			label.String("host.name", hostname),
		),
	})

	OnExitSecondary(func(ctx context.Context) {
		if err := upclient.Close(); err != nil {
			logrus.WithContext(ctx).WithError(err).Error("uptrace.Close failed")
		}
	})

	return nil
}

func Uptrace() *uptrace.Client {
	return upclient
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/scripts/Conduit.postman_collection.json
{
	"info": {
		"_postman_id": "0574ad8a-a525-43ae-8e1e-5fd9756037f4",
		"name": "Conduit",
		"description": "Collection for testing the Conduit API\n\nhttps://github.com/gothinkster/realworld",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Auth",
			"item": [
				{
					"name": "Register",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"if (!(environment.isIntegrationTest)) {",
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"user\" property'] = responseJSON.hasOwnProperty('user');",
									"",
									"var user = responseJSON.user || {};",
									"",
									"tests['User has \"email\" property'] = user.hasOwnProperty('email');",
									"tests['User has \"username\" property'] = user.hasOwnProperty('username');",
									"tests['User has \"bio\" property'] = user.hasOwnProperty('bio');",
									"tests['User has \"image\" property'] = user.hasOwnProperty('image');",
									"tests['User has \"token\" property'] = user.hasOwnProperty('token');",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"user\":{\"email\":\"{{EMAIL}}\", \"password\":\"{{PASSWORD}}\", \"username\":\"{{USERNAME}}\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/users",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"users"
							]
						}
					},
					"response": []
				},
				{
					"name": "Login",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"user\" property'] = responseJSON.hasOwnProperty('user');",
									"",
									"var user = responseJSON.user || {};",
									"",
									"tests['User has \"email\" property'] = user.hasOwnProperty('email');",
									"tests['User has \"username\" property'] = user.hasOwnProperty('username');",
									"tests['User has \"bio\" property'] = user.hasOwnProperty('bio');",
									"tests['User has \"image\" property'] = user.hasOwnProperty('image');",
									"tests['User has \"token\" property'] = user.hasOwnProperty('token');",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"user\":{\"email\":\"{{EMAIL}}\", \"password\":\"{{PASSWORD}}\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/users/login",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"users",
								"login"
							]
						}
					},
					"response": []
				},
				{
					"name": "Login and Remember Token",
					"event": [
						{
							"listen": "test",
							"script": {
								"id": "a7674032-bf09-4ae7-8224-4afa2fb1a9f9",
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"user\" property'] = responseJSON.hasOwnProperty('user');",
									"",
									"var user = responseJSON.user || {};",
									"",
									"tests['User has \"email\" property'] = user.hasOwnProperty('email');",
									"tests['User has \"username\" property'] = user.hasOwnProperty('username');",
									"tests['User has \"bio\" property'] = user.hasOwnProperty('bio');",
									"tests['User has \"image\" property'] = user.hasOwnProperty('image');",
									"tests['User has \"token\" property'] = user.hasOwnProperty('token');",
									"",
									"if(tests['User has \"token\" property']){",
									"    pm.globals.set('token', user.token);",
									"}",
									"",
									"tests['Global variable \"token\" has been set'] = pm.globals.get('token') === user.token;",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"user\":{\"email\":\"{{EMAIL}}\", \"password\":\"{{PASSWORD}}\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/users/login",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"users",
								"login"
							]
						}
					},
					"response": []
				},
				{
					"name": "Current User",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"user\" property'] = responseJSON.hasOwnProperty('user');",
									"",
									"var user = responseJSON.user || {};",
									"",
									"tests['User has \"email\" property'] = user.hasOwnProperty('email');",
									"tests['User has \"username\" property'] = user.hasOwnProperty('username');",
									"tests['User has \"bio\" property'] = user.hasOwnProperty('bio');",
									"tests['User has \"image\" property'] = user.hasOwnProperty('image');",
									"tests['User has \"token\" property'] = user.hasOwnProperty('token');",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/user",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"user"
							]
						}
					},
					"response": []
				},
				{
					"name": "Update User",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"user\" property'] = responseJSON.hasOwnProperty('user');",
									"",
									"var user = responseJSON.user || {};",
									"",
									"tests['User has \"email\" property'] = user.hasOwnProperty('email');",
									"tests['User has \"username\" property'] = user.hasOwnProperty('username');",
									"tests['User has \"bio\" property'] = user.hasOwnProperty('bio');",
									"tests['User has \"image\" property'] = user.hasOwnProperty('image');",
									"tests['User has \"token\" property'] = user.hasOwnProperty('token');",
									""
								]
							}
						}
					],
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"user\":{\"email\":\"{{EMAIL}}\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/user",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"user"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Articles",
			"item": [
				{
					"name": "All Articles",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles by Author",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?author=johnjacob",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "author",
									"value": "johnjacob"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles Favorited by Username",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"    ",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?favorited=jane",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "favorited",
									"value": "jane"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles by Tag",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?tag=dragons",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "tag",
									"value": "dragons"
								}
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Articles, Favorite, Comments",
			"item": [
				{
					"name": "Create Article",
					"event": [
						{
							"listen": "test",
							"script": {
								"id": "e711dbf8-8065-4ba8-8b74-f1639a7d8208",
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"article\" property'] = responseJSON.hasOwnProperty('article');",
									"",
									"var article = responseJSON.article || {};",
									"",
									"tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"pm.globals.set('slug', article.slug);",
									"",
									"tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"article\":{\"title\":\"How to train your dragon\", \"description\":\"Ever wonder how?\", \"body\":\"Very carefully.\", \"tagList\":[\"dragons\",\"training\"]}}"
						},
						"url": {
							"raw": "{{APIURL}}/articles",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							]
						}
					},
					"response": []
				},
				{
					"name": "Feed",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/feed",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"feed"
							]
						}
					},
					"response": []
				},
				{
					"name": "All Articles",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							]
						}
					},
					"response": []
				},
				{
					"name": "All Articles with auth",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles by Author",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?author={{USERNAME}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "author",
									"value": "{{USERNAME}}"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles by Author with auth",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?author={{USERNAME}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "author",
									"value": "{{USERNAME}}"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles Favorited by Username",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"    ",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?favorited=jane",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "favorited",
									"value": "jane"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles Favorited by Username with auth",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"    ",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?favorited=jane",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "favorited",
									"value": "jane"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Single Article by slug",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"article\" property'] = responseJSON.hasOwnProperty('article');",
									"",
									"var article = responseJSON.article || {};",
									"",
									"tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Articles by Tag",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"articles\" property'] = responseJSON.hasOwnProperty('articles');",
									"    tests['Response contains \"articlesCount\" property'] = responseJSON.hasOwnProperty('articlesCount');",
									"    tests['articlesCount is an integer'] = Number.isInteger(responseJSON.articlesCount);",
									"",
									"    if(responseJSON.articles.length){",
									"        var article = responseJSON.articles[0];",
									"",
									"        tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"        tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"        tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"        tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"        tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"        tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"        tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"        tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"        tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"        tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"        tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"        tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"        tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"        tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"    } else {",
									"        tests['articlesCount is 0 when feed is empty'] = responseJSON.articlesCount === 0;",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles?tag=dragons",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles"
							],
							"query": [
								{
									"key": "tag",
									"value": "dragons"
								}
							]
						}
					},
					"response": []
				},
				{
					"name": "Update Article",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"if (!(environment.isIntegrationTest)) {",
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"article\" property'] = responseJSON.hasOwnProperty('article');",
									"",
									"var article = responseJSON.article || {};",
									"",
									"tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "PUT",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"article\":{\"body\":\"With two hands\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Favorite Article",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"article\" property'] = responseJSON.hasOwnProperty('article');",
									"",
									"var article = responseJSON.article || {};",
									"",
									"tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"tests[\"Article's 'favorited' property is true\"] = article.favorited === true;",
									"tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"tests[\"Article's 'favoritesCount' property is greater than 0\"] = article.favoritesCount > 0;",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}/favorite",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}",
								"favorite"
							]
						}
					},
					"response": []
				},
				{
					"name": "Unfavorite Article",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"article\" property'] = responseJSON.hasOwnProperty('article');",
									"",
									"var article = responseJSON.article || {};",
									"",
									"tests['Article has \"title\" property'] = article.hasOwnProperty('title');",
									"tests['Article has \"slug\" property'] = article.hasOwnProperty('slug');",
									"tests['Article has \"body\" property'] = article.hasOwnProperty('body');",
									"tests['Article has \"createdAt\" property'] = article.hasOwnProperty('createdAt');",
									"tests['Article\\'s \"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.createdAt);",
									"tests['Article has \"updatedAt\" property'] = article.hasOwnProperty('updatedAt');",
									"tests['Article\\'s \"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(article.updatedAt);",
									"tests['Article has \"description\" property'] = article.hasOwnProperty('description');",
									"tests['Article has \"tagList\" property'] = article.hasOwnProperty('tagList');",
									"tests['Article\\'s \"tagList\" property is an Array'] = Array.isArray(article.tagList);",
									"tests['Article has \"author\" property'] = article.hasOwnProperty('author');",
									"tests['Article has \"favorited\" property'] = article.hasOwnProperty('favorited');",
									"tests['Article has \"favoritesCount\" property'] = article.hasOwnProperty('favoritesCount');",
									"tests['favoritesCount is an integer'] = Number.isInteger(article.favoritesCount);",
									"tests[\"Article's \\\"favorited\\\" property is false\"] = article.favorited === false;",
									""
								]
							}
						}
					],
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}/favorite",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}",
								"favorite"
							]
						}
					},
					"response": []
				},
				{
					"name": "Create Comment for Article",
					"event": [
						{
							"listen": "test",
							"script": {
								"id": "9f90c364-cc68-4728-961a-85eb00197d7b",
								"type": "text/javascript",
								"exec": [
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"comment\" property'] = responseJSON.hasOwnProperty('comment');",
									"",
									"var comment = responseJSON.comment || {};",
									"",
									"tests['Comment has \"id\" property'] = comment.hasOwnProperty('id');",
									"pm.globals.set('commentId', comment.id);",
									"",
									"tests['Comment has \"body\" property'] = comment.hasOwnProperty('body');",
									"tests['Comment has \"createdAt\" property'] = comment.hasOwnProperty('createdAt');",
									"tests['\"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(comment.createdAt);",
									"tests['Comment has \"updatedAt\" property'] = comment.hasOwnProperty('updatedAt');",
									"tests['\"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(comment.updatedAt);",
									"tests['Comment has \"author\" property'] = comment.hasOwnProperty('author');",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"comment\":{\"body\":\"Thank you so much!\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}/comments",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}",
								"comments"
							]
						}
					},
					"response": []
				},
				{
					"name": "All Comments for Article",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"comments\" property'] = responseJSON.hasOwnProperty('comments');",
									"",
									"    if(responseJSON.comments.length){",
									"        var comment = responseJSON.comments[0];",
									"",
									"        tests['Comment has \"id\" property'] = comment.hasOwnProperty('id');",
									"        tests['Comment has \"body\" property'] = comment.hasOwnProperty('body');",
									"        tests['Comment has \"createdAt\" property'] = comment.hasOwnProperty('createdAt');",
									"        tests['\"createdAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(comment.createdAt);",
									"        tests['Comment has \"updatedAt\" property'] = comment.hasOwnProperty('updatedAt');",
									"        tests['\"updatedAt\" property is an ISO 8601 timestamp'] = /^\\d{4,}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d.\\d+(?:[+-][0-2]\\d:[0-5]\\d|Z)$/.test(comment.updatedAt);",
									"        tests['Comment has \"author\" property'] = comment.hasOwnProperty('author');",
									"    }",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}/comments",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}",
								"comments"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete Comment for Article",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}/comments/{{commentId}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}",
								"comments",
								"{{commentId}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete Article",
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/articles/{{slug}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"articles",
								"{{slug}}"
							]
						}
					},
					"response": []
				}
			],
			"event": [
				{
					"listen": "prerequest",
					"script": {
						"id": "67853a4a-e972-4573-a295-dad12a46a9d7",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				},
				{
					"listen": "test",
					"script": {
						"id": "3057f989-15e4-484e-b8fa-a041043d0ac0",
						"type": "text/javascript",
						"exec": [
							""
						]
					}
				}
			]
		},
		{
			"name": "Profiles",
			"item": [
				{
					"name": "Register Celeb",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"if (!(environment.isIntegrationTest)) {",
									"var responseJSON = JSON.parse(responseBody);",
									"",
									"tests['Response contains \"user\" property'] = responseJSON.hasOwnProperty('user');",
									"",
									"var user = responseJSON.user || {};",
									"",
									"tests['User has \"email\" property'] = user.hasOwnProperty('email');",
									"tests['User has \"username\" property'] = user.hasOwnProperty('username');",
									"tests['User has \"bio\" property'] = user.hasOwnProperty('bio');",
									"tests['User has \"image\" property'] = user.hasOwnProperty('image');",
									"tests['User has \"token\" property'] = user.hasOwnProperty('token');",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"user\":{\"email\":\"celeb_{{EMAIL}}\", \"password\":\"{{PASSWORD}}\", \"username\":\"celeb_{{USERNAME}}\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/users",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"users"
							]
						}
					},
					"response": []
				},
				{
					"name": "Profile",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"if (!(environment.isIntegrationTest)) {",
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"profile\" property'] = responseJSON.hasOwnProperty('profile');",
									"    ",
									"    var profile = responseJSON.profile || {};",
									"    ",
									"    tests['Profile has \"username\" property'] = profile.hasOwnProperty('username');",
									"    tests['Profile has \"bio\" property'] = profile.hasOwnProperty('bio');",
									"    tests['Profile has \"image\" property'] = profile.hasOwnProperty('image');",
									"    tests['Profile has \"following\" property'] = profile.hasOwnProperty('following');",
									"}",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/profiles/celeb_{{USERNAME}}",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"profiles",
								"celeb_{{USERNAME}}"
							]
						}
					},
					"response": []
				},
				{
					"name": "Follow Profile",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"if (!(environment.isIntegrationTest)) {",
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"profile\" property'] = responseJSON.hasOwnProperty('profile');",
									"    ",
									"    var profile = responseJSON.profile || {};",
									"    ",
									"    tests['Profile has \"username\" property'] = profile.hasOwnProperty('username');",
									"    tests['Profile has \"bio\" property'] = profile.hasOwnProperty('bio');",
									"    tests['Profile has \"image\" property'] = profile.hasOwnProperty('image');",
									"    tests['Profile has \"following\" property'] = profile.hasOwnProperty('following');",
									"    tests['Profile\\'s \"following\" property is true'] = profile.following === true;",
									"}",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "POST",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": "{\"user\":{\"email\":\"{{EMAIL}}\"}}"
						},
						"url": {
							"raw": "{{APIURL}}/profiles/celeb_{{USERNAME}}/follow",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"profiles",
								"celeb_{{USERNAME}}",
								"follow"
							]
						}
					},
					"response": []
				},
				{
					"name": "Unfollow Profile",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"if (!(environment.isIntegrationTest)) {",
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"",
									"    tests['Response contains \"profile\" property'] = responseJSON.hasOwnProperty('profile');",
									"    ",
									"    var profile = responseJSON.profile || {};",
									"    ",
									"    tests['Profile has \"username\" property'] = profile.hasOwnProperty('username');",
									"    tests['Profile has \"bio\" property'] = profile.hasOwnProperty('bio');",
									"    tests['Profile has \"image\" property'] = profile.hasOwnProperty('image');",
									"    tests['Profile has \"following\" property'] = profile.hasOwnProperty('following');",
									"    tests['Profile\\'s \"following\" property is false'] = profile.following === false;",
									"}",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "DELETE",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							},
							{
								"key": "Authorization",
								"value": "Token {{token}}"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/profiles/celeb_{{USERNAME}}/follow",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"profiles",
								"celeb_{{USERNAME}}",
								"follow"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Tags",
			"item": [
				{
					"name": "All Tags",
					"event": [
						{
							"listen": "test",
							"script": {
								"type": "text/javascript",
								"exec": [
									"var is200Response = responseCode.code === 200;",
									"",
									"tests['Response code is 200 OK'] = is200Response;",
									"",
									"if(is200Response){",
									"    var responseJSON = JSON.parse(responseBody);",
									"    ",
									"    tests['Response contains \"tags\" property'] = responseJSON.hasOwnProperty('tags');",
									"    tests['\"tags\" property returned as array'] = Array.isArray(responseJSON.tags);",
									"}",
									""
								]
							}
						}
					],
					"request": {
						"method": "GET",
						"header": [
							{
								"key": "Content-Type",
								"value": "application/json"
							},
							{
								"key": "X-Requested-With",
								"value": "XMLHttpRequest"
							}
						],
						"body": {
							"mode": "raw",
							"raw": ""
						},
						"url": {
							"raw": "{{APIURL}}/tags",
							"host": [
								"{{APIURL}}"
							],
							"path": [
								"tags"
							]
						}
					},
					"response": []
				}
			]
		}
	]
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/scripts/README.md
## RealWorld API Spec

Test scripts are copied from [Real World API specs](https://github.com/gothinkster/realworld/tree/master/api).

export APIURL=172.21.37.37:8000
export USERNAME=usef
export EMAIL=sample-email@gmail.com
export PASSWORD=rahasia

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/scripts/run-api-tests.sh
#!/usr/bin/env bash
set -x

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

APIURL=${APIURL:-https://conduit.productionready.io/api}
USERNAME=${USERNAME:-u`date +%s`}
EMAIL=${EMAIL:-$USERNAME@mail.com}
PASSWORD=${PASSWORD:-password}

npx newman run $SCRIPTDIR/Conduit.postman_collection.json \
  --delay-request 500 \
  --global-var "APIURL=$APIURL" \
  --global-var "USERNAME=$USERNAME" \
  --global-var "EMAIL=$EMAIL" \
  --global-var "PASSWORD=$PASSWORD"

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/scripts/swagger.json
{
  "swagger": "2.0",
  "info": {
    "description": "Conduit API",
    "version": "1.0.0",
    "title": "Conduit API",
    "contact": {
      "name": "RealWorld",
      "url": "https://realworld.io"
    },
    "license": {
      "name": "MIT License",
      "url": "https://opensource.org/licenses/MIT"
    }
  },
  "basePath": "/api",
  "schemes": [
    "https",
    "http"
  ],
  "produces": [
    "application/json"
  ],
  "consumes": [
    "application/json"
  ],
  "securityDefinitions": {
    "Token": {
      "description": "For accessing the protected API resources, you must have received a a valid JWT token after registering or logging in. This JWT token must then be used for all protected resources by passing it in via the 'Authorization' header.\n\nA JWT token is generated by the API by either registering via /users or logging in via /users/login.\n\nThe following format must be in the 'Authorization' header :\n\n    Token: xxxxxx.yyyyyyy.zzzzzz\n    \n",
      "type": "apiKey",
      "name": "Authorization",
      "in": "header"
    }
  },
  "paths": {
    "/users/login": {
      "post": {
        "summary": "Existing user login",
        "description": "Login for existing user",
        "tags": [
          "User and Authentication"
        ],
        "operationId": "Login",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "description": "Credentials to use",
            "schema": {
              "$ref": "#/definitions/LoginUserRequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/UserResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/users": {
      "post": {
        "summary": "Register a new user",
        "description": "Register a new user",
        "tags": [
          "User and Authentication"
        ],
        "operationId": "CreateUser",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "description": "Details of the new user to register",
            "schema": {
              "$ref": "#/definitions/NewUserRequest"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/UserResponse"
            }
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "get": {
        "summary": "Get current user",
        "description": "Gets the currently logged-in user",
        "tags": [
          "User and Authentication"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "GetCurrentUser",
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/UserResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "put": {
        "summary": "Update current user",
        "description": "Updated user information for current user",
        "tags": [
          "User and Authentication"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "UpdateCurrentUser",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "description": "User details to update. At least **one** field is required.",
            "schema": {
              "$ref": "#/definitions/UpdateUserRequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/UserResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/profiles/{username}": {
      "get": {
        "summary": "Get a profile",
        "description": "Get a profile of a user of the system. Auth is optional",
        "tags": [
          "Profile"
        ],
        "operationId": "GetProfileByUsername",
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "Username of the profile to get",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/ProfileResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/profiles/{username}/follow": {
      "post": {
        "summary": "Follow a user",
        "description": "Follow a user by username",
        "tags": [
          "Profile"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "FollowUserByUsername",
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "Username of the profile you want to follow",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/ProfileResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "delete": {
        "summary": "Unfollow a user",
        "description": "Unfollow a user by username",
        "tags": [
          "Profile"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "UnfollowUserByUsername",
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "Username of the profile you want to unfollow",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/ProfileResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/articles/feed": {
      "get": {
        "summary": "Get recent articles from users you follow",
        "description": "Get most recent articles from users you follow. Use query parameters to limit. Auth is required",
        "tags": [
          "Articles"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "GetArticlesFeed",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "Limit number of articles returned (default is 20)",
            "required": false,
            "default": 20,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Offset/skip number of articles (default is 0)",
            "required": false,
            "default": 0,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/MultipleArticlesResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/articles": {
      "get": {
        "summary": "Get recent articles globally",
        "description": "Get most recent articles globally. Use query parameters to filter results. Auth is optional",
        "tags": [
          "Articles"
        ],
        "operationId": "GetArticles",
        "parameters": [
          {
            "name": "tag",
            "in": "query",
            "description": "Filter by tag",
            "required": false,
            "type": "string"
          },
          {
            "name": "author",
            "in": "query",
            "description": "Filter by author (username)",
            "required": false,
            "type": "string"
          },
          {
            "name": "favorited",
            "in": "query",
            "description": "Filter by favorites of a user (username)",
            "required": false,
            "type": "string"
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Limit number of articles returned (default is 20)",
            "required": false,
            "default": 20,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Offset/skip number of articles (default is 0)",
            "required": false,
            "default": 0,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/MultipleArticlesResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "post": {
        "summary": "Create an article",
        "description": "Create an article. Auth is required",
        "tags": [
          "Articles"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "CreateArticle",
        "parameters": [
          {
            "name": "article",
            "in": "body",
            "required": true,
            "description": "Article to create",
            "schema": {
              "$ref": "#/definitions/NewArticleRequest"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/SingleArticleResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/articles/{slug}": {
      "get": {
        "summary": "Get an article",
        "description": "Get an article. Auth not required",
        "tags": [
          "Articles"
        ],
        "operationId": "GetArticle",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article to get",
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/SingleArticleResponse"
            }
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "put": {
        "summary": "Update an article",
        "description": "Update an article. Auth is required",
        "tags": [
          "Articles"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "UpdateArticle",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article to update",
            "type": "string"
          },
          {
            "name": "article",
            "in": "body",
            "required": true,
            "description": "Article to update",
            "schema": {
              "$ref": "#/definitions/UpdateArticleRequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/SingleArticleResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "delete": {
        "summary": "Delete an article",
        "description": "Delete an article. Auth is required",
        "tags": [
          "Articles"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "DeleteArticle",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article to delete",
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/articles/{slug}/comments": {
      "get": {
        "summary": "Get comments for an article",
        "description": "Get the comments for an article. Auth is optional",
        "tags": [
          "Comments"
        ],
        "operationId": "GetArticleComments",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article that you want to get comments for",
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/MultipleCommentsResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "post": {
        "summary": "Create a comment for an article",
        "description": "Create a comment for an article. Auth is required",
        "tags": [
          "Comments"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "CreateArticleComment",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article that you want to create a comment for",
            "type": "string"
          },
          {
            "name": "comment",
            "in": "body",
            "required": true,
            "description": "Comment you want to create",
            "schema": {
              "$ref": "#/definitions/NewCommentRequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/SingleCommentResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/articles/{slug}/comments/{id}": {
      "delete": {
        "summary": "Delete a comment for an article",
        "description": "Delete a comment for an article. Auth is required",
        "tags": [
          "Comments"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "DeleteArticleComment",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article that you want to delete a comment for",
            "type": "string"
          },
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "ID of the comment you want to delete",
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/articles/{slug}/favorite": {
      "post": {
        "summary": "Favorite an article",
        "description": "Favorite an article. Auth is required",
        "tags": [
          "Favorites"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "CreateArticleFavorite",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article that you want to favorite",
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/SingleArticleResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      },
      "delete": {
        "summary": "Unfavorite an article",
        "description": "Unfavorite an article. Auth is required",
        "tags": [
          "Favorites"
        ],
        "security": [
          {
            "Token": []
          }
        ],
        "operationId": "DeleteArticleFavorite",
        "parameters": [
          {
            "name": "slug",
            "in": "path",
            "required": true,
            "description": "Slug of the article that you want to unfavorite",
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/SingleArticleResponse"
            }
          },
          "401": {
            "description": "Unauthorized"
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    },
    "/tags": {
      "get": {
        "summary": "Get tags",
        "description": "Get tags. Auth not required",
        "responses": {
          "200": {
            "description": "OK",
            "schema": {
              "$ref": "#/definitions/TagsResponse"
            }
          },
          "422": {
            "description": "Unexpected error",
            "schema": {
              "$ref": "#/definitions/GenericErrorModel"
            }
          }
        }
      }
    }
  },
  "definitions": {
    "LoginUser": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string"
        },
        "password": {
          "type": "string",
          "format": "password"
        }
      },
      "required": [
        "email",
        "password"
      ]
    },
    "LoginUserRequest": {
      "type": "object",
      "properties": {
        "user": {
          "$ref": "#/definitions/LoginUser"
        }
      },
      "required": [
        "user"
      ]
    },
    "NewUser": {
      "type": "object",
      "properties": {
        "username": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "password": {
          "type": "string",
          "format": "password"
        }
      },
      "required": [
        "username",
        "email",
        "password"
      ]
    },
    "NewUserRequest": {
      "type": "object",
      "properties": {
        "user": {
          "$ref": "#/definitions/NewUser"
        }
      },
      "required": [
        "user"
      ]
    },
    "User": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string"
        },
        "token": {
          "type": "string"
        },
        "username": {
          "type": "string"
        },
        "bio": {
          "type": "string"
        },
        "image": {
          "type": "string"
        }
      },
      "required": [
        "email",
        "token",
        "username",
        "bio",
        "image"
      ]
    },
    "UserResponse": {
      "type": "object",
      "properties": {
        "user": {
          "$ref": "#/definitions/User"
        }
      },
      "required": [
        "user"
      ]
    },
    "UpdateUser": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string"
        },
        "token": {
          "type": "string"
        },
        "username": {
          "type": "string"
        },
        "bio": {
          "type": "string"
        },
        "image": {
          "type": "string"
        }
      }
    },
    "UpdateUserRequest": {
      "type": "object",
      "properties": {
        "user": {
          "$ref": "#/definitions/UpdateUser"
        }
      },
      "required": [
        "user"
      ]
    },
    "ProfileResponse": {
      "type": "object",
      "properties": {
        "profile": {
          "$ref": "#/definitions/Profile"
        }
      },
      "required": [
        "profile"
      ]
    },
    "Profile": {
      "type": "object",
      "properties": {
        "username": {
          "type": "string"
        },
        "bio": {
          "type": "string"
        },
        "image": {
          "type": "string"
        },
        "following": {
          "type": "boolean"
        }
      },
      "required": [
        "username",
        "bio",
        "image",
        "following"
      ]
    },
    "Article": {
      "type": "object",
      "properties": {
        "slug": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "body": {
          "type": "string"
        },
        "tagList": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "createdAt": {
          "type": "string",
          "format": "date-time"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time"
        },
        "favorited": {
          "type": "boolean"
        },
        "favoritesCount": {
          "type": "integer"
        },
        "author": {
          "$ref": "#/definitions/Profile"
        }
      },
      "required": [
        "slug",
        "title",
        "description",
        "body",
        "tagList",
        "createdAt",
        "updatedAt",
        "favorited",
        "favoritesCount",
        "author"
      ]
    },
    "SingleArticleResponse": {
      "type": "object",
      "properties": {
        "article": {
          "$ref": "#/definitions/Article"
        }
      },
      "required": [
        "article"
      ]
    },
    "MultipleArticlesResponse": {
      "type": "object",
      "properties": {
        "articles": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Article"
          }
        },
        "articlesCount": {
          "type": "integer"
        }
      },
      "required": [
        "articles",
        "articlesCount"
      ]
    },
    "NewArticle": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "body": {
          "type": "string"
        },
        "tagList": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "title",
        "description",
        "body"
      ]
    },
    "NewArticleRequest": {
      "type": "object",
      "properties": {
        "article": {
          "$ref": "#/definitions/NewArticle"
        }
      },
      "required": [
        "article"
      ]
    },
    "UpdateArticle": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "body": {
          "type": "string"
        }
      }
    },
    "UpdateArticleRequest": {
      "type": "object",
      "properties": {
        "article": {
          "$ref": "#/definitions/UpdateArticle"
        }
      },
      "required": [
        "article"
      ]
    },
    "Comment": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "createdAt": {
          "type": "string",
          "format": "date-time"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time"
        },
        "body": {
          "type": "string"
        },
        "author": {
          "$ref": "#/definitions/Profile"
        }
      },
      "required": [
        "id",
        "createdAt",
        "updatedAt",
        "body",
        "author"
      ]
    },
    "SingleCommentResponse": {
      "type": "object",
      "properties": {
        "comment": {
          "$ref": "#/definitions/Comment"
        }
      },
      "required": [
        "comment"
      ]
    },
    "MultipleCommentsResponse": {
      "type": "object",
      "properties": {
        "comments": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Comment"
          }
        }
      },
      "required": [
        "comments"
      ]
    },
    "NewComment": {
      "type": "object",
      "properties": {
        "body": {
          "type": "string"
        }
      },
      "required": [
        "body"
      ]
    },
    "NewCommentRequest": {
      "type": "object",
      "properties": {
        "comment": {
          "$ref": "#/definitions/NewComment"
        }
      },
      "required": [
        "comment"
      ]
    },
    "TagsResponse": {
      "type": "object",
      "properties": {
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": [
        "tags"
      ]
    },
    "GenericErrorModel": {
      "type": "object",
      "properties": {
        "errors": {
          "type": "object",
          "properties": {
            "body": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "body"
          ]
        }
      },
      "required": [
        "errors"
      ]
    }
  }
}
--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/testbed/http.go
package testbed

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"time"

	"github.com/uptrace/go-realworld-example-app/org"
	"github.com/uptrace/go-realworld-example-app/rwe"

	. "github.com/onsi/gomega"
)

func setToken(req *http.Request, userID uint64) {
	if userID == 0 {
		return
	}

	token, err := org.CreateUserToken(userID, time.Hour)
	Expect(err).NotTo(HaveOccurred())

	req.Header.Set("Authorization", "Token "+token)
}

func ParseJSON(resp *httptest.ResponseRecorder, code int) map[string]interface{} {
	res := make(map[string]interface{})
	err := json.Unmarshal(resp.Body.Bytes(), &res)
	Expect(err).NotTo(HaveOccurred())

	Expect(resp.Code).To(Equal(code))

	return res
}

func serve(req *http.Request) *httptest.ResponseRecorder {
	resp := httptest.NewRecorder()
	rwe.Router.ServeHTTP(resp, req)
	return resp
}

func Get(url string) *httptest.ResponseRecorder {
	return GetWithToken(url, 0)
}

func GetWithToken(url string, userID uint64) *httptest.ResponseRecorder {
	req := httptest.NewRequest("GET", url, nil)
	req.Header.Set("Content-Type", "application/json")
	setToken(req, userID)
	return serve(req)
}

func Post(url, data string) *httptest.ResponseRecorder {
	return PostWithToken(url, data, 0)
}

func PostWithToken(url, data string, userID uint64) *httptest.ResponseRecorder {
	req := httptest.NewRequest("POST", url, bytes.NewBufferString(data))
	req.Header.Set("Content-Type", "application/json")
	setToken(req, userID)
	return serve(req)
}

func PutWithToken(url, data string, userID uint64) *httptest.ResponseRecorder {
	req := httptest.NewRequest("PUT", url, bytes.NewBufferString(data))
	req.Header.Set("Content-Type", "application/json")
	setToken(req, userID)
	return serve(req)
}

func DeleteWithToken(url string, userID uint64) *httptest.ResponseRecorder {
	req := httptest.NewRequest("DELETE", url, nil)
	req.Header.Set("Content-Type", "application/json")
	setToken(req, userID)
	return serve(req)
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/testbed/util.go
package testbed

import (
	"context"

	. "github.com/onsi/gomega"
	"github.com/onsi/gomega/gstruct"
	"github.com/uptrace/go-realworld-example-app/rwe"
)

func ExtendKeys(a, b gstruct.Keys) gstruct.Keys {
	res := make(gstruct.Keys)
	for k, v := range a {
		res[k] = v
	}
	for k, v := range b {
		res[k] = v
	}
	return res
}

func ResetAll(ctx context.Context) {
	truncateDB(ctx)

	err := rwe.RedisRing().FlushDB(ctx).Err()
	Expect(err).NotTo(HaveOccurred())
}

func truncateDB(ctx context.Context) {
	cmd := "TRUNCATE users, favorite_articles, follow_users, comments, articles, article_tags"
	_, err := rwe.PGMain().ExecContext(ctx, cmd)
	Expect(err).NotTo(HaveOccurred())
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/xconfig/config.go
package xconfig

import (
	"flag"
	"io/ioutil"
	"os"
	"path/filepath"

	"gopkg.in/yaml.v2"
)

var (
	envFlag    = flag.String("env", "dev", "environment, e.g. development or production")
	appDirFlag = flag.String("app_dir", "app", "path to the app dir")
)

type Config struct {
	AppDir  string
	Service string
	Env     string

	RedisCache *RedisRing `yaml:"redis_cache"`
	PGMain     *Postgres  `yaml:"pg_main"`

	Uptrace struct {
		DSN string `yaml:"dsn"`
	} `yaml:"uptrace"`

	SecretKey string `yaml:"secret_key"`
}

func LoadConfig(service string) (*Config, error) {
	return loadConfigEnv(service, *appDirFlag, *envFlag)
}

func LoadConfigEnv(service, env string) (*Config, error) {
	return loadConfigEnv(service, *appDirFlag, env)
}

func loadConfigEnv(service, appDir, env string) (*Config, error) {
	appDir, err := filepath.Abs(appDir)
	if err != nil {
		return nil, err
	}

	appDir = findAppDir(appDir, env)
	f, err := os.Open(joinPath(appDir, env))
	if err != nil {
		return nil, err
	}

	b, err := ioutil.ReadAll(f)
	if err != nil {
		return nil, err
	}

	cfg, err := parseConfig(b)
	if err != nil {
		return nil, err
	}

	cfg.AppDir = appDir
	cfg.Service = service
	cfg.Env = env

	return cfg, nil
}

func findAppDir(appDir, env string) string {
	saved := appDir
	for i := 0; i < 10; i++ {
		cfgPath := joinPath(appDir, env)
		_, err := os.Stat(cfgPath)
		if err == nil {
			return appDir
		}

		if appDir == "." {
			break
		}
		appDir = filepath.Dir(filepath.Dir(appDir))
		appDir = filepath.Join(appDir, "app")
	}
	return saved
}

func joinPath(appDir, env string) string {
	return filepath.Join(appDir, "config", env+".yml")
}

func parseConfig(b []byte) (*Config, error) {
	cfg := new(Config)
	err := yaml.Unmarshal(b, cfg)
	if err != nil {
		return nil, err
	}
	return cfg, nil
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/xconfig/postgres.go
package xconfig

import (
	"time"

	"github.com/go-pg/pg/v10"
)

type Postgres struct {
	Addr     string
	Database string
	User     string
	Password string
	SSL      bool

	MaxRetries int `yaml:"max_retries"`

	DialTimeout  time.Duration `yaml:"dial_timeout"`
	ReadTimeout  time.Duration `yaml:"read_timeout"`
	WriteTimeout time.Duration `yaml:"write_timeout"`

	PoolSize     int           `yaml:"pool_size"`
	MinIdleConns int           `yaml:"min_idle_conns"`
	MaxConnAge   time.Duration `yaml:"max_conn_age"`
	PoolTimeout  time.Duration `yaml:"pool_timeout"`
	IdleTimeout  time.Duration `yaml:"idle_timeout"`

	ConnectionPoolPort string `yaml:"connection_pool_port"`
}

func (cfg *Postgres) Options() *pg.Options {
	return &pg.Options{
		User:     cfg.User,
		Password: cfg.Password,
		Database: cfg.Database,

		MaxRetries: cfg.MaxRetries,

		DialTimeout:  cfg.DialTimeout,
		ReadTimeout:  cfg.ReadTimeout,
		WriteTimeout: cfg.WriteTimeout,

		PoolSize:     cfg.PoolSize,
		MinIdleConns: cfg.MinIdleConns,
		MaxConnAge:   cfg.MaxConnAge,
		PoolTimeout:  cfg.PoolTimeout,
		IdleTimeout:  cfg.IdleTimeout,
	}
}

--#

--% /tmp/hapus/jakartaee/go-realworld-example-app/xconfig/redis.go
package xconfig

import (
	"time"

	"github.com/go-redis/redis/v8"
)

type RedisRing struct {
	Addrs    map[string]string
	Password string
	DB       int

	MaxRetries int `yaml:"max_retries"`

	PoolSize    int           `yaml:"pool_size"`
	PoolTimeout time.Duration `yaml:"pool_timeout"`
	IdleTimeout time.Duration `yaml:"idle_timeout"`

	DialTimeout  time.Duration `yaml:"dial_timeout"`
	ReadTimeout  time.Duration `yaml:"read_timeout"`
	WriteTimeout time.Duration `yaml:"write_timeout"`
}

func (cfg *RedisRing) Options() *redis.RingOptions {
	return &redis.RingOptions{
		Addrs:    cfg.Addrs,
		Password: cfg.Password,
		DB:       cfg.DB,

		MaxRetries: cfg.MaxRetries,

		DialTimeout:  cfg.DialTimeout,
		ReadTimeout:  cfg.ReadTimeout,
		WriteTimeout: cfg.WriteTimeout,

		PoolSize:    cfg.PoolSize,
		PoolTimeout: cfg.PoolTimeout,
		IdleTimeout: cfg.IdleTimeout,
	}
}

--#

