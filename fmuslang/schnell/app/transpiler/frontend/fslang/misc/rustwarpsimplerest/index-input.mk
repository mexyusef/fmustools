--% index/fmus
rust-groceries-mongo-api,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/.gitignore)
	Cargo.toml,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/Cargo.toml)
	HAPUS.md,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/HAPUS.md)
	README.md,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/README.md)
	run.bat,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/run.bat)
	run.sh,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/run.sh)
	test.sh,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/test.sh)
    docker-compose.yml,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/rustwarpsimplerest/dc.mk=index/fmus)
    $* chmod a+x *.sh
	src,d(/mk)
		main.rs,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/src/main.rs)
		data,d(/mk)
			mod.rs,f(e=utama=C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/src/data/mod.rs)
--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/.gitignore
/target
NOTES

--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/Cargo.toml
[package]
name = "rust-groceries-mongo-api"
version = "0.1.0"
authors = ["Paul Done"]
edition = "2018"

[dependencies]
bson = "1.1.*"
futures = { version = "0.3.*"}
mongodb = "1.1.*"
serde = {version = "1.0.*", features = ["derive"]}
tokio = {version = "0.2.*", features = ["full"]}
warp = "0.2.*"

--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/HAPUS.md
http://localhost:8080/v1/groceries
--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/README.md
# rust-groceries-mongo-api

Sample Rust project which shows how to easily expose a REST API using the [Warp](https://docs.rs/warp/) web framework, to provide a simple _Groceries_ stock management example scenario. This is based on the commonly referenced [Creating a REST API in Rust with warp](https://blog.logrocket.com/creating-a-rest-api-in-rust-with-warp/) blog post, but refactored to use a MongoDB database as a backing store, rather than the in-memory _HashMap_ used in the blog post. In this project, the [MongoDB Rust Driver](https://docs.rs/mongodb/) is used (in its default _async_ mode) and the [Rust Serde](https://serde.rs/) framework is utilised to easily convert BSON returned from MongoDB into Rust types and then into JSON to be returned by the REST API calls.

## Building & Running The Project

_(ensure you've cloned/copied this GitHub project first to your local machine, and that you have an accessible MongoDB database running locally or remotely)_

 1. Install the latest version of the [Rust development environment](https://www.rust-lang.org/tools/install), if it isn't already installed, via the __rustup__ utility, including the _rustc_ compiler & the _cargo_ package/build manager. _NOTE:_ If building on Windows 10, first ensure you have Microsoft's [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16) installed (and importantly, when running Micosrosoft's _build tools_ installer, choose the _C++ build tools_ option)

 2. From a terminal/prompt/shell, from this project's root folder, run Rust's _cargo_ command to build the project and run the debug version of the application which will start listening for Grocery REST API requests, as shown in the example below (change the URL to match the specific MongoDB database deployment target you want to test):
 
```console
cargo build
# Example connnecting to locally running MongoDB database
cargo run -- 'mongodb://localhost:27017'
# Example connnecting to a remote MongoDB Atlas clustered database
cargo run -- 'mongodbv+srv://myusr:pswd@mycluster.a113z.mongodb.net'
```

&nbsp;_OPTIONAL_: Build an _executable_ version of the application and then run it:
```console
cargo build --release
target/release/rust-groceries-mongo-api 'mongodb://localhost:27017'
```

## Testing The REST API Via The Command Line

From a terminal/prompt/shell, the following commands can be run to test the running REST API Groceries service (you can also run the `./test.sh` script provided in this project, which automates these tests)...

&nbsp;__Insert 3 apples:__
```console
curl -sS --location --request POST 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples",
    "quantity": 3
}'
```

&nbsp;__List all the groceries in stock:__
```console
curl -sS --location --request GET 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain'
```

&nbsp;__Add 5 more apples:__
```console
curl -sS --location --request PUT 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples",
    "quantity": 5
}'
```

&nbsp;__Delete all the apples:__
```console
curl --location --request DELETE 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples"
}'
```


--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/run.bat
cargo run -- 'mongodb://usef:rahasia@__IF_ETH0'
--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/run.sh
cargo run -- 'mongodb://usef:rahasia@__IF_ETH0'

--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/test.sh
#!/bin/bash

if ! which jq > /dev/null; then
    printf "'jq' utility is not on the path - install it first - e.g.: sudo apt install jq"
fi

printf "\nInitial HTTP GET output: \n"
curl -sS --location --request GET 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain'

printf "\nDelete Apples HTTP DELETE output: \n"
curl -sS --location --request DELETE 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples"
}'

printf "\nTest no apples HTTP GET result: \n"
if ! curl -sS --location --request GET 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' | jq '.[] | select(.name=="apples")' | grep apples; then
    printf "\n----OK: No apples exist\n"
else
    printf "\n----ERROR: Apples exist\n"
    exit 1
fi

printf "\nAdd Apples HTTP POST output: \n"
curl -sS --location --request POST 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples",
    "quantity": 3
}'

printf "\nTest apples exist HTTP GET result: \n"
if ! curl -sS --location --request GET 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' | jq '.[] | select(.name=="apples")' | grep apples; then
    printf "\n----ERROR: No apples exist\n"
    exit 1
else
    printf "\n----OK: Apples exist\n"
fi

printf "\nDelete Apples HTTP DELETE output: \n"
curl --location --request DELETE 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples"
}'

