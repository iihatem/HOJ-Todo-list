## Overall Project Outline

1. **Project Setup & Requirements**

   - Git repository setup (branch strategy, issue tracking)
   - Development environment setup (virtual environment, Flask app scaffold)
   - Database setup (MongoDB)
   - AWS user management (AWS Cognito or equivalent)
   - Task assignment & timeline

2. **Core Features**

   - User Authentication (sign-up, sign-in, sign-out)
   - Create/Edit/Delete tasks
   - Collaborative lists (invite users to lists, shared updates)
   - Basic UI for listing tasks

3. **Enhancements & Extras**

   - Error handling
   - Notifications or real-time updates (if time allows)
   - Deployed version (could use AWS services or any preferred hosting)

4. **Testing & Documentation**
   - Unit tests (Flask routes, database operations)
   - Integration tests for collaborative features
   - API documentation (endpoints, usage)
   - README with instructions to install & run

---

## Day-by-Day Timeline

### **Day 1: Project Initialization & Architecture**

**Deadline: End of Day 1**

- **Person A**

  1. **Repository Setup**: Create a GitHub repository and set up branch organization (e.g., `main`, `dev`, feature branches).
  2. **Virtual Environment & Flask Scaffold**:
     - Initialize a Flask project structure.
     - Add basic folder structure (`app`, `templates`, `static`, etc.).

- **Person B**

  1. **MongoDB Setup**:
     - Set up a local or cloud MongoDB instance.
     - Create a database (e.g., `todo_app`) with an initial `users` and `lists` collection.
  2. **Research AWS Cognito**: Familiarize yourself with AWS Cognito or chosen AWS user management approach.

- **Person C**
  1. **Requirements & UI Mockups**:
     - Draft a quick wireframe or mockup for the user interface (login screen, dashboard, collaborative lists, etc.).
     - Outline essential routes/endpoints needed for the Flask app (e.g., `/login`, `/signup`, `/todo`, `/todo/:id`, `/invite`, etc.).

**Goal by End of Day 1**:

- Everyone can clone the repo.
- Basic Flask project is running locally.
- MongoDB is set up.
- High-level architecture and UI flow are clear.

---

### **Day 2: User Authentication & AWS Cognito Integration**

**Deadline: End of Day 2**

- **Person A**

  1. **User Authentication (Flask Part)**:
     - Implement Flask routes for sign-up, sign-in, sign-out.
     - Hash passwords if doing local auth (although AWS Cognito may handle this).
  2. **Link to MongoDB**:
     - Create a `User` model or schema in Python to interact with MongoDB.

- **Person B**

  1. **AWS Cognito Setup**:
     - Create a Cognito User Pool.
     - Integrate Cognito user pool into the Flask app (obtain credentials, environment variables, etc.).
  2. **Write Documentation**:
     - Document steps needed to configure AWS Cognito for the project (for your teammates to replicate if needed).

- **Person C**
  1. **Frontend for Authentication**:
     - Create basic HTML templates for sign-up, sign-in, and sign-out.
     - Ensure forms capture the required data (username, password, email, etc.).
  2. **Basic Styling/Structure**:
     - Implement minimal styling using either Bootstrap or a CSS framework to ensure usability.

**Goal by End of Day 2**:

- Users can register and log in/out using either direct Flask sessions or AWS Cognito integration.
- Basic front-end forms exist for authentication.

---

### **Day 3: To-Do List Functionality (CRUD)**

**Deadline: End of Day 3**

- **Person A**

  1. **Task Model & DB Integration**:
     - Create a `Task` model or structure in MongoDB.
     - Ensure the schema has fields like `title`, `description`, `status`, `due_date`, `owner_id`, etc.
  2. **Create/Read/Update/Delete (CRUD) Operations**:
     - Implement Flask routes to handle task creation, reading tasks, updating tasks, and deleting tasks.

- **Person B**

  1. **Testing the CRUD Endpoints**:
     - Write basic unit tests or integration tests to verify the routes (using something like `pytest` or `unittest`).
     - Verify that tasks are being stored and retrieved properly in MongoDB.

