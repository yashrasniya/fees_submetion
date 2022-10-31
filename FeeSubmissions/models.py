from django.db import models
from student_profile.models import Student


class FeeSubmissions(models.Model):
    semester_list = [
        (f'{a}-Semester', f'{a}-Semester') for a in range(1, 9)
    ]
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    data = models.DateField(null=False)
    ReceiptNumber = models.CharField(max_length=20, null=False)
    TransactionNumber = models.CharField(max_length=20, null=False)
    Semester = models.CharField(max_length=20, choices=semester_list, null=False)

    TuitionFee = models.IntegerField(null=False)
    ExamFee = models.IntegerField(null=False)
    Enrollmentfee = models.IntegerField(null=False)
    RegistrationFee = models.IntegerField(null=False)
    SecurityDeposited = models.IntegerField(null=False)
    SportFee = models.IntegerField(null=False)
    DevelopmentFee = models.IntegerField(null=False)
    WelfareFee = models.IntegerField(null=False)

    amount = models.IntegerField()



    @property
    def TotalAmount(self):
        self.amount = self.TuitionFee + \
                      self.ExamFee + \
                      self.Enrollmentfee + \
                      self.RegistrationFee + \
                      self.SecurityDeposited + \
                      self.SportFee + \
                      self.DevelopmentFee + \
                      self.WelfareFee
