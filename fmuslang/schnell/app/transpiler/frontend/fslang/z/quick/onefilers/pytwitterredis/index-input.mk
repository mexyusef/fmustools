--% index/fmus
pytwidis,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=C:/work/rework/redis-twitter-console/.gitignore)
	LICENSE,f(e=utama=C:/work/rework/redis-twitter-console/LICENSE)
	Pipfile,f(e=utama=C:/work/rework/redis-twitter-console/Pipfile)
	Pipfile.lock,f(e=utama=C:/work/rework/redis-twitter-console/Pipfile.lock)
	README.md,f(e=utama=C:/work/rework/redis-twitter-console/README.md)
	redis-twitter-console,d(/mk)
		authentication.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/authentication.py)
		database.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/database.py)
		errors.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/errors.py)
		main.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/main.py)
		users.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/users.py)
		utils.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/utils.py)
		views.py,f(e=utama=C:/work/rework/redis-twitter-console/redis-twitter-console/views.py)
--#

--% C:/work/rework/redis-twitter-console/.gitignore
# IDE
.vscode/

# Environment
.env

--#

--% C:/work/rework/redis-twitter-console/LICENSE
MIT License

Copyright (c) 2021 Nicholas Dwiarto W.

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

--% C:/work/rework/redis-twitter-console/Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
redis = "*"

[dev-packages]
black = "*"
pylint = "*"
python-dotenv = "*"

[scripts]
start = "python redis-twitter-console/main.py"
lint = "pylint redis-twitter-console/"
format = "black redis-twitter-console/"

[requires]
python_version = "3.9"

[pipenv]
allow_prereleases = true

--#

