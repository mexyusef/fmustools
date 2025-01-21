--% run.sh
make build
--#

--% index/fmus
gocli,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=C:/tmp/rework/gh-prompt/.gitignore)
	.goreleaser.yml,f(e=utama=C:/tmp/rework/gh-prompt/.goreleaser.yml)
	go.mod,f(e=utama=C:/tmp/rework/gh-prompt/go.mod)
	go.sum,f(e=utama=C:/tmp/rework/gh-prompt/go.sum)
	LICENSE,f(e=utama=C:/tmp/rework/gh-prompt/LICENSE)
	Makefile,f(e=utama=C:/tmp/rework/gh-prompt/Makefile)
	README.md,f(e=utama=C:/tmp/rework/gh-prompt/README.md)
	run.sh,f(e=__FILE__=run.sh)
	$*chmod a+x run.sh
	.github,d(/mk)
		workflows,d(/mk)
			lint.yml,f(e=utama=C:/tmp/rework/gh-prompt/.github/workflows/lint.yml)
			release.yml,f(e=utama=C:/tmp/rework/gh-prompt/.github/workflows/release.yml)
	cmd,d(/mk)
		gh-prompt,d(/mk)
			main.go,f(e=utama=C:/tmp/rework/gh-prompt/cmd/gh-prompt/main.go)
	completer,d(/mk)
		argument.go,f(e=utama=C:/tmp/rework/gh-prompt/completer/argument.go)
		client.go,f(e=utama=C:/tmp/rework/gh-prompt/completer/client.go)
		completer.go,f(e=utama=C:/tmp/rework/gh-prompt/completer/completer.go)
		config.go,f(e=utama=C:/tmp/rework/gh-prompt/completer/config.go)
		option.go,f(e=utama=C:/tmp/rework/gh-prompt/completer/option.go)
	internal,d(/mk)
		debug,d(/mk)
			log.go,f(e=utama=C:/tmp/rework/gh-prompt/internal/debug/log.go)
--#

--% C:/tmp/rework/gh-prompt/.gitignore
# Binaries for programs and plugins
bin/
dist/
gh-prompt
*.exe
*.dll
*.so
*.dylib

# Test binary, build with `go test -c`
*.test

# Output of the go coverage tool, specifically when used with LiteIDE
*.out

# glide
vendor/

--#

--% C:/tmp/rework/gh-prompt/.goreleaser.yml
project_name: gh-prompt
env:
  - GO111MODULE=on
before:
  hooks:
    - go mod tidy
builds:
  - main: ./cmd/gh-prompt/main.go
    binary: gh-prompt
    ldflags:
      - -s -w
      - -X main.Version={{.Version}}
      - -X main.Revision={{.ShortCommit}}
    env:
      - CGO_ENABLED=0
archives:
  - name_template: '{{ .ProjectName }}_{{ .Os }}_{{ .Arch }}{{ if .Arm }}v{{ .Arm }}{{ end }}'
    replacements:
      darwin: darwin
      linux: linux
      386: i386
      amd64: x86_64
    format: zip
release:
  prerelease: auto
--#

--% C:/tmp/rework/gh-prompt/go.mod
module github.com/c-bata/gh-prompt

go 1.13

require (
	github.com/c-bata/go-prompt v0.2.3
	github.com/cli/cli v0.5.5-pre.1.0.20200212221032-c27d7807a06a
	github.com/mattn/go-isatty v0.0.12 // indirect
	github.com/mattn/go-runewidth v0.0.8 // indirect
	github.com/mattn/go-tty v0.0.3 // indirect
	github.com/pkg/term v0.0.0-20190109203006-aa71e9d9e942 // indirect
	golang.org/x/sys v0.0.0-20200212091648-12a6c2dcc1e4 // indirect
)

--#