- **Person C**
  1. **Frontend for Task Management**:
     - Create pages/templates for listing tasks (dashboard), creating a new task, editing a task.
     - Connect front-end forms to the Flask routes (e.g., POST form data).
  2. **UI/UX Enhancement** (time permitting):
     - Add basic input validation or user feedback messages (e.g., "Task created successfully!").

**Goal by End of Day 3**:

- A user can log in and manage their tasks (create, view, edit, delete).
- Data is persisted in MongoDB.

---

### **Day 4: Collaborative Lists**

**Deadline: End of Day 4**

- **Person A**

  1. **List Model & Collaboration Logic**:
     - Implement a `List` collection in MongoDB with fields like `name`, `members` (array of user IDs), `tasks` (array of task IDs or references).
     - Create routes to create a list, invite other users to join, and fetch lists with their tasks.

- **Person B**

  1. **Invite System**:
     - Implement a system where a user can invite another user to collaborate on a list (by username or email).
     - Check if the invited user is already in the database and if they’re not already a collaborator.

- **Person C**
  1. **UI for Collaboration**:
     - Update the dashboard to show all lists the logged-in user is a member of.
     - Add an “Invite” button or form to invite other users (with an email or username field).
  2. **Testing with Real User Flows**:
     - Test invites, accepting invites (or automatically adding a user), and verifying collaborative tasks.

**Goal by End of Day 4**:

- Collaboration is functional: Users can create lists, invite others, and see tasks in the shared lists.

---

### **Day 5: Polishing, Error Handling, and Additional Features**

**Deadline: End of Day 5**

- **Person A**

  1. **Error Handling & Edge Cases**:
     - Make sure routes return helpful messages for missing parameters, invalid invites, etc.
  2. **Security**:
     - Verify that only collaborators can see/edit tasks in a list.
     - Ensure no unauthorized updates are possible.

- **Person B**

  1. **Tests & Coverage**:
     - Expand test coverage, including authentication and collaboration.
     - Ensure passing tests for different user roles (owner vs. collaborator).

- **Person C**
  1. **Frontend Refinements**:
     - Improve the look and feel of the site (CSS, layout).
     - Add responsive design touches, if time permits.

**Goal by End of Day 5**:

- The app is stable, user-friendly, and mostly bug-free.
- Security checks and error handling are in place.

---

### **Day 6: Deployment & Final Integration**

**Deadline: End of Day 6**

- **Person A & B** (can work together on deployment):

  1. **AWS or Alternative Deployment**:
     - If using AWS, configure your Flask app on AWS Elastic Beanstalk or an EC2 instance.
     - Ensure environment variables for database and Cognito details are set up properly.
  2. **MongoDB Setup for Production**:
     - If using a hosted MongoDB solution (e.g., Atlas), update the connection strings in production.

- **Person C**
  1. **Smoke Test the Deployed App**:
     - Once deployed, run through a test of the entire flow (sign-up, create a task, create a list, invite collaborator, etc.).
  2. **Bug Fixes & UI Tweaks**:
     - Quickly address any last-minute UI or user experience issues found during the smoke test.

**Goal by End of Day 6**:

- A live version of the app is accessible via a public URL.
- Basic production environment is configured.

---

### **Day 7: Final Review & Documentation**

**Deadline: End of Day 7**

- **Everyone**
  1. **Project Documentation**:
     - Finalize the README with setup steps, environment variables, deployment instructions, usage instructions, etc.
  2. **Code Clean-Up**:
     - Remove any debug logs, unused code, or commented-out sections.
     - Ensure a consistent coding style.
  3. **Presentation / Demo**:
     - Prepare a quick demo (screenshots or a walkthrough) for how to use the app.
  4. **Retrospective**:
     - Discuss what you learned, challenges faced, and how to improve for next time.

**Goal by End of Day 7**:

- A fully functional collaborative to-do list app with authentication, collaboration features, and a clean codebase that’s well-documented.

---

## Wrap-Up

This plan ensures each person has clear responsibilities and deadlines. By the end of the week, you’ll have a working collaborative to-do list application, experience with Flask, MongoDB, AWS (Cognito), and real-world collaboration skills. Adjust tasks as needed to fit your strengths and schedules. Good luck!
