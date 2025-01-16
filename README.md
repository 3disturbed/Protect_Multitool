## Contents
- [UXD (User Experience Design)](#user-experience-ux)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Team](#team)
  - [Ben](#ben)
  - [Loch](#loch)
  - [Mick](#mick)
  - [Mus](#mus)
  - [Tamanna](#tamanna)
  - [Fatima](#fatima)
- [Temp](#temp)
- [Automated WhatsApp message event](#automated-whatsapp-message-event)
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