printf "\nTest no apples HTTP GET result: \n"
if ! curl -sS --location --request GET 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' | jq '.[] | select(.name=="apples")' | grep apples; then
    printf "\n----OK: No apples exist\n"
else
    printf "\n----ERROR: Apples exist\n"
    exit 1
fi

printf "\nAdd Apples HTTP PUT output: \n"
curl -sS --location --request PUT 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "name": "apples",
    "quantity": 5
}'

printf "\nTest apples exist HTTP GET result: \n"
if ! curl -sS --location --request GET 'localhost:8080/v1/groceries' \
--header 'Content-Type: application/json' \
--header 'Content-Type: text/plain' | jq '.[] | select(.name=="apples")' | grep apples; then
    printf "\n----ERROR: No apples exist\n"
    exit 1
else
    printf "\n----OK: Apples exist\n"
fi

printf "\n"

--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/src/main.rs
use std::env;
use std::error::Error;
use std::net::Ipv4Addr;
use std::process::exit;
use warp::{http, Filter};


mod data;
pub use crate::data::{GroceryId, GroceryItem, GroceryMgr};


const LISTEN_ADDRESS: Ipv4Addr = Ipv4Addr::new(127, 0, 0, 1);
const LISTEN_PORT: u16 = 8080;
const RSC_NAME: &str = "groceries";
const PAYLOAD_LIMIT: u64 = 1024 * 16;


// Main app which starts Groceries REST API listener
//
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error + Send + Sync>> {
    let url = get_url_arg_or_exit();
    let groceries = GroceryMgr::new(&url).await?;
    let groceries_ref = warp::any().map(move || groceries.clone());
    let api_path_filter_chain = warp::path("v1")
        .and(warp::path(RSC_NAME))
        .and(warp::path::end());
    let upsert_filter_chain = api_path_filter_chain
        .and(capture_grocery_json())
        .and(groceries_ref.clone())
        .and_then(upsert_grocery_list);
    // POST filter chain
    let add_items = warp::post()
        .and(upsert_filter_chain.clone());
    // PUT filter chain
    let update_item = warp::put()
        .and(upsert_filter_chain.clone());
    // GET filter chain
    let get_items = warp::get()
        .and(api_path_filter_chain)
        .and(groceries_ref.clone())
        .and_then(get_grocery_list);
    // DELETE filter chain
    let delete_item = warp::delete()
        .and(api_path_filter_chain)
        .and(capture_grocery_id_json())
        .and(groceries_ref.clone())
        .and_then(delete_grocery_list);
    let routes = add_items.or(get_items).or(delete_item).or(update_item);
    warp::serve(routes).run((LISTEN_ADDRESS, LISTEN_PORT)).await;
    Ok(())
}


// Extract the URL parameter passed on the command line or exit if not provided
//
fn get_url_arg_or_exit() -> String {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("\nERROR: A MongoDB URL needs to provided as an argument to this tool\n");
        exit(1);
    }

    args[1].to_string()
}


// Insert/update grocery item record in back-end DB
//
async fn upsert_grocery_list(item: GroceryItem, groceries: GroceryMgr)
                             -> Result<impl warp::Reply, warp::Rejection> {
    match groceries.db_upsert_groceries(item).await {
        Ok(_) => Ok(warp::reply::with_status("Added items to the grocery list",
                    http::StatusCode::CREATED)),
        Err(e) => {
            eprintln!("Error upserting data: {:#?}", e);
            Err(warp::reject())
        }
    }

}


