#-*- coding: utf-8 -*-
import os
import re
import datetime
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
        for industry in os.listdir(raw_filepath):
            for region in os.listdir(os.path.join(raw_filepath, industry)):
                for category in os.listdir(os.path.join(raw_filepath, industry, region)):
                    for filename in os.listdir(os.path.join(raw_filepath, industry, region, category)):
                        if os.path.isdir(os.path.join(raw_filepath, industry, region, category, filename)):
                            relative_path = os.path.join(industry, region, category, filename)
                            for childname in os.listdir(os.path.join(raw_filepath, relative_path)):
                                content = ''
                                split_tuple = os.path.splitext(childname)
                                title = filename + '-' + split_tuple[0]
                                title_split = re.split(r'\s+', filename)
                                department = title_split[-1] if len(title_split) > 1 else ""
                                url = None
                                time_list = re.findall(r'(\d+)\.(\d+)\.(\d+)', title)
                                time = datetime.date(*map(int, time_list[-1])) if len(time_list) > 0 else None

                                with open(os.path.join(text_filepath, relative_path, split_tuple[0] + '.txt'), 'rb') as f:
                                    content = f.read()
                                    with open(os.path.join(raw_filepath, relative_path, childname), 'rb') as target_f:
                                        url = File(target_f)
                                        url.name = url.name.decode('utf8')
                                        instance = Document(title=title.decode('utf8'), content=content.decode('utf8'), department=department.decode('utf8'), time=time, url=url, region=region.decode('utf8'), industry=industry.decode('utf8'), category=category.decode('utf8'))
                                        instance.save()
                        else:
                            relative_path = os.path.join(industry, region, category)
                            content = ''
                            split_tuple = os.path.splitext(filename)
                            title = split_tuple[0]
                            title_split = re.split(r'\s+', title)
                            department = title_split[-1] if len(title_split) > 1 else ""
                            url = None
                            time_list = re.findall(r'(\d+)\.(\d+)\.(\d+)', title)
                            time = datetime.date(*map(int, time_list[-1])) if len(time_list) > 0 else None
 

                            with open(os.path.join(text_filepath, relative_path, split_tuple[0] + '.txt'), 'rb') as f:
                                content = f.read()
                                with open(os.path.join(raw_filepath, relative_path, filename), 'rb') as target_f:
                                    url = File(target_f)
                                    url.name = url.name.decode('utf8')
                                    instance = Document(title=title.decode('utf8'), content=content.decode('utf8'), department=department.decode('utf8'), time=time, url=url, region=region.decode('utf8'), industry=industry.decode('utf8'), category=category.decode('utf8'))
                                    instance.save()


