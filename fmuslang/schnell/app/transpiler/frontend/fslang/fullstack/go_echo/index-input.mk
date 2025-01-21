--% index/fmus
goecho,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/.gitignore)
	.travis.yml,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/.travis.yml)
	Dockerfile,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/Dockerfile)
	go.mod,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/go.mod)
	go.sum,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/go.sum)
	LICENSE,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/LICENSE)
	logo.png,f(b64=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/logo.png)
	main.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/main.go)
	Makefile,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/Makefile)
	readme.md,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/readme.md)
	realworld.db,f(b64=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/realworld.db)
	run.sh,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/run.sh)
	article,d(/mk)
		article.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/article/article.go)
	db,d(/mk)
		db.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/db/db.go)
	docs,d(/mk)
		docs.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/docs/docs.go)
		swagger.json,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/docs/swagger.json)
		swagger.yaml,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/docs/swagger.yaml)
	handler,d(/mk)
		article.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/article.go)
		article_test.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/article_test.go)
		handler.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/handler.go)
		handler_test.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/handler_test.go)
		request.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/request.go)
		response.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/response.go)
		routes.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/routes.go)
		user.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/user.go)
		user_test.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/user_test.go)
	model,d(/mk)
		article.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/model/article.go)
		user.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/model/user.go)
	router,d(/mk)
		router.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/router/router.go)
		validator.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/router/validator.go)
		middleware,d(/mk)
			jwt.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/router/middleware/jwt.go)
	store,d(/mk)
		article.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/store/article.go)
		user.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/store/user.go)
	user,d(/mk)
		user.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/user/user.go)
	utils,d(/mk)
		errors.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/utils/errors.go)
		jwt.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/utils/jwt.go)
		utils.go,f(e=utama=/tmp/hapus/jakartaee/golang-echo-realworld-example-app/utils/utils.go)
--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/.gitignore
# See http://help.github.com/ignore-files/ for more about ignoring files.

# dependencies
/node_modules
/bower_components

# IDEs and editors
/.idea
.project
.classpath
*.launch
.settings/


#System Files
.DS_Store
Thumbs.db

vendor/
*.db
.vscode/

# ignore default binary name generated with Makefile
golang-echo-realworld-example-app

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/.travis.yml
# This is a weird way of telling Travis to use the fast container-based test
# runner instead of the slow VM-based runner.
sudo: false

language: go

env:
  - GO111MODULE=on

# Only the last two Go releases are supported by the Go team with security
# updates. Any older versions be considered deprecated. Don't bother testing
# with them.
go:
  - 1.11.x
  - master

# Only clone the most recent commit.
git:
  depth: 1
# Don't email me the results of the test runs.
#notifications:
#  email: false

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/Dockerfile
#
# 1. Build Container
#
FROM golang:1.12.1 AS build

ENV GO111MODULE=on \
    GOOS=linux \
    GOARCH=amd64

RUN mkdir -p /src

# First add modules list to better utilize caching
COPY go.sum go.mod /src/

WORKDIR /src

# Download dependencies
RUN go mod download

COPY . /src

# Build components.
# Put built binaries and runtime resources in /app dir ready to be copied over or used.
RUN go install -installsuffix cgo -ldflags="-w -s" && \
    mkdir -p /app && \
    cp -r $GOPATH/bin/golang-echo-realworld-example-app /app/

#
# 2. Runtime Container
#
FROM alpine

LABEL maintainer="Sina Saeidi <xesina@gmail.com>"

ENV TZ=Asia/Jakarta \
    PATH="/app:${PATH}"

RUN apk add --update --no-cache \
    sqlite \
    tzdata \
    ca-certificates \
    bash \
    && \
    cp --remove-destination /usr/share/zoneinfo/${TZ} /etc/localtime && \
    echo "${TZ}" > /etc/timezone

# See http://stackoverflow.com/questions/34729748/installed-go-binary-not-found-in-path-on-alpine-linux-docker
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

WORKDIR /app

COPY --from=build /app /app/

EXPOSE 8585

CMD ["./golang-echo-realworld-example-app"]

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/go.mod
module github.com/xesina/golang-echo-realworld-example-app

go 1.12

