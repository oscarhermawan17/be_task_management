## Back End (Python - Flask) - Task Managemenent App
Front End Task Management

### 1. Overview of this application
This is a RESTful API app that helps users view, create, edit, and delete their tasks. <br/>
Technologies Used:
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>JWT</li>
  <li>PostgreSQL</li>
  <li>SQL Alchemy</li>
</ul>
The frontend can be seen [here](https://github.com/oscarhermawan17/fe_task_management)


### 2. Minimun Requirement
<ul>
  <li>Python version 3.12.x</li>
  <li>PostgreSQL version 16.x</li>
</ul>

### 3. How To Run This App (Step by Step) ?
<ul>
  <li>Make sure you have PostgreSQL and still running on your machine</li>
  <li>Create a database named <code>task_management</code></li>
  <li>Make sure you have an account that has full access to that database</code></li>
  <li>
    Rename .env.example file to be .env (in the root folder)
    <ul>
      <li>SECRET_KEY=<code>secret</code> (<code>secret</code> is used for cryptographic operations such as signing cookies and tokens in a web application)</li>
      <li>DATABASE_URL=<code>dburl</code> (<code>dburl</code> is the connection string for the PostgreSQL database)</li>
      <li>JWT_SECRET_KEY=<code>jwt</code> (<code>jwt</code> is is used to sign and verify JSON Web Tokens (JWTs). It ensures that the tokens are secure and can be trusted by the server to authenticate users and other operations involving JWTs)</li>
      <li>PORT=<code>port</code> (<code>port</code> is specifies the port on which the web application will run)</li>
      <li>CORS_ORIGINS=<code>cors</code> (<code>cors</code> is defines which domains are permitted to make requests to the server. This specifies the allowed origins for Cross-Origin Resource Sharing (CORS))</li>
    </ul>
  </li>
  <li>Run <code>python -m venv venv</code> or <code>python3 -m venv venv</code> . It would create a venv (stands for "virtual environment") folder in the root folder</li>
  <li>If you see venv folder in the root foolder. Then run <code>source venv/bin/activate</code> for Mac/Linux, or <code>.\venv\Scripts\activate</code> for Powershell on Windows</li>
  <li>Run <code>pip install -r requirements.txt</code> . This command will download all modules and may take a while.</li>
  <li>Run <code>python seeder.py</code> or <code>python3 seeder.py</code>. This command will create new tables and populate the user and task tables with data, allowing us to log in using the <code>username: oscar</code> and <code>password: oscar</code>"</li>
  <li>Run <code>flask run</code>. This command will run our application in development mode."</li>
  <li>To check our app is running well, check <code>http://localhost:port/</code>. If our app running well, it would send content "Hello, Flask!.</li>
</ul>

### 4. How To Run Unit Test ?
-

### 5. List of API
| How to ?                | URL                      | Method | Need Token ? | Body |
| ------------------------| ------------------------ | ------ |--------------|------|
| Sign to App             | <code>/signin</code>     | POST   | No        | username, and password |
| Sign upp                | <code>/signup</code>     | POST   | No        | username, and password |
| Create a new Task       | <code>/tasks</code>      | POST   | Yes       | title, description, and status |
| Get all tasks           | <code>/tasks</code>      | GET    | Yes       | - |
| Update an existing task | <code>/tasks/:id</code>  | PUT    | Yes       | title, description, and status |
| Delete a task           | <code>/task/:id</code>   | DELETE | Yes       | - |

