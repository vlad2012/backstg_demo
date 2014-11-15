from django.db import models

class Calc(models.Model):
  value = models.IntegerField()
  number = models.IntegerField(primary_key=True)
  occurencies = models.IntegerField(default=0)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('number',)

  def save(self, *args, **kwargs):
    if self.number < 1 or self.number > 100:
      raise ValueError("The %s number shall be between 0 and 100" % self.number)
    if self.number == 1:
      self.value = 0
    else:
      self.value = (self.number*(self.number+1)/2)**2 - self.number*(self.number+1)*(2*self.number+1)/6 
    
    self.occurencies += 1
    super(Calc, self).save(*args, **kwargs)



