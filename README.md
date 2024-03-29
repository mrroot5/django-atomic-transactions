# Django atomic transactions
This project simulate a virtual wallet to use Django atomic transactions.

Staff users could do almost any type of action while regular users only could
do things with their own wallets.

Only superusers could change wallet balance.

## Requirements

* docker engine >= 19.03.
* docker-compose >= 1.27.

## Tested on

* Ubuntu 18.04 (Bionic).
* docker engine == 20.10.9.
* docker-compose == 1.28.4.

## How to use this project?

### Using make command (recommended)

If you can run a `Makefile` command, you can use a "fast init" with: `make loaddata`.

### Build

Build docker image:

```shell
make build
```

#### Migrate

Apply django migrations:

```shell
make migrate
```

#### Runserver

Run django runserver command:

```shell
make dev
```

#### Uvicorn

Run uvicorn server:

```shell
make uvicorn
```

#### Load sample data

Apply `initial_data.json` fixture. This action will erase all previous data:

```shell
make loaddata
```

#### Run tests

```shell
make tests
```

### Using docker-compose

#### Step 1: Build

```shell
docker-compose -p django_atomic_transactions -f environment/docker-compose.yml build
```

#### Step 2: Migrate

Apply django migrations:

```shell
docker-compose -p django_atomic_transactions -f environment/docker-compose.yml run --rm --service-ports web migrate
```

#### Step 3: Run service

* **Runserver**

Run django runserver command:

```shell
docker-compose -p django_atomic_transactions -f environment/docker-compose.yml run --rm --service-ports web dev
```

* **Uvicorn**

Run uvicorn server:

```shell
docker-compose -p django_atomic_transactions -f environment/docker-compose.yml run --rm --service-ports web uvicorn
```

#### Step 4: Load sample data

Apply `initial_data.json` fixture. This action will erase all previous data:

```shell
docker-compose -p django_atomic_transactions -f environment/docker-compose.yml run --rm --service-ports web loaddata
```

#### Step 5: Run tests

```shell
docker-compose -p django_atomic_transactions -f environment/docker-compose.yml run --rm --service-ports web python manage.py test --failfast api
```

## Know issues

### Database connection error: web service could not connect to db service

Sometimes when try to migrate it gets an error message like that. The IP is an example:

```shell
Is the server running on host "db" (<192.168.1.25>) and accepting
	TCP/IP connections on port 5432?
```

When `web` is up and running and `db` is not ready yet, we could have this type of error.
In this situation try to execute it again.

## TODO

* Use possitive integer instead of float / decimal fields to save `amount`.
Use type to control possitve or negative transactions. Do not forget validations!
This will improve performance.
* Move DRF views logic like transactions from views to model. With this change we avoid our DRF dependance and we change it to another technology in the future.
* Remove staff accounts (html select) from regular user wallet and transactions creation UI.
* Auto create a **transaction** error on atomic `IntegrityError`.
* Add `flake8` to testing stage.
* Create a **view** using django **templates** and **css grid** to show `GetNumClientAccounts`.
* Create a **business** flow:
  * Create **business** account.
  * Create **business** wallet.
  * Create **business** transactions.
  * Allow **business** to manage their our client accounts.
* Enable django **admin login** with created users.
* Enable django **password validations** on user creation.
* Finish **Dockerfile production** stage.
* Improve `pg_ready` in container `healthcheck`.

...

Are you here yet? OK, nice one. I should invite you to a cup of coffee.
Just give me your wallet username and password to get in touch hehehe (yep, a simple joke).