require (
	github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751
	github.com/dgrijalva/jwt-go v3.2.0+incompatible
	github.com/go-openapi/spec v0.19.7 // indirect
	github.com/go-openapi/swag v0.19.9 // indirect
	github.com/go-playground/locales v0.12.1 // indirect
	github.com/go-playground/universal-translator v0.16.0 // indirect
	github.com/gosimple/slug v1.5.0
	github.com/jinzhu/gorm v1.9.8
	github.com/labstack/echo/v4 v4.1.16
	github.com/labstack/gommon v0.3.1-0.20210908060213-57d86603b883
	github.com/leodido/go-urn v1.1.0 // indirect
	github.com/mailru/easyjson v0.7.1 // indirect
	github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be // indirect
	github.com/stretchr/testify v1.4.0
	github.com/swaggo/echo-swagger v1.0.0
	github.com/swaggo/swag v1.6.5
	golang.org/x/crypto v0.0.0-20200429183012-4b2356b1ed79
	golang.org/x/net v0.0.0-20200501053045-e0ff5e5a1de5 // indirect
	golang.org/x/tools v0.0.0-20200502202811-ed308ab3e770 // indirect
	gopkg.in/go-playground/validator.v9 v9.28.0
	gopkg.in/yaml.v2 v2.2.8 // indirect
)

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/go.sum
cloud.google.com/go v0.26.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
cloud.google.com/go v0.34.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
cloud.google.com/go v0.37.4 h1:glPeL3BQJsbF6aIIYfZizMwc5LTYz250bDMjttbBGAU=
cloud.google.com/go v0.37.4/go.mod h1:NHPJ89PdicEuT9hdPXMROBD91xc5uRDxsMtSB16k7hw=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/KyleBanks/depth v1.2.1 h1:5h8fQADFrWtarTdtDudMmGsC7GPbOAu6RVB3ffsVFHc=
github.com/KyleBanks/depth v1.2.1/go.mod h1:jzSb9d0L43HxTQfT+oSA1EEp2q+ne2uh6XgeJcm8brE=
github.com/PuerkitoBio/purell v1.1.0/go.mod h1:c11w/QuzBsJSee3cPx9rAFu61PvFxuPbtSwDGJws/X0=
github.com/PuerkitoBio/purell v1.1.1 h1:WEQqlqaGbrPkxLJWfBwQmfEAE1Z7ONdDLqrN38tNFfI=
github.com/PuerkitoBio/purell v1.1.1/go.mod h1:c11w/QuzBsJSee3cPx9rAFu61PvFxuPbtSwDGJws/X0=
github.com/PuerkitoBio/urlesc v0.0.0-20170810143723-de5bf2ad4578 h1:d+Bc7a5rLufV/sSk/8dngufqelfh6jnri85riMAaF/M=
github.com/PuerkitoBio/urlesc v0.0.0-20170810143723-de5bf2ad4578/go.mod h1:uGdkoq3SwY9Y+13GIhn11/XLaGBb4BfwItxLd5jeuXE=
github.com/Shopify/sarama v1.19.0/go.mod h1:FVkBWblsNy7DGZRfXLU0O9RCGt5g3g3yEuWXgklEdEo=
github.com/Shopify/toxiproxy v2.1.4+incompatible/go.mod h1:OXgGpZ6Cli1/URJOF1DMxUHB2q5Ap20/P/eIdh4G0pI=
github.com/alecthomas/template v0.0.0-20160405071501-a0175ee3bccc/go.mod h1:LOuyumcjzFXgccqObfd/Ljyb9UuFJ6TxHnclSeseNhc=
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751 h1:JYp7IbQjafoB+tBA3gMyHYHrpOtNuDiK/uB5uXxq5wM=
github.com/alecthomas/template v0.0.0-20190718012654-fb15b899a751/go.mod h1:LOuyumcjzFXgccqObfd/Ljyb9UuFJ6TxHnclSeseNhc=
github.com/alecthomas/units v0.0.0-20151022065526-2efee857e7cf/go.mod h1:ybxpYRFXyAe+OPACYpWeL0wqObRcbAqCMya13uyzqw0=
github.com/apache/thrift v0.12.0/go.mod h1:cp2SuWMxlEZw2r+iP2GNCdIi4C1qmUzdZFSVb+bacwQ=
github.com/beorn7/perks v0.0.0-20180321164747-3a771d992973/go.mod h1:Dwedo/Wpr24TaqPxmxbtue+5NUziq4I4S80YR8gNf3Q=
github.com/client9/misspell v0.3.4/go.mod h1:qj6jICC3Q7zFZvVWo7KLAzC3yx5G7kyvSDkc90ppPyw=
github.com/cpuguy83/go-md2man/v2 v2.0.0-20190314233015-f79a8a8ca69d/go.mod h1:maD7wRr/U5Z6m/iR4s+kqSMx2CaBsrgA7czyZG/E6dU=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/denisenkom/go-mssqldb v0.0.0-20190423183735-731ef375ac02 h1:PS3xfVPa8N84AzoWZHFCbA0+ikz4f4skktfjQoNMsgk=
github.com/denisenkom/go-mssqldb v0.0.0-20190423183735-731ef375ac02/go.mod h1:zAg7JM8CkOJ43xKXIj7eRO9kmWm/TW578qo+oDO6tuM=
github.com/dgrijalva/jwt-go v3.2.0+incompatible h1:7qlOGliEKZXTDg6OTjfoBKDXWrumCAMpl/TFQ4/5kLM=
github.com/dgrijalva/jwt-go v3.2.0+incompatible/go.mod h1:E3ru+11k8xSBh+hMPgOLZmtrrCbhqsmaPHjLKYnJCaQ=
github.com/eapache/go-resiliency v1.1.0/go.mod h1:kFI+JgMyC7bLPUVY133qvEBtVayf5mFgVsvEsIPBvNs=
github.com/eapache/go-xerial-snappy v0.0.0-20180814174437-776d5712da21/go.mod h1:+020luEh2TKB4/GOp8oxxtq0Daoen/Cii55CzbTV6DU=
github.com/eapache/queue v1.1.0/go.mod h1:6eCeP0CKFpHLu8blIFXhExK/dRa7WDZfr6jVFPTqq+I=
github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5 h1:Yzb9+7DPaBjB8zlTR87/ElzFsnQfuHnVUVqpZZIcV5Y=
github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5/go.mod h1:a2zkGnVExMxdzMo3M0Hi/3sEU+cWnZpSni0O6/Yb/P0=
github.com/fsnotify/fsnotify v1.4.7/go.mod h1:jwhsz4b93w/PPRr/qN1Yymfu8t87LnFCMoQvtojpjFo=
github.com/ghodss/yaml v1.0.0/go.mod h1:4dBDuWmgqj2HViK6kFavaiC9ZROes6MMH2rRYeMEF04=
github.com/gin-contrib/gzip v0.0.1/go.mod h1:fGBJBCdt6qCZuCAOwWuFhBB4OOq9EFqlo5dEaFhhu5w=
github.com/gin-contrib/sse v0.0.0-20170109093832-22d885f9ecc7/go.mod h1:VJ0WA2NBN22VlZ2dKZQPAPnyWw5XTlK1KymzLKsr59s=
github.com/gin-contrib/sse v0.0.0-20190301062529-5545eab6dad3/go.mod h1:VJ0WA2NBN22VlZ2dKZQPAPnyWw5XTlK1KymzLKsr59s=
github.com/gin-contrib/sse v0.1.0/go.mod h1:RHrZQHXnP2xjPF+u1gW/2HnVO7nvIa9PG3Gm+fLHvGI=
github.com/gin-gonic/gin v1.3.0/go.mod h1:7cKuhb5qV2ggCFctp2fJQ+ErvciLZrIeoOSOm6mUr7Y=
github.com/gin-gonic/gin v1.4.0/go.mod h1:OW2EZn3DO8Ln9oIKOvM++LBO+5UPHJJDH72/q/3rZdM=
github.com/go-kit/kit v0.8.0/go.mod h1:xBxKIO96dXMWWy0MnWVtmwkA9/13aqxPnvrjFYMA2as=
github.com/go-logfmt/logfmt v0.3.0/go.mod h1:Qt1PoO58o5twSAckw1HlFXLmHsOX5/0LbT9GBnD5lWE=
github.com/go-openapi/jsonpointer v0.17.0/go.mod h1:cOnomiV+CVVwFLk0A/MExoFMjwdsUdVpsRhURCKh+3M=
github.com/go-openapi/jsonpointer v0.19.2/go.mod h1:3akKfEdA7DF1sugOqz1dVQHBcuDBPKZGEoHC/NkiQRg=
github.com/go-openapi/jsonpointer v0.19.3 h1:gihV7YNZK1iK6Tgwwsxo2rJbD1GTbdm72325Bq8FI3w=
github.com/go-openapi/jsonpointer v0.19.3/go.mod h1:Pl9vOtqEWErmShwVjC8pYs9cog34VGT37dQOVbmoatg=
github.com/go-openapi/jsonreference v0.17.0/go.mod h1:g4xxGn04lDIRh0GJb5QlpE3HfopLOL6uZrK/VgnsK9I=
github.com/go-openapi/jsonreference v0.19.0/go.mod h1:g4xxGn04lDIRh0GJb5QlpE3HfopLOL6uZrK/VgnsK9I=
github.com/go-openapi/jsonreference v0.19.2/go.mod h1:jMjeRr2HHw6nAVajTXJ4eiUwohSTlpa0o73RUL1owJc=
github.com/go-openapi/jsonreference v0.19.3 h1:5cxNfTy0UVC3X8JL5ymxzyoUZmo8iZb+jeTWn7tUa8o=
github.com/go-openapi/jsonreference v0.19.3/go.mod h1:rjx6GuL8TTa9VaixXglHmQmIL98+wF9xc8zWvFonSJ8=
github.com/go-openapi/spec v0.19.0/go.mod h1:XkF/MOi14NmjsfZ8VtAKf8pIlbZzyoTvZsdfssdxcBI=
github.com/go-openapi/spec v0.19.4/go.mod h1:FpwSN1ksY1eteniUU7X0N/BgJ7a4WvBFVA8Lj9mJglo=
github.com/go-openapi/spec v0.19.7 h1:0xWSeMd35y5avQAThZR2PkEuqSosoS5t6gDH4L8n11M=
github.com/go-openapi/spec v0.19.7/go.mod h1:Hm2Jr4jv8G1ciIAo+frC/Ft+rR2kQDh8JHKHb3gWUSk=
github.com/go-openapi/swag v0.17.0/go.mod h1:AByQ+nYG6gQg71GINrmuDXCPWdL640yX49/kXLo40Tg=
github.com/go-openapi/swag v0.19.2/go.mod h1:POnQmlKehdgb5mhVOsnJFsivZCEZ/vjK9gh66Z9tfKk=
github.com/go-openapi/swag v0.19.5/go.mod h1:POnQmlKehdgb5mhVOsnJFsivZCEZ/vjK9gh66Z9tfKk=
github.com/go-openapi/swag v0.19.9 h1:1IxuqvBUU3S2Bi4YC7tlP9SJF1gVpCvqN0T2Qof4azE=
github.com/go-openapi/swag v0.19.9/go.mod h1:ao+8BpOPyKdpQz3AOJfbeEVpLmWAvlT1IfTe5McPyhY=
github.com/go-playground/locales v0.12.1 h1:2FITxuFt/xuCNP1Acdhv62OzaCiviiE4kotfhkmOqEc=
github.com/go-playground/locales v0.12.1/go.mod h1:IUMDtCfWo/w/mtMfIE/IG2K+Ey3ygWanZIBtBW0W2TM=
github.com/go-playground/universal-translator v0.16.0 h1:X++omBR/4cE2MNg91AoC3rmGrCjJ8eAeUP/K/EKx4DM=
github.com/go-playground/universal-translator v0.16.0/go.mod h1:1AnU7NaIRDWWzGEKwgtJRd2xk99HeFyHw3yid4rvQIY=
github.com/go-sql-driver/mysql v1.4.1 h1:g24URVg0OFbNUTx9qqY1IRZ9D9z3iPyi5zKhQZpNwpA=
github.com/go-sql-driver/mysql v1.4.1/go.mod h1:zAC/RDZ24gD3HViQzih4MyKcchzm+sOG5ZlKdlhCg5w=
github.com/go-stack/stack v1.8.0/go.mod h1:v0f6uXyyMGvRgIKkXu+yp6POWl0qKG85gN/melR3HDY=
github.com/gogo/protobuf v1.1.1/go.mod h1:r8qH/GZQm5c6nD/R0oafs1akxWv10x8SbQlK7atdtwQ=
github.com/gogo/protobuf v1.2.0/go.mod h1:r8qH/GZQm5c6nD/R0oafs1akxWv10x8SbQlK7atdtwQ=
github.com/golang/glog v0.0.0-20160126235308-23def4e6c14b/go.mod h1:SBH7ygxi8pfUlaOkMMuAQtPIUF8ecWP5IEl/CR7VP2Q=
github.com/golang/mock v1.1.1/go.mod h1:oTYuIxOrZwtPieC+H1uAHpcLFnEyAGVDL/k47Jfbm0A=
github.com/golang/mock v1.2.0/go.mod h1:oTYuIxOrZwtPieC+H1uAHpcLFnEyAGVDL/k47Jfbm0A=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.1/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/snappy v0.0.0-20180518054509-2e65f85255db/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/google/btree v0.0.0-20180813153112-4030bb1f1f0c/go.mod h1:lNA+9X1NB3Zf8V7Ke586lFgjr2dZNuvo3lPJSGZ5JPQ=
github.com/google/go-cmp v0.2.0 h1:+dTQ8DZQJz0Mb/HjFlkptS1FeQ4cWSnN941F8aEG4SQ=
github.com/google/go-cmp v0.2.0/go.mod h1:oXzfMopK8JAjlY9xF4vHSVASa0yLyX7SntLO5aqRK0M=
github.com/google/martian v2.1.0+incompatible/go.mod h1:9I4somxYTbIHy5NJKHRl3wXiIaQGbYVAs8BPL6v8lEs=
github.com/google/pprof v0.0.0-20181206194817-3ea8567a2e57/go.mod h1:zfwlbNMJ+OItoe0UupaVj+oy1omPYYDuagoSzA8v9mc=
github.com/googleapis/gax-go/v2 v2.0.4/go.mod h1:0Wqv26UfaUD9n4G6kQubkQ+KchISgw+vpHVxEJEs9eg=
github.com/gorilla/context v1.1.1/go.mod h1:kBGZzfjB9CEq2AlWe17Uuf7NDRt0dE0s8S51q0aT7Yg=
github.com/gorilla/mux v1.6.2/go.mod h1:1lud6UwP+6orDFRuTfBEV8e9/aOM/c4fVVCaMa2zaAs=
github.com/gosimple/slug v1.5.0 h1:AIIjgCjHcLpX8LzM2NpG4QGW9kUfqv0OLiFRfPv/H3E=
github.com/gosimple/slug v1.5.0/go.mod h1:ER78kgg1Mv0NQGlXiDe57DpCyfbNywXXZ9mIorhxAf0=
github.com/hashicorp/golang-lru v0.5.0/go.mod h1:/m3WP610KZHVQ1SGc6re/UDhFvYD7pJ4Ao+sR/qLZy8=
github.com/hpcloud/tail v1.0.0/go.mod h1:ab1qPbhIpdTxEkNHXyeSf5vhxWSCs/tWer42PpOxQnU=
github.com/jinzhu/gorm v1.9.8 h1:n5uvxqLepIP2R1XF7pudpt9Rv8I3m7G9trGxJVjLZ5k=
github.com/jinzhu/gorm v1.9.8/go.mod h1:bdqTT3q6dhSph2K3pWxrHP6nqxuAp2yQ3KFtc3U3F84=
github.com/jinzhu/inflection v0.0.0-20180308033659-04140366298a h1:eeaG9XMUvRBYXJi4pg1ZKM7nxc5AfXfojeLLW7O5J3k=
github.com/jinzhu/inflection v0.0.0-20180308033659-04140366298a/go.mod h1:h+uFLlag+Qp1Va5pdKtLDYj+kHp5pxUVkryuEj+Srlc=
github.com/jinzhu/now v1.0.0 h1:6WV8LvwPpDhKjo5U9O6b4+xdG/jTXNPwlDme/MTo8Ns=
github.com/jinzhu/now v1.0.0/go.mod h1:oHTiXerJ20+SfYcrdlBO7rzZRJWGwSTQ0iUY2jI6Gfc=
github.com/json-iterator/go v1.1.5/go.mod h1:+SdeFBvtyEkXs7REEP0seUULqWtbJapLOCVDaaPEHmU=
github.com/json-iterator/go v1.1.6/go.mod h1:+SdeFBvtyEkXs7REEP0seUULqWtbJapLOCVDaaPEHmU=
github.com/jstemmer/go-junit-report v0.0.0-20190106144839-af01ea7f8024/go.mod h1:6v2b51hI/fHJwM22ozAgKL4VKDeJcHhJFhtBdhmNjmU=
github.com/julienschmidt/httprouter v1.2.0/go.mod h1:SYymIcj16QtmaHHD7aYtjjsJG7VTCxuUUipMqKk8s4w=
github.com/kisielk/gotool v1.0.0/go.mod h1:XhKaO+MFFWcvkIS/tQcRk01m1F5IRFswLeQ+oQHNcck=
github.com/konsorten/go-windows-terminal-sequences v1.0.1/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/kr/logfmt v0.0.0-20140226030751-b84e30acd515/go.mod h1:+0opPa2QZZtGFBFZlji/RkVcI2GknAs/DXo4wKdlNEc=
github.com/kr/pretty v0.1.0 h1:L/CwN0zerZDmRFUapSPitk6f+Q3+0za1rQkzVuMiMFI=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/pty v1.1.5/go.mod h1:9r2w37qlBe7rQ6e1fg1S/9xpWHSnaqNdHD3WcMdbPDA=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/labstack/echo/v4 v4.0.0/go.mod h1:tZv7nai5buKSg5h/8E6zz4LsD/Dqh9/91Mvs7Z5Zyno=
github.com/labstack/echo/v4 v4.1.16 h1:8swiwjE5Jkai3RPfZoahp8kjVCRNq+y7Q0hPji2Kz0o=
github.com/labstack/echo/v4 v4.1.16/go.mod h1:awO+5TzAjvL8XpibdsfXxPgHr+orhtXZJZIQCVjogKI=
github.com/labstack/gommon v0.2.8/go.mod h1:/tj9csK2iPSBvn+3NLM9e52usepMtrd5ilFYA+wQNJ4=
github.com/labstack/gommon v0.3.0 h1:JEeO0bvc78PKdyHxloTKiF8BD5iGrH8T6MSeGvSgob0=
github.com/labstack/gommon v0.3.0/go.mod h1:MULnywXg0yavhxWKc+lOruYdAhDwPK9wf0OL7NoOu+k=
github.com/labstack/gommon v0.3.1-0.20210908060213-57d86603b883 h1:VsSbAmJM2d4fuBb00XmcSgTjQXrhHhJQ+BiVcn+ovTA=
github.com/labstack/gommon v0.3.1-0.20210908060213-57d86603b883/go.mod h1:8tPUG24r1uHlDFcOdbvEckrNsFOY5PjJraZ+9L1liPU=
github.com/leodido/go-urn v1.1.0 h1:Sm1gr51B1kKyfD2BlRcLSiEkffoG96g6TPv6eRoEiB8=
github.com/leodido/go-urn v1.1.0/go.mod h1:+cyI34gQWZcE1eQU7NVgKkkzdXDQHr1dBMtdAPozLkw=
github.com/lib/pq v1.1.0 h1:/5u4a+KGJptBRqGzPvYQL9p0d/tPR4S31+Tnzj9lEO4=
github.com/lib/pq v1.1.0/go.mod h1:5WUZQaWbwv1U+lTReE5YruASi9Al49XbQIvNi/34Woo=
github.com/mailru/easyjson v0.0.0-20180823135443-60711f1a8329/go.mod h1:C1wdFJiN94OJF2b5HbByQZoLdCWB1Yqtg26g4irojpc=
github.com/mailru/easyjson v0.0.0-20190614124828-94de47d64c63/go.mod h1:C1wdFJiN94OJF2b5HbByQZoLdCWB1Yqtg26g4irojpc=
github.com/mailru/easyjson v0.0.0-20190626092158-b2ccc519800e/go.mod h1:C1wdFJiN94OJF2b5HbByQZoLdCWB1Yqtg26g4irojpc=
github.com/mailru/easyjson v0.7.0/go.mod h1:KAzv3t3aY1NaHWoQz1+4F1ccyAH66Jk7yos7ldAVICs=
github.com/mailru/easyjson v0.7.1 h1:mdxE1MF9o53iCb2Ghj1VfWvh7ZOwHpnVG/xwXrV90U8=
github.com/mailru/easyjson v0.7.1/go.mod h1:KAzv3t3aY1NaHWoQz1+4F1ccyAH66Jk7yos7ldAVICs=
github.com/mattn/go-colorable v0.0.9/go.mod h1:9vuHe8Xs5qXnSaW/c/ABM9alt+Vo+STaOChaDxuIBZU=
github.com/mattn/go-colorable v0.1.0/go.mod h1:9vuHe8Xs5qXnSaW/c/ABM9alt+Vo+STaOChaDxuIBZU=
github.com/mattn/go-colorable v0.1.2/go.mod h1:U0ppj6V5qS13XJ6of8GYAs25YV2eR4EVcfRqFIhoBtE=
github.com/mattn/go-colorable v0.1.6 h1:6Su7aK7lXmJ/U79bYtBjLNaha4Fs1Rg9plHpcH+vvnE=
github.com/mattn/go-colorable v0.1.6/go.mod h1:u6P/XSegPjTcexA+o6vUJrdnUu04hMope9wVRipJSqc=
github.com/mattn/go-isatty v0.0.4/go.mod h1:M+lRXTBqGeGNdLjl/ufCoiOlB5xdOkqRJdNxMWT7Zi4=
github.com/mattn/go-isatty v0.0.7/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.8/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.9/go.mod h1:YNRxwqDuOph6SZLI9vUUz6OYw3QyUt7WiY2yME+cCiQ=
github.com/mattn/go-isatty v0.0.12 h1:wuysRhFDzyxgEmMf5xjvJ2M9dZoWAXNNr5LSBS7uHXY=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-isatty v0.0.14 h1:yVuAays6BHfxijgZPzw+3Zlu5yQgKGP2/hcQbHb7S9Y=
github.com/mattn/go-isatty v0.0.14/go.mod h1:7GGIvUiUoEMVVmxf/4nioHXj79iQHKdU27kJ6hsGG94=
github.com/mattn/go-sqlite3 v1.10.0 h1:jbhqpg7tQe4SupckyijYiy0mJJ/pRyHvXf7JdWK860o=
github.com/mattn/go-sqlite3 v1.10.0/go.mod h1:FPy6KqzDD04eiIsT53CuJW3U88zkxoIYsOqkbpncsNc=
github.com/matttproud/golang_protobuf_extensions v1.0.1/go.mod h1:D8He9yQNgCq6Z5Ld7szi9bcBfOoFv/3dc6xSMkL2PC0=
github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v1.0.1/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/mwitkow/go-conntrack v0.0.0-20161129095857-cc309e4a2223/go.mod h1:qRWi+5nqEBWmkhHvq77mSJWrCKwh8bxhgT7d/eI7P4U=
github.com/onsi/ginkgo v1.6.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/ginkgo v1.7.0/go.mod h1:lLunBs/Ym6LB5Z9jYTR76FiuTmxDTDusOGeTQH+WWjE=
github.com/onsi/gomega v1.4.3/go.mod h1:ex+gbHU/CVuBBDIJjb2X0qEXbFg53c61hWP/1CpauHY=
github.com/openzipkin/zipkin-go v0.1.6/go.mod h1:QgAqvLzwWbR/WpD4A3cGpPtJrZXNIiJc5AZX7/PBEpw=
github.com/pierrec/lz4 v2.0.5+incompatible/go.mod h1:pdkljMzZIN41W+lC3N2tnIh5sFi+IEE17M5jbnwPHcY=
github.com/pkg/errors v0.8.0/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.8.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/prometheus/client_golang v0.9.1/go.mod h1:7SWBe2y4D6OKWSNQJUaRYU/AaXPKyh/dDVn+NZz0KFw=
github.com/prometheus/client_golang v0.9.3-0.20190127221311-3c4408c8b829/go.mod h1:p2iRAGwDERtqlqzRXnrOVns+ignqQo//hLXqYxZYVNs=
github.com/prometheus/client_model v0.0.0-20180712105110-5c3871d89910/go.mod h1:MbSGuTsp3dbXC40dX6PRTWyKYBIrTGTE9sqQNg2J8bo=
github.com/prometheus/client_model v0.0.0-20190115171406-56726106282f/go.mod h1:MbSGuTsp3dbXC40dX6PRTWyKYBIrTGTE9sqQNg2J8bo=
github.com/prometheus/common v0.2.0/go.mod h1:TNfzLD0ON7rHzMJeJkieUDPYmFC7Snx/y86RQel1bk4=
github.com/prometheus/procfs v0.0.0-20181005140218-185b4288413d/go.mod h1:c3At6R/oaqEKCNdg8wHV1ftS6bRYblBhIjjI8uT2IGk=
github.com/prometheus/procfs v0.0.0-20190117184657-bf6a532e95b1/go.mod h1:c3At6R/oaqEKCNdg8wHV1ftS6bRYblBhIjjI8uT2IGk=
github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be h1:ta7tUOvsPHVHGom5hKW5VXNc2xZIkfCKP8iaqOyYtUQ=
github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be/go.mod h1:MIDFMn7db1kT65GmV94GzpX9Qdi7N/pQlwb+AN8wh+Q=
github.com/rcrowley/go-metrics v0.0.0-20181016184325-3113b8401b8a/go.mod h1:bCqnVzQkZxMG4s8nGwiZ5l3QUCyqpo9Y+/ZMZ9VjZe4=
github.com/russross/blackfriday/v2 v2.0.1/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/satori/go.uuid v1.2.0/go.mod h1:dA0hQrYB0VpLJoorglMZABFdXlWrHn1NEOzdhQKdks0=
github.com/shurcooL/sanitized_anchor_name v1.0.0/go.mod h1:1NzhyTcUVG4SuEtjjoZeVRXNmyL/1OwPU0+IJeTBvfc=
github.com/sirupsen/logrus v1.2.0/go.mod h1:LxeOpSwHxABJmUn/MG1IvRgCAasNZTLOkJPxbbu5VWo=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.1.1/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.2.0/go.mod h1:qt09Ya8vawLte6SNmTgCsAVtYtaKzEcn8ATUoHMkEqE=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0 h1:2E4SXV/wtOkTonXsotYi4li6zVWxYlZuYNCXe9XRJyk=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/swaggo/echo-swagger v1.0.0 h1:ppQFt6Am3/MHIUmTpZOwi4gggMZ/W9zmKP4Z9ahTe5c=
github.com/swaggo/echo-swagger v1.0.0/go.mod h1:Vnz3c2TGeFpoZPSV3CkWCrvyfU0016Gq/S0j4JspQnM=
github.com/swaggo/files v0.0.0-20190704085106-630677cd5c14 h1:PyYN9JH5jY9j6av01SpfRMb+1DWg/i3MbGOKPxJ2wjM=
github.com/swaggo/files v0.0.0-20190704085106-630677cd5c14/go.mod h1:gxQT6pBGRuIGunNf/+tSOB5OHvguWi8Tbt82WOkf35E=
github.com/swaggo/gin-swagger v1.2.0 h1:YskZXEiv51fjOMTsXrOetAjrMDfFaXD79PEoQBOe2W0=
github.com/swaggo/gin-swagger v1.2.0/go.mod h1:qlH2+W7zXGZkczuL+r2nEBR2JTT+/lX05Nn6vPhc7OI=
github.com/swaggo/swag v1.5.1/go.mod h1:1Bl9F/ZBpVWh22nY0zmYyASPO1lI/zIwRDrpZU+tv8Y=
github.com/swaggo/swag v1.6.3/go.mod h1:wcc83tB4Mb2aNiL/HP4MFeQdpHUrca+Rp/DRNgWAUio=
github.com/swaggo/swag v1.6.5 h1:2C+t+xyK6p1sujqncYO/VnMvPZcBJjNdKKyxbOdAW8o=
github.com/swaggo/swag v1.6.5/go.mod h1:Y7ZLSS0d0DdxhWGVhQdu+Bu1QhaF5k0RD7FKdiAykeY=
github.com/ugorji/go v1.1.4/go.mod h1:uQMGLiO92mf5W77hV/PUCpI3pbzQx3CRekS0kk+RGrc=
github.com/ugorji/go v1.1.5-pre/go.mod h1:FwP/aQVg39TXzItUBMwnWp9T9gPQnXw4Poh4/oBQZ/0=
github.com/ugorji/go/codec v0.0.0-20181022190402-e5e69e061d4f/go.mod h1:VFNgLljTbGfSG7qAOspJ7OScBnGdDN/yBr0sguwnwf0=
github.com/ugorji/go/codec v1.1.5-pre/go.mod h1:tULtS6Gy1AE1yCENaw4Vb//HLH5njI2tfCQDUqRd8fI=
github.com/urfave/cli v1.20.0/go.mod h1:70zkFmudgCuE/ngEzBv17Jvp/497gISqfk5gWijbERA=
github.com/urfave/cli v1.22.2/go.mod h1:Gos4lmkARVdJ6EkW0WaNv/tZAAMe9V7XWyB60NtXRu0=
github.com/valyala/bytebufferpool v1.0.0 h1:GqA5TC/0021Y/b9FG4Oi9Mr3q7XYx6KllzawFIhcdPw=
github.com/valyala/bytebufferpool v1.0.0/go.mod h1:6bBcMArwyJ5K/AmCkWv1jt77kVWyCJ6HpOuEn7z0Csc=
github.com/valyala/fasttemplate v0.0.0-20170224212429-dcecefd839c4/go.mod h1:50wTf68f99/Zt14pr046Tgt3Lp2vLyFZKzbFXTOabXw=
github.com/valyala/fasttemplate v1.0.1/go.mod h1:UQGH1tvbgY+Nz5t2n7tXsz52dQxojPUpymEIMZ47gx8=
github.com/valyala/fasttemplate v1.1.0 h1:RZqt0yGBsps8NGvLSGW804QQqCUYYLsaOjTVHy1Ocw4=
github.com/valyala/fasttemplate v1.1.0/go.mod h1:UQGH1tvbgY+Nz5t2n7tXsz52dQxojPUpymEIMZ47gx8=
github.com/yuin/goldmark v1.1.27/go.mod h1:3hX8gzYuyVAZsxl0MRgGTJEmQBFcNTphYh9decYSb74=
go.opencensus.io v0.20.1/go.mod h1:6WKK9ahsWS3RSO+PY9ZHZUfv2irvY6gN279GOPZjmmk=
golang.org/x/crypto v0.0.0-20180904163835-0709b304e793/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190130090550-b01c7a725664/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190325154230-a5d413f7728c/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190611184440-5c40567a22f8/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20191011191535-87dc89f01550/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/crypto v0.0.0-20200221231518-2aa609cf4a9d/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200429183012-4b2356b1ed79 h1:IaQbIIB2X/Mp/DKctl6ROxz1KyMlKp4uyvL6+kQ7C88=
golang.org/x/crypto v0.0.0-20200429183012-4b2356b1ed79/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/exp v0.0.0-20190121172915-509febef88a4/go.mod h1:CJ0aWSM057203Lf6IL+f9T1iT9GByDxfZKAQTCR3kQA=
golang.org/x/lint v0.0.0-20181026193005-c67002cb31c3/go.mod h1:UVdnD1Gm6xHRNCYTkRU2/jEulfH38KcIWyp/GAMgvoE=
golang.org/x/lint v0.0.0-20190227174305-5b3e6a55c961/go.mod h1:wehouNa3lNwaWXcvxsM5YxQ5yQlVC4a0KAMCusXpPoU=
golang.org/x/lint v0.0.0-20190301231843-5614ed5bae6f/go.mod h1:UVdnD1Gm6xHRNCYTkRU2/jEulfH38KcIWyp/GAMgvoE=
golang.org/x/mod v0.2.0 h1:KU7oHjnv3XNWfa5COkzUifxZmxp1TyI7ImMXqFxLwvQ=
golang.org/x/mod v0.2.0/go.mod h1:s0Qsj1ACt9ePp/hMypM3fl4fZqREWJwdYDEqhRiZZUA=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180826012351-8a410e7b638d/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180906233101-161cd47e91fd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20181005035420-146acd28ed58/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20181114220301-adae6a3d119a/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20181220203305-927f97764cc3/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190108225652-1e06a53dbb7e/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190125091013-d26f9f9a57f3/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190213061140-3a22650c66bd/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190503192946-f4e77d36d62c/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190611141213-3f473d35a33a/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190613194153-d28f0bde5980/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190620200207-3b0461eec859/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20190827160401-ba9fcec4b297/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20191204025024-5ee1b9f4859a/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200226121028-0de0cce0169b/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200501053045-e0ff5e5a1de5 h1:WQ8q63x+f/zpC8Ac1s9wLElVoHhm32p6tudrU72n1QA=
golang.org/x/net v0.0.0-20200501053045-e0ff5e5a1de5/go.mod h1:qpuaurCH72eLCgpAm/N6yyVIVM9cpaDIP3A8BGJEC5A=
golang.org/x/oauth2 v0.0.0-20180821212333-d2e6202438be/go.mod h1:N/0e6XlmueqKjAGxoOufVs8QHGRruUQn6yWY3a++T0U=
golang.org/x/oauth2 v0.0.0-20190226205417-e64efc72b421/go.mod h1:gOpvHmFTYa4IltrdGE7lF6nIHvwfUNPOp7c8zoXwtLw=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181108010431-42b317875d0f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181221193216-37e7f081c4d4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190227155943-e225da77a7e6/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180830151530-49385e6e1522/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20180905080454-ebe1bf3edb33/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20180909124046-d0be0721c37e/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20181116152217-5ac8a444bdc5/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20181122145206-62eef0e2fa9b/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20181228144115-9a3f9b0469bb/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190129075346-302c3dd5f1cc/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190222072716-a9d3bda3a223/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190610200419-93c9922d18ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190616124812-15dcb6c0061f/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190813064441-fde4db37ae7a/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200223170610-d5e6a3e2c0ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200323222414-85ca7c5b95cd/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200501145240-bc7a7d42d5c3 h1:5B6i6EAiSYyejWfvc5Rc9BbI3rzIsrrXfAQBWnYfn+w=
golang.org/x/sys v0.0.0-20200501145240-bc7a7d42d5c3/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210630005230-0f9fa26af87c h1:F1jZWGFhYfh0Ci55sIpILtKKK8p3i2/krTr0H1rg74I=
golang.org/x/sys v0.0.0-20210630005230-0f9fa26af87c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.1-0.20180807135948-17ff2d5776d2/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.2 h1:tW2bmiBqwgJj/UpqtC8EpXEZVYOwU0yG4iWbprSVAcs=
golang.org/x/text v0.3.2/go.mod h1:bEr9sfX3Q8Zfm5fL9x+3itogRgK3+ptLWKqgva+5dAk=
golang.org/x/time v0.0.0-20181108054448-85acf8d2951c/go.mod h1:tRJNPiyCQ0inRvYxbN9jk5I+vvW/OXSQhTDSoE431IQ=
golang.org/x/tools v0.0.0-20180828015842-6cd1fcedba52/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190114222345-bf090417da8b/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190226205152-f727befe758c/go.mod h1:9Yl7xja0Znq3iFh3HoIrodX9oNMXvdceNzlUR8zjMvY=
golang.org/x/tools v0.0.0-20190312170243-e65039ee4138/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190606050223-4d9ae51c2468/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20190611222205-d73e1c7e250b/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20190614205625-5aca471b1d59/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
golang.org/x/tools v0.0.0-20191119224855-298f0cb1881e/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20191205060818-73c7173a9f7d/go.mod h1:b+2E5dAYhXwXZwtnZ6UAqBI28+e2cm9otk0dWdXHAEo=
golang.org/x/tools v0.0.0-20200502202811-ed308ab3e770 h1:M9Fif0OxNji8w+HvmhVQ8KJtiZOsjU9RgslJGhn95XE=
golang.org/x/tools v0.0.0-20200502202811-ed308ab3e770/go.mod h1:EkVYQZoAsY45+roYkvgYkIh4xh/qjgUK9TdY2XT94GE=
golang.org/x/xerrors v0.0.0-20190717185122-a985d3407aa7/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191011141410-1b5146add898/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/api v0.3.1/go.mod h1:6wY9I6uQWHQ8EM57III9mq/AjF+i8G65rmVagqKMtkk=
google.golang.org/appengine v1.1.0/go.mod h1:EbEs0AVv82hx2wNQdGPgUI5lhzA/G0D9YwlJXL52JkM=
google.golang.org/appengine v1.4.0 h1:/wp5JvzpHIxhs/dumFmF7BXTf3Z+dd4uXta4kVyO508=
google.golang.org/appengine v1.4.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/genproto v0.0.0-20180817151627-c66870c02cf8/go.mod h1:JiN7NxoALGmiZfu7CAH4rXhgtRTLTxftemlI0sWmxmc=
google.golang.org/genproto v0.0.0-20190307195333-5fe7a883aa19/go.mod h1:VzzqZJRnGkLBvHegQrXjBqPurQTc5/KpmUdxsrq26oE=
google.golang.org/genproto v0.0.0-20190404172233-64821d5d2107/go.mod h1:VzzqZJRnGkLBvHegQrXjBqPurQTc5/KpmUdxsrq26oE=
google.golang.org/grpc v1.17.0/go.mod h1:6QZJwpn2B+Zp71q/5VxRsJ6NXXVCE5NRUHRo+f3cWCs=
google.golang.org/grpc v1.19.0/go.mod h1:mqu4LbDTu4XGKhr4mRzUsmM4RtVoemTSY81AxZiDr8c=
gopkg.in/alecthomas/kingpin.v2 v2.2.6/go.mod h1:FMv+mEhP44yOT+4EoQTLFTRgOQ1FBLkstjWtayDeSgw=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127 h1:qIbj1fsPNlZgppZ+VLlY7N33q108Sa+fhmuc+sWQYwY=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/fsnotify.v1 v1.4.7/go.mod h1:Tz8NjZHkW78fSQdbUxIjBTcgA1z1m8ZHf0WmKUhAMys=
gopkg.in/go-playground/assert.v1 v1.2.1 h1:xoYuJVE7KT85PYWrN730RguIQO0ePzVRfFMXadIrXTM=
gopkg.in/go-playground/assert.v1 v1.2.1/go.mod h1:9RXL0bg/zibRAgZUYszZSwO/z8Y/a8bDuhia5mkpMnE=
gopkg.in/go-playground/validator.v8 v8.18.2/go.mod h1:RX2a/7Ha8BgOhfk7j780h4/u/RRjR0eouCJSH80/M2Y=
gopkg.in/go-playground/validator.v9 v9.28.0 h1:6pzvnzx1RWaaQiAmv6e1DvCFULRaz5cKoP5j1VcrLsc=
gopkg.in/go-playground/validator.v9 v9.28.0/go.mod h1:+c9/zcJMFNgbLvly1L1V+PpxWdVbfP1avr/N00E2vyQ=
gopkg.in/tomb.v1 v1.0.0-20141024135613-dd632973f1e7/go.mod h1:dt/ZhP58zS4L8KSrWDmTeBkI65Dw0HsyUHuEVlX15mw=
gopkg.in/yaml.v2 v2.2.1/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.7/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.8 h1:obN1ZagJSUGI0Ek/LBmuj4SNLPfIny3KsKFopxRdj10=
gopkg.in/yaml.v2 v2.2.8/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
honnef.co/go/tools v0.0.0-20180728063816-88497007e858/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190102054323-c2f93a96b099/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=
honnef.co/go/tools v0.0.0-20190106161140-3f1c8253044a/go.mod h1:rf3lG4BRIbNafJWhAfAdb/ePZxsR/4RtNHQocxwk9r4=

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/LICENSE
MIT License

