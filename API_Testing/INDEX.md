*** ============= HTTP Requests ============= ***
- GET: Lấy data từ server 
- POST: Gửi data đến server
- PUT: Update data on a server
- DELETE: Xoá data từ server

*** *** *** *** *** *** GET *** *** *** *** *** *** 

*** EX1 ***
Url: https://reqres.in/api/users?page=2
Link img: https://prnt.sc/8GELlRj3h5qz

tests["Validating Status Code"] = responseCode.code == 200;
tests["Validating response body"] = responseBody.has("Janet");
var response = JSON.parse(responseBody);
tests["page no"] = response.page == 2;

*** EX2 ***
Test first name - last name 
url: https://reqres.in/api/users/2
Link img: https://prnt.sc/yO_pFeVXRTAA

tests["validating response body"] = responseBody.has("Janet")
tests["Validating response body"] = responseBody.has("Weaver");
var response = JSON.parse(responseBody);
tests["verify first name"] = response.data.first_name == "Janet";
tests["verify last name"] = response.data.last_name == "Weaver";


*** *** *** *** *** *** POST *** *** *** *** *** *** 

*** EX1: Test data vừa tạo ***
Url: https://reqres.in/api/users
Link img: https://prnt.sc/q8tjQUaPuNxH

- body:
    {
        "name": "phero",
        "job": "leader"
    }
- test

var response = JSON.parse(responseBody);
tests["name"] = response.name == "phero"
tests["job"] = response.job == "leader"

tests["Validating Status Code"] = responseCode.code == 201;

*** EX2: Login ***
Url: https://reqres.in/api/login

tests["Validating Token presence"] = responseBody.has("token")
var response = JSON.parse(responseBody)
tests["token"] = response.token == "QpwL5tke4Pnpja7X4"

*** ============= Data Driven Testing ============= ***
 
How to Run Colection
Export/ import Collections
=>Tạo DataDrivenTesting trên postman -> tạo data CSV -> import vào

*** ============= Authorizations ============= ***

1) Basic Auth:
https://postman-echo.com/basic-auth
 username: postman
 password: password

2) API Key Auth
Get Request: https://api.openweathermap.org/data/2.5/forecast/daily?q=Delhi&cnt=1
API Key/appid: fe9c5cddb7e01d747b4611c3fc9eaf2c