// Find all grocery item records from back-end DB
//
async fn get_grocery_list(groceries: GroceryMgr)
                          -> Result<impl warp::Reply, warp::Rejection> {
    match groceries.db_find_groceries().await {
        Ok(result) => Ok(warp::reply::json(&result)),
        Err(e) => {
            eprintln!("Error deleting data: {}", e.to_string());
            Err(warp::reject())
        }
    }
}


// Delete specific grocery item record from back-end DB
//
async fn delete_grocery_list(id: GroceryId, groceries: GroceryMgr)
                             -> Result<impl warp::Reply, warp::Rejection> {
    match groceries.db_delete_groceries(id).await {
        Ok(_) => Ok(warp::reply::with_status("Removed item from grocery list",
                    http::StatusCode::OK)),
        Err(e) => {
            eprintln!("Error deleting data: {}", e.to_string());
            Err(warp::reject())
        }
    }
}


// Capture Grocery Item full record JSON request payload JSON content
//
fn capture_grocery_json() -> impl Filter<Extract = (GroceryItem,),
                                         Error = warp::Rejection> + Clone {
    warp::body::content_length_limit(PAYLOAD_LIMIT).and(warp::body::json())
}


// Capture Grocery Item Id JSON request payload JSON content
//
fn capture_grocery_id_json() -> impl Filter<Extract = (GroceryId,),
                                            Error = warp::Rejection> + Clone {
    warp::body::content_length_limit(PAYLOAD_LIMIT).and(warp::body::json())
}

--#

--% C:/work/hapus-iterative-fullstack/proshop2/rust-groceries-mongo-api/src/data/mod.rs
use futures::prelude::*;
use mongodb::{
    bson::doc,
    options::{FindOptions, UpdateOptions},
    {Client, Collection},
};
use serde::{Deserialize, Serialize};
use std::error::Error;


const DB_NAME: &str = "groceries";
const COLL_NAME: &str = "items";


#[derive(Debug, Clone)]
pub struct GroceryMgr {
    coll: Collection,
}


// Grocery item record
#[derive(Debug, Deserialize, Serialize, Clone)]
pub struct GroceryItem {
    pub name: String,
    pub quantity: i32,
}



// Grocery item id
#[derive(Debug, Deserialize, Serialize, Clone)]
pub struct GroceryId {
    pub name: String,
}


// Manages interaction with Grocery datbaase collection
//
impl GroceryMgr {
    // Create new instance of Grocery manager using provided MongoDB URL
    //
    pub async fn new(db_url: &str) -> Result<Self, Box<dyn Error + Send + Sync>> {
        let client = Client::with_uri_str(db_url).await?;
        let coll = client.database(DB_NAME).collection(COLL_NAME);
        Ok(GroceryMgr { coll })
    }


    // Query Groceries collection returning list of all grocery items & quantities
    //
    pub async fn db_find_groceries(&self) -> Result<Vec<GroceryItem>, Box<dyn Error>> {
        let mut results = vec![];
        let find_options = FindOptions::builder().sort(doc! {"name": 1}).build();
        let mut cursor = self.coll.find(doc! {}, find_options).await?;

        while let Some(record) = cursor.next().await {
            match record {
                Ok(doc) => results.push(bson::de::from_bson(bson::Bson::Document(doc.clone()))?),
                Err(e) => return Err(e.into()),
            };
        }

        Ok(results)
    }


    // Insert/update new/existing Grocery item record with adding new quantity
    //
    pub async fn db_upsert_groceries(&self, item: GroceryItem) -> Result<(), Box<dyn Error>> {
        let update_options = UpdateOptions::builder().upsert(true).build();
        self.coll
            .update_one(
                doc! {"name": item.name},
                doc! {"$inc": {"quantity": item.quantity}},
                update_options,
            )
            .await?;
        Ok(())
    }


    // Delete Grocey item record from Groceries collection which matches item name
    //
    pub async fn db_delete_groceries(&self, id: GroceryId) -> Result<(), Box<dyn Error>> {
        self.coll.delete_one(doc! {"name": id.name}, None).await?;
        Ok(())
    }
}

--#