Copyright (c) 2020 Sina Saeidi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/logo.png
iVBORw0KGgoAAAANSUhEUgAABoUAAAEBCAYAAAC+OawFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAABcRAAAXEQHKJvM/AAAAB3RJTUUH4gYKFAUixJ274AAAIABJREFUeNrs3Xt8ZHV9//HXmcAuF2UDioogmRXBG5IsKJgssAleuoTLJrYqCnWz1bZeqoy/qqdVNzmb1dpTqwzeKlYlWxWt2s6CEJBWk6ibeKtJsPVuk6xa8YYbRCCBne/vj+9ZCdk5k0nmnJk5M+/n45EHbObkO+d8zznfOXM+5/v5gIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIhIBXmel1YvJM++ffu88fHxvRMTE9p/IiIiIiIiIiIiItLQHHVBcZ7nNTuOk3EcJwNM5fP5jOd5U+qZ2jY+Pt4DZIGWJb++dmFhwevq6jqgHhIRERERERERERGRRqOgUBG7d+/uMcYsDyzgOM6egwcPZjzPU3Chxuzbt6/NcZwssCVkkXnHcTLt7e1D6i0RERERERERERERaSQKChXgeV5bKpUqFlgAmAe8/v7+rHqs+kZGRprXr1/vAVeX+CdjjuN47e3to+o9EREREREREREREWkECgot4Xlec1NTU9YYs30VfzbtOE5m586do+rB6hgfH88AHrBhDX++Z2FhIaOUciIiIiIiIiIiIiJS7xQUCgwODpYTWAC4Mag3NKverIyJiYlOIGuMaS2zqXnA6+jo0KwvEREREREREREREalbDR8U2r17d6cxZohldYPWaN4Ykx0YGPB0aMVnYmIiHdR62hZx03OO4/QppZyIiIiIiIiIiIiI1KOGDQp5npcO6gZti6H5uSCl3F4dYtEZGRlpXrduXcZxnAxrn9FVihsdx8m0t7fPqtdFREREREREREREpF40XFDI87xmx3EyjuMMVODtxvL5fJ9SypVvfHy8B8gSzYyuUswbY7KLi4tZ1RsSERERERERERERkXrQUEGhwcHBPmzdoJZKvq8xZpcxJut5noILq7Rv3742x3GywJYqrcIckOno6NCsLxERERERERERERFJtIYICgV1gzyqF1gAmAcy/f39QzrsVjYyMtK8fv36LLC9RlZpzBiT2bx585T2joiIiIiIiIiIiIgkUV0HhTzPa25qasoaY7bX0GqN5fP5jOd5Ci6EGB8fz2BndG2owdW7dmFhwVNKORERERERERERERFJmroNCu3atctzHCdDbQYWcBxnz8GDBzNKKfeQiYmJTmPMEBVO77cG847jZNrb24e010REREREREREREQkKVL1tkGe57UNDg7OOo4zQI0GhACMMdtTqdRsUOdIgHw+3wk0J2BVNxhj2rTHRERERERERERERCRJ6jEoNIVNPTZf46s6b4zJ5vP5vToMrc2bN3sLCwtpYE8Nr+Yex3E2dnR0ZLTHRERERERERERERCRJ6jZ9nOd5zY7jeI7j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SZIkSdLcGBQqU7VvgmrvAGR9wDYrZB5qbKtkrN7alQxc3pNMWCGSJEmSJEmSJM3PvlZBE1T7rgf6GR7rh8oQ0GWl7NVkLWH91q5ks1UhSZIkSZIkSdLCuVKomap9o1R7uyFZB0xaIXVNkbBupCvp3rrCgJAkSZIkSZIkSUUxKNQK1ZVDkK0CNgBTVgjk9bBhWUb3yIpkyOqQJEmSJEmSJKlYBoVapdq3k2rvIGTdwKalXBU12JRlrBrpSgY39yQ7fXNIkiRJkiRJklQ89xRqtWrfTmCA4bFBoHtJXXuNbVmNgct7kgnfCJIkSZIkSZIklcugULuo9k0AE0vlcrf0JKNAvzdekiRJkiRJkqTmMH1c+3PPIUmSJEmSJEmStGCJVdDmhseWQ2U9cFrBJW+Iexr9zjHjtf6swjUlXMWZyzLcL0iSJEmSJEmSpBZypVC7q/btjMGbrAfY1GFnf3GW0TPSlaw3ICRJkiRJkiRJUmsZFOoU1b4Jqr0DkK0GtrX1udbYVslYPdKVrL28J5nw5kmSJEmSJEmS1Hr7WgUdpto3CvQzPNYPlSGgq43ObrKWsH5rV7LZGyVJkiRJkiRJUntxpVCnqvaNUu3thmQdMNnis5kiYd1IV9K9dYUBIUmSJEmSJEmS2pFBoU5XXTkE2SpgAzDV5KNPARuWZXSPrEiGvBmSJEmSJEmSJLUvg0KLQbVvJ9XeQci6gU3NOGQNNmUZq0a6ksHNPclOb4IkSZIkSZIkSe3NoNBiEoNDA5D1ABeXcowa27KMnq1dycDlPcmElS5JkiRJkiRJUmcwKLQYVfsmqPauhWw1sK2QMhO2VzJWj3Qn/QaDJEmSJEmSJEnqPAaFFrNq3yjV3n5I1gGT8yxlkoR1IyuSVVt6klErVZIkSZIkSZKkzmRQaCmorhyi2tsNnAxMzfKvpoANI11J98iKZMhKlCRJkiRJkiSpsxkUWkqqvRsh6wY27OWVZy7L6B7pSgatNEmSJEmSJEmSpEVm7Xht+dHjtW5rQpIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkSZIkzcH/B+263MD1tq5DAAAAAElFTkSuQmCC
--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/main.go
package main

import (
	"github.com/xesina/golang-echo-realworld-example-app/db"
	"github.com/xesina/golang-echo-realworld-example-app/handler"
	"github.com/xesina/golang-echo-realworld-example-app/router"
	"github.com/xesina/golang-echo-realworld-example-app/store"

	echoSwagger "github.com/swaggo/echo-swagger"                 // echo-swagger middleware
	_ "github.com/xesina/golang-echo-realworld-example-app/docs" // docs is generated by Swag CLI, you have to import it.
)

// @title Swagger Example API
// @version 1.0
// @description Conduit API
// @title Conduit API

// @host 127.0.0.1:8585
// @BasePath /api

// @schemes http https
// @produce	application/json
// @consumes application/json

// @securityDefinitions.apikey ApiKeyAuth
// @in header
// @name Authorization

