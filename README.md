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
- Step 3: Distribute incoming requests between 3 backend servers using round robin algorithm. Requests from clients are now served from multiple servers.
- Step 4: 