--% C:/work/rework/redis-twitter-console/Pipfile.lock
{
    "_meta": {
        "hash": {
            "sha256": "8320a57a21d6aec26611895b5e8475f7c00227b6ea7c1c74b0aa7d2ad05a5fa1"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.9"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "redis": {
            "hashes": [
                "sha256:0e7e0cfca8660dea8b7d5cd8c4f6c5e29e11f31158c0b0ae91a397f00e5a05a2",
                "sha256:432b788c4530cfe16d8d943a09d40ca6c16149727e4afe8c2c9d5580c59d9f24"
            ],
            "index": "pypi",
            "version": "==3.5.3"
        }
    },
    "develop": {
        "appdirs": {
            "hashes": [
                "sha256:7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41",
                "sha256:a841dacd6b99318a741b166adb07e19ee71a274450e68237b4650ca1055ab128"
            ],
            "version": "==1.4.4"
        },
        "astroid": {
            "hashes": [
                "sha256:4db03ab5fc3340cf619dbc25e42c2cc3755154ce6009469766d7143d1fc2ee4e",
                "sha256:8a398dfce302c13f14bab13e2b14fe385d32b73f4e4853b9bdfb64598baa1975"
            ],
            "markers": "python_version ~= '3.6'",
            "version": "==2.5.6"
        },
        "black": {
            "hashes": [
                "sha256:bff7067d8bc25eb21dcfdbc8c72f2baafd9ec6de4663241a52fb904b304d391f",
                "sha256:fc9bcf3b482b05c1f35f6a882c079dc01b9c7795827532f4cc43c0ec88067bbc"
            ],
            "index": "pypi",
            "version": "==21.4b2"
        },
        "click": {
            "hashes": [
                "sha256:d2b5255c7c6349bc1bd1e59e08cd12acbbd63ce649f2588755783aa94dfb6b1a",
                "sha256:dacca89f4bfadd5de3d7489b7c8a566eee0d3676333fbb50030263894c38c0dc"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
            "version": "==7.1.2"
        },
        "colorama": {
            "hashes": [
                "sha256:5941b2b48a20143d2267e95b1c2a7603ce057ee39fd88e7329b0c292aa16869b",
                "sha256:9f47eda37229f68eee03b24b9748937c7dc3868f906e8ba69fbcbdd3bc5dc3e2"
            ],
            "markers": "sys_platform == 'win32'",
            "version": "==0.4.4"
        },
        "isort": {
            "hashes": [
                "sha256:0a943902919f65c5684ac4e0154b1ad4fac6dcaa5d9f3426b732f1c8b5419be6",
                "sha256:2bb1680aad211e3c9944dbce1d4ba09a989f04e238296c87fe2139faa26d655d"
            ],
            "markers": "python_version >= '3.6' and python_version < '4.0'",
            "version": "==5.8.0"
        },
        "lazy-object-proxy": {
            "hashes": [
                "sha256:17e0967ba374fc24141738c69736da90e94419338fd4c7c7bef01ee26b339653",
                "sha256:1fee665d2638491f4d6e55bd483e15ef21f6c8c2095f235fef72601021e64f61",
                "sha256:22ddd618cefe54305df49e4c069fa65715be4ad0e78e8d252a33debf00f6ede2",
                "sha256:24a5045889cc2729033b3e604d496c2b6f588c754f7a62027ad4437a7ecc4837",
                "sha256:410283732af311b51b837894fa2f24f2c0039aa7f220135192b38fcc42bd43d3",
                "sha256:4732c765372bd78a2d6b2150a6e99d00a78ec963375f236979c0626b97ed8e43",
                "sha256:489000d368377571c6f982fba6497f2aa13c6d1facc40660963da62f5c379726",
                "sha256:4f60460e9f1eb632584c9685bccea152f4ac2130e299784dbaf9fae9f49891b3",
                "sha256:5743a5ab42ae40caa8421b320ebf3a998f89c85cdc8376d6b2e00bd12bd1b587",
                "sha256:85fb7608121fd5621cc4377a8961d0b32ccf84a7285b4f1d21988b2eae2868e8",
                "sha256:9698110e36e2df951c7c36b6729e96429c9c32b3331989ef19976592c5f3c77a",
                "sha256:9d397bf41caad3f489e10774667310d73cb9c4258e9aed94b9ec734b34b495fd",
                "sha256:b579f8acbf2bdd9ea200b1d5dea36abd93cabf56cf626ab9c744a432e15c815f",
                "sha256:b865b01a2e7f96db0c5d12cfea590f98d8c5ba64ad222300d93ce6ff9138bcad",
                "sha256:bf34e368e8dd976423396555078def5cfc3039ebc6fc06d1ae2c5a65eebbcde4",
                "sha256:c6938967f8528b3668622a9ed3b31d145fab161a32f5891ea7b84f6b790be05b",
                "sha256:d1c2676e3d840852a2de7c7d5d76407c772927addff8d742b9808fe0afccebdf",
                "sha256:d7124f52f3bd259f510651450e18e0fd081ed82f3c08541dffc7b94b883aa981",
                "sha256:d900d949b707778696fdf01036f58c9876a0d8bfe116e8d220cfd4b15f14e741",
                "sha256:ebfd274dcd5133e0afae738e6d9da4323c3eb021b3e13052d8cbd0e457b1256e",
                "sha256:ed361bb83436f117f9917d282a456f9e5009ea12fd6de8742d1a4752c3017e93",
                "sha256:f5144c75445ae3ca2057faac03fda5a902eff196702b0a24daf1d6ce0650514b"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
            "version": "==1.6.0"
        },
        "mccabe": {
            "hashes": [
                "sha256:ab8a6258860da4b6677da4bd2fe5dc2c659cff31b3ee4f7f5d64e79735b80d42",
                "sha256:dd8d182285a0fe56bace7f45b5e7d1a6ebcbf524e8f3bd87eb0f125271b8831f"
            ],
            "version": "==0.6.1"
        },
        "mypy-extensions": {
            "hashes": [
                "sha256:090fedd75945a69ae91ce1303b5824f428daf5a028d2f6ab8a299250a846f15d",
                "sha256:2d82818f5bb3e369420cb3c4060a7970edba416647068eb4c5343488a6c604a8"
            ],
            "version": "==0.4.3"
        },
        "pathspec": {
            "hashes": [
                "sha256:86379d6b86d75816baba717e64b1a3a3469deb93bb76d613c9ce79edc5cb68fd",
                "sha256:aa0cb481c4041bf52ffa7b0d8fa6cd3e88a2ca4879c533c9153882ee2556790d"
            ],
            "version": "==0.8.1"
        },
        "pylint": {
            "hashes": [
                "sha256:586d8fa9b1891f4b725f587ef267abe2a1bad89d6b184520c7f07a253dd6e217",
                "sha256:f7e2072654a6b6afdf5e2fb38147d3e2d2d43c89f648637baab63e026481279b"
            ],
            "index": "pypi",
            "version": "==2.8.2"
        },
        "python-dotenv": {
            "hashes": [
                "sha256:00aa34e92d992e9f8383730816359647f358f4a3be1ba45e5a5cefd27ee91544",
                "sha256:b1ae5e9643d5ed987fc57cc2583021e38db531946518130777734f9589b3141f"
            ],
            "index": "pypi",
            "version": "==0.17.1"
        },
        "regex": {
            "hashes": [
                "sha256:01afaf2ec48e196ba91b37451aa353cb7eda77efe518e481707e0515025f0cd5",
                "sha256:11d773d75fa650cd36f68d7ca936e3c7afaae41b863b8c387a22aaa78d3c5c79",
                "sha256:18c071c3eb09c30a264879f0d310d37fe5d3a3111662438889ae2eb6fc570c31",
                "sha256:1e1c20e29358165242928c2de1482fb2cf4ea54a6a6dea2bd7a0e0d8ee321500",
                "sha256:281d2fd05555079448537fe108d79eb031b403dac622621c78944c235f3fcf11",
                "sha256:314d66636c494ed9c148a42731b3834496cc9a2c4251b1661e40936814542b14",
                "sha256:32e65442138b7b76dd8173ffa2cf67356b7bc1768851dded39a7a13bf9223da3",
                "sha256:339456e7d8c06dd36a22e451d58ef72cef293112b559010db3d054d5560ef439",
                "sha256:3916d08be28a1149fb97f7728fca1f7c15d309a9f9682d89d79db75d5e52091c",
                "sha256:3a9cd17e6e5c7eb328517969e0cb0c3d31fd329298dd0c04af99ebf42e904f82",
                "sha256:47bf5bf60cf04d72bf6055ae5927a0bd9016096bf3d742fa50d9bf9f45aa0711",
                "sha256:4c46e22a0933dd783467cf32b3516299fb98cfebd895817d685130cc50cd1093",
                "sha256:4c557a7b470908b1712fe27fb1ef20772b78079808c87d20a90d051660b1d69a",
                "sha256:52ba3d3f9b942c49d7e4bc105bb28551c44065f139a65062ab7912bef10c9afb",
                "sha256:563085e55b0d4fb8f746f6a335893bda5c2cef43b2f0258fe1020ab1dd874df8",
                "sha256:598585c9f0af8374c28edd609eb291b5726d7cbce16be6a8b95aa074d252ee17",
                "sha256:619d71c59a78b84d7f18891fe914446d07edd48dc8328c8e149cbe0929b4e000",
                "sha256:67bdb9702427ceddc6ef3dc382455e90f785af4c13d495f9626861763ee13f9d",
                "sha256:6d1b01031dedf2503631d0903cb563743f397ccaf6607a5e3b19a3d76fc10480",
                "sha256:741a9647fcf2e45f3a1cf0e24f5e17febf3efe8d4ba1281dcc3aa0459ef424dc",
                "sha256:7c2a1af393fcc09e898beba5dd59196edaa3116191cc7257f9224beaed3e1aa0",
                "sha256:7d9884d86dd4dd489e981d94a65cd30d6f07203d90e98f6f657f05170f6324c9",
                "sha256:90f11ff637fe8798933fb29f5ae1148c978cccb0452005bf4c69e13db951e765",
                "sha256:919859aa909429fb5aa9cf8807f6045592c85ef56fdd30a9a3747e513db2536e",
                "sha256:96fcd1888ab4d03adfc9303a7b3c0bd78c5412b2bfbe76db5b56d9eae004907a",
                "sha256:97f29f57d5b84e73fbaf99ab3e26134e6687348e95ef6b48cfd2c06807005a07",
                "sha256:980d7be47c84979d9136328d882f67ec5e50008681d94ecc8afa8a65ed1f4a6f",
                "sha256:a91aa8619b23b79bcbeb37abe286f2f408d2f2d6f29a17237afda55bb54e7aac",
                "sha256:ade17eb5d643b7fead300a1641e9f45401c98eee23763e9ed66a43f92f20b4a7",
                "sha256:b9c3db21af35e3b3c05764461b262d6f05bbca08a71a7849fd79d47ba7bc33ed",
                "sha256:bd28bc2e3a772acbb07787c6308e00d9626ff89e3bfcdebe87fa5afbfdedf968",
                "sha256:bf5824bfac591ddb2c1f0a5f4ab72da28994548c708d2191e3b87dd207eb3ad7",
                "sha256:c0502c0fadef0d23b128605d69b58edb2c681c25d44574fc673b0e52dce71ee2",
                "sha256:c38c71df845e2aabb7fb0b920d11a1b5ac8526005e533a8920aea97efb8ec6a4",
                "sha256:ce15b6d103daff8e9fee13cf7f0add05245a05d866e73926c358e871221eae87",
                "sha256:d3029c340cfbb3ac0a71798100ccc13b97dddf373a4ae56b6a72cf70dfd53bc8",
                "sha256:e512d8ef5ad7b898cdb2d8ee1cb09a8339e4f8be706d27eaa180c2f177248a10",
                "sha256:e8e5b509d5c2ff12f8418006d5a90e9436766133b564db0abaec92fd27fcee29",
                "sha256:ee54ff27bf0afaf4c3b3a62bcd016c12c3fdb4ec4f413391a90bd38bc3624605",
                "sha256:fa4537fb4a98fe8fde99626e4681cc644bdcf2a795038533f9f711513a862ae6",
                "sha256:fd45ff9293d9274c5008a2054ecef86a9bfe819a67c7be1afb65e69b405b3042"
            ],
            "version": "==2021.4.4"
        },
        "toml": {
            "hashes": [
                "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b",
                "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f"
            ],
            "markers": "python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "version": "==0.10.2"
        },
        "wrapt": {
            "hashes": [
                "sha256:b62ffa81fb85f4332a4f609cab4ac40709470da05643a082ec1eb88e6d9b97d7"
            ],
            "version": "==1.12.1"
        }
    }
}

--#

--% C:/work/rework/redis-twitter-console/README.md
# Redis Twitter Console

Sample application to demonstrate the usage of Redis and Python Console to make a simple Twitter clone.

## Introduction

This application is a port from [Redis's official guidelines](https://redis.io/topics/twitter-clone). It was written in PHP and it used Redis on Linux. My version uses [Redis Labs](https://redislabs.com/), which is Redis database on cloud, similar to MongoDB Atlas. This application also supports Redis on Linux too, so you have no need to worry.

## Database Schema

Redis is not your usual database. It is a data-structure database used for caching, but with the right design, it could also be used as a conventional database (with the additional feature of being extremely fast). We use hashes to store data, and hashes/lists/sorted sets to store identifiers, according to Redis's guide. In this application, the notation `uid` means user-id and `tid` means the tweet-id.

Keys used here are as follows:

- `next_user_id`, a sequence used to auto-increment `user_id`, used in `user`, `users`, and `tweet_user`.
- `next_tweet_id`, a sequence used to auto-increment `tweet_id`, used in `tweets` and `tweet_user`.
- `users`, a hash to store all references of primary keys used to identify users (`uid`).
- `user:{uid}`, a hash used to store the user's data. Referenced by the `users` hash.
- `followers:{uid}`, a sorted set with the aim to store the latest followers of a user (`uid`).
- `following:{uid}`, a sorted set with the aim to store the latest followings of a user (`uid`).
- `tweets:{tid}`, a hash used to store all of the tweets.
- `tweet_user:{uid}`, a list to store all references to a user's tweet (`tid`).
- `timeline`, a list to store all references to the latest 1000 tweets (`tid`).

For further information, try all of the features, then check the condition of the database by using the 'Get All Data (Debug)' functionality in the application.

## Features

- User can sign up and login. **For the sake of simplicity, passwords are stored in plaintext.**
- User can get their own profile. They can see their personal data, their tweets, their followers, and their followings.
- User can post their own tweet.
- User can follow someone.
- User can see other users profile.
- User can unfollow someone.
- User can see the global timeline of the latest 1000 posts.
- User can update their own username.
- User can log out.
- User can exit the application.
- User can get all data available in the Redis database.
- User can flush the Redis database.
- Error handling exists in every module. Some edge test-cases are also covered in this application.
- Every function is documented properly.

## Requirements

- Python 3.5 and up
- Pipenv version 2020 and up
- Redis version 4.0 and up

## Installation

- Clone the repository.

```bash
git clone
```

- Switch to the repository.

```bash
cd redis-twitter-console
```

- Activate `pipenv` shell.

```bash
pipenv shell
```

- Install all dependencies.

```bash
pipenv install
```

- Setup environment variables in an `.env` file.

```bash
touch .env
nano .env

# fill the environment variables here
REDIS_HOST=YOUR_REDIS_HOST
REDIS_PORT=YOUR_REDIS_PORT
REDIS_PASSWORD=YOUR_REDIS_PASSWORD
```

- Run the application.

```bash
pipenv run start
```

## Development

After coding, do not forget to run the formatter, linter, and type-checker.

```bash
pipenv shell
pipenv run format
pipenv run lint
```

## Notes

Will be moved to [@lauslim12-old](https://github.com/lauslim12-old/) soon as this is only a temporary repository that I use to familiarize myself with Redis environment.

## License

MIT License. Feel free to use this as you see fit.

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/authentication.py
"""This Python module is for authentication purposes."""

from time import time
from typing import Callable, Literal, Union

from redis import Redis

from errors import DuplicateUserError, EmptyInputError, NotAuthenticatedError
from utils import is_string_blank


def auth_guard(uid: int) -> bool:
    """Checks if the current user is authenticated or not.

    Parameters:
    -----------
    uid (int): User id

    Returns:
    --------
    bool: If the user is logged is logged in, else raise exception
    """
    if not uid:
        raise NotAuthenticatedError()

    return True


def sign_in(redis: Redis) -> Union[int, bool]:
    """Logs in a user with an algorithm.

    Algorithm:
    ----------
    1. Get username and password.
    2. Sanity check, ensure that inputs are fulfilled.
    3. Check if username exists. If yes, fetch data from 'user' HSET.
    4. Check if passwords match.

    Parameters:
    -----------
    redis (Redis): Redis instance

    Returns:
    --------
    int or None: Either integer or boolean
    """
    username = input("Input your username: ")
    password = input("Input your password: ")

    if is_string_blank(username) or is_string_blank(password):
        raise EmptyInputError()

    user_id = redis.hget("users", username)

    if not user_id:
        print("Wrong username or password!")
        return False

    real_password = redis.hget(f"user:{user_id}", "password")

    if password != real_password:
        print("Wrong username or password!")
        return False

    print("You have been successfully authenticated!")
    return user_id


def sign_up(redis: Redis):
    """Signs up a user. Algorithm:

    Algorithm:
    ----------
    1. Increment 'user_id'.
    2. Sanity check, if username or password is empty, raise exception.
    3. Check if the user exists.
    4. Store username and password in a 'user' HSET.
    5. Store the primary key (user_id) in 'users' HSET for easy fetching.

    Parameters:
    -----------
    redis (Redis): Redis instance

    Returns:
    --------
    None

    """
    username = input("Input your username: ")
    password = input("Input your password: ")

    if is_string_blank(username) or is_string_blank(password):
        raise EmptyInputError()

    if redis.hexists("users", username):
        raise DuplicateUserError()

    user_id = redis.incr("next_user_id")

    user_data = {
        "uid": user_id,
        "username": username,
        "password": password,
        "registration_date": int(time()),
        "modification_date": int(time()),
    }

    redis.hset(f"user:{user_id}", mapping=user_data)
    redis.hset("users", username, user_id)

    print("You have been successfully signed up!")


def with_authentication(
    custom_function: Callable, uid: int, *args: tuple
) -> Union[Callable, bool]:
    """Closure that returns a function, used to check for authentication."""
    if auth_guard(uid):
        return custom_function(*args)

    return False

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/database.py
"""This module is to configure our database."""

from dotenv import dotenv_values, find_dotenv
from redis import Redis, StrictRedis


def flush_database(redis: Redis) -> None:
    """Flushes our database."""
    redis.flushdb()
    print("Database flushed!")


def get_all_data(redis: Redis) -> None:
    """Gets all data that are available at your Redis instance."""
    strings = []
    hashes = []
    zsets = []
    lists = []
    sets = []

    keys = redis.keys("*")
    print(f"Keys available: {keys}", end="\n")

    for key in keys:
        redis_type = redis.type(key)

        if redis_type == "string":
            vals = redis.get(key)
            strings.append(f"Key is '{key}' - Data type is string: {vals}")

        if redis_type == "hash":
            vals = redis.hgetall(key)
            hashes.append(f"Key is '{key}' - Data type is hash: {vals}")

        if redis_type == "zset":
            vals = redis.zrange(key, 0, -1)
            zsets.append(f"Key is '{key}' - Data type is sorted set: {vals}")

        if redis_type == "list":
            vals = redis.lrange(key, 0, -1)
            lists.append(f"Key is '{key}' - Data type is list: {vals}")

        if redis_type == "set":
            vals = redis.smembers(key)
            sets.append(f"Key is '{key}' - Data type is set: {vals}")

    print("\nStrings: ")
    for item in strings:
        print(item)

    print("\nHashes: ")
    for item in hashes:
        print(item)

    print("\nZsets: ")
    for item in zsets:
        print(item)

    print("\nLists: ")
    for item in lists:
        print(item)

    print("\nSets: ")
    for item in sets:
        print(item)


def redis_init() -> Redis:
    """Initializes Redis session."""
    config = dotenv_values(find_dotenv())

    redis = StrictRedis(
        host=config["REDIS_HOST"],
        port=config["REDIS_PORT"],
        password=config["REDIS_PASSWORD"],
        decode_responses=True,
    )

    return redis

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/errors.py
"""This module is to catch custom operational errors."""


class DuplicateUserError(Exception):
    """Error will be thrown if there are duplicate users."""

    def __init__(self):
        super().__init__(self)
        self.message = "User is already registered!"


class EmptyInputError(Exception):
    """Error will be thrown if the user fails to enter an input."""

    def __init__(self):
        super().__init__(self)
        self.message = "Your input is empty! Please fill in the input!"


class FollowError(Exception):
    """Error will be thrown if the user attempts to follow themselves."""

    def __init__(self):
        super().__init__(self)
        self.message = "You cannot follow yourself!"


class NotAuthenticatedError(Exception):
    """Error will be thrown if the users is not authenticated."""

    def __init__(self):
        super().__init__(self)
        self.message = "You are not authenticated! Please log in!"


class UserDoesNotExistError(Exception):
    """Error will be thrown if the user searched does not exist."""

    def __init__(self):
        super().__init__(self)
        self.message = "User that you are looking for does not exist!"


class UserIsNotYourFollowingError(Exception):
    """Error will be thrown if the user is not a part of your 'following'."""

    def __init__(self):
        super().__init__(self)
        self.message = "User that you want to remove is not a part of your following!"

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/main.py
"""This module is the starting point of our application."""

from typing import Union

# Our modules
from authentication import sign_in, sign_up, with_authentication
from database import redis_init, get_all_data, flush_database
from errors import (
    DuplicateUserError,
    EmptyInputError,
    FollowError,
    NotAuthenticatedError,
    UserDoesNotExistError,
    UserIsNotYourFollowingError,
)
from users import (
    follow,
    logout,
    profile,
    other_profile,
    timeline,
    tweet,
    unfollow,
    update_profile,
)
from views import exit_menu, main_menu


def main():
    """Main function that will be run in the application."""
    # Only needs this global variable to keep track of sessions
    authentication: Union[int, bool] = False

    # Initialize redis
    redis = redis_init()

    # Enter infinite loop
    while True:
        main_menu()

        try:
            choice = int(input("Input: "))

            if choice == 1:
                sign_up(redis)

            elif choice == 2:
                authentication = sign_in(redis)

            elif choice == 3:
                with_authentication(profile, authentication, redis, authentication)

            elif choice == 4:
                with_authentication(tweet, authentication, redis, authentication)

            elif choice == 5:
                with_authentication(follow, authentication, redis, authentication)

            elif choice == 6:
                with_authentication(other_profile, authentication, redis)

            elif choice == 7:
                with_authentication(unfollow, authentication, redis, authentication)

            elif choice == 8:
                timeline(redis)

            elif choice == 9:
                with_authentication(
                    update_profile, authentication, redis, authentication
                )

            elif choice == 10:
                authentication = logout()

            elif choice == 11:
                exit_menu()

            elif choice == 12:
                get_all_data(redis)

            elif choice == 13:
                flush_database(redis)

            else:
                raise ValueError()

        except ValueError:
            print("Please input a correct value!")
            continue

        except (
            DuplicateUserError,
            EmptyInputError,
            FollowError,
            NotAuthenticatedError,
            UserDoesNotExistError,
            UserIsNotYourFollowingError,
        ) as err:
            print(err.message)
            continue

        finally:
            input("\nPress any key to continue!")


if __name__ == "__main__":
    main()

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/users.py
"""This module is to manage our users."""

from time import time

from redis import Redis

from errors import (
    DuplicateUserError,
    EmptyInputError,
    FollowError,
    UserDoesNotExistError,
    UserIsNotYourFollowingError,
)
from utils import is_string_blank


def follow(redis: Redis, uid: int) -> None:
    """Follows another user.

    Algorithm:
    ----------
    1. Enter the username of someone that one wants to follow.
    2. Sanity check, if the string is blank, raise an exception.
    3. Check if user ID exists.
    4. Fetch the user id from 'users' hash.
    5. If the current user wants to follow themselves, then raise an exception.
    6. Create a mapping to store data in zset (sorted set).
    7. Store 'following' and 'followers' with the suitable IDs.

    Parameters:
    -----------
    redis (Redis): Redis instance
    uid (int): User id

    Returns:
    --------
    None
    """
    follow_username = input("Enter the username of someone to follow: ")

    if is_string_blank(follow_username):
        raise EmptyInputError()

    if not redis.hexists("users", follow_username):
        raise UserDoesNotExistError()

    user_id_to_be_followed = redis.hget("users", follow_username)

    if user_id_to_be_followed == uid:
        raise FollowError()

    following_mapping = {user_id_to_be_followed: int(time())}
    followers_mapping = {uid: int(time())}

    redis.zadd(f"following:{uid}", following_mapping)
    redis.zadd(f"followers:{user_id_to_be_followed}", followers_mapping)

    print(f"You have successfully followed {follow_username}")


def logout() -> False:
    """Logs out a user."""
    print("You have been logged out!")
    return False


def other_profile(redis: Redis) -> None:
    """Try to look at other people's profile.

    Algorithm:
    ----------
    1. Take input of username.
    2. Sanity check, if blank raise an exception.
    3. Check if user exists.
    4. Fetch the 'user_id' in 'users' HSET.
    5. Fetch the user's data in 'user' HSET.
    6. Display our data.

    Parameters:
    -----------
    redis (Redis): Redis instance

    Returns:
    --------
    None
    """
    target_username = input("Enter the username that you want to see: ")

    if is_string_blank(target_username):
        raise EmptyInputError()

    if not redis.hget("users", target_username):
        raise UserDoesNotExistError()

    uid = redis.hget("users", target_username)
    user_data = redis.hgetall(f"user:{uid}")
    tweet_data = redis.lrange(f"tweet_user:{uid}", 0, -1)
    following_data = redis.zrange(f"following:{uid}", 0, -1)
    followers_data = redis.zrange(f"followers:{uid}", 0, -1)

    print("Their personal data:")
    print(user_data)

    print("\nTheir tweets:")
    for item in tweet_data:
        post = redis.hgetall(f"tweet:{item}")
        print(post)

    print("\nTheir following:")
    for item in following_data:
        user = redis.hgetall(f"user:{item}")
        print(user)

    print("\nTheir followers:")
    for item in followers_data:
        user = redis.hgetall(f"user:{item}")
        print(user)


def profile(redis: Redis, uid: int) -> None:
    """Get personal data according to the session key.

    Algorithm:
    ----------
    1. Get all user's data from 'user' hash (intentionally hide passwords).
    2. Get all user's tweets from 'tweet_user' list.
    3. Get all user's following data from 'following' sorted set.
    4. Get all user's followers data from 'followers' sorted set.
    5. Display data in the screen.

    Parameters:
    -----------
    redis (Redis): Redis instance
    uid (int): User id

    Returns:
    --------
    None
    """
    user_data = redis.hgetall(f"user:{uid}")
    tweet_data = redis.lrange(f"tweet_user:{uid}", 0, -1)
    following_data = redis.zrange(f"following:{uid}", 0, -1)
    followers_data = redis.zrange(f"followers:{uid}", 0, -1)

    print("My personal data:")

    user_data.pop("password", "secret")
    print(user_data)

    print("\nMy tweets:")
    for item in tweet_data:
        post = redis.hgetall(f"tweet:{item}")
        print(post)

    print("\nMy following:")
    for item in following_data:
        user = redis.hgetall(f"user:{item}")
        print(user)

    print("\nMy followers:")
    for item in followers_data:
        user = redis.hgetall(f"user:{item}")
        print(user)


def timeline(redis: Redis) -> None:
    """Gets the global timeline of what's happening in the world.

    Algorithm:
    ----------
    1. Get all recent tweets.

    Parameters:
    ----------
    redis (Redis): Redis instance

    Returns:
    --------
    None
    """
    recent_tweets_list = redis.lrange("timeline", 0, 1000)

    print("All recent tweets: ")
    for item in recent_tweets_list:
        post = redis.hgetall(f"tweet:{item}")
        print(post)


def tweet(redis: Redis, uid: int) -> None:
    """Send a tweet connected to the user's account.

    Algorithm:
    ----------
    1. Get tweet.
    2. Sanity check, if tweet is blank, raise an exception.
    3. Increment 'tweet_id', as it is a standalone entity.
    4. Store our tweet data in a HSET.
    5. Store our tweet identifier for a certain user in LPUSH (list).
    6. Store the reference to the tweet in an LPUSH (list) for the global timeline.
    7. Trim the 'timeline' Redis list to the latest 1000 tweet references.

    Parameters:
    -----------
    redis (Redis): Redis instance
    uid (int): User id

    Returns:
    --------
    None
    """
    content = input("What's on your mind: ")

    if is_string_blank(content):
        raise EmptyInputError()

    tweet_data = {
        "uid": uid,
        "content": content,
        "date_posted": int(time()),
        "date_modified": int(time()),
    }

    tweet_id = redis.incr("next_tweet_id")
    redis.hset(f"tweet:{tweet_id}", mapping=tweet_data)
    redis.lpush(f"tweet_user:{uid}", tweet_id)
    redis.lpush("timeline", tweet_id)
    redis.ltrim("timeline", 0, 1000)

    print("Tweet has been successfully inserted!")


def unfollow(redis: Redis, uid: int) -> None:
    """Unfollows a user.

    Algorithm:
    ----------
    1. Get the sorted set of the user.
    2. Sanity check, if the user id is blank, raise an exception.
    3. Get the targeted user ID.
    4. If user does not exist, raise an exception.
    5. If targeted user is not in the 'following' of the current user, raise an exception.
    6. Remove from the sorted set of the current user, and change the suitable followers/following.

    Parameters:
    -----------
    redis (Redis): Redis instance
    uid (int): User id

    Returns:
    -------
    None
    """
    username_to_be_unfollowed = input("Enter the username that you want to unfollow: ")
    user_id_to_be_unfollowed = redis.hget("users", username_to_be_unfollowed)

    if is_string_blank(username_to_be_unfollowed):
        raise EmptyInputError()

    if not user_id_to_be_unfollowed:
        raise UserDoesNotExistError()

    if not redis.zscore(f"following:{uid}", user_id_to_be_unfollowed):
        raise UserIsNotYourFollowingError()

    redis.zrem(f"following:{uid}", user_id_to_be_unfollowed)
    redis.zrem(f"followers:{user_id_to_be_unfollowed}", uid)

    print(
        f"You have succesfully unfollowed a person with username {username_to_be_unfollowed}!"
    )


def update_profile(redis: Redis, uid: int) -> None:
    """Updates a user.

    Algorithm:
    ----------
    1. Get the input.
    2. Sanity checks.
    3. Check for duplicate username.
    4. Update the hash for 'user:id'.

    Parameters:
    -----------
    redis (Redis): Redis instance
    uid (int): User id

    Returns:
    --------
    """
    new_username = input("Enter your new username here: ")

    if is_string_blank(new_username):
        raise EmptyInputError()

    if redis.hexists("users", new_username):
        raise DuplicateUserError()

    new_user_data = {"username": new_username, "modification_date": int(time())}
    old_username = redis.hget(f"user:{uid}", "username")

    redis.hset(f"user:{uid}", mapping=new_user_data)
    redis.hdel("users", old_username)
    redis.hset("users", new_username, uid)

    print("Your personal data has been successfully updated!")

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/utils.py
"""This module is to store our utilities."""


def is_string_blank(string: str) -> bool:
    """Checks if a string is empty/blank or not.

    Parameters:
    ----------
    string (str): String to be checked.

    Returns:
    -------
    bool: Bool value whether the string is empty or not.
    """
    if string and string.strip():
        return False

    return True

--#

--% C:/work/rework/redis-twitter-console/redis-twitter-console/views.py
"""This module is to store our views, or print statements."""

import sys

from os import system


def exit_menu() -> None:
    """Exits the program."""
    print("Thanks for using this Redis playground!")
    sys.exit()


def main_menu() -> None:
    """This view is to render our simple main menu."""
    system("cls")
    print("======================================")
    print("         Redis Python Example         ")
    print("======================================")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Get My Profile")
    print("4. Tweet")
    print("5. Follow Someone")
    print("6. Search Profile")
    print("7. Unfollow Someone")
    print("8. Timeline")
    print("9. Update Username")
    print("10. Logout")
    print("11. Exit")
    print("12. Get All Data (Debug)")
    print("13. Flush Database (Debug)")

--#