func main() {
	r := router.New()

	r.GET("/swagger/*", echoSwagger.WrapHandler)

	v1 := r.Group("/api")

	d := db.New()
	db.AutoMigrate(d)

	us := store.NewUserStore(d)
	as := store.NewArticleStore(d)
	h := handler.NewHandler(us, as)
	h.Register(v1)
	r.Logger.Fatal(r.Start("0.0.0.0:8585"))
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/Makefile
#@IgnoreInspection BashAddShebang
export ROOT=$(realpath $(dir $(lastword $(MAKEFILE_LIST))))
export DEBUG=true
export APP=golang-echo-realworld-example-app
export LDFLAGS="-w -s"

all: build test

build:
	go build -race  .

build-static:
	CGO_ENABLED=0 go build -race -v -o $(APP) -a -installsuffix cgo -ldflags $(LDFLAGS) .

run:
	go run -race .

############################################################
# Test
############################################################

test:
	go test -v -race ./...

container:
	docker build -t echo-realworld .

run-container:
	docker run --rm -it echo-realworld

.PHONY: build run build-static test container

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/readme.md
# ![RealWorld Example App](logo.png)

> ### Golang/Echo codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.

### [Demo](https://github.com/gothinkster/realworld)&nbsp;&nbsp;&nbsp;&nbsp;[RealWorld](https://github.com/gothinkster/realworld)

[![Build Status](https://travis-ci.org/xesina/golang-echo-realworld-example-app.svg?branch=master)](https://travis-ci.org/xesina/golang-echo-realworld-example-app)

This codebase was created to demonstrate a fully fledged fullstack application built with **Golang/Echo** including CRUD operations, authentication, routing, pagination, and more.

## Getting started

### Install Golang (go1.11+)

Please check the official golang installation guide before you start. [Official Documentation](https://golang.org/doc/install)
Also make sure you have installed a go1.11+ version.

### Environment Config

make sure your ~/.*shrc have those variable:

```bash
➜  echo $GOPATH
/Users/xesina/go
➜  echo $GOROOT
/usr/local/go/
➜  echo $PATH
...:/usr/local/go/bin:/Users/xesina/test//bin:/usr/local/go/bin
```

For more info and detailed instructions please check this guide: [Setting GOPATH](https://github.com/golang/go/wiki/SettingGOPATH)

### Clone the repository

Clone this repository:

```bash
➜ git clone https://github.com/xesina/golang-echo-realworld-example-app.git
```

Or simply use the following command which will handle cloning the repo:

```bash
➜ go get -u -v github.com/xesina/golang-echo-realworld-example-app
```

Switch to the repo folder

```bash
➜ cd $GOPATH/src/github.com/xesina/golang-echo-realworld-example-app
```

### Install dependencies

```bash
➜ go mod download
```

### Run

```bash
➜ go run main.go
```

### Build

```bash
➜ go build
```

### Tests

```bash
➜ go test ./...
```

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/realworld.db
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ZHhfdGFnc19kZWxldGVkX2F0IE9OICJ0YWdzIihkZWxldGVkX2F0KSCBJxEHFxUVAYIxdGFibGV0YWdzdGFncxJDUkVBVEUgVEFCTEUgInRhZ3MiICgiaWQiIGludGVnZXIgcHJpbWFyeSBrZXkgYXV0b2luY3JlbWVudCwiY3JlYXRlZF9hdCIgZGF0ZXRpbWUsInVwZGF0ZWRfYXQiIGRhdGV0aW1lLCJkZWxldGVkX2F0IiBkYXRldGltZSwidGFnIiB2YXJjaGFyKDI1NSkgKWsQBxc7HQGBC2luZGV4aWR4X2NvbW1lbnRzX2RlbGV0ZWRfYXRjb21tZW50cxFDUkVBVEUgSU5ERVggaWR4X2NvbW1lbnRzX2RlbGV0ZWRfYXQgT04gImNvbW1lbnRzIihkZWxldGVkX2F0KSCBWw8HFx0dAYMJdGFibGVjb21tZW50c2NvbW1lbnRzEENSRUFURSBUQUJMRSAiY29tbWVudHMiICgiaWQiIGludGVnZXIgcHJpbWFyeSBrZXkgYXV0b2luY3JlbWVudCwiY3JlYXRlZF9hdCIgZGF0ZXRpbWUsInVwZGF0ZWRfYXQiIGRhdGV0aW1lLCJkZWxldGVkX2F0IiBkYXRldGltZSwiYXJ0aWNsZV9pZCIgaW50ZWdlciwidXNlcl9pZCIgaW50ZWdlciwiYm9keSIgdmFyY2hhcigyNTUpICliDgcXLx0BgQVpbmRleHVpeF9hcnRpY2xlc19zbHVnYXJ0aWNsZXMPQ1JFQVRFIFVOSVFVRSBJTkRFWCB1aXhfYXJ0aWNsZXNfc2x1ZyBPTiAiYXJ0aWNsZXMiKCJzbHVnIikgaw0HFzsdAYELaW5kZXhpZHhfYXJ0aWNsZXNfZGVsZXRlZF9hdGFydGljbGVzDkNSRUFURSBJTkRFWCBpZHhfYXJ0aWNsZXNfZGVsZXRlZF9hdCBPTiAiYXJ0aWNsZXMiKGRlbGV0ZWRfYXQpIIIeDAcXHR0BhA90YWJsZWFydGljbGVzYXJ0aWNsZXMNQ1JFQVRFIFRBQkxFICJhcnRpY2xlcyIgKCJpZCIgaW50ZWdlciBwcmltYXJ5IGtleSBhdXRvaW5jcmVtZW50LCJjcmVhdGVkX2F0IiBkYXRldGltZSwidXBkYXRlZF9hdCIgZGF0ZXRpbWUsImRlbGV0ZWRfYXQiIGRhdGV0aW1lLCJzbHVnIiB2YXJjaGFyKDI1NSkgTk9UIE5VTEwsInRpdGxlIiB2YXJjaGFyKDI1NSkgTk9UIE5VTEwsImRlc2NyaXB0aW9uIiB2YXJjaGFyKDI1NSksImJvZHkiIHZhcmNoYXIoMjU1KSwiYXV0aG9yX2lkIiBpbnRlZ2VyICmBDQoHFyUlAYFddGFibGVhcnRpY2xlX3RhZ3NhcnRpY2xlX3RhZ3MLQ1JFQVRFIFRBQkxFICJhcnRpY2xlX3RhZ3MiICgiYXJ0aWNsZV9pZCIgaW50ZWdlciwidGFnX2lkIiBpbnRlZ2VyLCBQUklNQVJZIEtFWSAoImFydGljbGVfaWQiLCJ0YWdfaWQiKSk3CwYXSyUBAGluZGV4c3FsaXRlX2F1dG9pbmRleF9hcnRpY2xlX3RhZ3NfMWFydGljbGVfdGFncwyBFwgHFxsbAYIFdGFibGVmb2xsb3dzZm9sbG93cwlDUkVBVEUgVEFCTEUgImZvbGxvd3MiICgiZm9sbG93ZXJfaWQiIGludCBub3QgbnVsbCwiZm9sbG93aW5nX2lkIiBpbnQgbm90IG51bGwgLCBQUklNQVJZIEtFWSAoImZvbGxvd2VyX2lkIiwiZm9sbG93aW5nX2lkIikpLQkGF0EbAQBpbmRleHNxbGl0ZV9hdXRvaW5kZXhfZm9sbG93c18xZm9sbG93cwpYBwYXKxcBfWluZGV4dWl4X3VzZXJzX2VtYWlsdXNlcnMIQ1JFQVRFIFVOSVFVRSBJTkRFWCB1aXhfdXNlcnNfZW1haWwgT04gInVzZXJzIigiZW1haWwiKSBiBgcXMRcBgQlpbmRleHVpeF91c2Vyc191c2VybmFtZXVzZXJzB0NSRUFURSBVTklRVUUgSU5ERVggdWl4X3VzZXJzX3VzZXJuYW1lIE9OICJ1c2VycyIoInVzZXJuYW1lIikgXgUGFzUXAX9pbmRleGlkeF91c2Vyc19kZWxldGVkX2F0dXNlcnMGQ1JFQVRFIElOREVYIGlkeF91c2Vyc19kZWxldGVkX2F0IE9OICJ1c2VycyIoZGVsZXRlZF9hdCkgUAQGFysrAVl0YWJsZXNxbGl0ZV9zZXF1ZW5jZXNxbGl0ZV9zZXF1ZW5jZQVDUkVBVEUgVEFCTEUgc3FsaXRlX3NlcXVlbmNlKG5hbWUsc2VxKYIfAwcXFxcBhB10YWJsZXVzZXJzdXNlcnMEQ1JFQVRFIFRBQkxFICJ1c2VycyIgKCJpZCIgaW50ZWdlciBwcmltYXJ5IGtleSBhdXRvaW5jcmVtZW50LCJjcmVhdGVkX2F0IiBkYXRldGltZSwidXBkYXRlZF9hdCIgZGF0ZXRpbWUsImRlbGV0ZWRfYXQiIGRhdGV0aW1lLCJ1c2VybmFtZSIgdmFyY2hhcigyNTUpIE5PVCBOVUxMLCJlbWFpbCIgdmFyY2hhcigyNTUpIE5PVCBOVUxMLCJwYXNzd29yZCIgdmFyY2hhcigyNTUpIE5PVCBOVUxMLCJiaW8iIHZhcmNoYXIoMjU1KSwiaW1hZ2UiIHZhcmNoYXIoMjU1KSApgQYBBxcfHwGBW3RhYmxlZmF2b3JpdGVzZmF2b3JpdGVzAkNSRUFURSBUQUJMRSAiZmF2b3JpdGVzIiAoInVzZXJfaWQiIGludGVnZXIsImFydGljbGVfaWQiIGludGVnZXIsIFBSSU1BUlkgS0VZICgidXNlcl9pZCIsImFydGljbGVfaWQiKSkxAgYXRR8BAGluZGV4c3FsaXRlX2F1dG9pbmRleF9mYXZvcml0ZXNfMWZhdm9yaXRlcwMAAAAIAAAAAA0AAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADQAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/run.sh
go mod download
go run main.go

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/article/article.go
package article

import (
	"github.com/xesina/golang-echo-realworld-example-app/model"
)

type Store interface {
	GetBySlug(string) (*model.Article, error)
	GetUserArticleBySlug(userID uint, slug string) (*model.Article, error)
	CreateArticle(*model.Article) error
	UpdateArticle(*model.Article, []string) error
	DeleteArticle(*model.Article) error
	List(offset, limit int) ([]model.Article, int, error)
	ListByTag(tag string, offset, limit int) ([]model.Article, int, error)
	ListByAuthor(username string, offset, limit int) ([]model.Article, int, error)
	ListByWhoFavorited(username string, offset, limit int) ([]model.Article, int, error)
	ListFeed(userID uint, offset, limit int) ([]model.Article, int, error)

	AddComment(*model.Article, *model.Comment) error
	GetCommentsBySlug(string) ([]model.Comment, error)
	GetCommentByID(uint) (*model.Comment, error)
	DeleteComment(*model.Comment) error

	AddFavorite(*model.Article, uint) error
	RemoveFavorite(*model.Article, uint) error
	ListTags() ([]model.Tag, error)
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/db/db.go
package db

import (
	"fmt"

	"os"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"github.com/xesina/golang-echo-realworld-example-app/model"
)

func New() *gorm.DB {
	db, err := gorm.Open("sqlite3", "./realworld.db")
	if err != nil {
		fmt.Println("storage err: ", err)
	}
	db.DB().SetMaxIdleConns(3)
	db.LogMode(true)
	return db
}

func TestDB() *gorm.DB {
	db, err := gorm.Open("sqlite3", "./../realworld_test.db")
	if err != nil {
		fmt.Println("storage err: ", err)
	}
	db.DB().SetMaxIdleConns(3)
	db.LogMode(false)
	return db
}

func DropTestDB() error {
	if err := os.Remove("./../realworld_test.db"); err != nil {
		return err
	}
	return nil
}

//TODO: err check
func AutoMigrate(db *gorm.DB) {
	db.AutoMigrate(
		&model.User{},
		&model.Follow{},
		&model.Article{},
		&model.Comment{},
		&model.Tag{},
	)
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/docs/docs.go
// GENERATED BY THE COMMAND ABOVE; DO NOT EDIT
// This file was generated by swaggo/swag

package docs

import (
	"bytes"
	"encoding/json"
	"strings"

	"github.com/alecthomas/template"
	"github.com/swaggo/swag"
)

var doc = `{
    "schemes": {{ marshal .Schemes }},
    "swagger": "2.0",
    "info": {
        "description": "{{.Description}}",
        "title": "{{.Title}}",
        "contact": {},
        "license": {},
        "version": "{{.Version}}"
    },
    "host": "{{.Host}}",
    "basePath": "{{.BasePath}}",
    "paths": {
        "/articles": {
            "get": {
                "description": "Get most recent articles globally. Use query parameters to filter results. Auth is optional",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Get recent articles globally",
                "operationId": "get-articles",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Filter by tag",
                        "name": "tag",
                        "in": "query"
                    },
                    {
                        "type": "string",
                        "description": "Filter by author (username)",
                        "name": "author",
                        "in": "query"
                    },
                    {
                        "type": "string",
                        "description": "Filter by favorites of a user (username)",
                        "name": "favorited",
                        "in": "query"
                    },
                    {
                        "type": "integer",
                        "description": "Limit number of articles returned (default is 20)",
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "type": "integer",
                        "description": "Offset/skip number of articles (default is 0)",
                        "name": "offset",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.articleListResponse"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Create an article. Auth is require",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Create an article",
                "operationId": "create-article",
                "parameters": [
                    {
                        "description": "Article to create",
                        "name": "article",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.articleCreateRequest"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/feed": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Get most recent articles from users you follow. Use query parameters to limit. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Get recent articles from users you follow",
                "operationId": "feed",
                "parameters": [
                    {
                        "type": "integer",
                        "description": "Limit number of articles returned (default is 20)",
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "type": "integer",
                        "description": "Offset/skip number of articles (default is 0)",
                        "name": "offset",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.articleListResponse"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}": {
            "get": {
                "description": "Get an article. Auth not required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Get an article",
                "operationId": "get-article",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article to get",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "put": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Update an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Update an article",
                "operationId": "update-article",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article to update",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    },
                    {
                        "description": "Article to update",
                        "name": "article",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.articleUpdateRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Delete an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Delete an article",
                "operationId": "delete-article",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article to delete",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "additionalProperties": true
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}/comments": {
            "get": {
                "description": "Get the comments for an article. Auth is optional",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "comment"
                ],
                "summary": "Get the comments for an article",
                "operationId": "get-comments",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to get comments for",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.commentListResponse"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Create a comment for an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "comment"
                ],
                "summary": "Create a comment for an article",
                "operationId": "add-comment",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to create a comment for",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    },
                    {
                        "description": "Comment you want to create",
                        "name": "comment",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.createCommentRequest"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.singleCommentResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}/comments/{id}": {
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Delete a comment for an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "comment"
                ],
                "summary": "Delete a comment for an article",
                "operationId": "delete-comments",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to delete a comment for",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    },
                    {
                        "type": "integer",
                        "description": "ID of the comment you want to delete",
                        "name": "id",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "additionalProperties": true
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}/favorite": {
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Favorite an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "favorite"
                ],
                "summary": "Favorite an article",
                "operationId": "favorite",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to favorite",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Unfavorite an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "favorite"
                ],
                "summary": "Unfavorite an article",
                "operationId": "unfavorite",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to unfavorite",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/profiles/{username}": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Get a profile of a user of the system. Auth is optional",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "profile"
                ],
                "summary": "Get a profile",
                "operationId": "get-profile",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Username of the profile to get",
                        "name": "username",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/profiles/{username}/follow": {
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Follow a user by username",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "follow"
                ],
                "summary": "Follow a user",
                "operationId": "follow",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Username of the profile you want to follow",
                        "name": "username",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.profileResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Unfollow a user by username",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "follow"
                ],
                "summary": "Unfollow a user",
                "operationId": "unfollow",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Username of the profile you want to unfollow",
                        "name": "username",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/tags": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Get tags",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "tag"
                ],
                "summary": "Get tags",
                "operationId": "tags",
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.tagListResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/user": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Gets the currently logged-in user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Get the current user",
                "operationId": "current-user",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "put": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Update user information for current user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Update current user",
                "operationId": "update-user",
                "parameters": [
                    {
                        "description": "User details to update. At least **one** field is required.",
                        "name": "user",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.userUpdateRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/users": {
            "post": {
                "description": "Register a new user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Register a new user",
                "operationId": "sign-up",
                "parameters": [
                    {
                        "description": "User info for registration",
                        "name": "user",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.userRegisterRequest"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/users/login": {
            "post": {
                "description": "Login for existing user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Login for existing user",
                "operationId": "login",
                "parameters": [
                    {
                        "description": "Credentials to use",
                        "name": "user",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.userLoginRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "handler.articleCreateRequest": {
            "type": "object",
            "required": [
                "body",
                "description",
                "title"
            ],
            "properties": {
                "article": {
                    "type": "object",
                    "properties": {
                        "body": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "tagList": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "title": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.articleListResponse": {
            "type": "object",
            "properties": {
                "articles": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/handler.articleResponse"
                    }
                },
                "articlesCount": {
                    "type": "integer"
                }
            }
        },
        "handler.articleResponse": {
            "type": "object",
            "properties": {
                "author": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        },
                        "image": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                },
                "body": {
                    "type": "string"
                },
                "createdAt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "favorited": {
                    "type": "boolean"
                },
                "favoritesCount": {
                    "type": "integer"
                },
                "slug": {
                    "type": "string"
                },
                "tagList": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "title": {
                    "type": "string"
                },
                "updatedAt": {
                    "type": "string"
                }
            }
        },
        "handler.articleUpdateRequest": {
            "type": "object",
            "properties": {
                "article": {
                    "type": "object",
                    "properties": {
                        "body": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "tagList": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "title": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.commentListResponse": {
            "type": "object",
            "properties": {
                "comments": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/handler.commentResponse"
                    }
                }
            }
        },
        "handler.commentResponse": {
            "type": "object",
            "properties": {
                "author": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        },
                        "image": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                },
                "body": {
                    "type": "string"
                },
                "createdAt": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
                "updatedAt": {
                    "type": "string"
                }
            }
        },
        "handler.createCommentRequest": {
            "type": "object",
            "required": [
                "body"
            ],
            "properties": {
                "comment": {
                    "type": "object",
                    "properties": {
                        "body": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.profileResponse": {
            "type": "object",
            "properties": {
                "profile": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        },
                        "image": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.singleArticleResponse": {
            "type": "object",
            "properties": {
                "article": {
                    "type": "object",
                    "$ref": "#/definitions/handler.articleResponse"
                }
            }
        },
        "handler.singleCommentResponse": {
            "type": "object",
            "properties": {
                "comment": {
                    "type": "object",
                    "$ref": "#/definitions/handler.commentResponse"
                }
            }
        },
        "handler.tagListResponse": {
            "type": "object",
            "properties": {
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        },
        "handler.userLoginRequest": {
            "type": "object",
            "required": [
                "email",
                "password"
            ],
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.userRegisterRequest": {
            "type": "object",
            "required": [
                "email",
                "password",
                "username"
            ],
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.userResponse": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "image": {
                            "type": "string"
                        },
                        "token": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.userUpdateRequest": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "image": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "utils.Error": {
            "type": "object",
            "properties": {
                "errors": {
                    "type": "object",
                    "additionalProperties": true
                }
            }
        }
    },
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}`

type swaggerInfo struct {
	Version     string
	Host        string
	BasePath    string
	Schemes     []string
	Title       string
	Description string
}

// SwaggerInfo holds exported Swagger Info so clients can modify it
var SwaggerInfo = swaggerInfo{
	Version:     "1.0",
	Host:        "127.0.0.1:8585",
	BasePath:    "/api",
	Schemes:     []string{"http", "https"},
	Title:       "Conduit API",
	Description: "Conduit API",
}

type s struct{}

func (s *s) ReadDoc() string {
	sInfo := SwaggerInfo
	sInfo.Description = strings.Replace(sInfo.Description, "\n", "\\n", -1)

	t, err := template.New("swagger_info").Funcs(template.FuncMap{
		"marshal": func(v interface{}) string {
			a, _ := json.Marshal(v)
			return string(a)
		},
	}).Parse(doc)
	if err != nil {
		return doc
	}

	var tpl bytes.Buffer
	if err := t.Execute(&tpl, sInfo); err != nil {
		return doc
	}

	return tpl.String()
}

func init() {
	swag.Register(swag.Name, &s{})
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/docs/swagger.json
{
    "schemes": [
        "http",
        "https"
    ],
    "swagger": "2.0",
    "info": {
        "description": "Conduit API",
        "title": "Conduit API",
        "contact": {},
        "license": {},
        "version": "1.0"
    },
    "host": "127.0.0.1:8585",
    "basePath": "/api",
    "paths": {
        "/articles": {
            "get": {
                "description": "Get most recent articles globally. Use query parameters to filter results. Auth is optional",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Get recent articles globally",
                "operationId": "get-articles",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Filter by tag",
                        "name": "tag",
                        "in": "query"
                    },
                    {
                        "type": "string",
                        "description": "Filter by author (username)",
                        "name": "author",
                        "in": "query"
                    },
                    {
                        "type": "string",
                        "description": "Filter by favorites of a user (username)",
                        "name": "favorited",
                        "in": "query"
                    },
                    {
                        "type": "integer",
                        "description": "Limit number of articles returned (default is 20)",
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "type": "integer",
                        "description": "Offset/skip number of articles (default is 0)",
                        "name": "offset",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.articleListResponse"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Create an article. Auth is require",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Create an article",
                "operationId": "create-article",
                "parameters": [
                    {
                        "description": "Article to create",
                        "name": "article",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.articleCreateRequest"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/feed": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Get most recent articles from users you follow. Use query parameters to limit. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Get recent articles from users you follow",
                "operationId": "feed",
                "parameters": [
                    {
                        "type": "integer",
                        "description": "Limit number of articles returned (default is 20)",
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "type": "integer",
                        "description": "Offset/skip number of articles (default is 0)",
                        "name": "offset",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.articleListResponse"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}": {
            "get": {
                "description": "Get an article. Auth not required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Get an article",
                "operationId": "get-article",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article to get",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "put": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Update an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Update an article",
                "operationId": "update-article",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article to update",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    },
                    {
                        "description": "Article to update",
                        "name": "article",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.articleUpdateRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Delete an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "article"
                ],
                "summary": "Delete an article",
                "operationId": "delete-article",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article to delete",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "additionalProperties": true
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}/comments": {
            "get": {
                "description": "Get the comments for an article. Auth is optional",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "comment"
                ],
                "summary": "Get the comments for an article",
                "operationId": "get-comments",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to get comments for",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.commentListResponse"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Create a comment for an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "comment"
                ],
                "summary": "Create a comment for an article",
                "operationId": "add-comment",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to create a comment for",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    },
                    {
                        "description": "Comment you want to create",
                        "name": "comment",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.createCommentRequest"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.singleCommentResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}/comments/{id}": {
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Delete a comment for an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "comment"
                ],
                "summary": "Delete a comment for an article",
                "operationId": "delete-comments",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to delete a comment for",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    },
                    {
                        "type": "integer",
                        "description": "ID of the comment you want to delete",
                        "name": "id",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "object",
                            "additionalProperties": true
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/articles/{slug}/favorite": {
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Favorite an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "favorite"
                ],
                "summary": "Favorite an article",
                "operationId": "favorite",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to favorite",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Unfavorite an article. Auth is required",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "favorite"
                ],
                "summary": "Unfavorite an article",
                "operationId": "unfavorite",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Slug of the article that you want to unfavorite",
                        "name": "slug",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.singleArticleResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/profiles/{username}": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Get a profile of a user of the system. Auth is optional",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "profile"
                ],
                "summary": "Get a profile",
                "operationId": "get-profile",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Username of the profile to get",
                        "name": "username",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/profiles/{username}/follow": {
            "post": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Follow a user by username",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "follow"
                ],
                "summary": "Follow a user",
                "operationId": "follow",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Username of the profile you want to follow",
                        "name": "username",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.profileResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Unfollow a user by username",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "follow"
                ],
                "summary": "Unfollow a user",
                "operationId": "unfollow",
                "parameters": [
                    {
                        "type": "string",
                        "description": "Username of the profile you want to unfollow",
                        "name": "username",
                        "in": "path",
                        "required": true
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/tags": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Get tags",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "tag"
                ],
                "summary": "Get tags",
                "operationId": "tags",
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.tagListResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/user": {
            "get": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Gets the currently logged-in user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Get the current user",
                "operationId": "current-user",
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            },
            "put": {
                "security": [
                    {
                        "ApiKeyAuth": []
                    }
                ],
                "description": "Update user information for current user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Update current user",
                "operationId": "update-user",
                "parameters": [
                    {
                        "description": "User details to update. At least **one** field is required.",
                        "name": "user",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.userUpdateRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/users": {
            "post": {
                "description": "Register a new user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Register a new user",
                "operationId": "sign-up",
                "parameters": [
                    {
                        "description": "User info for registration",
                        "name": "user",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.userRegisterRequest"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        },
        "/users/login": {
            "post": {
                "description": "Login for existing user",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "tags": [
                    "user"
                ],
                "summary": "Login for existing user",
                "operationId": "login",
                "parameters": [
                    {
                        "description": "Credentials to use",
                        "name": "user",
                        "in": "body",
                        "required": true,
                        "schema": {
                            "$ref": "#/definitions/handler.userLoginRequest"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/handler.userResponse"
                        }
                    },
                    "400": {
                        "description": "Bad Request",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "422": {
                        "description": "Unprocessable Entity",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    },
                    "500": {
                        "description": "Internal Server Error",
                        "schema": {
                            "$ref": "#/definitions/utils.Error"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "handler.articleCreateRequest": {
            "type": "object",
            "required": [
                "body",
                "description",
                "title"
            ],
            "properties": {
                "article": {
                    "type": "object",
                    "properties": {
                        "body": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "tagList": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "title": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.articleListResponse": {
            "type": "object",
            "properties": {
                "articles": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/handler.articleResponse"
                    }
                },
                "articlesCount": {
                    "type": "integer"
                }
            }
        },
        "handler.articleResponse": {
            "type": "object",
            "properties": {
                "author": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        },
                        "image": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                },
                "body": {
                    "type": "string"
                },
                "createdAt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "favorited": {
                    "type": "boolean"
                },
                "favoritesCount": {
                    "type": "integer"
                },
                "slug": {
                    "type": "string"
                },
                "tagList": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "title": {
                    "type": "string"
                },
                "updatedAt": {
                    "type": "string"
                }
            }
        },
        "handler.articleUpdateRequest": {
            "type": "object",
            "properties": {
                "article": {
                    "type": "object",
                    "properties": {
                        "body": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "tagList": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "title": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.commentListResponse": {
            "type": "object",
            "properties": {
                "comments": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/handler.commentResponse"
                    }
                }
            }
        },
        "handler.commentResponse": {
            "type": "object",
            "properties": {
                "author": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        },
                        "image": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                },
                "body": {
                    "type": "string"
                },
                "createdAt": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
                "updatedAt": {
                    "type": "string"
                }
            }
        },
        "handler.createCommentRequest": {
            "type": "object",
            "required": [
                "body"
            ],
            "properties": {
                "comment": {
                    "type": "object",
                    "properties": {
                        "body": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.profileResponse": {
            "type": "object",
            "properties": {
                "profile": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        },
                        "image": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.singleArticleResponse": {
            "type": "object",
            "properties": {
                "article": {
                    "type": "object",
                    "$ref": "#/definitions/handler.articleResponse"
                }
            }
        },
        "handler.singleCommentResponse": {
            "type": "object",
            "properties": {
                "comment": {
                    "type": "object",
                    "$ref": "#/definitions/handler.commentResponse"
                }
            }
        },
        "handler.tagListResponse": {
            "type": "object",
            "properties": {
                "tags": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        },
        "handler.userLoginRequest": {
            "type": "object",
            "required": [
                "email",
                "password"
            ],
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.userRegisterRequest": {
            "type": "object",
            "required": [
                "email",
                "password",
                "username"
            ],
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.userResponse": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "image": {
                            "type": "string"
                        },
                        "token": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "handler.userUpdateRequest": {
            "type": "object",
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "bio": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "image": {
                            "type": "string"
                        },
                        "password": {
                            "type": "string"
                        },
                        "username": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "utils.Error": {
            "type": "object",
            "properties": {
                "errors": {
                    "type": "object",
                    "additionalProperties": true
                }
            }
        }
    },
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}
--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/docs/swagger.yaml
basePath: /api
definitions:
  handler.articleCreateRequest:
    properties:
      article:
        properties:
          body:
            type: string
          description:
            type: string
          tagList:
            items:
              type: string
            type: array
          title:
            type: string
        type: object
    required:
    - body
    - description
    - title
    type: object
  handler.articleListResponse:
    properties:
      articles:
        items:
          $ref: '#/definitions/handler.articleResponse'
        type: array
      articlesCount:
        type: integer
    type: object
  handler.articleResponse:
    properties:
      author:
        properties:
          bio:
            type: string
          following:
            type: boolean
          image:
            type: string
          username:
            type: string
        type: object
      body:
        type: string
      createdAt:
        type: string
      description:
        type: string
      favorited:
        type: boolean
      favoritesCount:
        type: integer
      slug:
        type: string
      tagList:
        items:
          type: string
        type: array
      title:
        type: string
      updatedAt:
        type: string
    type: object
  handler.articleUpdateRequest:
    properties:
      article:
        properties:
          body:
            type: string
          description:
            type: string
          tagList:
            items:
              type: string
            type: array
          title:
            type: string
        type: object
    type: object
  handler.commentListResponse:
    properties:
      comments:
        items:
          $ref: '#/definitions/handler.commentResponse'
        type: array
    type: object
  handler.commentResponse:
    properties:
      author:
        properties:
          bio:
            type: string
          following:
            type: boolean
          image:
            type: string
          username:
            type: string
        type: object
      body:
        type: string
      createdAt:
        type: string
      id:
        type: integer
      updatedAt:
        type: string
    type: object
  handler.createCommentRequest:
    properties:
      comment:
        properties:
          body:
            type: string
        type: object
    required:
    - body
    type: object
  handler.profileResponse:
    properties:
      profile:
        properties:
          bio:
            type: string
          following:
            type: boolean
          image:
            type: string
          username:
            type: string
        type: object
    type: object
  handler.singleArticleResponse:
    properties:
      article:
        $ref: '#/definitions/handler.articleResponse'
        type: object
    type: object
  handler.singleCommentResponse:
    properties:
      comment:
        $ref: '#/definitions/handler.commentResponse'
        type: object
    type: object
  handler.tagListResponse:
    properties:
      tags:
        items:
          type: string
        type: array
    type: object
  handler.userLoginRequest:
    properties:
      user:
        properties:
          email:
            type: string
          password:
            type: string
        type: object
    required:
    - email
    - password
    type: object
  handler.userRegisterRequest:
    properties:
      user:
        properties:
          email:
            type: string
          password:
            type: string
          username:
            type: string
        type: object
    required:
    - email
    - password
    - username
    type: object
  handler.userResponse:
    properties:
      user:
        properties:
          bio:
            type: string
          email:
            type: string
          image:
            type: string
          token:
            type: string
          username:
            type: string
        type: object
    type: object
  handler.userUpdateRequest:
    properties:
      user:
        properties:
          bio:
            type: string
          email:
            type: string
          image:
            type: string
          password:
            type: string
          username:
            type: string
        type: object
    type: object
  utils.Error:
    properties:
      errors:
        additionalProperties: true
        type: object
    type: object
host: 127.0.0.1:8585
info:
  contact: {}
  description: Conduit API
  license: {}
  title: Conduit API
  version: "1.0"
paths:
  /articles:
    get:
      consumes:
      - application/json
      description: Get most recent articles globally. Use query parameters to filter
        results. Auth is optional
      operationId: get-articles
      parameters:
      - description: Filter by tag
        in: query
        name: tag
        type: string
      - description: Filter by author (username)
        in: query
        name: author
        type: string
      - description: Filter by favorites of a user (username)
        in: query
        name: favorited
        type: string
      - description: Limit number of articles returned (default is 20)
        in: query
        name: limit
        type: integer
      - description: Offset/skip number of articles (default is 0)
        in: query
        name: offset
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.articleListResponse'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      summary: Get recent articles globally
      tags:
      - article
    post:
      consumes:
      - application/json
      description: Create an article. Auth is require
      operationId: create-article
      parameters:
      - description: Article to create
        in: body
        name: article
        required: true
        schema:
          $ref: '#/definitions/handler.articleCreateRequest'
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/handler.singleArticleResponse'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Create an article
      tags:
      - article
  /articles/{slug}:
    delete:
      consumes:
      - application/json
      description: Delete an article. Auth is required
      operationId: delete-article
      parameters:
      - description: Slug of the article to delete
        in: path
        name: slug
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            additionalProperties: true
            type: object
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Delete an article
      tags:
      - article
    get:
      consumes:
      - application/json
      description: Get an article. Auth not required
      operationId: get-article
      parameters:
      - description: Slug of the article to get
        in: path
        name: slug
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.singleArticleResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      summary: Get an article
      tags:
      - article
    put:
      consumes:
      - application/json
      description: Update an article. Auth is required
      operationId: update-article
      parameters:
      - description: Slug of the article to update
        in: path
        name: slug
        required: true
        type: string
      - description: Article to update
        in: body
        name: article
        required: true
        schema:
          $ref: '#/definitions/handler.articleUpdateRequest'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.singleArticleResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Update an article
      tags:
      - article
  /articles/{slug}/comments:
    get:
      consumes:
      - application/json
      description: Get the comments for an article. Auth is optional
      operationId: get-comments
      parameters:
      - description: Slug of the article that you want to get comments for
        in: path
        name: slug
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.commentListResponse'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      summary: Get the comments for an article
      tags:
      - comment
    post:
      consumes:
      - application/json
      description: Create a comment for an article. Auth is required
      operationId: add-comment
      parameters:
      - description: Slug of the article that you want to create a comment for
        in: path
        name: slug
        required: true
        type: string
      - description: Comment you want to create
        in: body
        name: comment
        required: true
        schema:
          $ref: '#/definitions/handler.createCommentRequest'
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/handler.singleCommentResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Create a comment for an article
      tags:
      - comment
  /articles/{slug}/comments/{id}:
    delete:
      consumes:
      - application/json
      description: Delete a comment for an article. Auth is required
      operationId: delete-comments
      parameters:
      - description: Slug of the article that you want to delete a comment for
        in: path
        name: slug
        required: true
        type: string
      - description: ID of the comment you want to delete
        in: path
        name: id
        required: true
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            additionalProperties: true
            type: object
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Delete a comment for an article
      tags:
      - comment
  /articles/{slug}/favorite:
    delete:
      consumes:
      - application/json
      description: Unfavorite an article. Auth is required
      operationId: unfavorite
      parameters:
      - description: Slug of the article that you want to unfavorite
        in: path
        name: slug
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.singleArticleResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Unfavorite an article
      tags:
      - favorite
    post:
      consumes:
      - application/json
      description: Favorite an article. Auth is required
      operationId: favorite
      parameters:
      - description: Slug of the article that you want to favorite
        in: path
        name: slug
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.singleArticleResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Favorite an article
      tags:
      - favorite
  /articles/feed:
    get:
      consumes:
      - application/json
      description: Get most recent articles from users you follow. Use query parameters
        to limit. Auth is required
      operationId: feed
      parameters:
      - description: Limit number of articles returned (default is 20)
        in: query
        name: limit
        type: integer
      - description: Offset/skip number of articles (default is 0)
        in: query
        name: offset
        type: integer
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.articleListResponse'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Get recent articles from users you follow
      tags:
      - article
  /profiles/{username}:
    get:
      consumes:
      - application/json
      description: Get a profile of a user of the system. Auth is optional
      operationId: get-profile
      parameters:
      - description: Username of the profile to get
        in: path
        name: username
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.userResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Get a profile
      tags:
      - profile
  /profiles/{username}/follow:
    delete:
      consumes:
      - application/json
      description: Unfollow a user by username
      operationId: unfollow
      parameters:
      - description: Username of the profile you want to unfollow
        in: path
        name: username
        required: true
        type: string
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/handler.userResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Unfollow a user
      tags:
      - follow
    post:
      consumes:
      - application/json
      description: Follow a user by username
      operationId: follow
      parameters:
      - description: Username of the profile you want to follow
        in: path
        name: username
        required: true
        type: string
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.profileResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Follow a user
      tags:
      - follow
  /tags:
    get:
      consumes:
      - application/json
      description: Get tags
      operationId: tags
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/handler.tagListResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Get tags
      tags:
      - tag
  /user:
    get:
      consumes:
      - application/json
      description: Gets the currently logged-in user
      operationId: current-user
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.userResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Get the current user
      tags:
      - user
    put:
      consumes:
      - application/json
      description: Update user information for current user
      operationId: update-user
      parameters:
      - description: User details to update. At least **one** field is required.
        in: body
        name: user
        required: true
        schema:
          $ref: '#/definitions/handler.userUpdateRequest'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.userResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      security:
      - ApiKeyAuth: []
      summary: Update current user
      tags:
      - user
  /users:
    post:
      consumes:
      - application/json
      description: Register a new user
      operationId: sign-up
      parameters:
      - description: User info for registration
        in: body
        name: user
        required: true
        schema:
          $ref: '#/definitions/handler.userRegisterRequest'
      produces:
      - application/json
      responses:
        "201":
          description: Created
          schema:
            $ref: '#/definitions/handler.userResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      summary: Register a new user
      tags:
      - user
  /users/login:
    post:
      consumes:
      - application/json
      description: Login for existing user
      operationId: login
      parameters:
      - description: Credentials to use
        in: body
        name: user
        required: true
        schema:
          $ref: '#/definitions/handler.userLoginRequest'
      produces:
      - application/json
      responses:
        "200":
          description: OK
          schema:
            $ref: '#/definitions/handler.userResponse'
        "400":
          description: Bad Request
          schema:
            $ref: '#/definitions/utils.Error'
        "401":
          description: Unauthorized
          schema:
            $ref: '#/definitions/utils.Error'
        "404":
          description: Not Found
          schema:
            $ref: '#/definitions/utils.Error'
        "422":
          description: Unprocessable Entity
          schema:
            $ref: '#/definitions/utils.Error'
        "500":
          description: Internal Server Error
          schema:
            $ref: '#/definitions/utils.Error'
      summary: Login for existing user
      tags:
      - user
schemes:
- http
- https
securityDefinitions:
  ApiKeyAuth:
    in: header
    name: Authorization
    type: apiKey
swagger: "2.0"

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/article.go
package handler

import (
	"errors"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
	"github.com/xesina/golang-echo-realworld-example-app/model"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
)

// GetArticle godoc
// @Summary Get an article
// @Description Get an article. Auth not required
// @ID get-article
// @Tags article
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article to get"
// @Success 200 {object} singleArticleResponse
// @Failure 400 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Router /articles/{slug} [get]
func (h *Handler) GetArticle(c echo.Context) error {
	slug := c.Param("slug")
	a, err := h.articleStore.GetBySlug(slug)

	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if a == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	return c.JSON(http.StatusOK, newArticleResponse(c, a))
}

// Articles godoc
// @Summary Get recent articles globally
// @Description Get most recent articles globally. Use query parameters to filter results. Auth is optional
// @ID get-articles
// @Tags article
// @Accept  json
// @Produce  json
// @Param tag query string false "Filter by tag"
// @Param author query string false "Filter by author (username)"
// @Param favorited query string false "Filter by favorites of a user (username)"
// @Param limit query integer false "Limit number of articles returned (default is 20)"
// @Param offset query integer false "Offset/skip number of articles (default is 0)"
// @Success 200 {object} articleListResponse
// @Failure 500 {object} utils.Error
// @Router /articles [get]
func (h *Handler) Articles(c echo.Context) error {
	var (
		articles []model.Article
		count    int
	)

	tag := c.QueryParam("tag")
	author := c.QueryParam("author")
	favoritedBy := c.QueryParam("favorited")

	offset, err := strconv.Atoi(c.QueryParam("offset"))
	if err != nil {
		offset = 0
	}

	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		limit = 20
	}

	if tag != "" {
		articles, count, err = h.articleStore.ListByTag(tag, offset, limit)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, nil)
		}
	} else if author != "" {
		articles, count, err = h.articleStore.ListByAuthor(author, offset, limit)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, nil)
		}
	} else if favoritedBy != "" {
		articles, count, err = h.articleStore.ListByWhoFavorited(favoritedBy, offset, limit)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, nil)
		}
	} else {
		articles, count, err = h.articleStore.List(offset, limit)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, nil)
		}
	}

	return c.JSON(http.StatusOK, newArticleListResponse(h.userStore, userIDFromToken(c), articles, count))
}

// Feed godoc
// @Summary Get recent articles from users you follow
// @Description Get most recent articles from users you follow. Use query parameters to limit. Auth is required
// @ID feed
// @Tags article
// @Accept  json
// @Produce  json
// @Param limit query integer false "Limit number of articles returned (default is 20)"
// @Param offset query integer false "Offset/skip number of articles (default is 0)"
// @Success 200 {object} articleListResponse
// @Failure 401 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/feed [get]
func (h *Handler) Feed(c echo.Context) error {
	var (
		articles []model.Article
		count    int
	)

	offset, err := strconv.Atoi(c.QueryParam("offset"))
	if err != nil {
		offset = 0
	}

	limit, err := strconv.Atoi(c.QueryParam("limit"))
	if err != nil {
		limit = 20
	}

	articles, count, err = h.articleStore.ListFeed(userIDFromToken(c), offset, limit)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, nil)
	}

	return c.JSON(http.StatusOK, newArticleListResponse(h.userStore, userIDFromToken(c), articles, count))
}

// CreateArticle godoc
// @Summary Create an article
// @Description Create an article. Auth is require
// @ID create-article
// @Tags article
// @Accept  json
// @Produce  json
// @Param article body articleCreateRequest true "Article to create"
// @Success 201 {object} singleArticleResponse
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles [post]
func (h *Handler) CreateArticle(c echo.Context) error {
	var a model.Article

	req := &articleCreateRequest{}
	if err := req.bind(c, &a); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}

	a.AuthorID = userIDFromToken(c)

	err := h.articleStore.CreateArticle(&a)
	if err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}

	return c.JSON(http.StatusCreated, newArticleResponse(c, &a))
}

// UpdateArticle godoc
// @Summary Update an article
// @Description Update an article. Auth is required
// @ID update-article
// @Tags article
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article to update"
// @Param article body articleUpdateRequest true "Article to update"
// @Success 200 {object} singleArticleResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/{slug} [put]
func (h *Handler) UpdateArticle(c echo.Context) error {
	slug := c.Param("slug")

	a, err := h.articleStore.GetUserArticleBySlug(userIDFromToken(c), slug)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if a == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	req := &articleUpdateRequest{}
	req.populate(a)

	if err := req.bind(c, a); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}

	if err = h.articleStore.UpdateArticle(a, req.Article.Tags); err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	return c.JSON(http.StatusOK, newArticleResponse(c, a))
}

// DeleteArticle godoc
// @Summary Delete an article
// @Description Delete an article. Auth is required
// @ID delete-article
// @Tags article
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article to delete"
// @Success 200 {object} map[string]interface{}
// @Failure 401 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/{slug} [delete]
func (h *Handler) DeleteArticle(c echo.Context) error {
	slug := c.Param("slug")

	a, err := h.articleStore.GetUserArticleBySlug(userIDFromToken(c), slug)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if a == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	err = h.articleStore.DeleteArticle(a)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	return c.JSON(http.StatusOK, map[string]interface{}{"result": "ok"})
}

// AddComment godoc
// @Summary Create a comment for an article
// @Description Create a comment for an article. Auth is required
// @ID add-comment
// @Tags comment
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article that you want to create a comment for"
// @Param comment body createCommentRequest true "Comment you want to create"
// @Success 201 {object} singleCommentResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/{slug}/comments [post]
func (h *Handler) AddComment(c echo.Context) error {
	slug := c.Param("slug")

	a, err := h.articleStore.GetBySlug(slug)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if a == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	var cm model.Comment

	req := &createCommentRequest{}
	if err := req.bind(c, &cm); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}

	if err = h.articleStore.AddComment(a, &cm); err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	return c.JSON(http.StatusCreated, newCommentResponse(c, &cm))
}

// GetComments godoc
// @Summary Get the comments for an article
// @Description Get the comments for an article. Auth is optional
// @ID get-comments
// @Tags comment
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article that you want to get comments for"
// @Success 200 {object} commentListResponse
// @Failure 422 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Router /articles/{slug}/comments [get]
func (h *Handler) GetComments(c echo.Context) error {
	slug := c.Param("slug")

	cm, err := h.articleStore.GetCommentsBySlug(slug)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	return c.JSON(http.StatusOK, newCommentListResponse(c, cm))
}

// DeleteComment godoc
// @Summary Delete a comment for an article
// @Description Delete a comment for an article. Auth is required
// @ID delete-comments
// @Tags comment
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article that you want to delete a comment for"
// @Param id path integer true "ID of the comment you want to delete"
// @Success 200 {object} map[string]interface{}
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/{slug}/comments/{id} [delete]
func (h *Handler) DeleteComment(c echo.Context) error {
	id64, err := strconv.ParseUint(c.Param("id"), 10, 32)
	id := uint(id64)

	if err != nil {
		return c.JSON(http.StatusBadRequest, utils.NewError(err))
	}

	cm, err := h.articleStore.GetCommentByID(id)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if cm == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	if cm.UserID != userIDFromToken(c) {
		return c.JSON(http.StatusUnauthorized, utils.NewError(errors.New("unauthorized action")))
	}

	if err := h.articleStore.DeleteComment(cm); err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	return c.JSON(http.StatusOK, map[string]interface{}{"result": "ok"})
}

// Favorite godoc
// @Summary Favorite an article
// @Description Favorite an article. Auth is required
// @ID favorite
// @Tags favorite
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article that you want to favorite"
// @Success 200 {object} singleArticleResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/{slug}/favorite [post]
func (h *Handler) Favorite(c echo.Context) error {
	slug := c.Param("slug")
	a, err := h.articleStore.GetBySlug(slug)

	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if a == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	if err := h.articleStore.AddFavorite(a, userIDFromToken(c)); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}

	return c.JSON(http.StatusOK, newArticleResponse(c, a))
}

// Unfavorite godoc
// @Summary Unfavorite an article
// @Description Unfavorite an article. Auth is required
// @ID unfavorite
// @Tags favorite
// @Accept  json
// @Produce  json
// @Param slug path string true "Slug of the article that you want to unfavorite"
// @Success 200 {object} singleArticleResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /articles/{slug}/favorite [delete]
func (h *Handler) Unfavorite(c echo.Context) error {
	slug := c.Param("slug")

	a, err := h.articleStore.GetBySlug(slug)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}

	if a == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}

	if err := h.articleStore.RemoveFavorite(a, userIDFromToken(c)); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}

	return c.JSON(http.StatusOK, newArticleResponse(c, a))
}

// Tags godoc
// @Summary Get tags
// @Description Get tags
// @ID tags
// @Tags tag
// @Accept  json
// @Produce  json
// @Success 201 {object} tagListResponse
// @Failure 400 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /tags [get]
func (h *Handler) Tags(c echo.Context) error {
	tags, err := h.articleStore.ListTags()
	if err != nil {
		return c.JSON(http.StatusInternalServerError, err)
	}

	return c.JSON(http.StatusOK, newTagListResponse(tags))
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/article_test.go
package handler

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"github.com/xesina/golang-echo-realworld-example-app/router"
	"github.com/xesina/golang-echo-realworld-example-app/router/middleware"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
)

func TestListArticlesCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	e := router.New()
	req := httptest.NewRequest(echo.GET, "/api/articles", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	assert.NoError(t, h.Articles(c))
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var aa articleListResponse
		err := json.Unmarshal(rec.Body.Bytes(), &aa)
		assert.NoError(t, err)
		assert.Equal(t, 2, aa.ArticlesCount)
	}
}

func TestGetArticlesCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	req := httptest.NewRequest(echo.GET, "/api/articles/:slug", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	assert.NoError(t, h.GetArticle(c))
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var a singleArticleResponse
		err := json.Unmarshal(rec.Body.Bytes(), &a)
		assert.NoError(t, err)
		assert.Equal(t, "article1-slug", a.Article.Slug)
		assert.Equal(t, 2, len(a.Article.TagList))
	}
}

func TestCreateArticlesCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	var (
		reqJSON = `{"article":{"title":"article2", "description":"article2", "body":"article2", "tagList":["tag1","tag2"]}}`
	)
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.POST, "/api/articles", strings.NewReader(reqJSON))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	err := jwtMiddleware(func(context echo.Context) error {
		return h.CreateArticle(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusCreated, rec.Code) {
		var a singleArticleResponse
		err := json.Unmarshal(rec.Body.Bytes(), &a)
		assert.NoError(t, err)
		assert.Equal(t, "article2", a.Article.Slug)
		assert.Equal(t, "article2", a.Article.Description)
		assert.Equal(t, "article2", a.Article.Title)
		assert.Equal(t, "user1", a.Article.Author.Username)
		assert.Equal(t, 2, len(a.Article.TagList))
	}
}

func TestUpdateArticlesCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	var (
		reqJSON = `{"article":{"title":"article1 part 2", "tagList":["tag3"]}}`
	)
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.PUT, "/api/articles/:slug", strings.NewReader(reqJSON))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.UpdateArticle(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var a singleArticleResponse
		err := json.Unmarshal(rec.Body.Bytes(), &a)
		assert.NoError(t, err)
		assert.Equal(t, "article1 part 2", a.Article.Title)
		assert.Equal(t, "article1-part-2", a.Article.Slug)
		assert.Equal(t, 1, len(a.Article.TagList))
		assert.Equal(t, "tag3", a.Article.TagList[0])
	}
}

func TestFeedCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.GET, "/api/articles/feed", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	err := jwtMiddleware(func(context echo.Context) error {
		return h.Feed(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var a articleListResponse
		err := json.Unmarshal(rec.Body.Bytes(), &a)
		assert.NoError(t, err)
		assert.Equal(t, 1, len(a.Articles))
		assert.Equal(t, a.ArticlesCount, len(a.Articles))
		assert.Equal(t, "article2 title", a.Articles[0].Title)
		assert.Equal(t, "article2 title", a.Articles[0].Title)
	}
}

func TestDeleteArticleCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.DELETE, "/api/articles/:slug", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.DeleteArticle(c)
	})(c)
	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, rec.Code)
}

func TestGetCommentsCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.GET, "/api/articles/:slug/comments", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(2)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug/comments")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.GetComments(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var cc commentListResponse
		err := json.Unmarshal(rec.Body.Bytes(), &cc)
		assert.NoError(t, err)
		assert.Equal(t, 1, len(cc.Comments))
	}
}

func TestAddCommentCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	var (
		reqJSON = `{"comment":{"body":"article1 comment2 by user2"}}`
	)
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.POST, "/api/articles/:slug/comments", strings.NewReader(reqJSON))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(2)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug/comments")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.AddComment(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusCreated, rec.Code) {
		var c singleCommentResponse
		err := json.Unmarshal(rec.Body.Bytes(), &c)
		assert.NoError(t, err)
		assert.Equal(t, "article1 comment2 by user2", c.Comment.Body)
		assert.Equal(t, "user2", c.Comment.Author.Username)
	}
}

func TestDeleteCommentCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.DELETE, "/api/articles/:slug/comments/:id", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug/comments/:id")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	c.SetParamNames("id")
	c.SetParamValues("1")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.DeleteComment(c)
	})(c)
	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, rec.Code)
}

func TestFavoriteCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.POST, "/api/articles/:slug/favorite", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(2)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug/comments")
	c.SetParamNames("slug")
	c.SetParamValues("article1-slug")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.Favorite(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var a singleArticleResponse
		err := json.Unmarshal(rec.Body.Bytes(), &a)
		assert.NoError(t, err)
		assert.Equal(t, "article1 title", a.Article.Title)
		assert.True(t, a.Article.Favorited)
		assert.Equal(t, 1, a.Article.FavoritesCount)
	}
}

func TestUnfavoriteCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.DELETE, "/api/articles/:slug/favorite", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/articles/:slug/favorite")
	c.SetParamNames("slug")
	c.SetParamValues("article2-slug")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.Unfavorite(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var a singleArticleResponse
		err := json.Unmarshal(rec.Body.Bytes(), &a)
		assert.NoError(t, err)
		assert.Equal(t, "article2 title", a.Article.Title)
		assert.False(t, a.Article.Favorited)
		assert.Equal(t, 0, a.Article.FavoritesCount)
	}
}

func TestGetTagsCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	req := httptest.NewRequest(echo.GET, "/api/tags", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	assert.NoError(t, h.Tags(c))
	if assert.Equal(t, http.StatusOK, rec.Code) {
		var tt tagListResponse
		err := json.Unmarshal(rec.Body.Bytes(), &tt)
		assert.NoError(t, err)
		assert.Equal(t, 2, len(tt.Tags))
		assert.Contains(t, tt.Tags, "tag1")
		assert.Contains(t, tt.Tags, "tag2")
	}
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/handler.go
package handler

import (
	"github.com/xesina/golang-echo-realworld-example-app/article"
	"github.com/xesina/golang-echo-realworld-example-app/user"
)

type Handler struct {
	userStore    user.Store
	articleStore article.Store
}

func NewHandler(us user.Store, as article.Store) *Handler {
	return &Handler{
		userStore:    us,
		articleStore: as,
	}
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/handler_test.go
package handler

import (
	"log"
	"os"
	"testing"

	"encoding/json"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"github.com/labstack/echo/v4"
	"github.com/xesina/golang-echo-realworld-example-app/article"
	"github.com/xesina/golang-echo-realworld-example-app/db"
	"github.com/xesina/golang-echo-realworld-example-app/model"
	"github.com/xesina/golang-echo-realworld-example-app/router"
	"github.com/xesina/golang-echo-realworld-example-app/store"
	"github.com/xesina/golang-echo-realworld-example-app/user"
)

var (
	d  *gorm.DB
	us user.Store
	as article.Store
	h  *Handler
	e  *echo.Echo
)

func TestMain(m *testing.M) {
	setup()
	code := m.Run()
	tearDown()
	os.Exit(code)
}

func authHeader(token string) string {
	return "Token " + token
}

func setup() {
	d = db.TestDB()
	db.AutoMigrate(d)
	us = store.NewUserStore(d)
	as = store.NewArticleStore(d)
	h = NewHandler(us, as)
	e = router.New()
	loadFixtures()
}

func tearDown() {
	_ = d.Close()
	if err := db.DropTestDB(); err != nil {
		log.Fatal(err)
	}
}

func responseMap(b []byte, key string) map[string]interface{} {
	var m map[string]interface{}
	json.Unmarshal(b, &m)
	return m[key].(map[string]interface{})
}

func loadFixtures() error {
	u1bio := "user1 bio"
	u1image := "http://realworld.io/user1.jpg"
	u1 := model.User{
		Username: "user1",
		Email:    "user1@realworld.io",
		Bio:      &u1bio,
		Image:    &u1image,
	}
	u1.Password, _ = u1.HashPassword("secret")
	if err := us.Create(&u1); err != nil {
		return err
	}

	u2bio := "user2 bio"
	u2image := "http://realworld.io/user2.jpg"
	u2 := model.User{
		Username: "user2",
		Email:    "user2@realworld.io",
		Bio:      &u2bio,
		Image:    &u2image,
	}
	u2.Password, _ = u2.HashPassword("secret")
	if err := us.Create(&u2); err != nil {
		return err
	}
	us.AddFollower(&u2, u1.ID)

	a := model.Article{
		Slug:        "article1-slug",
		Title:       "article1 title",
		Description: "article1 description",
		Body:        "article1 body",
		AuthorID:    1,
		Tags: []model.Tag{
			{
				Tag: "tag1",
			},
			{
				Tag: "tag2",
			},
		},
	}
	as.CreateArticle(&a)
	as.AddComment(&a, &model.Comment{
		Body:      "article1 comment1",
		ArticleID: 1,
		UserID:    1,
	})

	a2 := model.Article{
		Slug:        "article2-slug",
		Title:       "article2 title",
		Description: "article2 description",
		Body:        "article2 body",
		AuthorID:    2,
		Favorites: []model.User{
			u1,
		},
		Tags: []model.Tag{
			{
				Tag: "tag1",
			},
		},
	}
	as.CreateArticle(&a2)
	as.AddComment(&a2, &model.Comment{
		Body:      "article2 comment1 by user1",
		ArticleID: 2,
		UserID:    1,
	})
	as.AddFavorite(&a2, 1)

	return nil
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/request.go
package handler

import (
	"github.com/gosimple/slug"
	"github.com/labstack/echo/v4"
	"github.com/xesina/golang-echo-realworld-example-app/model"
)

type userUpdateRequest struct {
	User struct {
		Username string `json:"username"`
		Email    string `json:"email" validate:"email"`
		Password string `json:"password"`
		Bio      string `json:"bio"`
		Image    string `json:"image"`
	} `json:"user"`
}

func newUserUpdateRequest() *userUpdateRequest {
	return new(userUpdateRequest)
}

func (r *userUpdateRequest) populate(u *model.User) {
	r.User.Username = u.Username
	r.User.Email = u.Email
	r.User.Password = u.Password
	if u.Bio != nil {
		r.User.Bio = *u.Bio
	}
	if u.Image != nil {
		r.User.Image = *u.Image
	}
}

func (r *userUpdateRequest) bind(c echo.Context, u *model.User) error {
	if err := c.Bind(r); err != nil {
		return err
	}
	if err := c.Validate(r); err != nil {
		return err
	}
	u.Username = r.User.Username
	u.Email = r.User.Email
	if r.User.Password != u.Password {
		h, err := u.HashPassword(r.User.Password)
		if err != nil {
			return err
		}
		u.Password = h
	}
	u.Bio = &r.User.Bio
	u.Image = &r.User.Image
	return nil
}

type userRegisterRequest struct {
	User struct {
		Username string `json:"username" validate:"required"`
		Email    string `json:"email" validate:"required,email"`
		Password string `json:"password" validate:"required"`
	} `json:"user"`
}

func (r *userRegisterRequest) bind(c echo.Context, u *model.User) error {
	if err := c.Bind(r); err != nil {
		return err
	}
	if err := c.Validate(r); err != nil {
		return err
	}
	u.Username = r.User.Username
	u.Email = r.User.Email
	h, err := u.HashPassword(r.User.Password)
	if err != nil {
		return err
	}
	u.Password = h
	return nil
}

type userLoginRequest struct {
	User struct {
		Email    string `json:"email" validate:"required,email"`
		Password string `json:"password" validate:"required"`
	} `json:"user"`
}

func (r *userLoginRequest) bind(c echo.Context) error {
	if err := c.Bind(r); err != nil {
		return err
	}
	if err := c.Validate(r); err != nil {
		return err
	}
	return nil
}

type articleCreateRequest struct {
	Article struct {
		Title       string   `json:"title" validate:"required"`
		Description string   `json:"description" validate:"required"`
		Body        string   `json:"body" validate:"required"`
		Tags        []string `json:"tagList, omitempty"`
	} `json:"article"`
}

func (r *articleCreateRequest) bind(c echo.Context, a *model.Article) error {
	if err := c.Bind(r); err != nil {
		return err
	}
	if err := c.Validate(r); err != nil {
		return err
	}
	a.Title = r.Article.Title
	a.Slug = slug.Make(r.Article.Title)
	a.Description = r.Article.Description
	a.Body = r.Article.Body
	if r.Article.Tags != nil {
		for _, t := range r.Article.Tags {
			a.Tags = append(a.Tags, model.Tag{Tag: t})
		}
	}
	return nil
}

type articleUpdateRequest struct {
	Article struct {
		Title       string   `json:"title"`
		Description string   `json:"description"`
		Body        string   `json:"body"`
		Tags        []string `json:"tagList"`
	} `json:"article"`
}

func (r *articleUpdateRequest) populate(a *model.Article) {
	r.Article.Title = a.Title
	r.Article.Description = a.Description
	r.Article.Body = a.Body
}

func (r *articleUpdateRequest) bind(c echo.Context, a *model.Article) error {
	if err := c.Bind(r); err != nil {
		return err
	}
	if err := c.Validate(r); err != nil {
		return err
	}
	a.Title = r.Article.Title
	a.Slug = slug.Make(a.Title)
	a.Description = r.Article.Description
	a.Body = r.Article.Body
	return nil
}

type createCommentRequest struct {
	Comment struct {
		Body string `json:"body" validate:"required"`
	} `json:"comment"`
}

func (r *createCommentRequest) bind(c echo.Context, cm *model.Comment) error {
	if err := c.Bind(r); err != nil {
		return err
	}
	if err := c.Validate(r); err != nil {
		return err
	}
	cm.Body = r.Comment.Body
	cm.UserID = userIDFromToken(c)
	return nil
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/response.go
package handler

import (
	"time"

	"github.com/xesina/golang-echo-realworld-example-app/model"
	"github.com/xesina/golang-echo-realworld-example-app/user"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
	"github.com/labstack/echo/v4"
)

type userResponse struct {
	User struct {
		Username string  `json:"username"`
		Email    string  `json:"email"`
		Bio      *string `json:"bio"`
		Image    *string `json:"image"`
		Token    string  `json:"token"`
	} `json:"user"`
}

func newUserResponse(u *model.User) *userResponse {
	r := new(userResponse)
	r.User.Username = u.Username
	r.User.Email = u.Email
	r.User.Bio = u.Bio
	r.User.Image = u.Image
	r.User.Token = utils.GenerateJWT(u.ID)
	return r
}

type profileResponse struct {
	Profile struct {
		Username  string  `json:"username"`
		Bio       *string `json:"bio"`
		Image     *string `json:"image"`
		Following bool    `json:"following"`
	} `json:"profile"`
}

func newProfileResponse(us user.Store, userID uint, u *model.User) *profileResponse {
	r := new(profileResponse)
	r.Profile.Username = u.Username
	r.Profile.Bio = u.Bio
	r.Profile.Image = u.Image
	r.Profile.Following, _ = us.IsFollower(u.ID, userID)
	return r
}

type articleResponse struct {
	Slug           string    `json:"slug"`
	Title          string    `json:"title"`
	Description    string    `json:"description"`
	Body           string    `json:"body"`
	TagList        []string  `json:"tagList"`
	CreatedAt      time.Time `json:"createdAt"`
	UpdatedAt      time.Time `json:"updatedAt"`
	Favorited      bool      `json:"favorited"`
	FavoritesCount int       `json:"favoritesCount"`
	Author         struct {
		Username  string  `json:"username"`
		Bio       *string `json:"bio"`
		Image     *string `json:"image"`
		Following bool    `json:"following"`
	} `json:"author"`
}

type singleArticleResponse struct {
	Article *articleResponse `json:"article"`
}

type articleListResponse struct {
	Articles      []*articleResponse `json:"articles"`
	ArticlesCount int                `json:"articlesCount"`
}

func newArticleResponse(c echo.Context, a *model.Article) *singleArticleResponse {
	ar := new(articleResponse)
	ar.TagList = make([]string, 0)
	ar.Slug = a.Slug
	ar.Title = a.Title
	ar.Description = a.Description
	ar.Body = a.Body
	ar.CreatedAt = a.CreatedAt
	ar.UpdatedAt = a.UpdatedAt
	for _, t := range a.Tags {
		ar.TagList = append(ar.TagList, t.Tag)
	}
	for _, u := range a.Favorites {
		if u.ID == userIDFromToken(c) {
			ar.Favorited = true
		}
	}
	ar.FavoritesCount = len(a.Favorites)
	ar.Author.Username = a.Author.Username
	ar.Author.Image = a.Author.Image
	ar.Author.Bio = a.Author.Bio
	ar.Author.Following = a.Author.FollowedBy(userIDFromToken(c))
	return &singleArticleResponse{ar}
}

func newArticleListResponse(us user.Store, userID uint, articles []model.Article, count int) *articleListResponse {
	r := new(articleListResponse)
	r.Articles = make([]*articleResponse, 0)
	for _, a := range articles {
		ar := new(articleResponse)
		ar.TagList = make([]string, 0)
		ar.Slug = a.Slug
		ar.Title = a.Title
		ar.Description = a.Description
		ar.Body = a.Body
		ar.CreatedAt = a.CreatedAt
		ar.UpdatedAt = a.UpdatedAt
		for _, t := range a.Tags {
			ar.TagList = append(ar.TagList, t.Tag)
		}
		for _, u := range a.Favorites {
			if u.ID == userID {
				ar.Favorited = true
			}
		}
		ar.FavoritesCount = len(a.Favorites)
		ar.Author.Username = a.Author.Username
		ar.Author.Image = a.Author.Image
		ar.Author.Bio = a.Author.Bio
		ar.Author.Following, _ = us.IsFollower(a.AuthorID, userID)
		r.Articles = append(r.Articles, ar)
	}
	r.ArticlesCount = count
	return r
}

type commentResponse struct {
	ID        uint      `json:"id"`
	Body      string    `json:"body"`
	CreatedAt time.Time `json:"createdAt"`
	UpdatedAt time.Time `json:"updatedAt"`
	Author    struct {
		Username  string  `json:"username"`
		Bio       *string `json:"bio"`
		Image     *string `json:"image"`
		Following bool    `json:"following"`
	} `json:"author"`
}

type singleCommentResponse struct {
	Comment *commentResponse `json:"comment"`
}

type commentListResponse struct {
	Comments []commentResponse `json:"comments"`
}

func newCommentResponse(c echo.Context, cm *model.Comment) *singleCommentResponse {
	comment := new(commentResponse)
	comment.ID = cm.ID
	comment.Body = cm.Body
	comment.CreatedAt = cm.CreatedAt
	comment.UpdatedAt = cm.UpdatedAt
	comment.Author.Username = cm.User.Username
	comment.Author.Image = cm.User.Image
	comment.Author.Bio = cm.User.Bio
	comment.Author.Following = cm.User.FollowedBy(userIDFromToken(c))
	return &singleCommentResponse{comment}
}

func newCommentListResponse(c echo.Context, comments []model.Comment) *commentListResponse {
	r := new(commentListResponse)
	cr := commentResponse{}
	r.Comments = make([]commentResponse, 0)
	for _, i := range comments {
		cr.ID = i.ID
		cr.Body = i.Body
		cr.CreatedAt = i.CreatedAt
		cr.UpdatedAt = i.UpdatedAt
		cr.Author.Username = i.User.Username
		cr.Author.Image = i.User.Image
		cr.Author.Bio = i.User.Bio
		cr.Author.Following = i.User.FollowedBy(userIDFromToken(c))

		r.Comments = append(r.Comments, cr)
	}
	return r
}

type tagListResponse struct {
	Tags []string `json:"tags"`
}

func newTagListResponse(tags []model.Tag) *tagListResponse {
	r := new(tagListResponse)
	for _, t := range tags {
		r.Tags = append(r.Tags, t.Tag)
	}
	return r
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/routes.go
package handler

import (
	"github.com/labstack/echo/v4"
	"github.com/xesina/golang-echo-realworld-example-app/router/middleware"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
)

func (h *Handler) Register(v1 *echo.Group) {
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	guestUsers := v1.Group("/users")
	guestUsers.POST("", h.SignUp)
	guestUsers.POST("/login", h.Login)

	user := v1.Group("/user", jwtMiddleware)
	user.GET("", h.CurrentUser)
	user.PUT("", h.UpdateUser)

	profiles := v1.Group("/profiles", jwtMiddleware)
	profiles.GET("/:username", h.GetProfile)
	profiles.POST("/:username/follow", h.Follow)
	profiles.DELETE("/:username/follow", h.Unfollow)

	articles := v1.Group("/articles", middleware.JWTWithConfig(
		middleware.JWTConfig{
			Skipper: func(c echo.Context) bool {
				if c.Request().Method == "GET" && c.Path() != "/api/articles/feed" {
					return true
				}
				return false
			},
			SigningKey: utils.JWTSecret,
		},
	))
	articles.POST("", h.CreateArticle)
	articles.GET("/feed", h.Feed)
	articles.PUT("/:slug", h.UpdateArticle)
	articles.DELETE("/:slug", h.DeleteArticle)
	articles.POST("/:slug/comments", h.AddComment)
	articles.DELETE("/:slug/comments/:id", h.DeleteComment)
	articles.POST("/:slug/favorite", h.Favorite)
	articles.DELETE("/:slug/favorite", h.Unfavorite)
	articles.GET("", h.Articles)
	articles.GET("/:slug", h.GetArticle)
	articles.GET("/:slug/comments", h.GetComments)

	tags := v1.Group("/tags")
	tags.GET("", h.Tags)
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/user.go
package handler

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/xesina/golang-echo-realworld-example-app/model"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
)

// SignUp godoc
// @Summary Register a new user
// @Description Register a new user
// @ID sign-up
// @Tags user
// @Accept  json
// @Produce  json
// @Param user body userRegisterRequest true "User info for registration"
// @Success 201 {object} userResponse
// @Failure 400 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Router /users [post]
func (h *Handler) SignUp(c echo.Context) error {
	var u model.User
	req := &userRegisterRequest{}
	if err := req.bind(c, &u); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	if err := h.userStore.Create(&u); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	return c.JSON(http.StatusCreated, newUserResponse(&u))
}

// Login godoc
// @Summary Login for existing user
// @Description Login for existing user
// @ID login
// @Tags user
// @Accept  json
// @Produce  json
// @Param user body userLoginRequest true "Credentials to use"
// @Success 200 {object} userResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Router /users/login [post]
func (h *Handler) Login(c echo.Context) error {
	req := &userLoginRequest{}
	if err := req.bind(c); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	u, err := h.userStore.GetByEmail(req.User.Email)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}
	if u == nil {
		return c.JSON(http.StatusForbidden, utils.AccessForbidden())
	}
	if !u.CheckPassword(req.User.Password) {
		return c.JSON(http.StatusForbidden, utils.AccessForbidden())
	}
	return c.JSON(http.StatusOK, newUserResponse(u))
}

// CurrentUser godoc
// @Summary Get the current user
// @Description Gets the currently logged-in user
// @ID current-user
// @Tags user
// @Accept  json
// @Produce  json
// @Success 200 {object} userResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /user [get]
func (h *Handler) CurrentUser(c echo.Context) error {
	u, err := h.userStore.GetByID(userIDFromToken(c))
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}
	if u == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}
	return c.JSON(http.StatusOK, newUserResponse(u))
}

// UpdateUser godoc
// @Summary Update current user
// @Description Update user information for current user
// @ID update-user
// @Tags user
// @Accept  json
// @Produce  json
// @Param user body userUpdateRequest true "User details to update. At least **one** field is required."
// @Success 200 {object} userResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /user [put]
func (h *Handler) UpdateUser(c echo.Context) error {
	u, err := h.userStore.GetByID(userIDFromToken(c))
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}
	if u == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}
	req := newUserUpdateRequest()
	req.populate(u)
	if err := req.bind(c, u); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	if err := h.userStore.Update(u); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	return c.JSON(http.StatusOK, newUserResponse(u))
}

