from django.db import models
from django.utils import timezone
# نموذج المالك (Owner)
class Owner(models.Model):
    name = models.CharField(max_length=255)  # اسم المالك
    address = models.TextField()  # عنوان المالك
    phone = models.CharField(max_length=20)  # رقم هاتف المالك
    email = models.EmailField()  # البريد الإلكتروني للمالك

    def __str__(self):
        return self.name  # إعادة الاسم عند تحويل الكائن إلى نص

# نموذج المستأجر (Tenant)
class Tenant(models.Model):
    DOCUMENT_TYPES = [
        ('ID', 'بطاقة شخصية'),
        ('RESIDENCE', 'إقامة'),
        ('PASSPORT', 'جواز سفر'),
        ('TRADE', 'سجل تجاري'),
    ]

    name = models.CharField(max_length=255)  # اسم المستأجر
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)  # نوع الوثيقة (بطاقة شخصية، إقامة، جواز سفر، سجل تجاري)
    document_number = models.CharField(max_length=100)  # رقم الوثيقة
    address = models.TextField()  # عنوان المستأجر
    phone = models.CharField(max_length=20)  # رقم الهاتف
    email = models.EmailField()  # البريد الإلكتروني
    rental_start_date = models.DateField()  # تاريخ بدء الإيجار
    rental_end_date = models.DateField()  # تاريخ انتهاء الإيجار

    def __str__(self):
        return self.name  # إعادة الاسم عند تحويل الكائن إلى نص

# نموذج العقار (Property)
class Property(models.Model):
    PROPERTY_TYPES = [
        ('APARTMENT', 'شقة'),
        ('ROOM', 'غرفة'),
        ('SHOP', 'محل'),
    ]

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)  # نوع العقار
    address = models.TextField()  # عنوان العقار
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)  # المالك الذي يمتلك العقار
    price = models.DecimalField(max_digits=10, decimal_places=2)  # سعر الإيجار
    rooms = models.IntegerField(null=True, blank=True)  # عدد الغرف (إذا كان شقة أو غرفة)
    floor = models.IntegerField(null=True, blank=True)  # الطابق
    available = models.BooleanField(default=True)  # حالة العقار: هل هو متاح؟
    description = models.TextField()  # وصف العقار

    def __str__(self):
        return f'{self.property_type} - {self.address}'  # إعادة النوع والعنوان عند تحويل الكائن إلى نص

# نموذج عقد الإيجار (RentalContract)
class RentalContract(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='contracts', verbose_name="العقار")  # العقار المؤجر
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='contracts', verbose_name="المستأجر")  # المستأجر
    start_date = models.DateField(verbose_name="تاريخ بدء الإيجار")  # تاريخ بدء الإيجار
    end_date = models.DateField(verbose_name="تاريخ انتهاء الإيجار")  # تاريخ انتهاء الإيجار
    
    def __str__(self):
        return f'عقد {self.property} - {self.tenant.name}'  # إعادة العقار والمستأجر عند تحويل الكائن إلى
            
# نموذج وثائق المستأجر (TenantDocument)
class TenantDocument(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)  # المستأجر المرتبط بالوثيقة
    document_type = models.CharField(max_length=50)  # نوع الوثيقة (بطاقة، إقامة، جواز سفر، سجل تجاري)
    document_file = models.FileField(upload_to='documents/')  # مكان حفظ الوثيقة على الخادم

    def __str__(self):
        return f'{self.tenant.name} - {self.document_type}'  # إعادة اسم المستأجر ونوع الوثيقة عند تحويل الكائن إلى نص
class PropertyReview(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews', verbose_name="العقار")  # العقار المرتبط بالتقييم
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='reviews', verbose_name="المراجع")  # المراجع المرتبط بالتقييم
    rating = models.IntegerField(verbose_name="التقييم", choices=[(1, 'ضعيف'), (2, 'متوسط'), (3, 'جيد'), (4, 'ممتاز') ])  # التقييم
    comment = models.TextField(verbose_name="التعليق")  # التعليق

    def __str__(self):
        return f'تقييم {self.property} - {self.tenant.name} - {self.rating}'