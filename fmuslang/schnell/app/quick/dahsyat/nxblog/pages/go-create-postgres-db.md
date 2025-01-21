---
title: Create DB in Postgres
date: 2021/05/25
description: Create DB in Postgres
tag: go, postgresql, lib/pq
author: Yusef
---

My quick way to create a database in Go.

```
package main

import (
	"bufio"
	"database/sql"
	"fmt"
	"log"
	"os"
	_ "github.com/lib/pq"
)

func main() {
	conninfo := fmt.Sprintf("dbname=postgres host=localhost port=9022 user=usef password=rahasia sslmode=disable")
	fmt.Println("connstr:", conninfo)
	db, err := sql.Open("postgres", conninfo)
	if err != nil {
		log.Fatal(err)
	}

	// list sblm create
	hasil, err := db.Query("SELECT datname FROM pg_database WHERE datistemplate = false;")
	if err != nil {
		log.Fatal(err)
	}
	var table string
	counter := 1
	for hasil.Next() {
		hasil.Scan(&table)
		fmt.Println(fmt.Sprintf("%d. %s", counter, table))
		counter += 1
	}

	// create db
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Enter db name to create: ")
	scanner.Scan()
	dbName := scanner.Text()
	if dbName != "" {
		_, err = db.Exec("create database " + dbName)
	}
	if err != nil {
		log.Fatal(err)
	}

	// list setelah create
	hasil, err = db.Query("SELECT datname FROM pg_database WHERE datistemplate = false;")
	if err != nil {
		log.Fatal(err)
	}

	counter = 1
	for hasil.Next() {
		hasil.Scan(&table)
		fmt.Println(fmt.Sprintf("%d. %s", counter, table))
		counter += 1
	}
}
```

```
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"database/sql"
	_ "github.com/lib/pq"
)

func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {

	scn := bufio.NewScanner(os.Stdin)

	fmt.Println("Masukkan DDL create database:")

	var lines []string

	for scn.Scan() {
		line := scn.Text()
		if line == "." {
			break
		}

		lines = append(lines, line)
	}

	if err := scn.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		return
	}

	createTableStatement := strings.Join(lines, "\n")
	fmt.Printf("Terima createTableStatement: %v\n", createTableStatement)
	if len(createTableStatement) > 0 {

		scanner := bufio.NewScanner(os.Stdin)
		fmt.Print("Enter db name to list tables: ")
		scanner.Scan()
		dbName := scanner.Text()
		isCancel := false
		if dbName == "" {
			isCancel = true
		}
		if isCancel {
			return
		}
	
		conninfo := fmt.Sprintf("dbname=%v host=gisel.ddns.net port=9022 user=usef password=rahasia sslmode=disable", dbName)
		fmt.Println("connstr:", conninfo)
		db, err := sql.Open("postgres", conninfo)
		if err != nil {
			log.Fatal(err)
		}

		stmt, err1 := db.Prepare(createTableStatement)
		CheckError(err1)
		defer stmt.Close()
		_, err = stmt.Exec()
		CheckError(err)

		fmt.Println("ok...silahkan cek isi table dg fdb`table~list~fm dan f3")

	}

}

// kurang: list isi table langsung pada dbName
// kurang: describe table
// kurang: select * from all
```

Listing tables in a database in Go
```
package main

import (
	"database/sql"
	"fmt"
	"log"
	_ "github.com/lib/pq"
)

func main() {
	conninfo := fmt.Sprintf("dbname=postgres host=gisel.ddns.net port=9022 user=usef password=rahasia sslmode=disable")
	fmt.Println("connstr:", conninfo)
	db, err := sql.Open("postgres", conninfo)
	if err != nil {
		log.Fatal(err)
	}
	// https://dba.stackexchange.com/questions/1285/how-do-i-list-all-databases-and-tables-using-psql
	hasil, err := db.Query("SELECT datname FROM pg_database WHERE datistemplate = false;")
	if err != nil {
		log.Fatal(err)
	}
	var table string
	counter := 1
	for hasil.Next() {
		hasil.Scan(&table)
		fmt.Println(fmt.Sprintf("%d. %s", counter, table))
		counter += 1
	}
}
```