// GetProfile godoc
// @Summary Get a profile
// @Description Get a profile of a user of the system. Auth is optional
// @ID get-profile
// @Tags profile
// @Accept  json
// @Produce  json
// @Param username path string true "Username of the profile to get"
// @Success 200 {object} userResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /profiles/{username} [get]
func (h *Handler) GetProfile(c echo.Context) error {
	username := c.Param("username")
	u, err := h.userStore.GetByUsername(username)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}
	if u == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}
	return c.JSON(http.StatusOK, newProfileResponse(h.userStore, userIDFromToken(c), u))
}

// Follow godoc
// @Summary Follow a user
// @Description Follow a user by username
// @ID follow
// @Tags follow
// @Accept  json
// @Produce  json
// @Param username path string true "Username of the profile you want to follow"
// @Success 200 {object} profileResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /profiles/{username}/follow [post]
func (h *Handler) Follow(c echo.Context) error {
	followerID := userIDFromToken(c)
	username := c.Param("username")
	u, err := h.userStore.GetByUsername(username)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}
	if u == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}
	if err := h.userStore.AddFollower(u, followerID); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	return c.JSON(http.StatusOK, newProfileResponse(h.userStore, userIDFromToken(c), u))
}

// Unfollow godoc
// @Summary Unfollow a user
// @Description Unfollow a user by username
// @ID unfollow
// @Tags follow
// @Accept  json
// @Produce  json
// @Param username path string true "Username of the profile you want to unfollow"
// @Success 201 {object} userResponse
// @Failure 400 {object} utils.Error
// @Failure 401 {object} utils.Error
// @Failure 422 {object} utils.Error
// @Failure 404 {object} utils.Error
// @Failure 500 {object} utils.Error
// @Security ApiKeyAuth
// @Router /profiles/{username}/follow [delete]
func (h *Handler) Unfollow(c echo.Context) error {
	followerID := userIDFromToken(c)
	username := c.Param("username")
	u, err := h.userStore.GetByUsername(username)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, utils.NewError(err))
	}
	if u == nil {
		return c.JSON(http.StatusNotFound, utils.NotFound())
	}
	if err := h.userStore.RemoveFollower(u, followerID); err != nil {
		return c.JSON(http.StatusUnprocessableEntity, utils.NewError(err))
	}
	return c.JSON(http.StatusOK, newProfileResponse(h.userStore, userIDFromToken(c), u))
}

func userIDFromToken(c echo.Context) uint {
	id, ok := c.Get("user").(uint)
	if !ok {
		return 0
	}
	return id
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/handler/user_test.go
package handler

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"github.com/xesina/golang-echo-realworld-example-app/router/middleware"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
)

func TestSignUpCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	var (
		reqJSON = `{"user":{"username":"alice","email":"alice@realworld.io","password":"secret"}}`
	)
	req := httptest.NewRequest(echo.POST, "/api/users", strings.NewReader(reqJSON))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	assert.NoError(t, h.SignUp(c))
	if assert.Equal(t, http.StatusCreated, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "user")
		assert.Equal(t, "alice", m["username"])
		assert.Equal(t, "alice@realworld.io", m["email"])
		assert.Nil(t, m["bio"])
		assert.Nil(t, m["image"])
		assert.NotEmpty(t, m["token"])
	}
}

func TestLoginCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	var (
		reqJSON = `{"user":{"email":"user1@realworld.io","password":"secret"}}`
	)
	req := httptest.NewRequest(echo.POST, "/api/users/login", strings.NewReader(reqJSON))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	assert.NoError(t, h.Login(c))
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "user")
		assert.Equal(t, "user1", m["username"])
		assert.Equal(t, "user1@realworld.io", m["email"])
		assert.NotEmpty(t, m["token"])
	}
}

func TestLoginCaseFailed(t *testing.T) {
	tearDown()
	setup()
	var (
		reqJSON = `{"user":{"email":"userx@realworld.io","password":"secret"}}`
	)
	req := httptest.NewRequest(echo.POST, "/api/users/login", strings.NewReader(reqJSON))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	assert.NoError(t, h.Login(c))
	assert.Equal(t, http.StatusForbidden, rec.Code)
}

func TestCurrentUserCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.GET, "/api/users/login", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	err := jwtMiddleware(func(context echo.Context) error {
		return h.CurrentUser(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "user")
		assert.Equal(t, "user1", m["username"])
		assert.Equal(t, "user1@realworld.io", m["email"])
		assert.NotEmpty(t, m["token"])
	}
}

func TestCurrentUserCaseInvalid(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.GET, "/api/users/login", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(100)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	err := jwtMiddleware(func(context echo.Context) error {
		return h.CurrentUser(c)
	})(c)
	assert.NoError(t, err)
	assert.Equal(t, http.StatusNotFound, rec.Code)
}

func TestUpdateUserEmail(t *testing.T) {
	tearDown()
	setup()
	var (
		user1UpdateReq = `{"user":{"email":"user1@user1.me"}}`
	)
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.PUT, "/api/user", strings.NewReader(user1UpdateReq))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	err := jwtMiddleware(func(context echo.Context) error {
		return h.UpdateUser(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "user")
		assert.Equal(t, "user1", m["username"])
		assert.Equal(t, "user1@user1.me", m["email"])
		assert.NotEmpty(t, m["token"])
	}
}

func TestUpdateUserMultipleFields(t *testing.T) {
	tearDown()
	setup()
	var (
		user1UpdateReq = `{"user":{"username":"user11","email":"user11@user11.me","bio":"user11 bio"}}`
	)
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.PUT, "/api/user", strings.NewReader(user1UpdateReq))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	err := jwtMiddleware(func(context echo.Context) error {
		return h.UpdateUser(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "user")
		assert.Equal(t, "user11", m["username"])
		assert.Equal(t, "user11@user11.me", m["email"])
		assert.Equal(t, "user11 bio", m["bio"])
		assert.NotEmpty(t, m["token"])
	}
}

func TestGetProfileCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.GET, "/api/profiles/:username", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/profiles/:username")
	c.SetParamNames("username")
	c.SetParamValues("user1")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.GetProfile(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "profile")
		assert.Equal(t, "user1", m["username"])
		assert.Equal(t, "user1 bio", m["bio"])
		assert.Equal(t, "http://realworld.io/user1.jpg", m["image"])
		assert.Equal(t, false, m["following"])
	}
}

func TestGetProfileCaseNotFound(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.GET, "/api/profiles/:username", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/profiles/:username")
	c.SetParamNames("username")
	c.SetParamValues("userx")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.GetProfile(c)
	})(c)
	assert.NoError(t, err)
	assert.Equal(t, http.StatusNotFound, rec.Code)
}