--% C:/tmp/rework/gh-prompt/go.sum
github.com/AlecAivazis/survey/v2 v2.0.4/go.mod h1:WYBhg6f0y/fNYUuesWQc0PKbJcEliGcYHB9sNT3Bg74=
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/GeertJohan/go.incremental v1.0.0/go.mod h1:6fAjUhbVuX1KcMD3c8TEgVUqmo4seqhv0i0kdATSkM0=
github.com/GeertJohan/go.rice v1.0.0/go.mod h1:eH6gbSOAUv07dQuZVnBmoDP8mgsM1rtixis4Tib9if0=
github.com/Netflix/go-expect v0.0.0-20180615182759-c93bf25de8e8/go.mod h1:oX5x61PbNXchhh0oikYAH+4Pcfw5LKv21+Jnpr6r6Pc=
github.com/akavel/rsrc v0.8.0/go.mod h1:uLoCtb9J+EyAqh+26kdrTgmzRBFPGOolLWKpdxkKq+c=
github.com/alecthomas/assert v0.0.0-20170929043011-405dbfeb8e38 h1:smF2tmSOzy2Mm+0dGI2AIUHY+w0BUc+4tn40djz7+6U=
github.com/alecthomas/assert v0.0.0-20170929043011-405dbfeb8e38/go.mod h1:r7bzyVFMNntcxPZXK3/+KdruV1H5KSlyVY0gc+NgInI=
github.com/alecthomas/chroma v0.6.8 h1:TW4JJaIdbAbMyUtGEd6BukFlOKYvVQz3vVhLBEUNwMU=
github.com/alecthomas/chroma v0.6.8/go.mod h1:o9ohftueRi7H5be3+Q2cQCNa/YnLBFUNx40ZJfGVFKA=
github.com/alecthomas/colour v0.0.0-20160524082231-60882d9e2721 h1:JHZL0hZKJ1VENNfmXvHbgYlbUOvpzYzvy2aZU5gXVeo=
github.com/alecthomas/colour v0.0.0-20160524082231-60882d9e2721/go.mod h1:QO9JBoKquHd+jz9nshCh40fOfO+JzsoXy8qTHF68zU0=
github.com/alecthomas/kong v0.1.17-0.20190424132513-439c674f7ae0/go.mod h1:+inYUSluD+p4L8KdviBSgzcqEjUQOfC5fQDRFuc36lI=
github.com/alecthomas/kong v0.2.1-0.20190708041108-0548c6b1afae/go.mod h1:+inYUSluD+p4L8KdviBSgzcqEjUQOfC5fQDRFuc36lI=
github.com/alecthomas/kong-hcl v0.1.8-0.20190615233001-b21fea9723c8/go.mod h1:MRgZdU3vrFd05IQ89AxUZ0aYdF39BYoNFa324SodPCA=
github.com/alecthomas/repr v0.0.0-20180818092828-117648cd9897 h1:p9Sln00KOTlrYkxI1zYWl1QLnEqAqEARBEYa8FQnQcY=
github.com/alecthomas/repr v0.0.0-20180818092828-117648cd9897/go.mod h1:xTS7Pm1pD1mvyM075QCDSRqH6qRLXylzS24ZTpRiSzQ=
github.com/armon/consul-api v0.0.0-20180202201655-eb2c6b5be1b6/go.mod h1:grANhF5doyWs3UAsr3K4I6qtAmlQcZDesFNEHPZAzj8=
github.com/aybabtme/rgbterm v0.0.0-20170906152045-cc83f3b3ce59 h1:WWB576BN5zNSZc/M9d/10pqEx5VHNhaQ/yOVAkmj5Yo=
github.com/aybabtme/rgbterm v0.0.0-20170906152045-cc83f3b3ce59/go.mod h1:q/89r3U2H7sSsE2t6Kca0lfwTK8JdoNGS/yzM/4iH5I=
github.com/c-bata/go-prompt v0.2.3 h1:jjCS+QhG/sULBhAaBdjb2PlMRVaKXQgn+4yzaauvs2s=
github.com/c-bata/go-prompt v0.2.3/go.mod h1:VzqtzE2ksDBcdln8G7mk2RX9QyGjH+OVqOCSiVIqS34=
github.com/cli/cli v0.5.5-pre.1.0.20200212221032-c27d7807a06a h1:wbK/t+TuOuShfwgVqGkyS5sIwKCoCcYD9bIeED/a+Tg=
github.com/cli/cli v0.5.5-pre.1.0.20200212221032-c27d7807a06a/go.mod h1:Gl9lAiPw9W6kqXMlawLVI2VPoJ+pHmImV19zmt+nMQ4=
github.com/coreos/etcd v3.3.10+incompatible/go.mod h1:uF7uidLiAD3TWHmW31ZFd/JWoc32PjwdhPthX9715RE=
github.com/coreos/go-etcd v2.0.0+incompatible/go.mod h1:Jez6KQU2B/sWsbdaef3ED8NzMklzPG4d5KIOhIy30Tk=
github.com/coreos/go-semver v0.2.0/go.mod h1:nnelYz7RCh+5ahJtPPxZlU+153eP4D4r3EedlOD2RNk=
github.com/cpuguy83/go-md2man v1.0.10/go.mod h1:SmD6nW6nTyfqj6ABTjUi3V3JVMnlJmwcJI5acqYI6dE=
github.com/daaku/go.zipexe v1.0.0/go.mod h1:z8IiR6TsVLEYKwXAoE/I+8ys/sDkgTzSL0CLnGVd57E=
github.com/danwakefield/fnmatch v0.0.0-20160403171240-cbb64ac3d964 h1:y5HC9v93H5EPKqaS1UYVg1uYah5Xf51mBfIoWehClUQ=
github.com/danwakefield/fnmatch v0.0.0-20160403171240-cbb64ac3d964/go.mod h1:Xd9hchkHSWYkEqJwUGisez3G1QY8Ryz0sdWrLPMGjLk=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/dlclark/regexp2 v1.1.6 h1:CqB4MjHw0MFCDj+PHHjiESmHX+N7t0tJzKvC6M97BRg=
github.com/dlclark/regexp2 v1.1.6/go.mod h1:2pZnwuY/m+8K6iRw6wQdMtk+rH5tNGR1i55kozfMjCc=
github.com/fsnotify/fsnotify v1.4.7/go.mod h1:jwhsz4b93w/PPRr/qN1Yymfu8t87LnFCMoQvtojpjFo=
github.com/google/shlex v0.0.0-20191202100458-e7afc7fbc510 h1:El6M4kTTCOh6aBiKaUGG7oYTSPP8MxqL4YI3kZKwcP4=
github.com/google/shlex v0.0.0-20191202100458-e7afc7fbc510/go.mod h1:pupxD2MaaD3pAXIBCelhxNneeOaAeabZDe5s4K6zSpQ=
github.com/gorilla/csrf v1.6.0/go.mod h1:7tSf8kmjNYr7IWDCYhd3U8Ck34iQ/Yw5CJu7bAkHEGI=
github.com/gorilla/handlers v1.4.1/go.mod h1:Qkdc/uu4tH4g6mTK6auzZ766c4CA0Ng8+o/OAirnOIQ=
github.com/gorilla/mux v1.7.3/go.mod h1:1lud6UwP+6orDFRuTfBEV8e9/aOM/c4fVVCaMa2zaAs=
github.com/gorilla/securecookie v1.1.1/go.mod h1:ra0sb63/xPlUeL+yeDciTfxMRAA+MP+HVt/4epWDjd4=
github.com/hashicorp/go-version v1.2.0/go.mod h1:fltr4n8CU8Ke44wwGCBoEymUuxUHl09ZGVZPK5anwXA=
github.com/hashicorp/hcl v1.0.0/go.mod h1:E5yfLk+7swimpb2L/Alb/PJmXilQ/rhwaUYs4T20WEQ=
github.com/hinshun/vt10x v0.0.0-20180616224451-1954e6464174/go.mod h1:DqJ97dSdRW1W22yXSB90986pcOyQ7r45iio1KN2ez1A=
github.com/inconshreveable/mousetrap v1.0.0/go.mod h1:PxqpIevigyE2G7u3NXJIT2ANytuPF1OarO4DADm73n8=
github.com/jessevdk/go-flags v1.4.0/go.mod h1:4FA24M0QyGHXBuZZK/XkWh8h0e1EYbRYJSGM75WSRxI=
github.com/kballard/go-shellquote v0.0.0-20180428030007-95032a82bc51/go.mod h1:CzGEWj7cYgsdH8dAjBGEr58BoE7ScuLd+fwFZ44+/x8=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/pty v1.1.4/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/magiconair/properties v1.8.0/go.mod h1:PppfXfuXeibc/6YijjN8zIbojt8czPbwD3XqdrwzmxQ=
github.com/mattn/go-colorable v0.0.9/go.mod h1:9vuHe8Xs5qXnSaW/c/ABM9alt+Vo+STaOChaDxuIBZU=
github.com/mattn/go-colorable v0.1.2/go.mod h1:U0ppj6V5qS13XJ6of8GYAs25YV2eR4EVcfRqFIhoBtE=
github.com/mattn/go-colorable v0.1.4 h1:snbPLB8fVfU9iwbbo30TPtbLRzwWu6aJS6Xh4eaaviA=
github.com/mattn/go-colorable v0.1.4/go.mod h1:U0ppj6V5qS13XJ6of8GYAs25YV2eR4EVcfRqFIhoBtE=
github.com/mattn/go-isatty v0.0.4/go.mod h1:M+lRXTBqGeGNdLjl/ufCoiOlB5xdOkqRJdNxMWT7Zi4=
github.com/mattn/go-isatty v0.0.8/go.mod h1:Iq45c/XA43vh69/j3iqttzPXn0bhXyGjM0Hdxcsrc5s=
github.com/mattn/go-isatty v0.0.9/go.mod h1:YNRxwqDuOph6SZLI9vUUz6OYw3QyUt7WiY2yME+cCiQ=
github.com/mattn/go-isatty v0.0.10 h1:qxFzApOv4WsAL965uUPIsXzAKCZxN2p9UqdhFS4ZW10=
github.com/mattn/go-isatty v0.0.10/go.mod h1:qgIWMr58cqv1PHHyhnkY9lrL7etaEgOFcMEpPG5Rm84=
github.com/mattn/go-isatty v0.0.12 h1:wuysRhFDzyxgEmMf5xjvJ2M9dZoWAXNNr5LSBS7uHXY=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-runewidth v0.0.6/go.mod h1:H031xJmbD/WCDINGzjvQ9THkh0rPKHF+m2gUSrubnMI=
github.com/mattn/go-runewidth v0.0.8 h1:3tS41NlGYSmhhe/8fhGRzc+z3AYCw1Fe1WAyLuujKs0=
github.com/mattn/go-runewidth v0.0.8/go.mod h1:H031xJmbD/WCDINGzjvQ9THkh0rPKHF+m2gUSrubnMI=
github.com/mattn/go-tty v0.0.3 h1:5OfyWorkyO7xP52Mq7tB36ajHDG5OHrmBGIS/DtakQI=
github.com/mattn/go-tty v0.0.3/go.mod h1:ihxohKRERHTVzN+aSVRwACLCeqIoZAWpoICkkvrWyR0=
github.com/mgutz/ansi v0.0.0-20170206155736-9520e82c474b h1:j7+1HpAFS1zy5+Q4qx1fWh90gTKwiN4QCGoY9TWyyO4=
github.com/mgutz/ansi v0.0.0-20170206155736-9520e82c474b/go.mod h1:01TrycV0kFyexm33Z7vhZRXopbI8J3TDReVlkTgMUxE=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/mitchellh/go-wordwrap v1.0.0 h1:6GlHJ/LTGMrIJbwgdqdl2eEH8o+Exx/0m8ir9Gns0u4=
github.com/mitchellh/go-wordwrap v1.0.0/go.mod h1:ZXFpozHsX6DPmq2I0TCekCxypsnAUbP2oI0UX1GXzOo=
github.com/mitchellh/mapstructure v1.1.2/go.mod h1:FVVH3fgwuzCH5S8UJGiWEs2h04kUh9fWfEaFds41c1Y=
github.com/nkovacs/streamquote v0.0.0-20170412213628-49af9bddb229/go.mod h1:0aYXnNPJ8l7uZxf45rWW1a/uME32OF0rhiYGNQ2oF2E=
github.com/pelletier/go-toml v1.2.0/go.mod h1:5z9KED0ma1S8pY6P1sdut58dfprrGBbd/94hg7ilaic=
github.com/pkg/errors v0.8.0/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.8.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/term v0.0.0-20190109203006-aa71e9d9e942 h1:A7GG7zcGjl3jqAqGPmcNjd/D9hzL95SuoOQAaFNdLU0=
github.com/pkg/term v0.0.0-20190109203006-aa71e9d9e942/go.mod h1:eCbImbZ95eXtAUIbLAuAVnBnwf83mjf6QIVH8SHYwqQ=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/russross/blackfriday v1.5.2 h1:HyvC0ARfnZBqnXwABFeSZHpKvJHJJfPz81GNueLj0oo=
github.com/russross/blackfriday v1.5.2/go.mod h1:JO/DiYxRf+HjHt06OyowR9PTA263kcR/rfWxYHBV53g=
github.com/russross/blackfriday/v2 v2.0.1 h1:lPqVAte+HuHNfhJ/0LC98ESWRz8afy9tM/0RK8m9o+Q=
github.com/russross/blackfriday/v2 v2.0.1/go.mod h1:+Rmxgy9KzJVeS9/2gXHxylqXiyQDYRxCVz55jmeOWTM=
github.com/sergi/go-diff v1.0.0 h1:Kpca3qRNrduNnOQeazBd0ysaKrUJiIuISHxogkT9RPQ=
github.com/sergi/go-diff v1.0.0/go.mod h1:0CfEIISq7TuYL3j771MWULgwwjU+GofnZX9QAmXWZgo=
github.com/shurcooL/sanitized_anchor_name v1.0.0 h1:PdmoCO6wvbs+7yrJyMORt4/BmY5IYyJwS/kOiWx8mHo=
github.com/shurcooL/sanitized_anchor_name v1.0.0/go.mod h1:1NzhyTcUVG4SuEtjjoZeVRXNmyL/1OwPU0+IJeTBvfc=
github.com/spf13/afero v1.1.2/go.mod h1:j4pytiNVoe2o6bmDsKpLACNPDBIoEAkihy7loJ1B0CQ=
github.com/spf13/cast v1.3.0/go.mod h1:Qx5cxh0v+4UWYiBimWS+eyWzqEqokIECu5etghLkUJE=
github.com/spf13/cobra v0.0.5/go.mod h1:3K3wKZymM7VvHMDS9+Akkh4K60UwM26emMESw8tLCHU=
github.com/spf13/jwalterweatherman v1.0.0/go.mod h1:cQK4TGJAtQXfYWX+Ddv3mKDzgVb68N+wFjFa4jdeBTo=
github.com/spf13/pflag v1.0.3/go.mod h1:DYY7MBk1bdzusC3SYhjObp+wFpr4gzcvqqNjLnInEg4=
github.com/spf13/pflag v1.0.5/go.mod h1:McXfInJRrz4CZXVZOBLb0bTZqETkiAhM9Iw0y3An2Bg=
github.com/spf13/viper v1.3.2/go.mod h1:ZiWeW+zYFKm7srdB9IoDzzZXaJaI5eL9QjNiN/DMA2s=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.2.1/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0 h1:2E4SXV/wtOkTonXsotYi4li6zVWxYlZuYNCXe9XRJyk=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/tj/assert v0.0.0-20190920132354-ee03d75cd160 h1:NSWpaDaurcAJY7PkL8Xt0PhZE7qpvbZl5ljd8r6U0bI=
github.com/tj/assert v0.0.0-20190920132354-ee03d75cd160/go.mod h1:mZ9/Rh9oLWpLLDRpvE+3b7gP/C2YyLFYxNmcLnPTMe0=
github.com/tj/go-css v0.0.0-20191108133013-220a796d1705 h1:+UA89aFRjPMqdccHd9A0HLNCRDXIoElaDoW2C1V3TzA=
github.com/tj/go-css v0.0.0-20191108133013-220a796d1705/go.mod h1:e+JPLQ9wyQCgRnPenX2bo7MJoLphBHz5c1WUqaANSeA=
github.com/ugorji/go/codec v0.0.0-20181204163529-d75b2dcb6bc8/go.mod h1:VFNgLljTbGfSG7qAOspJ7OScBnGdDN/yBr0sguwnwf0=
github.com/valyala/bytebufferpool v1.0.0/go.mod h1:6bBcMArwyJ5K/AmCkWv1jt77kVWyCJ6HpOuEn7z0Csc=
github.com/valyala/fasttemplate v1.0.1/go.mod h1:UQGH1tvbgY+Nz5t2n7tXsz52dQxojPUpymEIMZ47gx8=
github.com/vilmibm/go-termd v0.0.4 h1:uCmDUZ3qZUblTN/D5Hvl+g1rTJj/HW746JQFWidqAyk=
github.com/vilmibm/go-termd v0.0.4/go.mod h1:ys+dRO6wlM3el0vPJmYBkhOPPozViBgDXHOEn1x5Vsc=
github.com/xordataexchange/crypt v0.0.3-0.20170626215501-b2862e3d0a77/go.mod h1:aYKd//L2LvnjZzWKhF00oedf4jCCReLcmhLdhm1A27Q=
golang.org/x/crypto v0.0.0-20181203042331-505ab145d0a9/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190530122614-20be4c3c3ed5 h1:8dUaAV7K4uHsF56JQWkprecIQKdPHtR9jCHF5nB8uzc=
golang.org/x/crypto v0.0.0-20190530122614-20be4c3c3ed5/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20181128092732-4ed8d59d0b35/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20181205085412-a5c9d58dba9a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190222072716-a9d3bda3a223/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190530182044-ad28b68e88f1/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190813064441-fde4db37ae7a/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191008105621-543471e840be/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20191120155948-bd437916bb0e h1:N7DeIrjYszNmSW409R3frPPwglRwMkXSBzwVbkOjLLA=
golang.org/x/sys v0.0.0-20191120155948-bd437916bb0e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200212091648-12a6c2dcc1e4 h1:sfkvUWPNGwSV+8/fNqctR5lS2AqCSqYwXdrjCxp/dXo=
golang.org/x/sys v0.0.0-20200212091648-12a6c2dcc1e4/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v2 v2.2.2 h1:ZCJp+EgiOT7lHqUV2J862kp8Qj64Jo6az82+3Td9dZw=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v3 v3.0.0-20191010095647-fc94e3f71652 h1:VKvJ/mQ4BgCjZUDggYFxTe0qv9jPMHsZPD4Xt91Y5H4=
gopkg.in/yaml.v3 v3.0.0-20191010095647-fc94e3f71652/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=

