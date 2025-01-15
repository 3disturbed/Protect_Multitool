# Protect_Multitool
Protect Multitool, A multitool to protect.


Login and Registration html template for dajango. Easily linked up to backend. 
User auth.
User profile. Change and updated emergency numbers.
Reponsive design. HTML CSS
User Freidnly.
Email confirmation? 
project_Multitool/template/registration/login.html register.html

Some color pallete stuff :
Primary: #4338CA
Success: #10B981
Alert: #EF4444
Warning: #F59E0B


Some ideas for safety transit:

Use djnago's build in datetimefield() to make sure user checks in. 

     last_check_in = models.DateTimeField()

    def requires_notification(self):
        time_passed = timezone.now() - self.last_check_in
        return time_passed > timedelta(minutes=40)

Tools:
- Celery - task management
- Twillo - sms 
- google maps api route planning

