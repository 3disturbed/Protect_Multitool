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
  - [Mick](#mick)
  - [Mus](#mus)
  - [Tamanna](#tamanna)
  - [Fatima](#fatima)
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
   - Message will be sent via WhatsApp and be very generic as it's for testing purposes - WhatsApp requires official business proof for specific message types which we won't have at the time of creation.

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

### Mick

#### Notes
- Tasks:
  - Complete README additions.
  - Submit the initial pull request.
- Notes:
  - Contact Ben or Dark for assistance if needed.

[Back to Contents](#contents)

### Mus

#### Notes
- Tasks:
  - Complete README additions.
  - Submit the initial pull request.
- Notes:
  - Contact Ben or Dark for assistance if needed.

[Back to Contents](#contents)

### Tamanna

#### Notes
- Tasks:
  - Review feature suggestions and provide feedback.
  - Contribute to UI/UX design brainstorming.

[Back to Contents](#contents)

### Fatima

#### Notes
- Tasks:
  - Complete README additions.
  - Submit the initial pull request.
- Notes:
  - Contact Ben or Dark for assistance if needed.

[Back to Contents](#contents)


## Temp
This section contains temporary notes and ideas for further development.

### Ideas for Safety Transit
- Utilize Django's built-in `DateTimeField` to monitor user check-ins. Example:

```python
from datetime import timedelta
from django.utils import timezone
from django.db import models

class CheckIn(models.Model):
    last_check_in = models.DateTimeField()

    def requires_notification(self):
        time_passed = timezone.now() - self.last_check_in
        return time_passed > timedelta(minutes=40)
```

[Back to Contents](#contents)

## Automated WhatsApp message event
Once triggered using a hidden feature like a game, this event will trigger an automated message to be sent via WhatsApp to the user's set emergency contacts.

Emergency contacts will be set via the user's account, using PostgreSQL and Django all auth.

Messaging will be sent using MessageBird API.

Message will be sent via WhatsApp and be very generic as it's for testing purposes - WhatsApp requires official business proof for specific message types which we won't have at the time of creation.

[Back to Contents](#contents)
