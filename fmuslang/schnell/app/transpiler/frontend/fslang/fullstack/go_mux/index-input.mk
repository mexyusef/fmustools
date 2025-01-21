--% index/fmus
gomux,d(/mk)
	%utama=__FILE__
	.dockerignore,f(e=utama=C:/dahsyat/mygomux/.dockerignore)
	.gitignore,f(e=utama=C:/dahsyat/mygomux/.gitignore)
	docker-compose.yml,f(e=utama=C:/dahsyat/mygomux/docker-compose.yml)
	Dockerfile,f(e=utama=C:/dahsyat/mygomux/Dockerfile)
	go.mod,f(e=utama=C:/dahsyat/mygomux/go.mod)
	go.sum,f(e=utama=C:/dahsyat/mygomux/go.sum)
	Makefile,f(e=utama=C:/dahsyat/mygomux/Makefile)
	README.md,f(e=utama=C:/dahsyat/mygomux/README.md)
	run.sh,f(e=utama=C:/dahsyat/mygomux/run.sh)
	service,f(b64=C:\work\kenza\sidoarjo-backup\go_mux_index_input.mk=C:/dahsyat/mygomux/service)
	$*chmod a+x *.sh
	cmd,d(/mk)
		cmd.go,f(e=utama=C:/dahsyat/mygomux/cmd/cmd.go)
	http,d(/mk)
		main.go,f(e=utama=C:/dahsyat/mygomux/http/main.go)
		api,d(/mk)
			admin,d(/mk)
				api.go,f(e=utama=C:/dahsyat/mygomux/http/api/admin/api.go)
				user.go,f(e=utama=C:/dahsyat/mygomux/http/api/admin/user.go)
			auth,d(/mk)
				api.go,f(e=utama=C:/dahsyat/mygomux/http/api/auth/api.go)
				login.go,f(e=utama=C:/dahsyat/mygomux/http/api/auth/login.go)
			client,d(/mk)
				api.go,f(e=utama=C:/dahsyat/mygomux/http/api/client/api.go)
				user.go,f(e=utama=C:/dahsyat/mygomux/http/api/client/user.go)
		middleware,d(/mk)
			cors.go,f(e=utama=C:/dahsyat/mygomux/http/middleware/cors.go)
			logger.go,f(e=utama=C:/dahsyat/mygomux/http/middleware/logger.go)
			max_client.go,f(e=utama=C:/dahsyat/mygomux/http/middleware/max_client.go)
		utils,d(/mk)
			handler.go,f(e=utama=C:/dahsyat/mygomux/http/utils/handler.go)
	pkg,d(/mk)
		storage,d(/mk)
			user.go,f(e=utama=C:/dahsyat/mygomux/pkg/storage/user.go)
			user_memory.go,f(e=utama=C:/dahsyat/mygomux/pkg/storage/user_memory.go)
		types,d(/mk)
			types.go,f(e=utama=C:/dahsyat/mygomux/pkg/types/types.go)
		util,d(/mk)
			util.go,f(e=utama=C:/dahsyat/mygomux/pkg/util/util.go)
			graceful,d(/mk)
				graceful.go,f(e=utama=C:/dahsyat/mygomux/pkg/util/graceful/graceful.go)
--#

--% C:/dahsyat/mygomux/.dockerignore
bin/
.env

Dockerfile
Makefile
README.md
--#

--% C:/dahsyat/mygomux/.gitignore
bin/
.env
--#

--% C:/dahsyat/mygomux/docker-compose.yml
version: '3'
services:
  server:
    build: ./
    ports:
      - "3000:3000"
--#

--% C:/dahsyat/mygomux/Dockerfile
#  BASE
FROM golang:alpine as base
WORKDIR /app
COPY go.mod .
COPY go.sum .
RUN go mod download

# BUILDER
FROM base as builder
COPY . .
RUN CGO_ENABLED=0 go build -ldflags "${XFLAGS} -s -w" -a -o service ./cmd/cmd.go

# UPX
# FROM douglaszuqueto/alpine-upx as upx
# FROM alpine as upx
# RUN apk update && apk add --no-cache upx && rm -rf /var/cache/apk/*
# WORKDIR /app
# COPY --from=builder /app/service /app
# RUN upx /app/service

