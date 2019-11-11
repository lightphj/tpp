from django.db import models
from django.utils import timezone


# Create your models here.
class ANNOUNCEMENT(models.Model):
    category = models.CharField(max_length=10, blank=True, null=True, verbose_name='직군 코드')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='제목')
    content = models.CharField(max_length=1000, blank=True, null=True, verbose_name='내용')
    sub_content = models.TextField(null=True,verbose_name ='상세내용')
    content_img = models.ImageField(blank=True,verbose_name='내용 삽입 이미지')
    thumbnail = models.ImageField(blank=True,verbose_name='썸네일')
    url = models.CharField(max_length=1000, blank=True, null=True, verbose_name='채용공고 연결 url')
    create_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(default=timezone.now)
    del_yn = models.CharField(max_length=1, default='N')

    def __str__(self):
        return self.title


class ANNOUNCE_DETAIL(models.Model):
    category = models.CharField(max_length=10, blank=True, null=True, verbose_name='직군 코드')
    job = models.CharField(max_length=10, blank=True, null=True, verbose_name='직무코드')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='제목')
    content = models.CharField(max_length=1000, blank=True, null=True, verbose_name='내용')
    sub_content = models.TextField(null=True, verbose_name='상세내용')
    content_img = models.ImageField(blank=True, verbose_name='내용 삽입 이미지')
    thumbnail = models.ImageField(blank=True, verbose_name='썸네일')
    url = models.CharField(max_length=1000, blank=True, null=True, verbose_name='채용공고 연결 url')
    rec_person_num = models.CharField(max_length=4, blank=True, null=True, verbose_name='parameter')
    from_date = models.DateTimeField(null=True,verbose_name='모집기간 from')
    to_date = models.DateTimeField(null=True,verbose_name='모집기간 to')
    howto = models.CharField(max_length=1000, blank=True, null=True, verbose_name='지원방법')
    create_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(default=timezone.now)
    del_yn = models.CharField(max_length=1, default='N')

    def __str__(self):
        return self.title


class USER(models.Model):
    user_id = models.CharField(max_length=20,default='00000000', verbose_name='kakao chat receive id')
    regist_category = models.CharField(max_length=10, blank=True, null=True, verbose_name='직군 즐겨찾기')
    send_notice_yn = models.CharField(max_length=1, default='N')
    create_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(default=timezone.now)
    del_yn = models.CharField(max_length=1, default='N')

    def __str__(self):
        return self.user_id

class QUESTION(models.Model):
    poll_id = models.IntegerField(max_length=4, default=-1, verbose_name='설문 ID')
    question_id = models.IntegerField(max_length=4, default=-1, verbose_name='문항 ID')
    subject = models.CharField(max_length=200, default='subject', verbose_name='질문')
    order_no = models.IntegerField(max_length=4,null=True,blank=True,db_index=True, verbose_name='문항번호')
    create_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(default=timezone.now)
    del_yn = models.CharField(max_length=1, default='N')

    def __str__(self):
        return self.subject

class ANSWER(models.Model):
    poll_id = models.IntegerField(max_length=4, default=-1, verbose_name='설문 ID')
    question_id = models.IntegerField(max_length=4, default=-1, verbose_name='문항 ID')
    user_id = models.ForeignKey(USER, on_delete=models.DO_NOTHING())
    val = models.CharField(max_length=10, default='0', verbose_name='답변값')
    create_date = models.DateTimeField(default=timezone.now)

class QUESTION_CATEGORY(models.Model):
    poll_id = models.IntegerField(max_length=4, default=-1, verbose_name='설문 ID')
    question_id = models.IntegerField(max_length=4, default=-1, verbose_name='문항 ID')
    category = models.CharField(max_length=4, default=' ', verbose_name='직군')
    answer_yn = models.CharField(max_length=1, default=' ', verbose_name='Y/N 일때 +1')


class CATEGORY(models.Model):
    category_cd = models.CharField(max_length=4, default=' ', verbose_name='직군코드')
    category_nm = models.CharField(max_length=4, default=' ', verbose_name='직군명')
    explain = models.TextField(null=True,blank=True, verbose_name='직군 상세설명')
    create_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(default=timezone.now)
    del_yn = models.CharField(max_length=1, default='N')
