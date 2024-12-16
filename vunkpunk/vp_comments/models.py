from django.db import models
from vp_forum.models import SaleCard
from vp_users.models import User


class Comment(models.Model):
    content: models.CharField = models.CharField(max_length=300)
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    post: models.ForeignKey = models.ForeignKey(SaleCard, on_delete=models.CASCADE, db_index=True)