--#

--% C:/tmp/rework/gh-prompt/LICENSE
MIT License

Copyright (c) 2020 Masashi SHIBATA

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

--% C:/tmp/rework/gh-prompt/Makefile
VERSION := $(shell git describe --tags --abbrev=0)
REVISION := $(shell git rev-parse --short HEAD)
LDFLAGS := -X 'main.Version=$(VERSION)' \
           -X 'main.Revision=$(REVISION)'
GOIMPORTS ?= goimports
GOCILINT ?= golangci-lint
GORELEASER ?= goreleaser
GO ?= GO111MODULE=on go

.DEFAULT_GOAL := help

.PHONY: fmt
fmt: ## Formatting source codes.
	@$(GOIMPORTS) -w .

.PHONY: lint
lint: ## Run golint and go vet.
	@$(GOCILINT) run --no-config --disable-all --enable=goimports --enable=misspell ./...

.PHONY: test
test:  ## Run the tests.
	@$(GO) test ./...

.PHONY: build
build: ## Build a binary.
	$(GO) build -o gh-prompt -ldflags "$(LDFLAGS)" ./cmd/gh-prompt/main.go


.PHONY: cross
cross: ## Cross build using goreleaser.
	$(GORELEASER) --snapshot --skip-publish --rm-dist

.PHONY: help
help: ## Show help text
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "    \033[36m%-20s\033[0m %s\n", $$1, $$2}'

