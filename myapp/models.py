from django.db import models

# Model for Services
class Service(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the service (e.g., Logo Design)")
    image = models.ImageField(upload_to='services/', help_text="Upload an image for the service")
    description = models.TextField(help_text="Description of the service")

    def __str__(self):
        return self.name

# Model for Portfolio Items
class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the project")
    image = models.ImageField(upload_to='portfolio/', help_text="Upload an image for the portfolio item")
    description = models.TextField(help_text="Description of the project")

    def __str__(self):
        return self.title

# Model for Testimonials
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, help_text="Name of the client")
    client_position = models.CharField(max_length=100, help_text="Client's position or company name", blank=True, null=True)
    client_image = models.ImageField(upload_to='testimonials/', help_text="Upload an image of the client", blank=True, null=True)
    feedback = models.TextField(help_text="Feedback or testimonial from the client")

    def __str__(self):
        return f"{self.client_name} - {self.client_position}"

# Model for Social Links
class SocialLink(models.Model):
    platform = models.CharField(max_length=50, help_text="Social media platform (e.g., Facebook)")
    url = models.URLField(help_text="URL to the social media profile")

    def __str__(self):
        return self.platform

# Model for Contact Feedback
class ContactFeedback(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the person submitting the feedback")
    email = models.EmailField(help_text="Email address of the person")
    subject = models.CharField(max_length=150, help_text="Subject of the message")
    message = models.TextField(help_text="The message content")
    submitted_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the feedback was submitted")

    def __str__(self):
        return f"{self.name} - {self.subject}"