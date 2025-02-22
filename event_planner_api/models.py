from django.db import models

# Create your models here.

class Event(models.Model):
    organizer = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)
    title = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.TextField()
    numberOfParticipants = models.IntegerField()
    description = models.TextField()
    capacity = models.IntegerField()
    imageUrl = models.ImageField()
    


class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user =  models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=True)


class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    host = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE, related_name='guest')
    rsvp = models.ForeignKey(RSVP, on_delete=models.CASCADE, null=True, blank=True)




class EventInfo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    host = models.ForeignKey(to='users.CustomUser', on_delete=models.CASCADE)
    total_invitations = models.IntegerField(default=0)
    total_rsvps = models.IntegerField(default=0)
    total_accepted_rsvps = models.IntegerField(default=0)
    total_rejected_rsvps = models.IntegerField(default=0)
    invitaion_accepted_rsvps = models.IntegerField(default=0)
    invitation_rejected_rsvps = models.IntegerField(default=0)



class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField(blank=True,null=True)
    file = models.FileField(blank=True, null=True)