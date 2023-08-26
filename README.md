# LoadBalancer
Application layer load balancer.
Programming Language - Python

Building an application layer load balancer that:
- Can send traffic to two or more servers
- Health check servers
- Handle any server that goes offline
- Handle any server that comes online

Following steps are being followed:
- Step 1: Build a basic server(load balancer) that can handle one request from the client and then forward it to the backend server. Recieving response from the backend server and then responding back to the client.
- Step 2: Use multi threading to handle requests from multiple clients.(Single server)
- Step 3: Distribute incoming requests among 3 backend servers using round robin algorithm. Requests from clients are now served from multiple servers.


Further imprpvements that can be done in the project;
- Implementing a more efficient load balancing algorithm.
- Implement a periodic health check on all servers and if health check fails on any server, we take it out of the available server list.

How to test the project?
Download and run the files in terminal using the following commands:
    python3 LoadBalancer.py 3 (Number of backend servers running)
    python3 BackendServer.py
    python3 BackendServe2.py
    python3 BackendServe3.py (if you want to run all the 3 servers)
    
POSTMAN tool was used to test the servers by sending the following 2 requests concurrently multiple times:
    http://localhost:1025/index.html
    http://localhost:1025/

