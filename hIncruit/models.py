from django.db import models
from django.utils import timezone


# Create your models here.
class ITEM(models.Model):
    upper_id = models.CharField(max_length=6, blank=True, null=True, verbose_name='상위ID')
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='그룹 ex) 공고,인재상,회사소개')
    category = models.CharField(max_length=10, blank=True, null=True, verbose_name='카테고리 ex) 공고부문, 주가,뉴스')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='제목')
    content = models.CharField(max_length=1000, blank=True, null=True, verbose_name='내용')
    sub_content = models.TextField(null=True,verbose_name ='상세내용')
    content_img = models.ImageField(blank=True,verbose_name='내용 삽입 이미지')
    thumbnail = models.ImageField(blank=True,verbose_name='썸네일')
    url = models.CharField(max_length=1000, blank=True, null=True, verbose_name='내용')
    param = models.CharField(max_length=10, blank=True, null=True, verbose_name='parameter')
    create_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(default=timezone.now)
    del_yn = models.CharField(max_length=1, default='N')

    def __str__(self):
        return self.title

class USER(models.Model):
    user_id = models.CharField(max_length=20,default='00000000', verbose_name='kakao chat receive id')
    regist_category = models.CharField(max_length=10, blank=True, null=True, verbose_name='즐겨찾기 등록한 부문, 비었으면 전체')
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
    subject = models.CharField(max_length=200, default='subject', verbose_name='제목')
    content = models.CharField(max_length=1000, default='content', verbose_name='내용')
    order = models.IntegerField(max_length=4,null=True,blank=True,db_index=True, verbose_name='순서')
    type = models.CharField(max_length=6, blank=True, null=True, verbose_name='답변형식')
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
