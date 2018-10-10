#-*- coding: utf-8 -*-
import os
import datetime
import uuid
from apiv1.models import Document
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('init', nargs=2)

    def handle(self, *args, **options):
        init = options['init']
        text_filepath = init[0]
        raw_filepath = init[1]
        file_list = os.listdir(text_filepath)
        for filename in file_list:
            content = ''
            cache = filename[0:-4].split('@')
            department = cache[0]
            title = cache[1]
            url = None
            time = datetime.date.today()
            target_filename = None
            if os.path.isfile(raw_filepath + filename[0:-4] + '.doc'):
                target_filename = raw_filepath + filename[0:-4] + '.doc'
            if os.path.isfile(raw_filepath + filename[0:-4] + '.docx'):
                target_filename = raw_filepath + filename[0:-4] + '.docx'
            if os.path.isfile(raw_filepath + filename[0:-4] + '.pdf'):
                target_filename = raw_filepath + filename[0:-4] + '.pdf'
            with open(text_filepath + filename, 'rb') as f:
                content = f.read()
                if target_filename is not None:
                    with open(target_filename, 'rb') as target_f:
                        url = File(target_f)
                        url.name = url.name.decode('utf8')
                        instance = Document(title=title.decode('utf8'), content=content.decode('utf8'), department=department.decode('utf8'), time=time, url=url)
                        instance.save()
                else:
                    url = File(f)
                    url.name = url.name.decode('utf8')
                    instance = Document(title=title.decode('utf8'), content=content.decode('utf8'), department=department.decode('utf8'), time=time, url=url)
                    instance.save()