--#

--% C:/tmp/rework/gh-prompt/README.md
# gh-prompt

![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)
[![GoDoc](https://godoc.org/github.com/c-bata/gh-prompt?status.svg)](https://godoc.org/github.com/c-bata/gh-prompt)


An interactive GitHub CLI featuring auto-complete. This tool provides powerful completion to GitHub's official CLI.

[![GIF animation](https://github.com/c-bata/assets/raw/master/gh-prompt/gh-prompt.gif)](#)

You can walk through issues, create pull requests, checkout pull requests locally, and more.
See https://cli.github.com/ for details.

## Installation

### Homebrew (for macOS users)

```
$ brew install c-bata/gh-prompt/gh-prompt
```

### Downloading standalone binary

Binaries are available from [github release](https://github.com/c-bata/gh-prompt/releases).

<details>
<summary>macOS (darwin) - amd64</summary>

```
wget https://github.com/c-bata/gh-prompt/releases/download/v0.0.1/gh-prompt_darwin_x86_64.zip
unzip gh-prompt_darwin_x86_64.zip
chmod +x gh-prompt
sudo mv ./gh-prompt /usr/local/bin/gh-prompt
```

</details>

<details>
<summary>Linux - amd64</summary>

```
wget https://github.com/c-bata/gh-prompt/releases/download/v0.0.1/gh-prompt_linux_x86_64.zip
unzip gh-prompt_linux_x86_64.zip
chmod +x gh-prompt
sudo mv ./gh-prompt /usr/local/bin/gh-prompt
```

</details>


<details>
<summary>Linux - i386</summary>

```
wget https://github.com/c-bata/gh-prompt/releases/download/v0.0.1/gh-prompt_linux_i386.zip
unzip gh-prompt_linux_i386.zip
chmod +x gh-prompt
sudo mv ./gh-prompt /usr/local/bin/gh-prompt
```

</details>

### Building from source

```
$ git clone git@github.com:c-bata/gh-prompt.git
$ cd gh-prompt
$ make build
```

You can create multi-platform binaries via goreleaser:

```
$ goreleaser --snapshot --skip-publish --rm-dist
```

## LICENSE

This software is licensed under the MIT License (See [LICENSE](./LICENSE)).

--#

--% C:/tmp/rework/gh-prompt/.github/workflows/lint.yml
name: Run lint checks
on:
  pull_request:
    branches:
      - master
jobs:
  lint:
    name: Lint checking on Ubuntu
    runs-on: ubuntu-latest

    steps:
      - name: Set up Go 1.13
        uses: actions/setup-go@v1
        with:
          go-version: 1.13
        id: go

      - name: Check out code into the Go module directory
        uses: actions/checkout@master

      - name: Running golangci-lint
        env:
          GO111MODULE: on
          GOPATH: /home/runner/work/
        run: |
          wget https://github.com/golangci/golangci-lint/releases/download/v1.20.1/golangci-lint-1.20.1-linux-amd64.tar.gz
          tar -xvf ./golangci-lint-1.20.1-linux-amd64.tar.gz
          GOCILINT=./golangci-lint-1.20.1-linux-amd64/golangci-lint make lint

--#

--% C:/tmp/rework/gh-prompt/.github/workflows/release.yml
name: release
on:
  push:
    tags:
      - "v[0-9]+.[0-9]+.[0-9]+"
jobs:
  goreleaser:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          fetch-depth: 1
      - name: Setup Go
        uses: actions/setup-go@v2
        with:
          go-version: 1.15
      - name: Run GoReleaser
        uses: goreleaser/goreleaser-action@v2
        with:
          version: latest
          args: release --rm-dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

--#

--% C:/tmp/rework/gh-prompt/cmd/gh-prompt/main.go
package main

import (
	"fmt"
	"os"
	"os/exec"
	"strings"

	"github.com/c-bata/gh-prompt/completer"
	"github.com/c-bata/gh-prompt/internal/debug"
	"github.com/c-bata/go-prompt"
	gpc "github.com/c-bata/go-prompt/completer"
)

var (
	Version  = "unset"
	Revision = "unset"
)

func executorFunc(s string) {
	s = strings.TrimSpace(s)
	if s == "" {
		return
	} else if s == "quit" || s == "exit" {
		fmt.Println("Bye!")
		os.Exit(0)
		return
	}

	cmd := exec.Command("/bin/sh", "-c", "gh "+s)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		fmt.Printf("Got error: %s\n", err.Error())
	}
	return
}

func main() {
	fmt.Printf("gh-prompt %s (rev-%s)\n", Version, Revision)
	fmt.Println("Please use `exit` or `Ctrl-D` to exit this program.")
	defer fmt.Println("Bye!")

	debug.Log("gh-prompt started")
	defer debug.Teardown()

	c, err := completer.NewCompleter(Version)
	if err == completer.ErrNotFoundRemotes {
		_, _ = fmt.Fprintf(os.Stderr, "Failed to get remote informations on your git directory.\n")
		os.Exit(1)
	} else if err != nil {
		_, _ = fmt.Fprintf(os.Stderr, "Initialization error: %s\n", err)
		_, _ = fmt.Fprintf(os.Stderr, "You current directory might not be a git repository.")
		os.Exit(1)
	}
	p := prompt.New(
		executorFunc,
		c.Complete,
		prompt.OptionTitle("gh-prompt: interactive GitHub CLI"),
		prompt.OptionPrefix(">>> "),
		prompt.OptionInputTextColor(prompt.Yellow),
		prompt.OptionCompletionWordSeparator(gpc.FilePathCompletionSeparator),
	)
	p.Run()
}

--#

--% C:/tmp/rework/gh-prompt/completer/argument.go
package completer

import (
	"fmt"

	"github.com/c-bata/gh-prompt/internal/debug"
	"github.com/c-bata/go-prompt"
)

var commands = []prompt.Suggest{
	{Text: "help", Description: "Help about any command"},
	{Text: "pr", Description: "Create, view, and checkout pull requests"},
	{Text: "repo", Description: "Create, clone, fork, and view repositories"},
	{Text: "issue", Description: "Create and view issues"},
	// Custom commands.
	{Text: "exit", Description: "Exit this program"},
}

func (c *Completer) argumentsCompleter(repo string, args []string) []prompt.Suggest {
	if len(args) <= 1 {
		return prompt.FilterHasPrefix(
			commands,
			args[0],
			true,
		)
	}

	switch args[0] {
	case "issue":
		debug.Log(fmt.Sprintf("here! %#v", args))
		if len(args) == 2 {
			return prompt.FilterHasPrefix(
				[]prompt.Suggest{
					{Text: "create", Description: "Create a new issue"},
					{Text: "list", Description: "List and filter issues in this repository"},
					{Text: "status", Description: "Show status of relevant issues"},
					{Text: "view", Description: "View an issue in the browser"},
				},
				args[1],
				true,
			)
		}
		if args[1] == "view" && len(args) == 3 {
			suggests := getIssueNumberSuggestions(c, repo)
			suggests = append(suggests, getIssueURLSuggestions(c, repo)...)
			return prompt.FilterHasPrefix(
				suggests,
				args[2],
				true,
			)
		}
	case "pr":
		if len(args) == 2 {
			return prompt.FilterHasPrefix(
				[]prompt.Suggest{
					{Text: "checkout", Description: "Check out a pull request in Git"},
					{Text: "create", Description: "Create a pull request"},
					{Text: "list", Description: "List and filter pull requests in this repository"},
					{Text: "status", Description: "Show status of relevant pull requests"},
					{Text: "view", Description: "View a pull request in the browser"},
				},
				args[1],
				true,
			)
		}
		if args[1] == "view" && len(args) == 3 {
			suggests := getPullRequestsNumberSuggestions(c, repo)
			suggests = append(suggests, getPullRequestsBranchSuggestions(c, repo)...)
			// This makes 'Text' section of completion window too long.
			// suggests = append(suggests, getPullRequestsURLSuggestions(c, repo)...)
			return prompt.FilterHasPrefix(
				suggests,
				args[2],
				true,
			)
		}
		if args[1] == "checkout" && len(args) == 3 {
			suggests := getPullRequestsNumberSuggestions(c, repo)
			suggests = append(suggests, getPullRequestsBranchSuggestions(c, repo)...)
			// This makes 'Text' section of completion window too long.
			// suggests = append(suggests, getPullRequestsURLSuggestions(c, repo)...)
			return prompt.FilterHasPrefix(
				suggests,
				args[2],
				true,
			)
		}
	case "repo":
		if len(args) == 2 {
			return prompt.FilterHasPrefix(
				[]prompt.Suggest{
					{Text: "clone", Description: "Clone a repository locally"},
					{Text: "create", Description: "Create a new repository"},
					{Text: "fork", Description: "Create a fork of a repository."},
					{Text: "view", Description: "View a repository in the browser."},
				},
				args[1],
				true,
			)
		}
	}
	return []prompt.Suggest{}
}

--#

--% C:/tmp/rework/gh-prompt/completer/client.go
package completer

import (
	"fmt"
	"sync"
	"time"

	"github.com/c-bata/gh-prompt/internal/debug"
	"github.com/c-bata/go-prompt"
	"github.com/cli/cli/api"
	"github.com/cli/cli/context"
)

const (
	thresholdFetchInterval = 60 * time.Second
	issueLimits            = 100
	pullRequestsLimits     = 100
)

var (
	issueCache       *sync.Map
	pullRequestCache *sync.Map
	lastFetchedAt    *sync.Map
	repoCache        *sync.Map
)

func init() {
	issueCache = new(sync.Map)
	pullRequestCache = new(sync.Map)
	lastFetchedAt = new(sync.Map)
	repoCache = new(sync.Map)
}

// client

func currentRepo(ctx *Completer, argRepo string) *api.Repository {
	if argRepo == "" {
		return ctx.repo
	}

	// check cache
	if cached, ok := repoCache.Load(argRepo); ok {
		return cached.(*api.Repository)
	}

	// load repo
	repoCtx, err := context.ResolveRemotesToRepos(ctx.remotes, ctx.client, argRepo)
	if err != nil {
		debug.Log(fmt.Sprintf("err: %s", err))
		return ctx.repo
	}

	repoOverride, err := repoCtx.BaseRepo()
	if err != nil {
		debug.Log(fmt.Sprintf("err: %s", err))
		return ctx.repo
	}
	// cache repo
	repoCache.Store(argRepo, repoOverride)
	return repoOverride
}

// expire

func shouldFetch(key string) bool {
	v, ok := lastFetchedAt.Load(key)
	if !ok {
		return true
	}
	t, ok := v.(time.Time)
	if !ok {
		return true
	}
	return time.Since(t) > thresholdFetchInterval
}

func updateLastFetchedAt(key string) {
	lastFetchedAt.Store(key, time.Now())
}

// issues

func fetchIssuesIfExpired(key string, client *api.Client, repo *api.Repository) {
	if !shouldFetch(key) {
		return
	}
	updateLastFetchedAt(key)

	debug.Log("Call a request to fetch issues.")
	issues, err := api.IssueList(client, repo, "open", nil, "", issueLimits)
	if err != nil {
		debug.Log(err.Error())
	}
	issueCache.Store(key, issues)
	debug.Log("Success to fetch issues")
}

func getIssueCache(key string) (issues []api.Issue, ok bool) {
	v, ok := issueCache.Load(key)
	if !ok {
		return nil, false
	}
	issues, ok = v.([]api.Issue)
	if !ok {
		return nil, ok
	}
	return issues, true
}

func getIssueNumberSuggestions(ctx *Completer, argRepo string) []prompt.Suggest {
	repo := currentRepo(ctx, argRepo)
	cacheKey := fmt.Sprintf("get_issues:%s:%s", repo.RepoOwner(), repo.RepoName())
	go fetchIssuesIfExpired(cacheKey, ctx.client, repo)

	issues, ok := getIssueCache(cacheKey)
	if !ok {
		return []prompt.Suggest{}
	}

	s := make([]prompt.Suggest, len(issues))
	for i := range issues {
		s[i] = prompt.Suggest{
			Text:        fmt.Sprintf("%d", issues[i].Number),
			Description: issues[i].Title,
		}
	}
	return s
}

func getIssueURLSuggestions(ctx *Completer, argRepo string) []prompt.Suggest {
	repo := currentRepo(ctx, argRepo)
	cacheKey := fmt.Sprintf("get_issues:%s:%s", repo.RepoOwner(), repo.RepoName())
	go fetchIssuesIfExpired(cacheKey, ctx.client, repo)

	issues, ok := getIssueCache(cacheKey)
	if !ok {
		return []prompt.Suggest{}
	}

	s := make([]prompt.Suggest, len(issues))
	for i := range issues {
		s[i] = prompt.Suggest{
			Text:        issues[i].URL,
			Description: issues[i].Title,
		}
	}
	return s
}

// pull requests

func fetchPullRequestsIfExpired(key string, client *api.Client, repo *api.Repository) {
	if !shouldFetch(key) {
		return
	}
	params := map[string]interface{}{
		"owner": repo.RepoOwner(),
		"repo":  repo.RepoName(),
		"state": []string{"OPEN"},
	}
	updateLastFetchedAt(key)

	debug.Log("Call a request to fetch pull requests.")
	pulls, err := api.PullRequestList(client, params, pullRequestsLimits)
	if err != nil {
		debug.Log(err.Error())
	}
	pullRequestCache.Store(key, pulls)
	debug.Log("Success to fetch pull requests")
}

func getPullRequestCache(key string) (pulls []api.PullRequest, ok bool) {
	v, ok := pullRequestCache.Load(key)
	if !ok {
		return nil, false
	}
	pulls, ok = v.([]api.PullRequest)
	if !ok {
		return nil, ok
	}
	return pulls, true
}

func getPullRequestsNumberSuggestions(ctx *Completer, argRepo string) []prompt.Suggest {
	repo := currentRepo(ctx, argRepo)
	cacheKey := fmt.Sprintf("get_pulls:%s:%s", repo.RepoOwner(), repo.RepoName())
	go fetchPullRequestsIfExpired(cacheKey, ctx.client, repo)

	pulls, ok := getPullRequestCache(cacheKey)
	if !ok {
		return []prompt.Suggest{}
	}

	s := make([]prompt.Suggest, len(pulls))
	for i := range pulls {
		s[i] = prompt.Suggest{
			Text:        fmt.Sprintf("%d", pulls[i].Number),
			Description: pulls[i].Title,
		}
	}
	return s
}

func getPullRequestsBranchSuggestions(ctx *Completer, argRepo string) []prompt.Suggest {
	repo := currentRepo(ctx, argRepo)
	cacheKey := fmt.Sprintf("get_pulls:%s:%s", repo.RepoOwner(), repo.RepoName())
	go fetchPullRequestsIfExpired(cacheKey, ctx.client, repo)

	pulls, ok := getPullRequestCache(cacheKey)
	if !ok {
		return []prompt.Suggest{}
	}

	s := make([]prompt.Suggest, len(pulls))
	for i := range pulls {
		s[i] = prompt.Suggest{
			Text:        pulls[i].BaseRefName,
			Description: pulls[i].Title,
		}
	}
	return s
}

func getPullRequestsURLSuggestions(ctx *Completer, argRepo string) []prompt.Suggest {
	repo := currentRepo(ctx, argRepo)
	cacheKey := fmt.Sprintf("get_pulls:%s:%s", repo.RepoOwner(), repo.RepoName())
	go fetchPullRequestsIfExpired(cacheKey, ctx.client, repo)

	pulls, ok := getPullRequestCache(cacheKey)
	if !ok {
		return []prompt.Suggest{}
	}

	s := make([]prompt.Suggest, len(pulls))
	for i := range pulls {
		s[i] = prompt.Suggest{
			Text:        pulls[i].URL,
			Description: pulls[i].Title,
		}
	}
	return s
}

--#

--% C:/tmp/rework/gh-prompt/completer/completer.go
package completer

import (
	"errors"
	"fmt"
	"net/url"
	"strings"

	"github.com/c-bata/go-prompt"
	"github.com/cli/cli/api"
	"github.com/cli/cli/context"
	"github.com/cli/cli/git"
)

var ErrNotFoundRemotes = errors.New("git remotes are not found on your current directory")

type Completer struct {
	client  *api.Client
	remotes context.Remotes
	repo    *api.Repository
}

func fromURL(u *url.URL) (owner, repo string, err error) {
	parts := strings.SplitN(strings.TrimPrefix(u.Path, "/"), "/", 3)
	if len(parts) < 2 {
		return "", "", fmt.Errorf("invalid path: %s", u.Path)
	}
	return parts[0], strings.TrimSuffix(parts[1], ".git"), nil
}

func NewCompleter(version string) (*Completer, error) {
	client, err := BasicClient(fmt.Sprintf("gh-prompt %s", version))
	if err != nil {
		return nil, err
	}

	gitRemotes, err := git.Remotes()
	if err != nil {
		return nil, err
	}
	if len(gitRemotes) == 0 {
		return nil, ErrNotFoundRemotes
	}
	remotes := make(context.Remotes, 0, len(gitRemotes))
	sshTranslate := git.ParseSSHConfig().Translator()
	for _, r := range gitRemotes {
		var owner, repo string
		if r.FetchURL != nil {
			owner, repo, _ = fromURL(sshTranslate(r.FetchURL))
		}
		if (owner == "" || repo == "") && r.PushURL != nil {
			owner, repo, _ = fromURL(sshTranslate(r.PushURL))
		}
		remotes = append(remotes, &context.Remote{
			Remote: r,
			Owner:  owner,
			Repo:   repo,
		})
	}

	repoContext, err := context.ResolveRemotesToRepos(remotes, client, "")
	if err != nil {
		return nil, err
	}

	baseRepo, err := repoContext.BaseRepo()
	if err != nil {
		return nil, err
	}

	return &Completer{
		client:  client,
		remotes: remotes,
		repo:    baseRepo,
	}, nil
}

func (c *Completer) Complete(d prompt.Document) []prompt.Suggest {
	if d.TextBeforeCursor() == "" {
		return prompt.FilterHasPrefix(commands, d.GetWordBeforeCursor(), true)
	}

	args := parseArgs(d.TextBeforeCursor())
	w := d.GetWordBeforeCursor()

	// If PIPE is in text before the cursor, returns empty suggestions.
	for i := range args {
		if args[i] == "|" {
			return []prompt.Suggest{}
		}
	}

	// If word before the cursor starts with "-", returns CLI flag options.
	if strings.HasPrefix(w, "-") {
		return c.optionCompleter(args, w)
	}

	// Return suggestions for option
	if suggests, found := c.completeOptionArguments(d); found {
		return suggests
	}

	commandArgs, skipNext := excludeOptions(args)
	if skipNext {
		// when type 'get pod -o ', we don't want to complete pods. we want to type 'json' or other.
		// So we need to skip argumentCompleter.
		return []prompt.Suggest{}
	}

	repo := checkRepoArg(d)
	return c.argumentsCompleter(repo, commandArgs)

}

func parseArgs(t string) []string {
	splits := strings.Split(t, " ")
	args := make([]string, 0, len(splits))

	for i := range splits {
		if i != len(splits)-1 && splits[i] == "" {
			continue
		}
		args = append(args, splits[i])
	}
	return args
}

func checkRepoArg(d prompt.Document) string {
	args := strings.Split(d.Text, " ")
	var found bool
	for i := 0; i < len(args); i++ {
		if found {
			return args[i]
		}
		if args[i] == "--repo" || args[i] == "-R" {
			found = true
			continue
		}
	}
	return ""
}

--#

--% C:/tmp/rework/gh-prompt/completer/config.go
package completer

import (
	"fmt"
	"os"

	"github.com/cli/cli/api"
	"github.com/cli/cli/context"
)

func BasicClient(ua string) (*api.Client, error) {
	opts := []api.ClientOption{
		api.AddHeader("User-Agent", ua),
	}
	if c, err := context.ParseDefaultConfig(); err == nil {
		opts = append(opts, api.AddHeader("Authorization", fmt.Sprintf("token %s", c.Token)))
	}
	if verbose := os.Getenv("DEBUG"); verbose != "" {
		opts = append(opts, api.VerboseLog(os.Stderr, false))
	}
	return api.NewClient(opts...), nil
}

--#

--% C:/tmp/rework/gh-prompt/completer/option.go
package completer

import (
	"strings"

	"github.com/c-bata/go-prompt"
)

var globalOptions = []prompt.Suggest{
	{Text: "--repo", Description: "Select another repository using the OWNER/REPO format"},
	{Text: "-R", Description: "Select another repository using the OWNER/REPO format"},
	{Text: "--help", Description: "Show help for command"},
}

func (c *Completer) optionCompleter(args []string, word string) []prompt.Suggest {
	l := len(args)
	long := strings.HasPrefix(word, "--")
	if l <= 2 {
		return prompt.FilterHasPrefix(globalOptions, word, false)
	}

	var suggests []prompt.Suggest
	commandArgs, _ := excludeOptions(args)
	switch commandArgs[0] {
	case "issue":
		switch commandArgs[1] {
		case "create":
			suggests = []prompt.Suggest{
				{Text: "-b", Description: "Supply a body. Will prompt for one otherwise."},
				{Text: "--body", Description: "Supply a body. Will prompt for one otherwise."},
				{Text: "-t", Description: "Supply a title. Will prompt for one otherwise."},
				{Text: "--title", Description: "Supply a title. Will prompt for one otherwise."},
				{Text: "-w", Description: "Open the browser to create an issue"},
				{Text: "--web", Description: "Open the browser to create an issue"},
			}
		case "list":
			suggests = []prompt.Suggest{
				{Text: "-a", Description: "Filter by assignee"},
				{Text: "--assignee", Description: "Filter by assignee"},
				{Text: "-l", Description: "Filter by label"},
				{Text: "--label", Description: "Filter by label"},
				{Text: "-L", Description: "Maximum number of issues to fetch (default 30)"},
				{Text: "--limit", Description: "Maximum number of issues to fetch (default 30)"},
				{Text: "-s", Description: "Filter by state: {open|closed|all}"},
				{Text: "--state", Description: "Filter by state: {open|closed|all}"},
			}
		case "status":
			suggests = []prompt.Suggest{}
		case "view":
			suggests = []prompt.Suggest{
				{Text: "-p", Description: "Display preview of issue content"},
				{Text: "--preview", Description: "Display preview of issue content"},
			}
		}
	case "pr":
		switch commandArgs[1] {
		case "checkout":
			suggests = []prompt.Suggest{}
		case "create":
			suggests = []prompt.Suggest{
				{Text: "-B", Description: "The branch into which you want your code merged"},
				{Text: "--base", Description: "The branch into which you want your code merged"},
				{Text: "-b", Description: "Supply a body. Will prompt for one otherwise."},
				{Text: "--body", Description: "Supply a body. Will prompt for one otherwise."},
				{Text: "-d", Description: "Mark pull request as a draft"},
				{Text: "--draft", Description: "Mark pull request as a draft"},
				{Text: "-t", Description: "Supply a title. Will prompt for one otherwise."},
				{Text: "--title", Description: "Supply a title. Will prompt for one otherwise."},
				{Text: "-w", Description: "Open the web browser to create a pull request"},
				{Text: "--web", Description: "Open the web browser to create a pull request"},
			}
		case "list":
			suggests = []prompt.Suggest{
				{Text: "-a", Description: "Filter by assignee"},
				{Text: "--assignee", Description: "Filter by assignee"},
				{Text: "-B", Description: "Filter by base branch"},
				{Text: "--base", Description: "Filter by base branch"},
				{Text: "-l", Description: "Filter by label"},
				{Text: "--label", Description: "Filter by label"},
				{Text: "-L", Description: "Maximum number of items to fetch (default 30)"},
				{Text: "--limit", Description: "Maximum number of items to fetch (default 30)"},
				{Text: "-s", Description: "Filter by state: {open|closed|merged|all} (default 'open')"},
				{Text: "--state", Description: "Filter by state: {open|closed|merged|all} (default 'open')"},
			}
		case "status":
			suggests = []prompt.Suggest{}
		case "view":
			suggests = []prompt.Suggest{
				{Text: "-p", Description: "Display preview of pull request content"},
				{Text: "--preview", Description: "Display preview of pull request content"},
			}
		}
	case "repo":
		switch commandArgs[1] {
		case "clone":
			suggests = []prompt.Suggest{}
		case "create":
			suggests = []prompt.Suggest{
				{Text: "-d", Description: "Description of repository"},
				{Text: "--description", Description: "Description of repository"},
				{Text: "--enable-issues", Description: "Enable issues in the new repository (default true)"},
				{Text: "--enable-wiki", Description: "Enable wiki in the new repository (default true)"},
				{Text: "-h", Description: "Repository home page URL"},
				{Text: "--homepage", Description: "Repository home page URL"},
				{Text: "--public", Description: "Make the new repository public"},
				{Text: "-t", Description: "The name of the organization team to be granted access"},
				{Text: "--team", Description: "The name of the organization team to be granted access"},
			}
		case "fork":
			suggests = []prompt.Suggest{
				{Text: "--clone", Description: "Clone fork: {true|false|prompt} (default 'prompt')"},
				{Text: "--remote", Description: "Add remote for fork: {true|false|prompt} (default 'prompt')"},
			}
		}
	default:
		suggests = []prompt.Suggest{}
	}

	suggests = append(suggests, globalOptions...)
	if long {
		return prompt.FilterContains(
			prompt.FilterHasPrefix(suggests, "--", false),
			strings.TrimLeft(args[l-1], "--"),
			true,
		)
	}
	return prompt.FilterContains(suggests, strings.TrimLeft(args[l-1], "-"), true)
}

func getPreviousOption(d prompt.Document) (cmds []string, option string, found bool) {
	args := strings.Split(d.TextBeforeCursor(), " ")
	l := len(args)
	if l >= 2 {
		option = args[l-2]
	}

	cmds, _ = excludeOptions(args)
	if strings.HasPrefix(option, "-") {
		return cmds, option, true
	}
	return nil, "", false
}

func (c *Completer) completeOptionArguments(d prompt.Document) ([]prompt.Suggest, bool) {
	cmds, option, found := getPreviousOption(d)
	if !found {
		return []prompt.Suggest{}, false
	}

	// repository
	if option == "-R" || option == "--repo" {
		return prompt.FilterHasPrefix(
			[]prompt.Suggest{},
			d.GetWordBeforeCursor(),
			true,
		), true
	}

	switch cmds[0] {
	case "issue":
		if len(cmds) < 2 {
			return []prompt.Suggest{}, false
		}

		switch cmds[1] {
		case "create":
			switch option {
			case "-b", "--body":
				return []prompt.Suggest{}, true
			case "-t", "--title":
				return []prompt.Suggest{}, true
			}
		case "list":
			switch option {
			case "-a", "--assignee":
				return []prompt.Suggest{}, true
			case "-l", "--label":
				// TODO(c-bata): complete label
				return []prompt.Suggest{}, true
			case "-L", "--limit":
				return []prompt.Suggest{}, true
			case "-s", "--state":
				return prompt.FilterHasPrefix(
					[]prompt.Suggest{
						{Text: "open"},
						{Text: "closed"},
						{Text: "all"},
					},
					d.GetWordBeforeCursor(),
					true,
				), true
			}
		}
	case "pr":
		if len(cmds) < 2 {
			return []prompt.Suggest{}, false
		}

		switch cmds[1] {
		case "create":
			switch option {
			case "-B", "--base":
				return []prompt.Suggest{}, true
			case "-b", "--body":
				return []prompt.Suggest{}, true
			case "-t", "--title":
				return []prompt.Suggest{}, true
			}
		case "list":
			switch option {
			case "-a", "--assignee":
				return []prompt.Suggest{}, true
			case "-B", "--base":
				return []prompt.Suggest{}, true
			case "-l", "--label":
				// TODO(c-bata): complete label
				return []prompt.Suggest{}, true
			case "-L", "--limit":
				return []prompt.Suggest{}, true
			case "-s", "--state":
				return prompt.FilterHasPrefix(
					[]prompt.Suggest{
						{Text: "open"},
						{Text: "closed"},
						{Text: "merged"},
						{Text: "all"},
					},
					d.GetWordBeforeCursor(),
					true,
				), true
			}
		}
	case "repo":
		if len(cmds) < 2 {
			return []prompt.Suggest{}, false
		}

		switch cmds[1] {
		case "fork":
			switch option {
			case "--clone":
				return []prompt.Suggest{
					{Text: "true"},
					{Text: "false"},
					{Text: "prompt"},
				}, true
			case "--remote":
				return []prompt.Suggest{
					{Text: "true"},
					{Text: "false"},
					{Text: "prompt"},
				}, true
			}
		}
	}

	return []prompt.Suggest{}, false
}

func excludeOptions(args []string) ([]string, bool) {
	l := len(args)
	if l == 0 {
		return nil, false
	}
	filtered := make([]string, 0, l)

	var skipNextArg bool
	for i := 0; i < len(args); i++ {
		if skipNextArg {
			skipNextArg = false
			continue
		}

		for _, s := range []string{
			"-b", "--body",
			"-t", "--title",
			"-a", "--assignee",
			"-l", "--label",
			"-L", "--limit",
			"-s", "--state",
			"-B", "--base",
			"-R", "--repo",
			"-d", "--description",
			"--enable-issues",
			"--enable-wiki",
			"--homepage",
			"-t", "--team",
			"--clone",
			"--remote",
		} {
			if strings.HasPrefix(args[i], s) {
				if strings.Contains(args[i], "=") {
					// we can specify option value like '-o=json'
					skipNextArg = false
				} else {
					skipNextArg = true
				}
				continue
			}
		}
		if strings.HasPrefix(args[i], "-") {
			continue
		}
		filtered = append(filtered, args[i])
	}
	return filtered, skipNextArg
}

--#

--% C:/tmp/rework/gh-prompt/internal/debug/log.go
package debug

import (
	"io/ioutil"
	"log"
	"os"
)

const (
	envEnableLog = "GH_PROMPT_LOG"
	logFileName  = "gh-prompt.log"
)

var (
	logfile *os.File
	logger  *log.Logger
)

func init() {
	enableLog := os.Getenv(envEnableLog)
	if enableLog == "true" || enableLog == "1" {
		var err error
		logfile, err = os.OpenFile(logFileName, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0666)
		if err == nil {
			logger = log.New(logfile, "", log.Llongfile)
			return
		}
	}
	logger = log.New(ioutil.Discard, "", log.Llongfile)
}

// Teardown to close logfile
func Teardown() {
	if logfile == nil {
		return
	}
	_ = logfile.Close()
}

func writeWithSync(calldepth int, msg string) {
	calldepth++
	if logfile == nil {
		return
	}
	_ = logger.Output(calldepth, msg)
	_ = logfile.Sync() // immediately write msg
}

// Log to output message
func Log(msg string) {
	calldepth := 2
	writeWithSync(calldepth, msg)
}

--#

