## Requirements
- Download and install [Docker daemon](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).
- (Optional) Download and install [Postman](https://www.postman.com/downloads/)

## Installation

### App
1. Manually generate a string of random characters and insert it into `.env` file after `SECRET_KEY=`:
`SECRET_KEY='<your_strting_here>'`

1. Open your OS terminal, change the working directory to the project and run the command below:
(if you already have another app running on port 8001, please find the line `- 8001:8080` and replace 8001 with a free port):
`docker-compose -p usermgmt up -d --build`
This will install and run the app

### Postman (optional)
For your convenience I created the endpoints collection that you can import into your Postman. Just open Postman and import `Users-API.postman_collection.json` file that comes with the project
## How to use
__NOTE 1__: if you changed the port please use it in the steps below instead of 8001.

__NOTE 2__: All endpoint specs are described in [API Doc](#api-doc) below

1. Create a user: the DB is empty, so you'll need to create the first user by using [create user](#1-create-user) endpoint
2. Send `username` and `password` that you created [login](#2-login) endpoint to authenticate
3. In response you will receive an auth token (session duration: 30 min). You should use it to get authorized in all other endpoints:
3.1 (Postman) In the "Authorization" tab of a request choose `Type: Bearer Token` and insert your token into the "Token" field
3.2 If you use curl or any other client you'll need to pass header: `Authorization: Bearer <token>`


## API Doc
1. [create user](#1-create-user)
1. [login](#2-login)
1. [view all users](#3-view-all-users)
1. [view user by id](#4-view-user-by-id)
1. [update user by id](#5-update-user-by-id)
1. [delete user by id](#6-delete-user-by-id)
1. [purge user by id](#7-purge-user-by-id)



## Endpoints
--------
### 1. create user

***Endpoint:***

```bash
Method: POST
Type: FORMDATA
URL: http://localhost:8001/users/create
```

***Body:***

| Key | Value |
| --- | ------|
| username | john_doe |
| password | qwerty123 |
| email | john.doe@example.com |
| info | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. |

### 2. login

***Endpoint:***

```bash
Method: POST
Type: FORMDATA
URL: http://localhost:8001/login
```

***Body:***

| Key | Value |
| --- | ------|
| username | john_doe |
| password | qwerty123 |

### 3. view all users

***Endpoint:***

```bash
Method: GET
Type:
URL: http://localhost:8001/users
```

***Query params:***

| Key | Value | Description |
| --- | ------|-------------|
| page | 1 | Default: 1 |
| per_page | 10 | Default: 10 |

### 4. view user by id

***Endpoint:***

```bash
Method: GET
Type:
URL: http://localhost:8001/users/:id
```

***URL variables:***

| Key | Value |
| --- | ------|
| id | 1 |

### 5. update user by id

***Endpoint:***

```bash
Method: POST
Type: FORMDATA
URL: http://localhost:8001/users/update/:id
```

***URL variables:***

| Key | Value |
| --- | ------|
| id | 1 |

***Body:***

| Key | Value |
| --- | ------|
| info | Changed info |

### 6. delete user by id

***Endpoint:***

```bash
Method: DELETE
Type:
URL: http://localhost:8001/users/delete/:id
```

***URL variables:***

| Key | Value |
| --- | ------|
| id | 1 |

### 7. purge user by id

***Endpoint:***

```bash
Method: DELETE
Type:
URL: http://localhost:8001/users/purge/:id
```

***URL variables:***

| Key | Value |
| --- | ------|
| id | 1 |


