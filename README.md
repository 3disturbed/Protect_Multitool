# Mission Statement

Protect Multitool is dedicated to empowering individuals by providing innovative safety solutions that integrate seamlessly into daily life. Our mission is to leverage technology to create discreet, accessible, and effective tools that enhance personal security, raise awareness about human trafficking and modern slavery, and foster a safer world for all.

[Visit Deployed Site on Heroku!](https://multitool-87412d08ac41.herokuapp.com/)

## Contents
- [UXD (User Experience Design)](#user-experience-ux)
- [Features](#features)
- [Safety Transit](#safety-transit)
- [Kicky Frog and Fake Games](#kicky-frog-and-fake-games)
- [Tech Stack](#tech-stack)
- [Installation & Setup Guide](#installation--setup-guide)
- [Contribution Guidelines](#contribution-guidelines)
- [API Documentation](#api-documentation)
- [Security Considerations](#security-considerations)
- [Testing & Debugging](#testing--debugging)
- [Deployment Guide](#deployment-guide)
- [License & Legal Considerations](#license--legal-considerations)
- [Team](#team)
  - [Ben](#ben)
  - [Loch](#loch)
  - [Michael](#michael-mccourt)
  - [Mus](#musaddeka-ali)
  - [Farha](#farha-tamanna-islam)
  - [Fatima](#fatima-abaji)
- [Temp](#temp)



## UI
Some color palette details:
- **Primary:** #4338CA
- **Success:** #10B981
- **Alert:** #EF4444
- **Warning:** #F59E0B

[Back to Contents](#contents)

## User Experience (UX)
The goal is to create a seamless and intuitive user experience that ensures easy navigation, high accessibility, and clear functionality. The design will include:

- **Responsive Design:** Optimized for desktop, tablet, and mobile devices.
- **Accessibility:** WCAG 2.1 compliance to ensure the platform is usable by all individuals, including those with disabilities.
- **User Flow:** Clear and concise navigation paths for different user personas.
- **Feedback Mechanisms:** Interactive alerts, success messages, and notifications.

[Back to Contents](#contents)

## Features
1. **Safety Transit Features:**
   - Timed check-ins using Django’s `DateTimeField` to ensure user safety.
   - Automated notifications if check-ins are missed.

2. **User Management:**
   - Registration and Login.
   - Profile management for updating emergency contacts.
   - Two-factor authentication for secure access.

3. **Interactive Tools:**
   - Google Maps API integration for route planning.
   - SMS notifications via Twilio.
   - Task management features using Celery.

4. **Notifications:**
   - Real-time alerts for critical updates.
   - Push notifications for missed check-ins or safety warnings.

5. **Automated WhatsApp message event:**
   - Once triggered using a hidden feature like a game, this event will trigger an automated message to be sent via WhatsApp to the user's set emergency contacts.
   - Emergency contacts will be set via the user's account, using PostgreSQL and Django all auth.
   - Messaging will be sent using MessageBird API.
   - Message will be sent via WhatsApp and is currently generic for testing purposes. Messages include user name, contact name, location (if user allows us to access their location) and in specific cases a URL and Secret key for accessing user routes.

[Back to Contents](#contents)

## Safety Transit
The Safety Transit feature functions as a **PIN-protected dead man's switch** that ensures user safety while in transit. 

- **How It Works:**
  - The user sets up a journey by inputting their origin, destination, and estimated travel time.
  - They receive periodic prompts to enter their PIN to confirm they are safe.
  - If the user does not enter their PIN within the allotted timeframe, an automated distress signal is sent to their designated emergency contact.
  - The distress signal includes the user's last known location, journey details, and any additional safety information.

- **Key Features:**
  - **Customizable Timeframes:** Users can set the check-in frequency based on travel duration.
  - **Silent Alarm Option:** If the user is in danger and cannot safely enter their PIN, they can enter an alternative code to send an alert silently.
  - **GPS Integration:** Automatically tracks the user's journey and updates emergency contacts on progress.
  - **Failsafe Mechanism:** If internet or GPS connectivity is lost, the system attempts to send a final update with the last known location.

[Back to Contents](#contents)

## Kicky Frog and Fake Games
To provide a **stealth distress signal**, the platform includes fake games like **Kicky Frog**, designed to help users discreetly trigger silent alarms.

- **How It Works:**
  - The user opens the fake game, which looks like an ordinary mobile game (e.g., a simple Flappy Bird-style game).
  - If the user fails on the first obstacle (deliberately or due to distress), the system triggers a silent alarm.
  - The silent alarm sends a distress message to the user's emergency contact, along with location data if available.

- **Key Features:**
  - **Disguised Interface:** Looks like a real game to avoid raising suspicion.
  - **Customizable Triggers:** Users can define multiple failure conditions to trigger the alarm.
  - **Fake Chat Option:** A built-in chat window that appears real but can be used to send pre-set distress messages.
  - **Stealth Activation:** Ensures a way to seek help without alerting potential threats.
  - **GPS-Enabled Alerts:** If enabled, the distress signal includes the user's location.

[Back to Contents](#contents)

## Tech Stack
- **Frontend:**
  - HTML, CSS, JavaScript.
  - Responsive design frameworks (e.g., Bootstrap or TailwindCSS).

- **Backend:**
  - Django – for its robust ORM and built-in features.
  - Celery – for task scheduling and asynchronous processing.

- **APIs and Integrations:**
  - Google Maps API – for route planning.
  - Twilio – for SMS notifications.

- **Database:**
  - PostgreSQL – for reliable and scalable data storage.

- **Hosting and Deployment:**
  - AWS or Heroku – for hosting the application.

[Back to Contents](#contents)


## Installation & Setup Guide
To set up the project locally, follow these steps:
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/protect-multitool.git
   ```
2. Navigate into the project directory:
   ```sh
   cd protect-multitool
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in a `.env` file.
5. Run migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

[Back to Contents](#contents)

## Contribution Guidelines
- Follow the branching model: feature branches should be prefixed with `feature/`, and bug fixes with `fix/`.
- Submit pull requests with detailed descriptions and relevant issue links.
- Follow PEP 8 style guidelines for Python and adhere to best practices for frontend code.

[Back to Contents](#contents)

## API Documentation
- **Authentication API**: Login, registration, and user management.
- **Safety Transit API**: Creating and managing user journeys.
- **Notification API**: Sending alerts via SMS, email, and WhatsApp.
- API documentation is auto-generated with Swagger.

[Back to Contents](#contents)

## Security Considerations
- Encrypted communications using HTTPS.
- Secure API endpoints with JWT authentication.
- Rate limiting to prevent abuse.

[Back to Contents](#contents)

## Testing & Debugging
- Run tests with:
   ```sh
   pytest
   ```
- Use logging and Django Debug Toolbar for debugging.

[Back to Contents](#contents)

## Deployment Guide
- The project is deployed using Heroku.
- CI/CD pipeline setup with GitHub Actions.
- Database hosted on AWS RDS.

[Back to Contents](#contents)

## License & Legal Considerations
- This project is licensed under the MIT License.
- If using third-party APIs, ensure compliance with their terms of service.

[Back to Contents](#contents)

## Team
### Ben Darlington
[GitHub](https://github.com/3disturbed)

[LinkedIn](https://www.linkedin.com/in/darlingtonben/)

- Scrum Leader
- Repo Manager
- Presentations
- Javascript / Game Developer

[Back to Contents](#contents)

### Loch

- UX / UI
- Landing Page Layout

#### Notes
- Create login and registration HTML templates for Django.
- Features:
  - User authentication.
  - Profile management for emergency contact updates.
  - Responsive design with HTML and CSS.
  - Optional email confirmation.
- File Structure:
  - `project_multitool/templates/registration/login.html`
  - `project_multitool/templates/registration/register.html`

[Back to Contents](#contents)

### Michael McCourt

[GitHub](https://github.com/Mickjitsu)

[LinkedIn](https://www.linkedin.com/in/michael-m-881b5194)

I'm a 27 year old half digital nomad constantly moving between Ireland, Holland and Spain with a military background before working in Tech Support and studying coding from last year with Code Institute.
The experience was awesome, I learnt a lot about working on a project that is backend heavy and had a lot of fun getting creative and implementing solutions.
-Back-end Engineer
-MessageBird/WhatsApp wizard



[Back to Contents](#contents)

### Musaddeka Ali
![image](https://github.com/user-attachments/assets/88542df0-2032-4d25-9982-508857d50b8a)

[Github](https://github.com/StringerMus)

[LinkedIn](https://www.linkedin.com/in/musaddekali/)
    
This Hackathon marks my first experience in a collaborative coding environment. Starting the course with no prior background in tech or coding, I am enjoying learning programming languages and building web applications. This project has been an opportunity for me to grow both technically and collaboratively - I’ve gained hands-on experience working in a team, contributing to repositories, and embracing effective teamwork practices. I’ve learned a lot from my teammates, including advice on best practices and exploring new technologies, which have broadened my perspective and skills.

[Back to Contents](#contents)

### Farha Tamanna Islam
![image](https://github.com/user-attachments/assets/0502af3f-0109-4dd2-88bc-cad31d74aff8)

[GitHub](https://github.com/farhatamannaislam)

[LinkedIn](https://www.linkedin.com/in/farha-tamanna-islam-sw-developer/)

Hi, I am Farha. I have worked in embedded development for several years but now embracing a new journey in full stack SW development. For me Hackathon is an excellent platform to sharpen skills and gather new experience. In this Hackathon we have worked in a very Dynamic and well structured team. Our Project goals to help people in their emergency situation. I am very happy to be a part of this project. Hope we can help people to assure their safety.



[Back to Contents](#contents)

### Fatima Abaji
![IMG_0187](https://github.com/user-attachments/assets/8e9acab4-d739-4453-9825-0a4af5ce68a1)

[GitHub](https://github.com/fatimaabaiji)

[LinkedIn](https://www.linkedin.com/in/fatima-abaiji-139290192/)

Participating in the hackathon has been an incredible experience. Collaborating with an amazing team allowed me to gain valuable insights into real-world software development challenges. As a junior developer, it was a fantastic opportunity to apply my skills in a practical setting, learn from more experienced teammates. The experience has greatly enhanced my understanding of teamwork, communication, and the fast-paced nature of development, making it an invaluable step in my growth as a developer.)

[Back to Contents](#contents)