# FINAL
# FROM douglaszuqueto/alpine-go
FROM alpine
ENV TZ=Asia/Bangkok
RUN apk update && apk add --no-cache tzdata ca-certificates && rm -rf /var/cache/apk/*
WORKDIR /app
# COPY --from=upx /app/service /app
COPY --from=builder /app/service /app
CMD ["./service"]

--#

--% C:/dahsyat/mygomux/go.mod
module mexusef/mygomux

go 1.15

require (
	github.com/google/uuid v1.3.0
	github.com/gorilla/handlers v1.5.1
	github.com/gorilla/mux v1.8.0
	golang.org/x/crypto v0.0.0-20220112180741-5e0467b6c7ce
)

--#

--% C:/dahsyat/mygomux/go.sum
github.com/felixge/httpsnoop v1.0.1 h1:lvB5Jl89CsZtGIWuTcDM1E/vkVs49/Ml7JJe07l8SPQ=
github.com/felixge/httpsnoop v1.0.1/go.mod h1:m8KPJKqk1gH5J9DgRY2ASl2lWCfGKXixSwevea8zH2U=
github.com/google/uuid v1.3.0 h1:t6JiXgmwXMjEs8VusXIJk2BXHsn+wx8BZdTaoZ5fu7I=
github.com/google/uuid v1.3.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/gorilla/handlers v1.5.1 h1:9lRY6j8DEeeBT10CvO9hGW0gmky0BprnvDI5vfhUHH4=
github.com/gorilla/handlers v1.5.1/go.mod h1:t8XrUpc4KVXb7HGyJ4/cEnwQiaxrX/hz1Zv/4g96P1Q=
github.com/gorilla/mux v1.8.0 h1:i40aqfkR1h2SlN9hojwV5ZA91wcXFOvkdNIeFDP5koI=
github.com/gorilla/mux v1.8.0/go.mod h1:DVbg23sWSpFRCP0SfiEN6jmj59UnW/n46BH5rLB71So=
golang.org/x/crypto v0.0.0-20220112180741-5e0467b6c7ce h1:Roh6XWxHFKrPgC/EQhVubSAGQ6Ozk6IdxHSzt1mR0EI=
golang.org/x/crypto v0.0.0-20220112180741-5e0467b6c7ce/go.mod h1:IxCIyHEi3zRg3s0A5j5BB6A9Jmi73HwBIUl50j+osU4=
golang.org/x/net v0.0.0-20211112202133-69e39bad7dc2/go.mod h1:9nx3DQGgdP8bBQD5qxJ1jj9UTztislL4KSBs9R2vV5Y=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210423082822-04245dca01da/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/text v0.3.6/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=

--#

--% C:/dahsyat/mygomux/Makefile
# include .env

.EXPORT_ALL_VARIABLES:

dev:
	go run cmd/cmd.go

prod:
	CGO_ENABLED=0
	go build -o ./bin/go-api-boilerplate ./cmd/cmd.go

upx: prod
	upx ./bin/go-api-boilerplate

docker:
	docker build -t douglaszuqueto/go-api-boilerplate .

docker-push: docker
	docker push douglaszuqueto/go-api-boilerplate

.PHONY: dev prod upx docker docker-push

--#

--% C:/dahsyat/mygomux/README.md
**docker-compose.yml,f(t=)

### Admin

| Description | http | path |
|:--:|:--:|:--|
| list | GET | /api/admin/user |
| get  | GET | /api/admin/user/:id |
| store | POST | /api/admin/user  |
| update | PUT | /api/admin/user/:id |
| delete | DELETE | /api/admin/user/:id |

### Public

| Description | http | path |
|:--:|:--:|:--|
| list | GET | /api/user |
| get  | GET | /api/user/:id |

### Auth

| Description | http | path |
|:--:|:--:|:--|
| admin | POST | /api/auth/admin/signin |
| public  | POST | /api/auth/client/signin |

### Standalone

* Build

```bash
make prod
```

* Deploy

```bash
./bin/go-api-boilerplate
```

### Docker

* Build

```bash
make docker
```

* Push

```bash
make docker-push
```

* Deploy

```bash
docker run -it --name go-api-boilerplate \
    -p 3000:3000 \
    douglaszuqueto/go-api-boilerplate:latest
```

--#

--% C:/dahsyat/mygomux/run.sh
CGO_ENABLED=0 go build -ldflags "${XFLAGS} -s -w" -a -o service ./cmd/cmd.go
--#

--% C:/dahsyat/mygomux/cmd/cmd.go
package main

import (
	"context"
	"fmt"
	"log"
	"strconv"
	"time"

	"mexusef/mygomux/http"
	"mexusef/mygomux/pkg/storage"
	"mexusef/mygomux/pkg/util"
	"mexusef/mygomux/pkg/util/graceful"
)

func main() {
	fmt.Println("API boilerplate")

	grace := graceful.New()

	storage.Open()

	insertData()

	// Start the api
	go http.Run()

	grace.Wait()
}

func insertData() {
	for i := 1; i <= 10; i++ {
		idString := strconv.Itoa(i)

		log.Println("Inserindo user:", idString)

		password, _ := util.GeneratePassword("password_" + idString)

		user := storage.User{
			Username:  "username_" + idString,
			Password:  password,
			State:     1,
			CreatedAt: time.Now(),
			UpdatedAt: time.Now().Add(time.Hour),
		}

		_, err := storage.GetDB().CreateUser(context.Background(), user)
		if err != nil {
			log.Println("CreateUser err", err)
		}
	}
}

--#

--% C:/dahsyat/mygomux/http/main.go
package http

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"mexusef/mygomux/http/api/admin"
	"mexusef/mygomux/http/api/auth"
	"mexusef/mygomux/http/api/client"
	"mexusef/mygomux/http/middleware"
	"mexusef/mygomux/http/utils"

	"github.com/gorilla/mux"
)

func routes() *mux.Router {
	router := mux.NewRouter()

	authService := auth.NewAuthAPI()
	adminService := admin.NewAdminAPI()
	clientService := client.NewClientAPI()

	authService.Register(
		router.PathPrefix("/api/auth").Subrouter(),
	)

	adminService.Register(
		router.PathPrefix("/api/admin").Subrouter(),
	)

	clientService.Register(
		router.PathPrefix("/api").Subrouter(),
	)

	router.NotFoundHandler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		json.NewEncoder(w).Encode(utils.ResponseError("error 404"))
	})

	return router
}

// Run run
func Run() {
	// If host is omitted, as in ":8080", Listen listens on all available interfaces instead of just the interface with the given host address
	addr := fmt.Sprintf(":%s", "3000")
	log.Printf("[API] API iniciada: http://0.0.0.0:%s", "3000")

	server := http.Server{
		Addr:         addr,
		Handler:      middleware.CORS(routes()),
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	log.Fatalln(server.ListenAndServe())
}

--#

--% C:/dahsyat/mygomux/http/api/admin/api.go
package admin

import (
	"mexusef/mygomux/http/middleware"
	"mexusef/mygomux/http/utils"

	"github.com/gorilla/mux"
)

// Service service
type Service struct {
	user *userAPI
}

// NewAdminAPI NewAdminAPI
func NewAdminAPI() *Service {
	return &Service{
		user: newUserAPI(),
	}
}

// Register Register
func (s *Service) Register(router *mux.Router) {
	router.Use(middleware.MaxClients)
	router.Use(middleware.Logger)

	routes := utils.Routes{

		// User
		utils.AddRoute("/user", "GET", s.user.All),
		utils.AddRoute("/user", "POST", s.user.Store),
		utils.AddRoute("/user/{id}", "GET", s.user.Get),
		utils.AddRoute("/user/{id}", "PUT", s.user.Update),
		utils.AddRoute("/user/{id}", "DELETE", s.user.Remove),
	}

	for _, r := range routes {
		router.HandleFunc(r.Path, r.Handler).Methods(r.Method)
	}
}

--#

--% C:/dahsyat/mygomux/http/api/admin/user.go
package admin

import (
	"context"
	"encoding/json"
	"net/http"
	"time"

	"mexusef/mygomux/http/utils"
	"mexusef/mygomux/pkg/storage"
)

type userAPI struct{}

func newUserAPI() *userAPI {
	return new(userAPI)
}

// All all
func (h *userAPI) All(w http.ResponseWriter, r *http.Request) {
	users, err := storage.GetDB().ListUser(context.Background())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess("", users))
}

// Get get
func (h *userAPI) Get(w http.ResponseWriter, r *http.Request) {
	id := utils.GetID(r)

	if err := id.IsValid(); err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	user, err := storage.GetDB().GetUser(context.Background(), id.String())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess("", user))
}

type storeRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
	State    uint32 `json:"state"`
}

type updateRequest struct {
	Password string `json:"-"`
	State    uint32 `json:"state"`
}

// Store store
func (h *userAPI) Store(w http.ResponseWriter, r *http.Request) {
	var request storeRequest

	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	user := storage.User{
		Username:  request.Username,
		Password:  request.Password,
		State:     request.State,
		CreatedAt: time.Now(),
		UpdatedAt: time.Now(),
	}

	id, err := storage.GetDB().CreateUser(context.Background(), user)
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess(id, nil))
}

// Update update
func (h *userAPI) Update(w http.ResponseWriter, r *http.Request) {
	id := utils.GetID(r)

	if err := id.IsValid(); err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	userDB, err := storage.GetDB().GetUser(context.Background(), id.String())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	var request updateRequest

	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	user := storage.User{
		ID:        userDB.ID,
		Username:  userDB.Username,
		Password:  request.Password,
		State:     request.State,
		CreatedAt: userDB.CreatedAt,
		UpdatedAt: time.Now(),
	}

	err = storage.GetDB().UpdateUser(context.Background(), user)
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess(user.ID, nil))
}

// Remove remove
func (h *userAPI) Remove(w http.ResponseWriter, r *http.Request) {
	id := utils.GetID(r)

	if err := id.IsValid(); err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	_, err := storage.GetDB().GetUser(context.Background(), id.String())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	err = storage.GetDB().DeleteUser(context.Background(), id.String())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess("", nil))
}

--#

--% C:/dahsyat/mygomux/http/api/auth/api.go
package auth

import (
	"mexusef/mygomux/http/middleware"
	"github.com/gorilla/mux"
)

// Service service
type Service struct {
	login *loginAPI
}

// NewAuthAPI NewAuthAPI
func NewAuthAPI() *Service {
	return &Service{
		login: newLoginAPI(),
	}
}

// Register Register
func (s *Service) Register(router *mux.Router) {
	router.Use(middleware.Logger)
	router.Use(middleware.MaxClients)

	router.HandleFunc("/admin/signin", s.login.AdminAuth).Methods("POST")
	router.HandleFunc("/client/signin", s.login.ClientAuth).Methods("POST")
}

--#

--% C:/dahsyat/mygomux/http/api/auth/login.go
package auth

import (
	"encoding/json"
	"net/http"

	"mexusef/mygomux/http/utils"
)

type loginAPI struct{}

type authRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

func newLoginAPI() *loginAPI {
	return new(loginAPI)
}

// AdminAuth AdminAuth
func (h *loginAPI) AdminAuth(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(utils.ResponseSuccess("", nil))
}

// ClientSignIn ClientSignIn
func (h *loginAPI) ClientAuth(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(utils.ResponseSuccess("", nil))
}

--#

--% C:/dahsyat/mygomux/http/api/client/api.go
package client

import (
	"mexusef/mygomux/http/middleware"
	"mexusef/mygomux/http/utils"

	"github.com/gorilla/mux"
)

// Service service
type Service struct {
	user *userAPI
}

// NewClientAPI NewClientAPI
func NewClientAPI() *Service {
	return &Service{
		user: newUserAPI(),
	}
}

// Register Register
func (s *Service) Register(router *mux.Router) {
	router.Use(middleware.Logger)
	router.Use(middleware.MaxClients)

	routes := utils.Routes{

		// User
		utils.AddRoute("/user", "GET", s.user.All),
		utils.AddRoute("/user/{id}", "GET", s.user.Get),
	}

	for _, r := range routes {
		router.HandleFunc(r.Path, r.Handler).Methods(r.Method)
	}
}

--#

--% C:/dahsyat/mygomux/http/api/client/user.go
package client

import (
	"context"
	"encoding/json"
	"net/http"

	"mexusef/mygomux/http/utils"
	"mexusef/mygomux/pkg/storage"
)

type userAPI struct{}

func newUserAPI() *userAPI {
	return new(userAPI)
}

// All all
func (h *userAPI) All(w http.ResponseWriter, r *http.Request) {
	users, err := storage.GetDB().ListUser(context.Background())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess("", users))
}

// Get get
func (h *userAPI) Get(w http.ResponseWriter, r *http.Request) {
	id := utils.GetID(r)

	if err := id.IsValid(); err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	user, err := storage.GetDB().GetUser(context.Background(), id.String())
	if err != nil {
		json.NewEncoder(w).Encode(utils.ResponseError(err.Error()))
		return
	}

	json.NewEncoder(w).Encode(utils.ResponseSuccess("", user))
}

--#

--% C:/dahsyat/mygomux/http/middleware/cors.go
package middleware

import (
	"net/http"

	"github.com/gorilla/handlers"
	"github.com/gorilla/mux"
)

// CORS cors
func CORS(routes *mux.Router) http.Handler {
	allowedHeaders := []string{"*"}
	allowedMethods := []string{"GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"}
	allowedOrigins := []string{"*"}

	return handlers.CORS(
		handlers.AllowedHeaders(allowedHeaders),
		handlers.AllowedMethods(allowedMethods),
		handlers.AllowedOrigins(allowedOrigins))(routes)
}

--#

--% C:/dahsyat/mygomux/http/middleware/logger.go
package middleware

import (
	"log"
	"net/http"
	"time"
)

// Logger wraps an HTTP handler and logs the request as necessary.
func Logger(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()

		next.ServeHTTP(w, r)

		log.Printf("(%s) \"%s %s %s\" %s", r.RemoteAddr, r.Method, r.RequestURI, r.Proto, time.Since(start))
	})
}

--#

--% C:/dahsyat/mygomux/http/middleware/max_client.go
package middleware

import "net/http"

var sema = make(chan struct{}, 5)

// MaxClients maxClients
func MaxClients(next http.Handler) http.Handler {

	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		sema <- struct{}{}
		next.ServeHTTP(w, r)
		<-sema
	})
}

--#

--% C:/dahsyat/mygomux/http/utils/handler.go
package utils

import (
	"net/http"

	"mexusef/mygomux/pkg/types"
	"github.com/gorilla/mux"
)

// Route route
type Route struct {
	Path    string
	Method  string
	Handler http.HandlerFunc
}

// Routes routes
type Routes []Route

// Error error
type Error struct {
	Error   bool   `json:"error"`
	Message string `json:"message"`
}

// Response as
type Response struct {
	Error Error       `json:"error"`
	Data  interface{} `json:"data"`
}

// Data data response
type Data struct {
	Data interface{} `json:"data"`
}

// AddRoute AddRoute
func AddRoute(path string, method string, handler http.HandlerFunc) Route {
	return Route{path, method, handler}
}

// GetVar getVar
func GetVar(r *http.Request, key string) types.UUID {
	vars := mux.Vars(r)
	id := vars[key]

	return types.UUID(id)
}

// GetID getVar
func GetID(r *http.Request) types.UUID {
	vars := mux.Vars(r)
	id := vars["id"]

	return types.UUID(id)
}

// ResponseSuccess ResponseSuccess
func ResponseSuccess(message string, i interface{}) Response {
	return Response{Error{false, message}, i}
}

// ResponseError ResponseError
func ResponseError(message string) Response {
	return Response{Error{true, message}, nil}
}

--#

--% C:/dahsyat/mygomux/pkg/storage/user.go
package storage

import (
	"context"
	"time"
)

// UserStorage UserStorage
type UserStorage interface {
	ListUser(ctx context.Context) ([]User, error)
	GetUser(ctx context.Context, id string) (User, error)
	CreateUser(ctx context.Context, u User) (string, error)
	UpdateUser(ctx context.Context, u User) error
	DeleteUser(ctx context.Context, id string) error
}

// User User
type User struct {
	ID        string    `json:"id"`
	Username  string    `json:"username"`
	Password  string    `json:"-"`
	State     uint32    `json:"state"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}

var db UserStorage

// GetDB getDB
func GetDB() UserStorage {
	return db
}

// Open open
func Open() {
	GetStorageType()
}

// GetStorageType getStorageType
func GetStorageType() {
	storageType := "memory"

	switch storageType {
	case "memory":
		db = NewUserMemoryStorage()
	default:
		panic("unknow storage type: " + storageType)
	}
}

--#

--% C:/dahsyat/mygomux/pkg/storage/user_memory.go
package storage

import (
	"context"
	"errors"
	"log"
	"sync"

	"mexusef/mygomux/pkg/util"
)

// UserMemoryStorage UserMemoryStorage
type UserMemoryStorage struct {
	db sync.Map
}

// NewUserMemoryStorage NewUserMemoryStorage
func NewUserMemoryStorage() *UserMemoryStorage {
	log.Println("Storage: UserMemoryStorage")

	return &UserMemoryStorage{
		db: sync.Map{},
	}
}

// ListUser ListUser
func (s *UserMemoryStorage) ListUser(ctx context.Context) ([]User, error) {
	var l []User
	s.db.Range(func(key interface{}, value interface{}) bool {
		u, ok := value.(User)
		if !ok {
			return false
		}

		// hide the password
		u.Password = ""

		l = append(l, u)
		return true
	})

	return l, nil
}

// GetUser GetUser
func (s *UserMemoryStorage) GetUser(ctx context.Context, id string) (User, error) {
	var l User

	value, ok := s.db.Load(id)
	if !ok {
		return l, errors.New("not found")
	}

	l = value.(User)

	// hide the password
	l.Password = ""

	return l, nil
}

// CreateUser CreateUser
func (s *UserMemoryStorage) CreateUser(ctx context.Context, u User) (string, error) {
	u.ID = util.GenerateID()

	s.db.Store(u.ID, u)

	return u.ID, nil
}

// UpdateUser UpdateUser
func (s *UserMemoryStorage) UpdateUser(ctx context.Context, u User) error {
	s.db.Store(u.ID, u)

	return nil
}

// DeleteUser DeleteUser
func (s *UserMemoryStorage) DeleteUser(ctx context.Context, id string) error {
	s.db.Delete(id)

	return nil
}

--#

--% C:/dahsyat/mygomux/pkg/types/types.go
package types

import (
	"errors"
	"regexp"
)

// UUID type
type UUID string

var uuidRegex = regexp.MustCompile("^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")

var errInvalidUUID = errors.New("ID invÃ¡lido")

// IsValid isValid
func (u *UUID) IsValid() error {
	if !uuidRegex.MatchString(string(*u)) {
		return errInvalidUUID
	}
	return nil
}

// String string
func (u *UUID) String() string {
	return string(*u)
}

--#

--% C:/dahsyat/mygomux/pkg/util/util.go
package util

import (
	"errors"

	"github.com/google/uuid"
	"golang.org/x/crypto/bcrypt"
)

// GenerateID GenerateID
func GenerateID() string {
	id := uuid.New()

	return id.String()
}

// GeneratePassword generatePassword
func GeneratePassword(password string) (string, error) {
	var passwordRequired error = errors.New("Senha obrigatÃ³ria")

	if len(password) == 0 {
		return "", passwordRequired
	}

	hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.MinCost)
	if err != nil {
		return "", passwordRequired
	}

	return string(hash), nil
}

--#

--% C:/dahsyat/mygomux/pkg/util/graceful/graceful.go
package graceful

import (
	"log"
	"os"
	"os/signal"
	"syscall"
)

// Signals Signals
type Signals struct {
	signalCh chan os.Signal
	doneCh   chan bool
}

// New New
func New() *Signals {
	s := &Signals{
		signalCh: make(chan os.Signal, 1),
		doneCh:   make(chan bool, 1),
	}

	signal.Notify(s.signalCh, syscall.SIGTERM, syscall.SIGINT)

	go func() {
		sig := <-s.signalCh
		log.Println("Signal stop:", sig)

		s.doneCh <- true
	}()

	return s
}

// Wait Wait
func (s *Signals) Wait() {
	<-s.doneCh
}

--#