func TestFollowCaseSuccess(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.POST, "/", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/profiles/:username/follow")
	c.SetParamNames("username")
	c.SetParamValues("user2")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.Follow(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "profile")
		assert.Equal(t, "user2", m["username"])
		assert.Equal(t, "user2 bio", m["bio"])
		assert.Equal(t, "http://realworld.io/user2.jpg", m["image"])
		assert.Equal(t, true, m["following"])
	}
}

func TestFollowCaseInvalidUser(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.POST, "/", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/profiles/:username/follow")
	c.SetParamNames("username")
	c.SetParamValues("userx")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.Follow(c)
	})(c)
	assert.NoError(t, err)
	assert.Equal(t, http.StatusNotFound, rec.Code)
}

func TestUnfollow(t *testing.T) {
	tearDown()
	setup()
	jwtMiddleware := middleware.JWT(utils.JWTSecret)
	req := httptest.NewRequest(echo.DELETE, "/api/profiles/:username/follow", nil)
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	req.Header.Set(echo.HeaderAuthorization, authHeader(utils.GenerateJWT(1)))
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetPath("/api/profiles/:username/follow")
	c.SetParamNames("username")
	c.SetParamValues("user2")
	err := jwtMiddleware(func(context echo.Context) error {
		return h.Unfollow(c)
	})(c)
	assert.NoError(t, err)
	if assert.Equal(t, http.StatusOK, rec.Code) {
		m := responseMap(rec.Body.Bytes(), "profile")
		assert.Equal(t, "user2", m["username"])
		assert.Equal(t, "user2 bio", m["bio"])
		assert.Equal(t, "http://realworld.io/user2.jpg", m["image"])
		assert.Equal(t, false, m["following"])
	}
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/model/article.go
package model

import (
	"github.com/jinzhu/gorm"
)

type Article struct {
	gorm.Model
	Slug        string `gorm:"unique_index;not null"`
	Title       string `gorm:"not null"`
	Description string
	Body        string
	Author      User
	AuthorID    uint
	Comments    []Comment
	Favorites   []User `gorm:"many2many:favorites;"`
	Tags        []Tag  `gorm:"many2many:article_tags;association_autocreate:false"`
}

type Comment struct {
	gorm.Model
	Article   Article
	ArticleID uint
	User      User
	UserID    uint
	Body      string
}

type Tag struct {
	gorm.Model
	Tag      string    `gorm:"unique_index"`
	Articles []Article `gorm:"many2many:article_tags;"`
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/model/user.go
package model

import (
	"errors"

	"github.com/jinzhu/gorm"
	"golang.org/x/crypto/bcrypt"
)

type User struct {
	gorm.Model
	Username   string `gorm:"unique_index;not null"`
	Email      string `gorm:"unique_index;not null"`
	Password   string `gorm:"not null"`
	Bio        *string
	Image      *string
	Followers  []Follow  `gorm:"foreignkey:FollowingID"`
	Followings []Follow  `gorm:"foreignkey:FollowerID"`
	Favorites  []Article `gorm:"many2many:favorites;"`
}

type Follow struct {
	Follower    User
	FollowerID  uint `gorm:"primary_key" sql:"type:int not null"`
	Following   User
	FollowingID uint `gorm:"primary_key" sql:"type:int not null"`
}

func (u *User) HashPassword(plain string) (string, error) {
	if len(plain) == 0 {
		return "", errors.New("password should not be empty")
	}
	h, err := bcrypt.GenerateFromPassword([]byte(plain), bcrypt.DefaultCost)
	return string(h), err
}

func (u *User) CheckPassword(plain string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(u.Password), []byte(plain))
	return err == nil
}

// FollowedBy Followings should be pre loaded
func (u *User) FollowedBy(id uint) bool {
	if u.Followers == nil {
		return false
	}
	for _, f := range u.Followers {
		if f.FollowerID == id {
			return true
		}
	}
	return false
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/router/router.go
package router

import (
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/labstack/gommon/log"
)

func New() *echo.Echo {
	e := echo.New()
	e.Logger.SetLevel(log.DEBUG)
	e.Pre(middleware.RemoveTrailingSlash())
	e.Use(middleware.Logger())
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{"*"},
		AllowHeaders: []string{echo.HeaderOrigin, echo.HeaderContentType, echo.HeaderAccept, echo.HeaderAuthorization},
		AllowMethods: []string{echo.GET, echo.HEAD, echo.PUT, echo.PATCH, echo.POST, echo.DELETE},
	}))
	e.Validator = NewValidator()
	return e
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/router/validator.go
package router

import "gopkg.in/go-playground/validator.v9"

func NewValidator() *Validator {
	return &Validator{
		validator: validator.New(),
	}
}

type Validator struct {
	validator *validator.Validate
}

func (v *Validator) Validate(i interface{}) error {
	return v.validator.Struct(i)
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/router/middleware/jwt.go
package middleware

import (
	"fmt"
	"net/http"

	"github.com/dgrijalva/jwt-go"
	"github.com/labstack/echo/v4"
	"github.com/xesina/golang-echo-realworld-example-app/utils"
)

type (
	JWTConfig struct {
		Skipper    Skipper
		SigningKey interface{}
	}
	Skipper      func(c echo.Context) bool
	jwtExtractor func(echo.Context) (string, error)
)

var (
	ErrJWTMissing = echo.NewHTTPError(http.StatusUnauthorized, "missing or malformed jwt")
	ErrJWTInvalid = echo.NewHTTPError(http.StatusForbidden, "invalid or expired jwt")
)

func JWT(key interface{}) echo.MiddlewareFunc {
	c := JWTConfig{}
	c.SigningKey = key
	return JWTWithConfig(c)
}

func JWTWithConfig(config JWTConfig) echo.MiddlewareFunc {
	extractor := jwtFromHeader("Authorization", "Token")
	return func(next echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			auth, err := extractor(c)
			if err != nil {
				if config.Skipper != nil {
					if config.Skipper(c) {
						return next(c)
					}
				}
				return c.JSON(http.StatusUnauthorized, utils.NewError(err))
			}
			token, err := jwt.Parse(auth, func(token *jwt.Token) (interface{}, error) {
				if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
					return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
				}
				return config.SigningKey, nil
			})
			if err != nil {
				return c.JSON(http.StatusForbidden, utils.NewError(ErrJWTInvalid))
			}
			if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
				userID := uint(claims["id"].(float64))
				c.Set("user", userID)
				return next(c)
			}
			return c.JSON(http.StatusForbidden, utils.NewError(ErrJWTInvalid))
		}
	}
}

// jwtFromHeader returns a `jwtExtractor` that extracts token from the request header.
func jwtFromHeader(header string, authScheme string) jwtExtractor {
	return func(c echo.Context) (string, error) {
		auth := c.Request().Header.Get(header)
		l := len(authScheme)
		if len(auth) > l+1 && auth[:l] == authScheme {
			return auth[l+1:], nil
		}
		return "", ErrJWTMissing
	}
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/store/article.go
package store

import (
	"github.com/jinzhu/gorm"
	"github.com/xesina/golang-echo-realworld-example-app/model"
)

type ArticleStore struct {
	db *gorm.DB
}

func NewArticleStore(db *gorm.DB) *ArticleStore {
	return &ArticleStore{
		db: db,
	}
}

func (as *ArticleStore) GetBySlug(s string) (*model.Article, error) {
	var m model.Article

	err := as.db.Where(&model.Article{Slug: s}).Preload("Favorites").Preload("Tags").Preload("Author").Find(&m).Error
	if err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}

		return nil, err
	}

	return &m, err
}

func (as *ArticleStore) GetUserArticleBySlug(userID uint, slug string) (*model.Article, error) {
	var m model.Article

	err := as.db.Where(&model.Article{Slug: slug, AuthorID: userID}).Find(&m).Error
	if err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}

		return nil, err
	}

	return &m, err
}

func (as *ArticleStore) CreateArticle(a *model.Article) error {
	tags := a.Tags

	tx := as.db.Begin()
	if err := tx.Create(&a).Error; err != nil {
		tx.Rollback()
		return err
	}

	for _, t := range a.Tags {
		err := tx.Where(&model.Tag{Tag: t.Tag}).First(&t).Error
		if err != nil && !gorm.IsRecordNotFoundError(err) {
			tx.Rollback()
			return err
		}

		if err := tx.Model(&a).Association("Tags").Append(t).Error; err != nil {
			tx.Rollback()
			return err
		}
	}

	if err := tx.Where(a.ID).Preload("Favorites").Preload("Tags").Preload("Author").Find(&a).Error; err != nil {
		tx.Rollback()
		return err
	}

	a.Tags = tags

	return tx.Commit().Error
}

func (as *ArticleStore) UpdateArticle(a *model.Article, tagList []string) error {
	tx := as.db.Begin()
	if err := tx.Model(a).Update(a).Error; err != nil {
		tx.Rollback()
		return err
	}

	tags := make([]model.Tag, 0)

	for _, t := range tagList {
		tag := model.Tag{Tag: t}

		err := tx.Where(&tag).First(&tag).Error
		if err != nil && !gorm.IsRecordNotFoundError(err) {
			tx.Rollback()
			return err
		}

		tags = append(tags, tag)
	}

	if err := tx.Model(a).Association("Tags").Replace(tags).Error; err != nil {
		tx.Rollback()
		return err
	}

	if err := tx.Where(a.ID).Preload("Favorites").Preload("Tags").Preload("Author").Find(a).Error; err != nil {
		tx.Rollback()
		return err
	}

	return tx.Commit().Error
}

func (as *ArticleStore) DeleteArticle(a *model.Article) error {
	return as.db.Delete(a).Error
}

func (as *ArticleStore) List(offset, limit int) ([]model.Article, int, error) {
	var (
		articles []model.Article
		count    int
	)

	as.db.Model(&articles).Count(&count)
	as.db.Preload("Favorites").
		Preload("Tags").
		Preload("Author").
		Offset(offset).
		Limit(limit).
		Order("created_at desc").Find(&articles)

	return articles, count, nil
}

func (as *ArticleStore) ListByTag(tag string, offset, limit int) ([]model.Article, int, error) {
	var (
		t        model.Tag
		articles []model.Article
		count    int
	)

	err := as.db.Where(&model.Tag{Tag: tag}).First(&t).Error
	if err != nil {
		return nil, 0, err
	}

	as.db.Model(&t).
		Preload("Favorites").
		Preload("Tags").
		Preload("Author").
		Offset(offset).
		Limit(limit).
		Order("created_at desc").
		Association("Articles").
		Find(&articles)

	count = as.db.Model(&t).Association("Articles").Count()

	return articles, count, nil
}

func (as *ArticleStore) ListByAuthor(username string, offset, limit int) ([]model.Article, int, error) {
	var (
		u        model.User
		articles []model.Article
		count    int
	)

	err := as.db.Where(&model.User{Username: username}).First(&u).Error
	if err != nil {
		return nil, 0, err
	}

	as.db.Where(&model.Article{AuthorID: u.ID}).
		Preload("Favorites").
		Preload("Tags").
		Preload("Author").
		Offset(offset).
		Limit(limit).
		Order("created_at desc").
		Find(&articles)
	as.db.Where(&model.Article{AuthorID: u.ID}).Model(&model.Article{}).Count(&count)

	return articles, count, nil
}

func (as *ArticleStore) ListByWhoFavorited(username string, offset, limit int) ([]model.Article, int, error) {
	var (
		u        model.User
		articles []model.Article
		count    int
	)

	err := as.db.Where(&model.User{Username: username}).First(&u).Error
	if err != nil {
		return nil, 0, err
	}

	as.db.Model(&u).
		Preload("Favorites").
		Preload("Tags").
		Preload("Author").
		Offset(offset).
		Limit(limit).
		Order("created_at desc").
		Association("Favorites").
		Find(&articles)

	count = as.db.Model(&u).Association("Favorites").Count()

	return articles, count, nil
}

func (as *ArticleStore) ListFeed(userID uint, offset, limit int) ([]model.Article, int, error) {
	var (
		u        model.User
		articles []model.Article
		count    int
	)

	err := as.db.First(&u, userID).Error
	if err != nil {
		return nil, 0, err
	}

	var followings []model.Follow

	as.db.Model(&u).Preload("Following").Preload("Follower").Association("Followings").Find(&followings)

	if len(followings) == 0 {
		return articles, 0, nil
	}

	ids := make([]uint, len(followings))
	for i, f := range followings {
		ids[i] = f.FollowingID
	}

	as.db.Where("author_id in (?)", ids).
		Preload("Favorites").
		Preload("Tags").
		Preload("Author").
		Offset(offset).
		Limit(limit).
		Order("created_at desc").
		Find(&articles)
	as.db.Where(&model.Article{AuthorID: u.ID}).Model(&model.Article{}).Count(&count)

	return articles, count, nil
}

func (as *ArticleStore) AddComment(a *model.Article, c *model.Comment) error {
	err := as.db.Model(a).Association("Comments").Append(c).Error
	if err != nil {
		return err
	}

	return as.db.Where(c.ID).Preload("User").First(c).Error
}

func (as *ArticleStore) GetCommentsBySlug(slug string) ([]model.Comment, error) {
	var m model.Article
	err := as.db.Where(&model.Article{Slug: slug}).Preload("Comments").Preload("Comments.User").First(&m).Error

	if err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}

		return nil, err
	}

	return m.Comments, nil
}

func (as *ArticleStore) GetCommentByID(id uint) (*model.Comment, error) {
	var m model.Comment
	if err := as.db.Where(id).First(&m).Error; err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}

		return nil, err
	}

	return &m, nil
}

func (as *ArticleStore) DeleteComment(c *model.Comment) error {
	return as.db.Delete(c).Error
}

func (as *ArticleStore) AddFavorite(a *model.Article, userID uint) error {
	usr := model.User{}
	usr.ID = userID

	return as.db.Model(a).Association("Favorites").Append(&usr).Error
}

func (as *ArticleStore) RemoveFavorite(a *model.Article, userID uint) error {
	usr := model.User{}
	usr.ID = userID

	return as.db.Model(a).Association("Favorites").Delete(&usr).Error
}

func (as *ArticleStore) ListTags() ([]model.Tag, error) {
	var tags []model.Tag
	if err := as.db.Find(&tags).Error; err != nil {
		return nil, err
	}

	return tags, nil
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/store/user.go
package store

import (
	"github.com/jinzhu/gorm"
	"github.com/xesina/golang-echo-realworld-example-app/model"
)

type UserStore struct {
	db *gorm.DB
}

func NewUserStore(db *gorm.DB) *UserStore {
	return &UserStore{
		db: db,
	}
}

func (us *UserStore) GetByID(id uint) (*model.User, error) {
	var m model.User
	if err := us.db.First(&m, id).Error; err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}
		return nil, err
	}
	return &m, nil
}

func (us *UserStore) GetByEmail(e string) (*model.User, error) {
	var m model.User
	if err := us.db.Where(&model.User{Email: e}).First(&m).Error; err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}
		return nil, err
	}
	return &m, nil
}

func (us *UserStore) GetByUsername(username string) (*model.User, error) {
	var m model.User
	if err := us.db.Where(&model.User{Username: username}).Preload("Followers").First(&m).Error; err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return nil, nil
		}
		return nil, err
	}
	return &m, nil
}

func (us *UserStore) Create(u *model.User) (err error) {
	return us.db.Create(u).Error
}

func (us *UserStore) Update(u *model.User) error {
	return us.db.Model(u).Update(u).Error
}

func (us *UserStore) AddFollower(u *model.User, followerID uint) error {
	return us.db.Model(u).Association("Followers").Append(&model.Follow{FollowerID: followerID, FollowingID: u.ID}).Error
}

func (us *UserStore) RemoveFollower(u *model.User, followerID uint) error {
	f := model.Follow{
		FollowerID:  followerID,
		FollowingID: u.ID,
	}
	if err := us.db.Model(u).Association("Followers").Find(&f).Error; err != nil {
		return err
	}
	if err := us.db.Delete(f).Error; err != nil {
		return err
	}
	return nil
}

func (us *UserStore) IsFollower(userID, followerID uint) (bool, error) {
	var f model.Follow
	if err := us.db.Where("following_id = ? AND follower_id = ?", userID, followerID).Find(&f).Error; err != nil {
		if gorm.IsRecordNotFoundError(err) {
			return false, nil
		}
		return false, err
	}
	return true, nil
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/user/user.go
package user

import (
	"github.com/xesina/golang-echo-realworld-example-app/model"
)

type Store interface {
	GetByID(uint) (*model.User, error)
	GetByEmail(string) (*model.User, error)
	GetByUsername(string) (*model.User, error)
	Create(*model.User) error
	Update(*model.User) error
	AddFollower(user *model.User, followerID uint) error
	RemoveFollower(user *model.User, followerID uint) error
	IsFollower(userID, followerID uint) (bool, error)
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/utils/errors.go
package utils

import (
	"fmt"

	"github.com/labstack/echo/v4"
	"gopkg.in/go-playground/validator.v9"
)

type Error struct {
	Errors map[string]interface{} `json:"errors"`
}

func NewError(err error) Error {
	e := Error{}
	e.Errors = make(map[string]interface{})
	switch v := err.(type) {
	case *echo.HTTPError:
		e.Errors["body"] = v.Message
	default:
		e.Errors["body"] = v.Error()
	}
	return e
}

func NewValidatorError(err error) Error {
	e := Error{}
	e.Errors = make(map[string]interface{})
	errs := err.(validator.ValidationErrors)
	for _, v := range errs {
		e.Errors[v.Field()] = fmt.Sprintf("%v", v.Tag())
	}
	return e
}

func AccessForbidden() Error {
	e := Error{}
	e.Errors = make(map[string]interface{})
	e.Errors["body"] = "access forbidden"
	return e
}

func NotFound() Error {
	e := Error{}
	e.Errors = make(map[string]interface{})
	e.Errors["body"] = "resource not found"
	return e
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/utils/jwt.go
package utils

import (
	"time"

	"github.com/dgrijalva/jwt-go"
)

var JWTSecret = []byte("!!SECRET!!")

func GenerateJWT(id uint) string {
	token := jwt.New(jwt.SigningMethodHS256)
	claims := token.Claims.(jwt.MapClaims)
	claims["id"] = id
	claims["exp"] = time.Now().Add(time.Hour * 72).Unix()
	t, _ := token.SignedString(JWTSecret)
	return t
}

--#

--% /tmp/hapus/jakartaee/golang-echo-realworld-example-app/utils/utils.go
package utils

--#

